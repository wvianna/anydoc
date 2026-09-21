#!/usr/bin/env python3
"""Parser Intel HEX -> binario + mapa de regioes (LSN50 AU915 v1.8.1)."""
import os, sys, json, collections

CAND = ["../../FIRMWARE/LSN50_AU915_v1.8.1.hex",
        "FIRMWARE/LSN50_AU915_v1.8.1.hex",
        "/home/william/git/anydoc/FIRMWARE/LSN50_AU915_v1.8.1.hex"]
PATH = sys.argv[1] if len(sys.argv) > 1 else next((c for c in CAND if os.path.exists(c)), CAND[0])
OUT = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("LSN50_BIN", "lsn50.bin")

mem = {}
bad = 0
base = 0
records = collections.Counter()
start_linear = None
for lineno, line in enumerate(open(PATH), 1):
    line = line.strip()
    if not line.startswith(':'):
        continue
    raw = bytes.fromhex(line[1:])
    n, addr, rtype = raw[0], (raw[1] << 8) | raw[2], raw[3]
    data = raw[4:4 + n]
    csum = (-(sum(raw[:-1]))) & 0xFF
    if csum != raw[-1]:
        bad += 1
    records[rtype] += 1
    if rtype == 0:
        for i, b in enumerate(data):
            mem[base + addr + i] = b
    elif rtype == 1:
        pass
    elif rtype == 2:
        base = int.from_bytes(data, 'big') << 4
    elif rtype == 4:
        base = int.from_bytes(data, 'big') << 16
    elif rtype == 5:
        start_linear = int.from_bytes(data, 'big')
    elif rtype == 3:
        pass

lo, hi = min(mem), max(mem)
print(f"checksums ruins={bad}")
print(f"records={dict(records)} start_linear={start_linear and hex(start_linear)}")
print(f"regiao 0x{lo:08X} .. 0x{hi:08X}  ({hi-lo+1} bytes, {len(mem)} gravados)")

# gaps
gaps = []
prev = None
for a in sorted(mem):
    if prev is not None and a != prev + 1:
        gaps.append((prev + 1, a - 1))
    prev = a
print("gaps:", [(hex(a), hex(b)) for a, b in gaps][:40], "total", len(gaps))

with open(OUT, 'wb') as f:
    f.write(bytes(mem.get(a, 0xFF) for a in range(lo, hi + 1)))
print("bin:", OUT, "base", hex(lo))

json.dump({"base": lo, "end": hi, "start_linear": start_linear},
          open(OUT + ".json", "w"), indent=1)
