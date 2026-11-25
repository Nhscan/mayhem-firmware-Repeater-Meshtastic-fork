#!/usr/bin/env python3
"""Validate actual external-app layout and retained built-in radio images."""
from pathlib import Path
import struct
import sys

build = Path(sys.argv[1] if len(sys.argv) > 1 else 'build')
base = build / 'firmware/baseband'
app = (build / 'firmware/application/auto_repeater.ppma').read_bytes()
address = struct.unpack_from('<I', app)[0]
length = struct.unpack_from('<I', app, 80)[0]
images = ['PCAP', 'PREP', 'PAMA', 'PNFM', 'PWFM', 'PRAT']
reserve = max((base / (tag + '.bin')).stat().st_size for tag in images)
assert app[76:80] == b'ARSV'
assert address == 0x10080000 + reserve, (address, reserve)
assert length + reserve <= 40960, (length, reserve)
assert len(app) == length + reserve + 4
assert len(app) % 4 == 0
assert sum(struct.unpack('<' + 'I' * (len(app) // 4), app)) & 0xffffffff == 0
assert app[length:-4] == (base / 'ARSV.bin').read_bytes()
print(f'PASS external UI: {length} bytes + {reserve} bytes radio reserve / 40960')
spi = (base / 'baseband.img').read_bytes()
offset = 0
tags = []
while offset + 12 <= len(spi):
    tag, size = struct.unpack_from('<4sI', spi, offset)
    if tag == bytes(4):
        break
    assert offset + 12 + size <= len(spi), (tag, size)
    tags.append(tag.decode('ascii'))
    offset += 12 + size
assert all(tag in tags for tag in images + ['PFUT', 'HRF1']), tags
print('PASS built-in capture/replay/audio/updater/factory images retained')
