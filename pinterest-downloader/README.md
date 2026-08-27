# Pinterest Video Downloader

Baixa varios videos do Pinterest de uma vez, salvando cada um numa pasta com o
nome do video. Vem com uma interface web local para colar os links e
acompanhar o progresso pelo navegador.

## Guia rapido para Windows (passo a passo, do zero)

Se voce nunca usou terminal/Python antes, siga exatamente estes passos:

1. **Instale o Python:**
   - Acesse https://www.python.org/downloads/ e clique em "Download Python".
   - Abra o instalador baixado. **Muito importante:** marque a caixinha
     **"Add python.exe to PATH"** (ou "Add Python to PATH") na primeira tela
     antes de clicar em "Install Now".

2. **Descompacte a pasta** `pinterest-downloader.zip` que voce recebeu (clique
   com o botao direito nela → "Extrair tudo...").

3. **Abra o terminal dentro da pasta:**
   - Abra a pasta `pinterest-downloader` extraida no Explorador de Arquivos.
   - Clique na barra de endereco (onde mostra o caminho da pasta), apague o
     texto, digite `cmd` e aperte Enter. Isso abre um terminal ja dentro da
     pasta certa.

4. **No terminal que abriu, digite este comando e aperte Enter:**

   ```
   pip install -r requirements.txt
   ```

   Espere terminar (pode demorar um pouco na primeira vez).

5. **Depois, digite este outro comando e aperte Enter:**

   ```
   python app.py
   ```

   Vai aparecer uma mensagem tipo `Running on http://127.0.0.1:5000`.
   **Deixe essa janela do terminal aberta** (nao feche).

6. **Abra o navegador** (Chrome, Edge, etc.) e acesse:

   ```
   http://127.0.0.1:5000
   ```

Pronto, a pagina do app deve aparecer. Cole os links do Pinterest, clique em
**Baixar todos** e acompanhe o progresso.

> Se o comando `pip` ou `python` der erro de "nao reconhecido como comando",
> geralmente e porque o Python foi instalado sem marcar "Add to PATH" — reinstale
> marcando essa opcao (passo 1) e reinicie o terminal.

## Uso (app web local) — resumo

```bash
cd pinterest-downloader
pip install -r requirements.txt
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

Na maioria dos casos **nao e preciso instalar ffmpeg** — os videos do
Pinterest costumam vir prontos num unico arquivo. Se algum pin especifico
precisar juntar audio e video separados, instale o ffmpeg:

- Windows: baixe em https://ffmpeg.org/download.html e adicione ao PATH
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`

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
