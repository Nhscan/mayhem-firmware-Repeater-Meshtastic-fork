#!/usr/bin/env python3
"""Check IPC allocation without changing an existing upstream legacy alias."""
from pathlib import Path
import re

text = (Path(__file__).resolve().parents[1] / 'firmware/common/message.hpp').read_text(encoding='utf-8')
body = text.split('enum class ID : uint32_t {', 1)[1].split('};', 1)[0]
pairs = re.findall(r'^\s*(\w+)\s*=\s*(\d+)\s*,', body, flags=re.M)
slots = {}
for name, value in pairs:
    slots.setdefault(int(value), set()).add(name)
# Upstream already shares 58. Preserve its ABI and reject any new collision.
duplicates = {value: names for value, names in slots.items() if len(names) > 1}
assert duplicates == {58: {'FSKRxConfigure', 'BlePacket'}}, duplicates
assert sorted(slots) == list(range(max(slots) + 1)), 'Unexpected gaps in dispatch slots'
print(f'PASS IPC ABI: {len(slots)} consecutive slots; upstream legacy alias retained, no new collisions')
