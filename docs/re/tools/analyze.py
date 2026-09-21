#!/usr/bin/env python3
"""Analise estatica do firmware LSN50 AU915 v1.8.1 (Cortex-M0+ / Thumb).

Produz:
  funcs.json  - uma entrada por funcao: tamanho, callers, callees, strings,
                globais de RAM, perifericos acessados, ramos/loops.
  funcs.txt   - relatorio legivel, ordenado por endereco.
"""
import os, struct, json, collections, re, sys
from capstone import *
from capstone.arm import *

BASE = 0x08000000
DATA = open(os.environ.get('LSN50_BIN', 'lsn50.bin'), 'rb').read()
END = BASE + len(DATA)
md = Cs(CS_ARCH_ARM, CS_MODE_THUMB + CS_MODE_MCLASS)
md.detail = True

RAM_LO, RAM_HI = 0x20000000, 0x20005000
CODE_LO, CODE_HI = BASE, END

PERIPH = {
    0x40000000: 'TIM2', 0x40000400: 'TIM3', 0x40000800: 'TIM6', 0x40000C00: 'TIM7',
    0x40001000: 'TIM21', 0x40001400: 'TIM22', 0x40002800: 'RTC', 0x40002C00: 'WWDG',
    0x40003000: 'IWDG', 0x40003800: 'SPI2', 0x40004400: 'USART2', 0x40004800: 'LPUART1',
    0x40004C00: 'USART4', 0x40005000: 'USART5', 0x40005400: 'I2C1', 0x40005800: 'I2C2',
    0x40005C00: 'USB', 0x40006000: 'USBRAM', 0x40006400: 'CRS', 0x40006800: 'PWR_CR?',
    0x40007000: 'PWR', 0x40007400: 'DAC', 0x40007800: 'I2C3', 0x40007C00: 'LPTIM1',
    0x40009400: 'WW?', 0x40009800: 'LPTIM2?', 0x40010000: 'SYSCFG', 0x40010400: 'EXTI',
    0x40012400: 'ADC1', 0x40012708: 'ADC_COMMON', 0x40013000: 'SPI1', 0x40013800: 'USART1',
    0x40013C00: 'TIM23?', 0x40014000: 'TIM24?', 0x40020000: 'DMA1', 0x40021000: 'RCC',
    0x40022000: 'FLASH', 0x40022400: 'FLASH_PECR?', 0x40023000: 'CRC', 0x40025000: 'RNG',
    0x40026000: 'AES', 0x40026400: 'AES?', 0x50000000: 'GPIOA', 0x50000400: 'GPIOB',
    0x50000800: 'GPIOC', 0x50000C00: 'GPIOD', 0x50001000: 'GPIOE', 0x50001C00: 'GPIOH',
}


def read(a, n=4):
    return DATA[a - BASE:a - BASE + n]


def cstr(a, m=72):
    if not (CODE_LO <= a < CODE_HI):
        return None
    b = read(a, m)
    z = b.find(b'\x00')
    if z < 3:
        return None
    s = b[:z]
    if all(c in (9, 10, 13) or 0x20 <= c < 0x7f for c in s):
        return s.decode('ascii').replace('\r', '\\r').replace('\n', '\\n')
    return None


# ---------------- 1. varredura linear ----------------
insns = {}                      # addr -> (size, mnemonic, op_str, detail)
a = BASE + 0xC0
while a < BASE + 0x15AE0:
    ins = next(md.disasm(read(a, 4), a, 1), None)
    if ins is None:
        insns[a] = (2, '.hword', f'0x{struct.unpack_from("<H", read(a,2))[0]:04X}', None)
        a += 2
        continue
    insns[a] = (ins.size, ins.mnemonic, ins.op_str, ins)
    a += ins.size
addrs = sorted(insns)

# ---------------- 2. limites de funcao ----------------
vec = [struct.unpack_from('<I', DATA, i * 4)[0] & ~1 for i in range(1, 48)]
vec = [v for v in vec if v]
starts = set(vec) | {BASE + 0xC0, BASE + 0xC0 + 0x14}
bl_targets = collections.defaultdict(set)
for ad in addrs:
    size, mn, ops, ins = insns[ad]
    if mn in ('bl', 'blx') and ops.startswith('#0x'):
        t = int(ops[1:], 16)
        if CODE_LO <= t < CODE_HI:
            starts.add(t)
            bl_targets[t].add(ad)
