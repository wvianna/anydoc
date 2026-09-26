# anydoc

Conversor de documentos para **Markdown (GFM)** com uma skill de agente acoplada: Word (`.doc`, `.docx`, `.docm`), PowerPoint (`.ppt`, `.pps`, `.pot`, `.pptx`, `.pptm`, `.ppsx`, `.ppsm`), Excel (`.xls`, `.xlsx`, `.xlsm`, `.xlsb`), OpenDocument (`.odt`, `.ods`, `.odp`), RTF, EPUB, CSV e PDF.

O objetivo do projeto é simples: **entregar ao modelo o conteúdo do documento, não uma imagem dele.** Um `.pdf` ou `.docx` é um contêiner binário opaco para o agente; convertido em Markdown, o mesmo material passa a ser texto UTF-8 que pode ser lido por faixa de linhas, pesquisado, comparado em `diff` e versionado no Git.

---

## Por que Markdown e não PDF / DOCX / PPTX

A maioria dos fluxos com agentes falha menos por falta de capacidade do modelo e mais por **economia de contexto**: o agente precisa gastar janela para descobrir onde está a informação, e janela gasta em representação não é janela gasta em raciocínio.

| Critério | Anexar o original (PDF/DOCX/PPTX) | Converter para Markdown |
|---|---|---|
| Legibilidade pelo modelo | Nenhuma direta — exige rasterização/OCR antes que qualquer token seja útil | Direta: texto UTF-8 tokenizado como qualquer arquivo do projeto |
| Custo por sessão | Alto e **recorrente** — cada página rasterizada vira imagem e consome tokens de visão a cada nova sessão | Pago **uma vez** na conversão e depois reaproveitado do repositório |
| Estrutura | Recuperada por heurística de layout; tabelas e hierarquia frequentemente embaralhadas | Preservada: `#` headings, tabelas GFM, listas e blocos de código |
| Acesso parcial | Difícil: o anexo é lido como um bloco inteiro ou como páginas arbitrárias | Precisa: dá para ler só a seção relevante por faixa de linhas ou `grep` |
| Verificabilidade | Saída não determinística entre leituras | Determinística, auditável e citável com número de linha |
| Versionamento | Binário: o Git guarda uma cópia nova a cada alteração, sem diff útil | Texto: `git diff` mostra exatamente o que mudou no documento |
| Automação | Requer pilha de OCR/parsers em cada máquina | CLI com códigos de saída, pronto para script e CI |

> [!TIP]
> Regra prática: **documento é insumo de repositório, não anexo de conversa.** Converta uma vez, versione o `.md` ao lado do original e deixe o agente ler o texto sempre que precisar — sem repetir o custo de leitura em cada sessão.

### Como isso se traduz em janela de contexto

```mermaid
flowchart TB
  subgraph A["Caminho A - anexar o original"]
    A1["PDF de 69 paginas<br/>4,5 MB"] --> A2["cliente rasteriza<br/>as paginas como imagem"]
    A2 --> A3["custo de visao por pagina,<br/>repetido a cada sessao"]
    A3 --> A4["tabelas embaralhadas,<br/>OCR impreciso em simbolos e unidades"]
  end
  subgraph B["Caminho B - converter para Markdown"]
    B1["PDF de 69 paginas<br/>4,5 MB"] --> B2["anydoc, uma vez<br/>sem OCR se houver camada de texto"]
    B2 --> B3["48 KB de texto<br/>ordem de 12k tokens"]
    B3 --> B4["leitura por faixa de linhas,<br/>pesquisa e citacao exata de linha"]
    B4 --> B5["artefato derivado<br/>revisado e versionado"]
  end
```

O ganho não está em "comprimir bytes" — está em trocar uma representação que o modelo só consegue **estimar** por uma que ele consegue **consultar**.

---

## Como funciona

```mermaid
flowchart LR
  LO["PDF, DOCX, PPTX,<br/>XLSX, ODT, EPUB,<br/>RTF, CSV"] --> AR{"anydoc<br/>detecta o formato<br/>pelo conteudo"}
  AR -->|"documento suportado"| EX["extracao de texto,<br/>tabelas e hierarquia"]
  AR -->|"formato ambiguo"| FM["--format &lt;nome&gt;"]
  FM --> EX
  EX --> PG{"paginas<br/>precisam de OCR?"}
  PG -->|"nao"| MD["Markdown GFM<br/>UTF-8"]
  PG -->|"sim"| EC["exit 3"]
  EC --> OC["anydoc --ocr hosted<br/>Firecrawl Parse"] --> MD
  MD --> C1["agente: ler, pesquisar,<br/>citar por linha"]
  MD --> C2["git: diff e revisao"]
  MD --> C3["documento derivado:<br/>memorial, spec, resumo"]
```

