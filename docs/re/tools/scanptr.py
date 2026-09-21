#!/usr/bin/env python3
"""Varre a imagem por palavras de 32 bits que apontam para um intervalo dado.
Uso: scanptr.py 0x080158C0 0x08015AE0"""
import os, struct, sys
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()
lo, hi = int(sys.argv[1], 16), int(sys.argv[2], 16)
n = len(DATA) // 4
words = struct.unpack_from('<%dI' % n, DATA, 0)
hits = {}
for i, w in enumerate(words):
    if lo <= w < hi:
        hits.setdefault(BASE + i * 4, []).append(w)
for a in sorted(hits):
    print(f"{a:08X}: " + ', '.join(f"{v:08X}" for v in hits[a]))
print(f"# {len(hits)} palavras em {n} varridas")
