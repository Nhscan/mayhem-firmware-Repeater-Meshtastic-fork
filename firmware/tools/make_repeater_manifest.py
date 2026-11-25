#!/usr/bin/env python3
"""Bind app-specific SD radio images to the exact external-app build."""
from pathlib import Path
import sys

def descriptor(path):
    data = Path(path).read_bytes()
    if not data or len(data) % 4:
        raise ValueError('Radio image must contain whole 32-bit words: ' + path)
    checksum = 2166136261
    for value in data:
        checksum = ((checksum ^ value) * 16777619) & 0xffffffff
    return '{%dU, 0x%08xU}' % (len(data), checksum)

if __name__ == '__main__':
    output = Path(sys.argv[1])
    output.write_text(
        '// Generated from this build; do not edit.\n#pragma once\n'
        '#include "external/auto_repeater/repeater_radio_image.hpp"\n'
        'namespace ui::external_app::auto_repeater {\n'
        'constexpr RadioImage capture_radio_image' + descriptor(sys.argv[2]) + ';\n'
        'constexpr RadioImage audio_radio_image' + descriptor(sys.argv[3]) + ';\n}\n',
        encoding='utf-8')
