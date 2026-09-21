#!/usr/bin/env python3
"""Gera docs/re/at-commands.csv a partir da tabela AT em flash."""
import os, struct, csv, sys
BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()


def rd(a, n):
    return DATA[a - BASE:a - BASE + n]


def cstr(a, m=80):
    b = rd(a, m); z = b.find(b'\x00')
    s = b[:z].decode('ascii', 'replace') if z > 0 else ''
    return s.replace('\r', '\\r').replace('\n', '\\n')


out = csv.writer(open('../at-commands.csv', 'w', newline=''))
out.writerow(['idx', 'entry_addr', 'nome', 'tam_nome', 'get_0x08', 'set_0x0C',
              'run_0x10', 'help_0x14'])
START, N, STRIDE = 0x08013E34, 61, 24
for i in range(N):
    a = START + i * STRIDE
    name, ln, f1, f2, f3, h = struct.unpack('<6I', rd(a, 24))
    out.writerow([i, f"0x{a:08X}", cstr(name), ln, f"0x{f1:08X}", f"0x{f2:08X}",
                  f"0x{f3:08X}", cstr(h)])
print("ok")
