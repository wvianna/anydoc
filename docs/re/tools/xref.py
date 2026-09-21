#!/usr/bin/env python3
"""Xrefs: encontra palavras de 32 bits que apontam para um alvo (literal pools,
vetores, tabelas). Uso: xref.py 08011234 [08011240 ...]"""
import os, struct, sys
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()
LO, HI = BASE, BASE + len(DATA)

words = struct.unpack_from('<%dI' % (len(DATA) // 4), DATA, 0)

targets = [int(a, 16) for a in sys.argv[1:]]
for t in targets:
    hits = [BASE + i * 4 for i, w in enumerate(words)
            if (w & ~1) == (t & ~1) and LO <= (w & ~1) < HI]
    print(f"0x{t:08X}: " + (', '.join(f"@0x{h:08X}" for h in hits) or "(sem xref literal)"))
