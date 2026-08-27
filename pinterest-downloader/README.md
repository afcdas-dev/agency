# Pinterest Video Downloader

Baixa varios videos do Pinterest de uma vez, salvando cada um numa pasta com o
nome do video. Vem com uma interface web local para colar os links e
acompanhar o progresso pelo navegador.

## Instalacao

```bash
cd pinterest-downloader
pip install -r requirements.txt
```

Tambem e necessario ter o **ffmpeg** instalado no sistema (usado para juntar
audio e video em um unico .mp4):

- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: baixe em https://ffmpeg.org/download.html e adicione ao PATH

## Uso (app web local)

```bash
python app.py
```

Abra **http://127.0.0.1:5000** no navegador. Na pagina:

1. Cole os links do Pinterest na caixa de texto (um por linha).
2. Defina o nome da pasta de destino (opcional).
3. Clique em **Baixar todos** e acompanhe a barra de progresso e o log em
   tempo real.
4. No final, a lista de videos baixados aparece com link para abrir/baixar
   cada um direto do navegador.

Os arquivos ficam salvos em `pinterest-downloader/downloads/<pasta>/`, cada
um nomeado com o titulo do pin (ex: `nome-do-video [id].mp4`). Links que
falharem nao interrompem o processo e ficam listados em `falhas.txt` dentro
da mesma pasta.

## Uso alternativo (linha de comando)

Se preferir rodar sem abrir o navegador, o script `download_pinterest.py`
faz a mesma coisa via terminal:

```bash
# edite o links.txt com um link por linha, depois:
python download_pinterest.py

# ou informe outro arquivo/pasta:
python download_pinterest.py meus_links.txt -o minha_pasta

# ou leia os links direto do terminal (Ctrl+D para finalizar):
python download_pinterest.py -
```
