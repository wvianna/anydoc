#!/usr/bin/env python3
"""Extrai, por caso de MOD, a sequencia de escritas no buffer de payload.
Heuristica: acompanha o registrador que aponta para o buffer (carregado de
[0x200000EC]) e imprime indice + expressao de origem."""
import os, sys, re, struct
from capstone import *
from capstone.arm import *
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()
md = Cs(CS_ARCH_ARM, CS_MODE_THUMB + CS_MODE_MCLASS)
md.detail = True


def rd(a, n=4):
    return DATA[a - BASE:a - BASE + n]


CASES = [(1, 0x0800E23C, 0x0800E312), (2, 0x0800E312, 0x0800E3B6),
         (3, 0x0800E3B6, 0x0800E4A8), (4, 0x0800E4A8, 0x0800E55E),
         (5, 0x0800E55E, 0x0800E60A), (6, 0x0800E60A, 0x0800E678),
         (7, 0x0800E678, 0x0800E728), (8, 0x0800E728, 0x0800E7BE),
         (9, 0x0800E7BE, 0x0800E880)]


def scan(lo, hi):
    a = lo
    ptrs = {}          # reg -> 'payload'
    desc = set()       # regs que contem 0x200000EC
    last = {}          # reg -> descricao da ultima origem
    out = []
    while a < hi:
        ins = next(md.disasm(rd(a, 4), a, 1), None)
        if ins is None:
            a += 2; continue
        mn, ops = ins.mnemonic, ins.op_str
        # ldr rX,[pc,#imm] -> descritor se o pool valer 0x200000EC
        m = re.match(r'(\w+), \[pc, #(0x[0-9a-f]+)\]', ops)
        if mn == 'ldr' and m:
            pool = ((a + 4) & ~3) + int(m.group(2), 16)
            val = struct.unpack_from('<I', rd(pool, 4))[0]
            if val == 0x200000EC:
                desc.add(m.group(1))
            elif val == 0x20000094:
                last[m.group(1)] = 'APPSTRUCT'
        m = re.match(r'(\w+), \[(\w+)\]', ops)
        if mn == 'ldr' and m and m.group(2) in desc:
            ptrs[m.group(1)] = 'payload'
        if mn == 'ldr' and m and m.group(2) in ptrs:
            ptrs[m.group(1)] = 'payload'
        # leituras de origem
        m = re.match(r'(\w+), \[sp, #(0x[0-9a-f]+)\]', ops)
        if mn == 'ldr' and m:
            last[m.group(1)] = f"[sp+{m.group(2)}] float"
        m = re.match(r'(\w+), \[sp, #(0x[0-9a-f]+)\]', ops)
        if mn == 'ldrh' and m:
            last[m.group(1)] = f"[sp+{m.group(2)}] u16"
        if mn == 'ldrb' and m:
            last[m.group(1)] = f"[sp+{m.group(2)}] u8"
        m = re.match(r'(\w+), \[r4, #(0x[0-9a-f]+)\]', ops)
        if mn == 'ldrh' and m:
            last[m.group(1)] = f"[0x20000094+{m.group(2)}] u16"
        if mn == 'ldrb' and m:
            last[m.group(1)] = f"[0x20000094+{m.group(2)}] u8"
        # escritas
        m = re.match(r'(\w+), \[(\w+)(?:, #(0x[0-9a-f]+))?\]', ops)
        if mn == 'strb' and m and ptrs.get(m.group(2)) == 'payload':
            idx = int(m.group(3), 16) if m.group(3) else 0
            src = last.get(m.group(1), m.group(1))
            out.append((idx, src, a))
        if mn == 'movs' and ops.startswith('r6, #0x'):
            out.append(('len', ops, a))
        a += ins.size
    return out


for n, lo, hi in CASES:
    print(f"\n##### MOD n={n} (0x{lo:08X}..0x{hi:08X})")
    for item in scan(lo, hi):
        print("   ", item)
