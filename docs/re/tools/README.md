# Ferramentas de engenharia reversa — firmware LSN50 AU915 v1.8.1

Scripts usados para produzir `docs/re/firmware-lsn50-v1.8.1-au915.md`.
Cadeia reprodutível, sem toolchain ARM (usa **Capstone** para desmontar Thumb/Cortex‑M0+).

## Dependências

```bash
python3 -m venv .venv && .venv/bin/pip install capstone
```

## Pipeline

```bash
cd docs/re/tools

# 1. Intel HEX -> binario contiguo (0x08000000..0x08015B8F)
python3 hexparse.py            # aceita: hexparse.py <hex> [saida.bin]
                               # saida padrao: lsn50.bin (ou $LSN50_BIN)

# 2. inventario de funcoes (usa o binario em $LSN50_BIN / lsn50.bin)
python3 analyze.py             # gera funcs.json e funcs.txt
python3 show.py 0x0800F000 0x08012500 [--str]   # perfil por faixa
python3 mkmap.py               # gera ../functions-map.csv

# 3. tabela de comandos AT
python3 attable.py             # dump legivel das 61 entradas (0x08013E34)
python3 mkcsv.py               # gera ../at-commands.csv

# 4. consultas pontuais
python3 dsm.py 0x0801245C 0x08012868   # desmontagem anotada de um intervalo
python3 an.py strings 5                # strings com endereco
python3 an.py vectors                  # tabela de vetores
python3 an.py hexdump 0800E5F4 0x18    # hexdump
python3 xref.py 08015954 08015A10      # quem aponta para um endereco (literal pool)
python3 tbl.py 08013E34 080143F0       # interpreta um intervalo como tabela de palavras
python3 scanptr.py 0x20000094 0x200000B4  # varre a imagem por ponteiros para uma faixa
python3 payload.py                     # sequencias de escrita do payload por MOD
```

Variável de ambiente `LSN50_BIN` sobrescreve o caminho do binário derivado
(útil para manter os artefatos fora do repositório).

## Notas de método

- `analyze.py` faz desmontagem linear e tolera dados no meio do código (não para no primeiro
  byte inválido, o que acontece com `Cs.disasm` puro).
- O início de função é detectado por: alvo de `BL/BLX`, entrada da tabela de vetores, ou prólogo
  (`push`/`sub sp`) imediatamente após `bx lr` / `pop {..,pc}` / `b`.
- Strings são lidas de *literal pools* (`ldr rX,[pc,#imm]`) **e** de `adr` (endereço =
  `align4(PC+4) + imm`); CR/LF/TAB são aceitos e escapados na saída.
- Periféricos são inferidos pelos literais de registrador (faixas `0x40000000`/`0x50000000`).
