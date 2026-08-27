#!/usr/bin/env python3
"""Baixa varios videos do Pinterest de uma vez a partir de uma lista de links."""

import argparse
import pathlib
import sys

from yt_dlp import YoutubeDL


def read_links(source: str) -> list[str]:
    if source == "-":
        raw_lines = sys.stdin.readlines()
    else:
        path = pathlib.Path(source)
        if not path.exists():
            print(f"Arquivo de links nao encontrado: {source}")
            sys.exit(1)
        raw_lines = path.read_text(encoding="utf-8").splitlines()

    links = []
    seen = set()
    for line in raw_lines:
        link = line.strip()
        if not link or link.startswith("#"):
            continue
        if link not in seen:
            seen.add(link)
            links.append(link)
    return links


def build_ydl_opts(out_dir: pathlib.Path) -> dict:
    return {
        "outtmpl": str(out_dir / "%(title).150B [%(id)s].%(ext)s"),
        "restrictfilenames": True,
        "windowsfilenames": True,
        "format": "best/bv*+ba",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "no_warnings": True,
        "quiet": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Baixa varios videos do Pinterest a partir de uma lista de links."
    )
    parser.add_argument(
        "links_file",
        nargs="?",
        default="links.txt",
        help="Arquivo .txt com um link por linha (use '-' para ler do stdin). Padrao: links.txt",
    )
    parser.add_argument(
        "-o", "--output", default="downloads", help="Pasta de destino (padrao: downloads)"
    )
    args = parser.parse_args()

    links = read_links(args.links_file)
    if not links:
        print(f"Nenhum link encontrado em {args.links_file}")
        sys.exit(1)

    out_dir = pathlib.Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = build_ydl_opts(out_dir)

    ok, fail = [], []
    print(f"Encontrados {len(links)} link(s). Baixando para '{out_dir}/'...\n")
    for i, url in enumerate(links, 1):
        print(f"[{i}/{len(links)}] {url}")
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            ok.append(url)
        except Exception as e:
            print(f"  Falhou: {e}")
            fail.append(url)
        print()

    print("=" * 50)
    print(f"Concluido: {len(ok)} sucesso(s), {len(fail)} falha(s).")
    if fail:
        fail_file = out_dir / "falhas.txt"
        fail_file.write_text("\n".join(fail), encoding="utf-8")
        print(f"Links que falharam foram salvos em: {fail_file}")


if __name__ == "__main__":
    main()
