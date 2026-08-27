# Pinterest Video Downloader

Baixa varios videos do Pinterest de uma vez, salvando cada um numa pasta com o
nome do video.

## Instalacao

```bash
pip install -r requirements.txt
```

Tambem e necessario ter o **ffmpeg** instalado no sistema (usado para juntar
audio e video em um unico .mp4):

- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: baixe em https://ffmpeg.org/download.html e adicione ao PATH

## Uso

1. Abra o arquivo `links.txt` e cole um link do Pinterest por linha:

   ```
   https://www.pinterest.com/pin/111111111111111111/
   https://www.pinterest.com/pin/222222222222222222/
   https://pin.it/abc123
   ```

2. Rode o script:

   ```bash
   python download_pinterest.py
   ```

   Os videos vao para a pasta `downloads/`, cada um nomeado com o titulo do
   pin (ex: `nome-do-video [id].mp4`).

### Opcoes

```bash
# Usar outro arquivo de links e outra pasta de saida
python download_pinterest.py meus_links.txt -o minha_pasta

# Ler os links direto do terminal (um por linha, Ctrl+D para finalizar)
python download_pinterest.py -
```

Links invalidos ou que falharem nao interrompem o processo: eles ficam
listados ao final em `downloads/falhas.txt`.