# prologos apos retorno
for i, ad in enumerate(addrs):
    size, mn, ops, ins = insns[ad]
    if mn in ('bx', 'pop', 'b') and (ins and (
            (mn == 'bx' and ops.strip() == 'lr') or
            (mn == 'pop' and 'pc' in ops) or mn == 'b')):
        nxt = ad + size
        if nxt in insns:
            size2, mn2, ops2, ins2 = insns[nxt]
            if mn2 in ('push', 'sub') and ('lr' in ops2 or mn2 == 'sub' and 'sp' in ops2):
                starts.add(nxt)
starts = sorted(x for x in starts if CODE_LO <= x < CODE_HI)

# ---------------- 3. perfil por funcao ----------------
funcs = []
for i, s in enumerate(starts):
    e = starts[i + 1] if i + 1 < len(starts) else BASE + 0x15AE0
    if e <= s:
        continue
    rec = dict(addr=s, end=e, size=e - s, callers=sorted(bl_targets.get(s, ())),
               callees=[], strings=[], ram=[], periph=set(), ninsn=0, branches=0)
    ad = s
    while ad < e and ad in insns:
        size, mn, ops, ins = insns[ad]
        rec['ninsn'] += 1
        if mn in ('bl', 'blx') and ops.startswith('#0x'):
            t = int(ops[1:], 16)
            if t not in rec['callees']:
                rec['callees'].append(t)
        if mn in ('b', 'cbz', 'cbnz', 'beq', 'bne', 'blt', 'bgt', 'ble', 'bge',
                  'bhi', 'bls', 'bhs', 'blo', 'bcc', 'bcs', 'bmi', 'bpl'):
            rec['branches'] += 1
        if ins:
            for o in ins.operands:
                if o.type == ARM_OP_MEM and o.mem.base == ARM_REG_PC:
                    pool = ((ad + 4) & ~3) + o.mem.disp
                    if CODE_LO <= pool < END - 4:
                        val = struct.unpack_from('<I', read(pool, 4))[0]
                        st = cstr(val)
                        if st and len(st) >= 3:
                            if st not in rec['strings']:
                                rec['strings'].append(st)
                        elif RAM_LO <= val < RAM_HI:
                            if val not in rec['ram']:
                                rec['ram'].append(val)
                        for p, name in PERIPH.items():
                            if p <= val < p + 0x400:
                                rec['periph'].add(f"{name}+0x{val-p:X}")
                elif o.type == ARM_OP_IMM and mn in ('adr', 'add') and o.imm != 0:
                    tgt = ((ad + 4) & ~3) + o.imm
                    st = cstr(tgt)
                    if st and len(st) >= 3 and st not in rec['strings']:
                        rec['strings'].append(st)
                    if CODE_LO <= tgt < END - 4:
                        val = struct.unpack_from('<I', read(tgt, 4))[0]
                        if RAM_LO <= val < RAM_HI and val not in rec['ram']:
                            rec['ram'].append(val)
                        for p, name in PERIPH.items():
                            if p <= val < p + 0x400:
                                rec['periph'].add(f"{name}+0x{val-p:X}")
        ad += size
    rec['periph'] = sorted(rec['periph'])
    funcs.append(rec)

json.dump(funcs, open('funcs.json', 'w'), indent=1)

with open('funcs.txt', 'w') as f:
    for r in funcs:
        f.write(f"\n===== 0x{r['addr']:08X}-0x{r['end']:08X} size=0x{r['size']:X} "
                f"insn={r['ninsn']} branches={r['branches']}\n")
        if r['callers']:
            f.write("  chamada por: " + ' '.join(f"{c:08X}" for c in r['callers'][:12]) + "\n")
        if r['callees']:
            f.write("  chama: " + ' '.join(f"{c:08X}" for c in r['callees'][:24]) + "\n")
        if r['strings']:
            f.write("  strings: " + ' | '.join(r['strings'][:14]) + "\n")
        if r['periph']:
            f.write("  perif: " + ' '.join(r['periph'][:10]) + "\n")
        if r['ram']:
            f.write("  RAM: " + ' '.join(f"{x:08X}" for x in r['ram'][:12]) + "\n")
print(f"{len(funcs)} funcoes; total {sum(r['size'] for r in funcs)} bytes")
