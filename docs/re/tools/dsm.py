#!/usr/bin/env python3
"""Disassembler anotado (Thumb, Cortex-M0+) tolerante a bytes invalidos.
Uso: disasm.py <start_hex> <end_hex> [> saida.asm]"""
import os, sys, struct
from capstone import *
from capstone.arm import *

BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()
md = Cs(CS_ARCH_ARM, CS_MODE_THUMB + CS_MODE_MCLASS)
md.detail = True


def read(a, n):
    return DATA[a - BASE:a - BASE + n]


def annotate(ins, addr):
    notes = []
    for o in ins.operands:
        if o.type == ARM_OP_MEM and o.mem.base == ARM_REG_PC:
            pool = ((addr + 4) & ~3) + o.mem.disp
            if BASE <= pool < BASE + len(DATA) - 4:
                val = struct.unpack_from('<I', read(pool, 4))[0]
                note = f"; [0x{pool:08X}]=0x{val:08X}"
                if BASE <= val < BASE + len(DATA):
                    s = read(val, 64).split(b'\x00')[0]
                    if len(s) >= 3 and all(0x20 <= c < 0x7f for c in s):
                        note += f' "{s.decode("ascii", "replace")}"'
                    else:
                        note += " {" + read(val, 12).hex(' ') + "}"
                elif 0x20000000 <= val < 0x20006000:
                    note += " (RAM)"
                notes.append(note)
        if o.type == ARM_OP_IMM and ins.mnemonic in ('adr', 'add'):
            val = o.imm
            s = read(val, 64).split(b'\x00')[0]
            if len(s) >= 3 and all(0x20 <= c < 0x7f for c in s):
                notes.append(f'"{s.decode("ascii", "replace")}"')
    return ' '.join(notes)


def run(start, end):
    a = start
    while a < end:
        ins = next(md.disasm(read(a, 4), a, 1), None)
        if ins is None:
            print(f"{a:08X}  {read(a,2).hex():<10} .hword   0x{struct.unpack_from('<H', read(a,2))[0]:04X}")
            a += 2
            continue
        if ins.address + ins.size > end:
            break
        n = annotate(ins, ins.address) or ''
        print(f"{ins.address:08X}  {ins.bytes.hex():<10} {ins.mnemonic:<8} {ins.op_str:<34} {n}")
        a += ins.size


if __name__ == '__main__':
    run(int(sys.argv[1], 16), int(sys.argv[2], 16))
