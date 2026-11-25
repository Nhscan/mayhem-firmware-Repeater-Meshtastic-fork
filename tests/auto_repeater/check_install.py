#!/usr/bin/env python3
"""Check the exact updater archive and matching repeater SD modules."""
from pathlib import Path
import struct
import sys
import tarfile

build = Path(sys.argv[1] if len(sys.argv) > 1 else 'build')
fw = build / 'firmware'
binary = (fw / 'portapack-mayhem-firmware.bin').read_bytes()
assert len(binary) == 1048576
assert sum(struct.unpack('<' + 'I' * (len(binary) // 4), binary)) & 0xffffffff == 0
archives = list(fw.glob('*.ppfw.tar'))
assert len(archives) == 1, archives
with tarfile.open(archives[0], mode='r:') as archive:
    members = archive.getmembers()
    names = [m.name for m in members]
    for relative in ['APPS/auto_repeater.ppma', 'BASEBAND/PRCP.bin', 'BASEBAND/PRAT.bin']:
        assert relative in names, relative
        source = fw / ('application' if relative.startswith('APPS/') else 'baseband') / Path(relative).name
        assert archive.extractfile(relative).read() == source.read_bytes(), relative
    firmware = [m for m in members if m.isfile() and m.name.startswith('FIRMWARE/')]
    assert len(firmware) == 1 and firmware[0].name.endswith('.bin')
    assert archive.extractfile(firmware[0]).read() == binary
    flash_index = names.index(firmware[0].name)
    assert all(names.index(n) < flash_index for n in ['APPS/auto_repeater.ppma', 'BASEBAND/PRCP.bin', 'BASEBAND/PRAT.bin'])
    with archives[0].open('rb') as stream:
        for member in members:
            stream.seek(member.offset + 257)
            assert stream.read(6) == b'ustar\0', member.name
print('PASS firmware: 1 MiB, checksum valid, USTAR update with exact apps/radio files before firmware')