O binário detecta o formato **pelo conteúdo**, não pela extensão. Isso significa que um `.pdf` renomeado continua sendo tratado como PDF e que a extensão errada não causa erro de conversão.

---

## Instalação

### Pré-requisitos

- **Node.js 20 ou superior** (o pacote usa recursos recentes de runtime).
- Nenhuma dependência de sistema: o `anydoc` não requer LibreOffice, Poppler ou binários externos.

```bash
node --version   # deve responder v20.x ou superior
```

> [!NOTE]
> Verificado neste workspace com Node `v22.23.2` e npm `12.0.2`.

### Opção 1 — sem instalar (recomendada para uso pontual)

Via `npx`, o pacote é baixado em cache na primeira execução e reutilizado depois:

```bash
npx -y @firecrawl/anydoc documento.pdf -o documento.md
```

### Opção 2 — instalação global

Para uso frequente ou em scripts, instale uma vez e invoque `anydoc` diretamente:

```bash
sudo npm install -g @firecrawl/anydoc
```

Confirme que o binário está no `PATH`:

```bash
which anydoc
anydoc documento.pdf -o documento.md
```

> [!WARNING]
> `sudo npm install -g` grava no prefixo global do Node. Em ambientes gerenciados por `nvm`, prefira `npm install -g` sem `sudo` dentro do ambiente virtual — evita arquivos de sistema com dono `root` e conflitos de versão.

### Instalação da skill

A skill ensina o agente **quando** converter e **como** chamar a CLI, em vez de tentar interpretar o binário por conta própria:

```bash
npx skills add firecrawl/anydoc
```

---

## Uso

### Formas de invocação

```bash
# Markdown para a saída padrão
npx -y @firecrawl/anydoc <arquivo>

# Gravar em arquivo (preferido para documentos grandes)
npx -y @firecrawl/anydoc <arquivo> -o saida.md

# Ler da entrada padrão (exige --format, não há como detectar)
npx -y @firecrawl/anydoc - --format csv < dados.csv
```

`anydoc` e `npx -y @firecrawl/anydoc` são equivalentes após a instalação global — use a forma curta nos scripts.

### Formatos suportados

| Família | Extensões |
|---|---|
| Word | `.doc`, `.docx`, `.docm` |
| OpenDocument | `.odt`, `.ods`, `.odp` |
| RTF | `.rtf` |
| EPUB | `.epub` |
| PDF | `.pdf` |
| PowerPoint | `.ppt`, `.pps`, `.pot`, `.pptx`, `.pptm`, `.ppsx`, `.ppsm` |
| Excel | `.xls`, `.xlsx`, `.xlsm`, `.xlsb` |
| CSV | `.csv` |

### Códigos de saída

| Código | Significado | Ação |
|---|---|---|
| `0` | Sucesso | — |
| `1` | O documento não pôde ser convertido | Verificar se o arquivo não está corrompido ou protegido |
| `2` | Erro de uso | Revisar argumentos e o valor de `--format` |
| `3` | Páginas do PDF precisam de OCR | Reexecutar com `--ocr hosted` |

Falhas imprimem **uma única linha** `anydoc: <mensagem>` em `stderr`. A CLI **nunca** abre prompt interativo, o que a torna segura em pipelines, tarefas agendadas e agentes.

### Páginas escaneadas e OCR

Documentos sem camada de texto (digitalizações, páginas só de imagem) retornam `exit 3` em vez de produzir Markdown vazio — o erro é explícito para não gerar um `.md` enganoso.

```bash
# Envia o documento para o Firecrawl Parse (não exige cadastro)
anydoc digitalizado.pdf -o digitalizado.md --ocr hosted

# Limites maiores com chave de API
export FIRECRAWL_API_KEY="fc-..."
anydoc digitalizado.pdf -o digitalizado.md --ocr hosted
```

