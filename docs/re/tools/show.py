#!/usr/bin/env python3
"""Mostra o perfil de funcoes cujo endereco esta em [lo,hi).
Uso: show.py 0x0800F000 0x08012500 [--str]"""
import json, sys
funcs = json.load(open('funcs.json'))
lo = int(sys.argv[1], 16)
hi = int(sys.argv[2], 16)
only_str = '--str' in sys.argv
for r in funcs:
    if not (lo <= r['addr'] < hi):
        continue
    if only_str and not r['strings']:
        continue
    print(f"\n== 0x{r['addr']:08X}-0x{r['end']:08X} size=0x{r['size']:X} insn={r['ninsn']} br={r['branches']}")
    if r['callers']:
        print("   <- " + ' '.join(f"{c:08X}" for c in r['callers'][:10]))
    if r['callees']:
        print("   -> " + ' '.join(f"{c:08X}" for c in r['callees'][:20]))
    if r['strings']:
        print("   str: " + ' | '.join(s.replace('\r','\\r').replace('\n','\\n') for s in r['strings'][:12]))
    if r['periph']:
        print("   per: " + ' '.join(r['periph'][:12]))
    if r['ram']:
        print("   ram: " + ' '.join(f"{x:08X}" for x in r['ram'][:14]))
