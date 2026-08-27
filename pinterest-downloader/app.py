#!/usr/bin/env python3
"""App web local para baixar varios videos do Pinterest de uma vez."""

import pathlib
import re
import threading

from flask import Flask, jsonify, render_template, request, send_from_directory

from yt_dlp import YoutubeDL

BASE_DIR = pathlib.Path(__file__).parent.resolve()
DOWNLOADS_ROOT = BASE_DIR / "downloads"

app = Flask(__name__)

job_lock = threading.Lock()
job_state = {
    "running": False,
    "total": 0,
    "done": 0,
    "current": "",
    "percent": "",
    "log": [],
    "ok": [],
    "fail": [],
    "output_dir": "",
    "folder": "",
}


def log(msg: str) -> None:
    with job_lock:
        job_state["log"].append(msg)
        job_state["log"] = job_state["log"][-300:]


def parse_links(text: str) -> list[str]:
    links = []
    seen = set()
    for line in text.splitlines():
        link = line.strip()
        if not link or link.startswith("#"):
            continue
        if link not in seen:
            seen.add(link)
            links.append(link)
    return links


def sanitize_folder(name: str) -> str:
    name = (name or "").strip() or "downloads"
    name = re.sub(r"[^A-Za-z0-9 _\-\.]", "_", name)
    return name or "downloads"


def make_progress_hook():
    def hook(d):
        if d.get("status") == "downloading":
            with job_lock:
                job_state["percent"] = (d.get("_percent_str") or "").strip()
        elif d.get("status") == "finished":
            with job_lock:
                job_state["percent"] = "100%"

    return hook


def run_download(links: list[str], out_dir: pathlib.Path, folder: str) -> None:
    ydl_opts = {
        "outtmpl": str(out_dir / "%(title).150B [%(id)s].%(ext)s"),
        "restrictfilenames": True,
        "windowsfilenames": True,
        "format": "best/bv*+ba",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "no_warnings": True,
        "quiet": True,
        "socket_timeout": 20,
        "progress_hooks": [make_progress_hook()],
    }

    with job_lock:
        job_state.update(
            running=True,
            total=len(links),
            done=0,
            current="",
            percent="",
            log=[],
            ok=[],
            fail=[],
            output_dir=str(out_dir),
            folder=folder,
        )

    try:
        out_dir.mkdir(parents=True, exist_ok=True)

        for i, url in enumerate(links, 1):
            with job_lock:
                job_state["current"] = url
                job_state["percent"] = ""
            log(f"[{i}/{len(links)}] Baixando: {url}")
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                with job_lock:
                    job_state["ok"].append(url)
                log("  OK")
            except Exception as e:
                with job_lock:
                    job_state["fail"].append(url)
                log(f"  Falhou: {e}")
            with job_lock:
                job_state["done"] = i

        with job_lock:
            if job_state["fail"]:
                (out_dir / "falhas.txt").write_text(
                    "\n".join(job_state["fail"]), encoding="utf-8"
                )
        log("Concluido.")
    except Exception as e:
        log(f"Erro inesperado, processo interrompido: {e}")
    finally:
        with job_lock:
            job_state["running"] = False
            job_state["current"] = ""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    with job_lock:
        if job_state["running"]:
            return jsonify({"error": "Ja existe um download em andamento."}), 409

    data = request.get_json(force=True, silent=True) or {}
    links = parse_links(data.get("links", ""))
    if not links:
        return jsonify({"error": "Nenhum link valido encontrado."}), 400

    folder = sanitize_folder(data.get("output", "downloads"))
    out_dir = DOWNLOADS_ROOT / folder

    thread = threading.Thread(target=run_download, args=(links, out_dir, folder), daemon=True)
    thread.start()
    return jsonify({"ok": True})


@app.route("/status")
def status():
    with job_lock:
        return jsonify(dict(job_state))


@app.route("/files")
def files():
    with job_lock:
        out_dir = job_state["output_dir"]
        folder = job_state["folder"]
    if not out_dir:
        return jsonify({"files": [], "folder": ""})
    path = pathlib.Path(out_dir)
    if not path.exists():
        return jsonify({"files": [], "folder": folder})
    items = [
        {"name": f.name, "size": f.stat().st_size}
        for f in sorted(path.iterdir())
        if f.is_file() and f.suffix.lower() in (".mp4", ".mkv", ".webm", ".mov")
    ]
    return jsonify({"files": items, "folder": folder})


@app.route("/downloads/<folder>/<path:filename>")
def serve_download(folder, filename):
    return send_from_directory(DOWNLOADS_ROOT / sanitize_folder(folder), filename)


if __name__ == "__main__":
    DOWNLOADS_ROOT.mkdir(exist_ok=True)
    print("Abra http://127.0.0.1:5000 no navegador")
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)
