# Comercial — Kit de Ferramentas de Rede 10 em 1

Pacote de produção pronto para disparo no **Higgsfield Marketing Studio** (`type=product`),
usando as gerações ilimitadas do free trial (`use_unlim: true`).

---

## 1. Produto

**KIT DE FERRAMENTAS DE REDE 10 EM 1** — "Tudo o que você precisa em um único kit."

| # | Item |
|---|------|
| 01 | Crimpador de cabo (3 em 1: decapagem, corte e crimpagem) |
| 02 | Testador de cabo |
| 03 | Descascador de fios |
| 04 | Ferramenta de impacto para conector (punch down) |
| 05 | Descascador multifuncional |
| 06 | Chave de fenda |
| 07 | Chave de fenda Phillips |
| 08 | Conectores RJ45 |
| 09 | Bota protetora para conector |
| 10 | Estojo organizador |

**Compatibilidade:** CAT5, CAT5e e CAT6 · conectores RJ45 (8 pinos) · cabos RJ11/12 (4 e 6 pinos).

**Público:** profissionais e entusiastas de redes e TI.

**Pilares de mensagem:** Ferramentas de qualidade · Organizado e prático · Ideal para redes e TI · Completo e versátil.

---

## 2. Imagens de origem (Google Drive)

Pasta: `12qVeggVDYwnbBbCB925reO1cRMiAvtQH`

| Arquivo | File ID | Conteúdo |
|---------|---------|----------|
| ferramenta-1.png | `1FF46O1npU3UnvuV3650Lw6aCgCqa2L2i` | Produto |
| ferramenta-2.png | `1T0jqxKST__WFfwTgREWuhVl-bgUTsNI4` | Alicate de crimpagem 3 em 1 — specs CAT5/5e/6, RJ45, RJ11/12 |
| ferramenta-3.png | `1_WDxwQJDRaf5gQuZSjEEWA9IN6LevRLi` | Arte principal do kit 10 em 1 com os 10 itens numerados |
| ferramenta-4.png | `1BOtmRC5KaGhAibyIbFKEj2vQRFaVYIDf` | Produto |

URL de importação (fetch feito pelo servidor do Higgsfield, não pelo proxy local):
`https://drive.google.com/uc?export=download&id=<FILE_ID>`

---

## 3. Roteiro — 15s vertical (9:16)

| Tempo | Cena | Texto em tela |
|-------|------|---------------|
| 0–2s | Mãos abrem o estojo sobre bancada escura; as 10 ferramentas alinhadas, luz rasante no metal | **KIT 10 EM 1** |
| 2–6s | Macro do crimpador cravando um conector RJ45 — clique firme, cabo CAT6 entrando nos 8 pinos | Crimpa, corta e decapa |
| 6–10s | Testador de cabo com LEDs acendendo em sequência; rede validada | CAT5 · CAT5e · CAT6 |
| 10–13s | Cada ferramenta voltando ao seu recorte no estojo; tampa fechando | Organizado e pronto pra próxima |
| 13–15s | Pack shot do kit fechado, fundo limpo | **TUDO O QUE VOCÊ PRECISA** |

---

## 4. Chamada de disparo

### Passo 1 — Importar as imagens
```
media_import_url(url="https://drive.google.com/uc?export=download&id=<FILE_ID>", type="image")   # x4
```

### Passo 2 — Criar o produto no Marketing Studio
```
show_marketing_studio(
  action = "create",
  type   = "product",
  title  = "Kit de Ferramentas de Rede 10 em 1",
  description = "Kit completo 10 em 1 para redes e TI: crimpador 3 em 1, testador de cabo, "
                "descascador de fios, ferramenta de impacto, descascador multifuncional, "
                "chave de fenda, chave Phillips, conectores RJ45, bota protetora e estojo "
                "organizador. Compativel com CAT5, CAT5e e CAT6, RJ45 (8 pinos) e RJ11/12.",
  medias = [ {value: <media_id>, role: "image"}, ... ]
)
```
Seguir o `next_step` retornado e guardar o `product_id`.

### Passo 3 — Gerar o video
```
generate_video(params = {
  model:          "marketing_studio_video",
  mode:           "product_showcase",     # preset escolhido — ver secao 4.1
  product_ids:    ["<product_uuid>"],     # plural; o servidor nao aceita product_id
  aspect_ratio:   "9:16",
  duration:       15,                     # faixa aceita pelo modelo: 12-15s
  resolution:     "1080p",                # default do modelo e 720p
  generate_audio: true,
  use_unlim:      true,
  prompt:         <ver secao 5>
})
```

### 4.1 — Preset (`mode`)

Confirmado no catalogo do Marketing Studio:

| Slug | Nome | Por que |
|------|------|---------|
| `product_showcase` | Product Showcase | **Primario.** Comercial focado no produto, sem creator falando — combina com o roteiro |
| `tv_spot` | TV Spot | Alternativa mais classica de comercial, se quiser tom institucional |
| `ugc_unboxing_asmr` | Unboxing ASMR | Alternativa: o click do crimpador e o encaixe no estojo rendem ASMR |

---

## 5. Prompt do video

> Cinematic 15-second product commercial for a 10-in-1 network technician tool kit,
> shot on a dark matte workbench with cool blue key light and warm rim light.
> Open on a top-down shot of two hands opening the organizer case, revealing ten tools
> seated in precise foam cutouts — light sweeps across brushed metal and blue rubber grips.
> Cut to an extreme macro of the crimping tool pressing an RJ45 connector onto a CAT6 cable,
> shallow depth of field, the eight gold pins snapping into place.
> Cut to the cable tester with green LEDs lighting up in sequence.
> Cut to each tool returning to its slot and the case closing with a clean snap.
> End on a centered hero pack shot of the closed kit on seamless background.
> Confident, precise, professional-grade energy. Smooth push-in camera moves,
> crisp foley-driven pacing, no on-screen people beyond hands.

**Texto em tela (PT-BR):** `KIT 10 EM 1` -> `Crimpa, corta e decapa` -> `CAT5 - CAT5e - CAT6` ->
`Organizado e pronto pra proxima` -> `TUDO O QUE VOCE PRECISA`

---

## 6. Variacoes previstas

- **9:16** — Reels / TikTok / Shorts (principal)
- **16:9** — YouTube pre-roll / site
- Corte de 12s (minimo do modelo) para paid social, reaproveitando as cenas 2-6s e o pack shot

---

## Status

Bloqueado no passo 1: a sessao do conector Higgsfield expirou.

Diagnostico (2 tentativas):

| Chamada | Resultado |
|---------|-----------|
| `models_explore(marketing_studio_video)` | OK — leitura de catalogo, nao exige sessao |
| `show_marketing_studio(action="presets")` | OK — leitura de catalogo, nao exige sessao |
| `balance` | Sessao expirada |
| `media_import_url` | Sessao expirada |
| `show_marketing_studio(action="list")` | Sessao expirada |

O servico esta no ar; o que falta e a autorizacao da conta. Reautorizar o conector Higgsfield
no cliente MCP (remover e adicionar de novo, se so reconectar nao abrir o login) destrava o
disparo — todo o resto acima ja esta definido e parametrizado.
