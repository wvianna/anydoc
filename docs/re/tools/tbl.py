#!/usr/bin/env python3
"""Interpreta um intervalo como tabela de palavras e resolve ponteiros."""
import os, struct, sys
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()


def read(a, n=None):
    n = len(DATA) - (a - BASE) if n is None else n
    return DATA[a - BASE:a - BASE + n]


def cstr(a, maxlen=48):
    b = read(a, maxlen)
    z = b.find(b'\x00')
    return b[:z].decode('ascii', 'replace') if z > 0 else None


start = int(sys.argv[1], 16)
end = int(sys.argv[2], 16)
for i in range(0, end - start, 4):
    a = start + i
    v = struct.unpack('<I', read(a, 4))[0]
    tag = ''
    if BASE + 0x100 <= v < BASE + len(DATA):
        s = cstr(v)
        tag = f'-> "{s}"' if s else f'-> code/data {v:08X}'
    elif 0x20000000 <= v < 0x20002000:
        tag = f'-> RAM {v:08X}'
    elif v < 0x100:
        tag = f'-> small {v}'
    print(f"{a:08X}: {v:08X}  {tag}")
