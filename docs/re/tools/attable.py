#!/usr/bin/env python3
"""Dump da tabela de comandos AT (60 entradas x 24 bytes @ 0x08013E34)."""
import os, struct
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()


def rd(a, n):
    return DATA[a - BASE:a - BASE + n]


def cstr(a, m=64):
    b = rd(a, m); z = b.find(b'\x00')
    return b[:z].decode('ascii', 'replace') if z > 0 else ''


START, N, STRIDE = 0x08013E34, 61, 24
for i in range(N):
    a = START + i * STRIDE
    name, ln, f1, f2, f3, help_ = struct.unpack('<6I', rd(a, 24))
    print(f"[{i:2d}] {a:08X} {cstr(name):<20} len={ln:<3} f1={f1:08X} f2={f2:08X} f3={f3:08X}  {cstr(help_, 60)[:60]}")
