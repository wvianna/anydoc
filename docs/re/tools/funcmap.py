#!/usr/bin/env python3
"""Inventario de funcoes: alvos de BL/BLX, vetores de interrupcao e prologos.
Uso: funcmap.py [--asm] para listar codigo; sem flag, resumo."""
import os, struct, sys, re, collections, subprocess
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()
LO, HI = BASE, BASE + len(DATA)

# --- 1. alvos de BL/BLX via decodificacao linear (usa o .asm gerado) ---
callers = collections.defaultdict(set)
targets = collections.Counter()
pat = re.compile(r'^([0-9A-F]{8})  [0-9a-f ]+\s(bl|blx)\s+#0x([0-9A-Fa-f]+)')
for line in open('full1.asm'):
    m = pat.match(line)
    if m:
        a, t = int(m.group(1), 16), int(m.group(3), 16)
        targets[t] |= 1
        callers[t].add(a)
for line in open('full.asm'):
    m = pat.match(line)
    if m:
        a, t = int(m.group(1), 16), int(m.group(3), 16)
        targets[t] |= 1
        callers[t].add(a)

# --- 2. vetores ---
vec = []
for i in range(1, 48):
    v = struct.unpack_from('<I', DATA, i * 4)[0]
    if v:
        vec.append(v & ~1)

starts = sorted(set(list(targets) + vec))
print(f"# {len(starts)} funcoes/alvos identificados")

# limites: usa o proximo alvo/endereco de codigo
for s in starts:
    nxt = min([x for x in starts if x > s], default=HI)
    size = nxt - s
    if size > 0x1000:
        size = 0x1000
    kind = 'VEC' if s in vec else '   '
    print(f"{s:08X} {kind} size<=0x{size:04X} callers={len(callers.get(s,()))}")