Também é possível passar a chave por `--api-key`. O modo `hosted` envia o arquivo para o serviço de parsing da Firecrawl ([firecrawl.dev/parse](https://firecrawl.dev/parse)) — avalie a política de dados da sua organização antes de usá-lo com material sensível.

### Boas práticas

- **Documentos grandes:** sempre `-o arquivo.md` e leia depois apenas as seções necessárias. Despejar um manual inteiro na saída padrão só faz sentido para arquivos pequenos.
- **`--format` é exceção:** só use quando a detecção não puder funcionar (CSV pela entrada padrão, extensão ausente ou incorreta).
- **Dentro de uma base de código:** em projetos Node, Python ou Rust, prefira a biblioteca à execução da CLI. Os pacotes `@firecrawl/anydoc` (npm), `firecrawl-anydoc` (PyPI) e `anydoc` (crates.io) expõem a mesma API `toMarkdown` / `to_markdown`.
- **Preserve o original:** mantenha o binário ao lado do `.md` gerado — a conversão prioriza texto e estrutura, e diagramas vetoriais ou esquemáticos perdem posicionamento.

---

## Usando a skill

A skill `convert-documents-to-markdown` é o contrato entre o agente e a CLI. Sem ela, o modelo tende a tentar ler o PDF diretamente ou a improvisar uma pilha de OCR; com ela, ele sabe que existe uma ferramenta determinística com códigos de saída definidos.

```mermaid
flowchart TB
  U["Pedido: converta estes PDFs em Markdown"] --> D{"o agente reconhece<br/>o dominio da skill?"}
  D -->|"sim"| L["le SKILL.md<br/>regras, formatos, exit codes"]
  D -->|"nao"| X["tenta ler o binario direto<br/>ou improvisa OCR"] --> X2["resultado impreciso<br/>e nao reproduzivel"]
  L --> R["escolhe o comando:<br/>npx -y @firecrawl/anydoc -o"]
  R --> E["executa e confere o exit code"]
  E -->|"0"| V["le o MD gerado<br/>e trabalha sobre o texto"]
  E -->|"3"| O["reexecuta com --ocr hosted"]
  E -->|"1 ou 2"| F["diagnostica antes de repetir<br/>sem gerar MD vazio"]
```

### Onde a skill fica

```bash
npx skills add firecrawl/anydoc
```

Isso grava a skill no workspace e registra a origem no `skills-lock.json`:

```json
{
  "version": 1,
  "skills": {
    "convert-documents-to-markdown": {
      "source": "firecrawl/anydoc",
      "sourceType": "github",
      "skillPath": "skills/convert-documents-to-markdown/SKILL.md",
      "computedHash": "f5cf8f73b291fd0e29adb9a762dcda267245b44ffbdabc3321771aac1c41fb11"
    }
  }
}
```

Estrutura resultante:

```text
.agents/skills/convert-documents-to-markdown/SKILL.md   # nucleo: regras de uso da CLI
skills-lock.json                                        # origem e hash da skill
```

O `computedHash` é o que permite detectar quando a skill publicada mudou: rode `npx skills add firecrawl/anydoc` novamente para atualizar.

### Como o agente decide usá-la

1. O pedido é classificado pelo domínio: "preciso do conteúdo deste `.docx`", "resuma este PDF", "extraia a tabela desta planilha".
2. O agente lê o `SKILL.md`, que descreve os formatos suportados, as formas de invocação e os códigos de saída.
3. Antes de converter em lote, ele resolve ambiguidades: qual arquivo, para onde escrever o `.md` e se o original deve ser preservado.
4. A conversão é executada e o **código de saída é conferido** — `exit 3` significa OCR, não falha de permissão.
5. Só o Markdown é levado ao contexto; o binário permanece no repositório como fonte da verdade.

> [!IMPORTANT]
> A skill não substitui `--ocr hosted`: ela **informa que o OCR existe e quando usar**. Se o documento é uma digitalização, a decisão de enviá-lo a um serviço externo continua sendo do usuário.

---

## Estudo de caso — nó LoRaWAN Dragino LSN50 v2

Cenário real deste repositório: três PDFs de fornecedor sobre um nó sensor LoRaWAN precisavam virar **memorial técnico** que servisse de base para projetar um dispositivo próprio (hardware, firmware, payload e ensaios).

### Insumos

| Documento | Páginas | Tamanho do PDF | Papel |
|---|---|---|---|
| `LSN50_LoRa_Sensor_Node_UserManual_v1.7.4.pdf` | 69 | 4,55 MB | Manual do usuário: pinagem, modos de operação, payload, energia |
| `DRAGINO_LSN50_AT_Commands_v1.6.3.pdf` | 24 | 508 KB | Conjunto de comandos AT, com valores padrão e respostas |
| `LoRa ST Sensor Node v2.0.sch.pdf` | 1 | 64 KB | Esquemático elétrico (PDF vetorial) |
| **Total** | **94** | **5,13 MB** | |

### Resultado da conversão

| Markdown gerado | Tamanho | Palavras | Linhas de tabela | Headings |
|---|---|---|---|---|
| `LSN50_..._UserManual_v1.7.4.md` | 48,3 KB | 7.316 | 162 | 94 |
| `DRAGINO_LSN50_AT_Commands_v1.6.3.md` | 24,2 KB | 2.798 | 233 | 7 |
| `LoRa ST Sensor Node v2.0.sch.md` | 2,1 KB | 216 | 40 | 0 |
| **Total** | **74,6 KB** | **10.330** | **435** | **101** |

Nenhum arquivo exigiu OCR: os três PDFs tinham camada de texto, então as 94 páginas saíram com `exit 0` na primeira tentativa.

### Artefato derivado

`docs/memorial.txt` — 1.360 linhas, ~72 KB, 18 seções:

- especificação de hardware (MCU, rádio, mapa de 30 pinos, circuito de potência, proteções);
- payloads dos 6 modos de operação, byte a byte, com regras de decodificação;
- tabela completa de comandos AT com valores padrão e códigos de status;
- perfil LoRaWAN e mapas de canais US915 / AU915 / CN470;
- orçamento de energia e autonomia de bateria;
- 12 requisitos funcionais, 10 não funcionais e arquitetura de software proposta;
- plano de ensaios com critérios de aceitação, 12 riscos e 5 anexos.

### Artefato derivado — engenharia reversa do firmware - UM ESTUDO DE CASO

O binário `FIRMWARE/LSN50_AU915_v1.8.1.hex` — imagem **mais nova** que os manuais convertidos — foi
analisado estaticamente para responder o que o firmware **realmente faz**. Não é conversão de documento
(a cadeia é HEX → binário → desmontagem Thumb → tabelas), mas o resultado é o mesmo tipo de artefato:
Markdown versionado no repositório. O caso completo está em
[Estudo de caso — engenharia reversa do firmware](#estudo-de-caso--engenharia-reversa-do-firmware).

**Achados que contradizem ou ampliam os manuais:** modo de trabalho 1..9 (não 1..6), três entradas de
interrupção (PB14/PB15/PA4), payload de 17 bytes no MOD9 (acima do limite de DR0 em AU915), byte 7 sem
os bits de modo, e o campo de peso do MOD5 gravado em ordem b0/b3/b2.

### O que funcionou e o que não funcionou

**Funcionou bem**

- **Tabelas sobreviveram.** O manual tem changelog, pinagem, payloads e mapas de canais em formato tabular; 435 linhas de tabela foram preservadas como GFM, mantendo a associação entre coluna e valor.
- **Citação precisa.** Com o `.md` no repositório, cada afirmação do memorial pôde ser ancorada em documento e seção (`[R1 §2.3.1]`), e o agente pôde reler apenas o trecho necessário.
- **Consumo previsível.** Os ~75 KB de Markdown representam uma fração pequena da janela de contexto, mesmo somando o memorial derivado.

**Não funcionou bem**

- **Esquemático elétrico.** O PDF vetorial de 1 página virou 40 linhas de tabela desestruturada: os rótulos de rede e nomes de componente aparecem, mas **sem posicionamento**. A conversão serve como índice de sinais, não como substituto do circuito — por isso, no memorial, todo valor de componente derivado do esquemático está marcado como "confirmar no PDF original".
- **Números e unidades em colunas próximas.** Em trechos com tabelas muito densas, a extração juntou rótulos de linhas vizinhas; qualquer dado crítico deve ser conferido contra o original.

> [!TIP]
> Conclusão prática do caso: **converta para Markdown o que é texto, mantenha o PDF para o que é geometria.** Manuais, comandos AT e planilhas ganham muito; diagramas, esquemáticos e plantas perdem informação e devem permanecer como original.

---

## Estudo de caso — engenharia reversa do firmware

O memorial da plataforma de referência fechou o que **a documentação diz**. Faltava o que **o firmware
faz**. A única fonte disponível era `FIRMWARE/LSN50_AU915_v1.8.1.hex` — uma imagem **mais nova que os
manuais** (v1.8.1 contra v1.7.4 do manual do usuário e v1.6.3 dos comandos AT) e **sem código-fonte,
sem projeto de compilação e sem mapa de memória publicado**.

O objetivo não foi clonar o produto: foi obter a **lógica de operação** — estruturas, formatos,
algoritmos e contratos de payload — para especificar um dispositivo novo com rastreabilidade, em vez de
herdar as suposições do manual. O resultado é `docs/re/firmware-lsn50-v1.8.1-au915.md`, e cada afirmação
carrega o endereço onde foi lida.

### Por que o manual não bastava

| Pergunta de projeto | Manual convertido | Binário analisado |
|---|---|---|
| Quantos modos de trabalho existem? | 6 | **9** (`"Mode of range is 1 to 9"`) |
| Quantas entradas de interrupção? | 1 | **3** — PB14, PB15 e PA4, com contadores independentes |
| Layout do byte 7 do payload | modo nos bits 2‑6 | **sem** os bits de modo: `(PB14<<7) + (entrada digital<<1) + (sensor I2C)` |
| Ordem dos bytes de peso no MOD5 | big‑endian | `b0, b3, b2` |
| Comandos AT | conjunto do manual v1.6.3 | **61** no binário, dos quais **17 não aparecem** no manual |
| Downlink | faixa clássica | faixa clássica `0x01`–`0x1F` **mais** extensões `0x20`–`0x33` |

Nenhuma dessas divergências aparece em um `diff` de documentos: elas só existem porque havia um binário
para desmontar e um texto de referência para comparar.

### Método: uma cadeia reprodutível

```mermaid
flowchart TB
  H["LSN50_AU915_v1.8.1.hex<br/>250.313 B, checksums validos"] --> B["binario contiguo<br/>88.976 B em 0x08000000..0x08015B8F"]
  B --> D["desmontagem Thumb / Cortex-M0+<br/>Capstone 5 + anotacao de literal pools"]
  D --> G["grafo de chamadas<br/>604 funcoes, 88.608 B cobertos"]
  G --> R["leitura dirigida<br/>main, laco, parser AT, payload, downlink, EEPROM"]
  R --> M["Markdown + CSV<br/>firmware-lsn50-v1.8.1-au915.md, at-commands.csv, functions-map.csv"]
```

1. Intel HEX → binário contíguo em `0x08000000..0x08015B8F` (`tools/hexparse.py`).
2. Desmontagem linear ARM **Thumb / Cortex‑M0+** com Capstone 5 (`tools/dsm.py`), tolerante a bytes
   inválidos — o *sweep* não para em dados — com anotação automática dos *literal pools* (valor + string).
3. Extração de strings com endereço (`tools/an.py strings`), agrupadas por faixa para delimitar módulos.
4. Grafo de chamadas por alvos de `BL/BLX` mais heurística de início de função (prólogo logo após
   `bx lr` / `pop {..,pc}` / `b`) → **604 funções**, cobrindo 88.608 bytes (`tools/analyze.py`).
5. Perfil por função — chamadores, chamados, strings referenciadas, globais de RAM e registradores de
   periférico — consolidado em `docs/re/functions-map.csv` (`tools/show.py`, `tools/mkmap.py`).
6. Leitura manual dirigida: `main`, laço principal, parser AT, montador de payload, dispatcher de
   downlink, drivers de sensor, GPIO/trilhos e EEPROM.
7. Extração da tabela de comandos AT e geração de CSV (`tools/attable.py`, `tools/mkcsv.py`).

| Ferramenta | Função |
|---|---|
| `hexparse.py` | Intel HEX → binário contíguo, validando os registros e a contiguidade |
| `analyze.py` | inventário de funções por alvos `BL/BLX`, vetores de interrupção e prólogos |
| `dsm.py` | desmontagem anotada de um intervalo (valores e strings dos *literal pools*) |
| `an.py` | strings com endereço, tabela de vetores e hexdump |
| `show.py`, `mkmap.py` | perfil por função e geração de `functions-map.csv` |
| `attable.py`, `mkcsv.py` | dump da tabela AT e geração de `at-commands.csv` |
| `xref.py`, `scanptr.py`, `tbl.py`, `payload.py` | consultas pontuais: quem aponta para um endereço, ocorrências de um ponteiro, leitura de tabela e sequências de escrita do payload |

Nenhuma toolchain ARM foi instalada: a desmontagem é 100 % Capstone (`capstone==5.0.7`, Python 3.12).

### O que o binário revelou

| Dimensão | Achado |
|---|---|
| Identidade | banner `LSN50 Device`, `Image Version: v1.8.1`, pilha `LoRaWan Stack: DR-LWS-007`, banda `AU915` **compilada** (sem comando AT de troca) |
| Flash e RAM | 88.976 B de 192 KB (46 %); 20 KB de RAM = 652 B de dados RW + 6.964 B de BSS; pilha de ~12,8 KB |
| Funções | 604, cobrindo 88.608 B — mapa de módulos por faixa de endereço (runtime, drivers, HAL, pilha LoRaWAN, aplicação, AT) |
| Console AT | 61 entradas de 24 B em `0x08013E34`, com ponteiros de `get`/`set`/`run`/`help`; **17 comandos** ausentes do manual v1.6.3 |
| Modos de trabalho | `switch` de 9 braços no montador de payload; payloads de 11 B na maioria, 12 B no MOD3 e **17 B no MOD9** |
| Entradas digitais | EXTI0_1/EXTI2_3/EXTI4_15 na tabela de vetores, combinadas com *polling* de PB14/PB15/PA4 no laço |
| Downlink | dispatcher em `0x0800845C`; extensões `0x20`–`0x33` com validação explícita de comprimento e faixa |
| Persistência | EEPROM de dados mapeada em `0x08080000`, sem driver de emulação; assinatura de 4 palavras dispara `factory_init`; `AT+FDR` preserva chaves |
| Toolchain | Keil MDK/ARMCC (tabela de *scatter-load* e *literal pools*), núcleo Cortex‑M0+ Thumb *only* |

Da leitura do laço principal (`0x080124D6`) saíram os princípios de arquitetura que o firmware novo deve
reproduzir:

- **Nada bloqueia.** Cada etapa é um flag verificado em um único laço; nenhum caminho espera por rádio, sensor ou console.
- **Um único caminho de transmissão.** Montar payload → depositar no descritor → emitir evento à pilha MAC (`0x08008A38`).
- **Uma única função de aquisição.** `0x08001B10` serve ao uplink e ao `AT+GETSENSORVALUE`, de modo que console e rádio nunca divirjam.
- **Detecção de borda por *polling*** das três entradas digitais a cada volta, com as IRQs mantendo os contadores por hardware.
- **Duas fontes de uplink:** por timer (`AT+TDC`) e por evento (mudança de entrada, interrupção ou comando AT).

### Confiança, limites e pontos abertos

- Cada linha do documento é marcada como **[V]** verificada no código desmontado (com endereço), **[I]**
  inferida por padrão de código/constante ou **[A]** a confirmar.
- A análise é **estática**: nada foi executado em hardware. Doze pontos permanecem **[A]** — polaridade do
  trilho de +5 V, instância e pinos do UART de console, enumeração opcode a opcode do downlink clássico,
  layout interno dos blocos de EEPROM, entre outros.
- A varredura automática por literais **subestima o GPIOA**, que é montado por deslocamento de imediato; as
  leituras de PA4/PA12 só apareceram na leitura manual dirigida. Nenhum resultado automático foi aceito sem
  essa conferência.

### Artefatos

| Artefato | Conteúdo |
|---|---|
| `docs/re/firmware-lsn50-v1.8.1-au915.md` | lógica do firmware: mapa de memória e de módulos, 604 funções, laço principal, payload dos 9 modos, parser AT, downlink, EEPROM, plano AU915 e guia de recodificação |
| `docs/re/at-commands.csv` | as **61** entradas da tabela de comandos AT, com endereço de entrada e os 4 ponteiros de handler |
| `docs/re/functions-map.csv` | inventário das 604 funções com papel inferido, strings, periféricos e globais de RAM |
| `docs/re/tools/` | pipeline reprodutível (HEX → binário → desmontagem anotada → tabelas), com `README.md` |

Reprodução da cadeia:

```bash
cd docs/re/tools
python3 -m venv .venv && .venv/bin/pip install capstone

python3 hexparse.py ../../../FIRMWARE/LSN50_AU915_v1.8.1.hex lsn50.bin
python3 analyze.py                        # funcs.json / funcs.txt
python3 mkmap.py                          # ../functions-map.csv
python3 attable.py && python3 mkcsv.py    # ../at-commands.csv
```

### Relação com o pipeline de conversão

Os dois artefatos se completam, e é isso que justifica os dois estarem neste repositório:

- **A conversão entregou a linha de base.** Os três manuais em Markdown deram o texto pesquisável para
  comparar com o binário — tabela de comandos, faixa de modos, layouts de payload, mapa de canais.
- **A engenharia reversa entregou o mesmo tipo de artefato.** Texto UTF-8 no repositório, citável por
  linha e por endereço, leve na janela de contexto e revisável por `git diff`.
- **O resultado alimenta a especificação.** `docs/memorial-newdevice.md` declara-se derivado da análise e
  referencia endereços para cada requisito **[V]**, em vez de repetir a documentação do fornecedor.

> [!NOTE]
> Documento convertido e documento desmontado respondem a perguntas diferentes: o manual diz o que o
> produto deveria fazer; o binário diz o que ele faz. Quando os dois divergem, a divergência é o achado —
> e ela só é visível porque ambos estão em texto, no mesmo repositório.

---

## Comandos usados no estudo de caso

Conversão dos PDFs do diretório `Node-Dragino - LSN50v2/`, gravando um `.md` ao lado de cada original:

```bash
cd "Node-Dragino - LSN50v2"

for f in *.pdf; do
  out="${f%.pdf}.md"
  echo "=== $f -> $out"
  npx -y @firecrawl/anydoc "$f" -o "$out"
  echo "exit=$?"
done

ls -la *.md
```

Os três arquivos retornaram `exit=0`. Para converter um arquivo específico:

```bash
anydoc "LSN50_LoRa_Sensor_Node_UserManual_v1.7.4.pdf" \
  -o "LSN50_LoRa_Sensor_Node_UserManual_v1.7.4.md"
```

Inspeção dos resultados e conferência de estrutura antes de alimentar o contexto:

```bash
wc -l *.md                       # volume por arquivo
grep -c '^|' *.md                # linhas de tabela preservadas
grep -c '^#' *.md                # hierarquia de headings
```

---

## Solução de problemas

| Sintoma | Causa provável | Correção |
|---|---|---|
| `exit 3` | Páginas sem camada de texto (digitalização) | `anydoc <arquivo> -o <saida>.md --ocr hosted` |
| `exit 2` | Argumentos inválidos ou `--format` incompatível | Revisar a linha de comando; usar `--format` apenas quando a detecção não puder funcionar |
| `exit 1` | Arquivo corrompido, protegido por senha ou não suportado | Confirmar a integridade do original e se o formato está na lista de suportados |
| Markdown gerado vazio ou quase vazio | PDF só de imagens **ou** extensão errada induzindo o parser | Tentar `--ocr hosted`; se for outro formato, informar `--format` |
| CSV pela entrada padrão falha | Não há conteúdo para detecção | `anydoc - --format csv < dados.csv` |
| `anydoc: command not found` | Instalação global ausente ou fora do `PATH` | Usar `npx -y @firecrawl/anydoc` ou corrigir o prefixo global do npm |
| Tabelas fora de ordem | Layout denso do documento original | Conferir os dados críticos no original; considerar converter apenas as seções necessárias |

---

## Referências

- Skill `convert-documents-to-markdown` — `.agents/skills/convert-documents-to-markdown/SKILL.md`
- Firecrawl Parse (OCR hospedado) — [firecrawl.dev/parse](https://firecrawl.dev/parse)
- Estudo de caso (documentos) — `docs/memorial.txt`
- Estudo de caso (firmware) — `docs/re/firmware-lsn50-v1.8.1-au915.md`, `docs/re/at-commands.csv`, `docs/re/functions-map.csv`
- Pipeline de engenharia reversa — `docs/re/tools/README.md`
- Especificação derivada do dispositivo novo — `docs/memorial-newdevice.md`
- Originais e Markdown convertidos — `Node-Dragino - LSN50v2/`
- Imagem analisada — `FIRMWARE/LSN50_AU915_v1.8.1.hex`

