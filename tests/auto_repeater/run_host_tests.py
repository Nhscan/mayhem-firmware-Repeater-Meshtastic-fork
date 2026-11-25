#!/usr/bin/env python3
"""Compile and run the repeater's portable regression programs."""
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / 'build/repeater-host-tests'
out.mkdir(parents=True, exist_ok=True)
cxx = os.environ.get('CXX', 'g++')
tests = ['control_test', 'sub_test', 'ook_test', 'quality_ui_test', 'file_test', 'radio_image_test']
for name in tests:
    exe = out / (name + ('.exe' if os.name == 'nt' else ''))
    command = [cxx, '-std=c++17', '-O2', '-Wall', '-Wextra', '-Itests/auto_repeater/stubs',
               '-Ifirmware/baseband', '-Ifirmware/common', 'tests/auto_repeater/' + name + '.cpp']
    if name == 'file_test':
        command += ['-DREPEATER_FILE_HOST_TEST', 'firmware/application/repeater_files.cpp']
    command += ['-o', str(exe)]
    subprocess.run(command, cwd=root, check=True)
    args = [str(exe)]
    if name == 'file_test':
        args.append(str(out / 'files'))
    subprocess.run(args, cwd=root, check=True)
    print('PASS ' + name, flush=True)
print('PASS all six repeater host regression programs')
