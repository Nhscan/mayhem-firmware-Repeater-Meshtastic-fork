#!/usr/bin/env python3
# Reserve room for either Meshtastic M4 image.
import sys
from pathlib import Path

output = Path(sys.argv[1])
images = [Path(name).read_bytes() for name in sys.argv[2:]]
if not images or any(not image for image in images):
    raise SystemExit("Missing or empty LoRa baseband image")
output.write_bytes(max(images, key=len))

