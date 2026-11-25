#!/usr/bin/env python3
"""Bound the repeater radio's known peak heap allocations from linked ELF types.

This is a static budget check, not a measurement of fragmentation or RF timing.
Static stacks/BSS are already excluded by the linker's heap symbols.
"""
from pathlib import Path
import sys
from elftools.elf.elffile import ELFFile

base = Path(sys.argv[1] if len(sys.argv) > 1 else 'build') / 'firmware/baseband'

def inspect(name, types):
    with (base / ('baseband_' + name + '.elf')).open('rb') as stream:
        elf = ELFFile(stream)
        symbols = {s.name: s.entry.st_value for s in elf.get_section_by_name('.symtab').iter_symbols()}
        heap = symbols['__heap_end__'] - symbols['__heap_base__']
        sizes = {}
        for cu in elf.get_dwarf_info().iter_CUs():
            for die in cu.iter_DIEs():
                attr = die.attributes.get('DW_AT_name')
                length = die.attributes.get('DW_AT_byte_size')
                if attr and length and attr.value in types:
                    sizes[attr.value] = max(sizes.get(attr.value, 0), length.value)
        assert all(t in sizes for t in types), (name, sizes, types)
        return heap, sizes

for name in ['capture', 'repeater_capture']:
    heap, sizes = inspect(name, [b'CaptureProcessor', b'StreamInput'])
    # Engine's largest ring capture: three 16 KiB buffers. BasebandThread
    # allocates 8192 complex8 DMA samples (16 KiB). Include allocator slack.
    known = sizes[b'CaptureProcessor'] + sizes[b'StreamInput'] + 3 * 16384 + 16384 + 128
    remaining = heap - known
    assert remaining >= 4096, (name, heap, known, remaining)
    print(f'PASS {name} known heap: {known}/{heap} bytes, {remaining} bytes headroom')

heap, sizes = inspect('repeater_audio', [b'RecordedTX', b'StreamOutput', b'AM', b'FM', b'SSB'])
known = sizes[b'RecordedTX'] + sizes[b'StreamOutput'] + max(sizes[t] for t in [b'AM', b'FM', b'SSB']) + 4 * 4096 + 16384 + 128
remaining = heap - known
assert remaining >= 4096, ('repeater_audio', heap, known, remaining)
print(f'PASS recorded audio known heap: {known}/{heap} bytes, {remaining} bytes headroom')
