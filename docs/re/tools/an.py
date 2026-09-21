#!/usr/bin/env python3
"""Utilitarios de analise: strings com endereco, vetores, xrefs, disassembly."""
import os, struct, sys, json, re
from capstone import *

BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()


def read(addr, n):
    off = addr - BASE
    return DATA[off:off + n]


def strings(minlen=4, encoding='ascii'):
    out = []
    if encoding == 'ascii':
        pat = re.compile(rb'[\x20-\x7e]{%d,}' % minlen)
    else:
        pat = re.compile(rb'(?:[\x20-\x7e]\x00){%d,}' % minlen)
    for m in pat.finditer(DATA):
        s = m.group()
        if encoding == 'utf16':
            s = s.decode('utf-16-le', 'replace')
        else:
            s = s.decode('ascii', 'replace')
        out.append((BASE + m.start(), s))
    return out


def vectors():
    sp = struct.unpack_from('<I', DATA, 0)[0]
    out = [("SP", sp)]
    for i in range(1, 70):
        v = struct.unpack_from('<I', DATA, i * 4)[0]
        if v == 0:
            continue
        out.append((f"[{i:2d}] {i-16 if i >= 16 else i}", v))
    return out


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'strings':
        minlen = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        for a, s in strings(minlen):
            print(f"{a:08X}  {s}")
    elif cmd == 'vectors':
        for n, v in vectors():
            print(f"{n:12s} 0x{v:08X}")
    elif cmd == 'hexdump':
        a = int(sys.argv[2], 16); n = int(sys.argv[3], 16)
        for i in range(0, n, 16):
            chunk = read(a + i, 16)
            print(f"{a+i:08X}  " + ' '.join(f"{b:02X}" for b in chunk))
