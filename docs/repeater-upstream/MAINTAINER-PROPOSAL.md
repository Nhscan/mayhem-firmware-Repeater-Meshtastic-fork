# Auto Repeater: maintainer scope proposal

I would like guidance on an acceptable scope for an Auto Repeater contribution to Mayhem. I have separated the repeater from my Meshtastic fork and measured it against upstream next before opening a PR.

The app records a threshold-triggered signal, waits a configured delay, plays it back on the selected TX frequency and returns to listening. It also offers manual playback, recording retention, gain settings and repeat/cooldown controls. The existing combined fork has been tested on my PortaPack; the newly isolated candidate still needs physical testing.

## Integration and measured limitation

The interface is an external Transceiver app on the SD card. The engine and file workers currently remain in firmware. Capture/replay/audio images switch beneath the external UI, so the app reserves the largest image's code region to avoid overwrite.

The isolated branch retains normal built-in baseband SPI storage and excludes Meshtastic, global SD-loader changes, updater changes and combined-fork releases.

The initial build against upstream 5bc230848cb17c666f34d07b70062bed682da1a2 compiled and linked, but final image generation required 1,066,628 bytes against the HackRF One limit of 1,048,576 bytes: **18,052 bytes too large**. The external UI linked section was 14,984 bytes. Capture linked at 24,608 bytes and recorded-audio TX at 18,496 bytes, so simply moving the remaining engine into that same external region is not a demonstrated solution.

[Source and preparation branch](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork/tree/upstream/repeater-only)

[Initial ARM build and size evidence](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork/actions/runs/45514616884)

Five portable regression programs passed locally and on Linux, including 1,000 automatic control cycles, file conversion, waveform recognition and capture-quality accounting. These are software checks, not RF or hardware proof of this candidate.

## Requested guidance

Would you consider a focused automatic IQ capture/replay app first, with file conversion, live protocol recognition and recorded-audio modes left for later? Or would you prefer a full-feature version with a separately reviewed, app-specific storage/loading design?

I would keep the full-feature working fork available while preparing any smaller upstream version. I am not proposing to relocate the other apps' basebands, raise the flash limit or submit an oversized build.

Before an implementation PR, I would provide a passing build with flash/RAM and app-layout evidence, physical testing of that exact version, real RF peer evidence, screenshots, documentation and attribution/license review. Development and this preparation used AI assistance; contributor ownership and human review are required.

This is a discussion draft. No maintainer message, upstream issue or PR has been sent for it.
