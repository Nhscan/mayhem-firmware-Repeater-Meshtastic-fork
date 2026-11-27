# Auto Repeater maintainer discussion draft

I have separated Auto Repeater from my Meshtastic fork and prepared a version against Mayhem next at `5bc230848cb17c666f34d07b70062bed682da1a2`. It now passes an ARM build and software checks, but I still need to test this exact version on physical hardware before an implementation PR.

The app records a threshold-triggered signal, waits a configured delay, transmits it on the chosen frequency and returns to listening. It also supports manual playback, retained IQ/WAV recordings, timing/gain controls, RX hopping, optional protocol recognition and RAW/BinRAW SUB conversion. The existing combined fork has user-tested hardware history; that is background rather than proof for this new candidate.

## Integration

The interface and a small radio-file loader are external. The engine and file workers currently remain in main firmware. Only optional capture-recognition and recorded-audio TX modules load from SD; normal built-in Capture, Replay and Audio RX keep their existing SPI storage and global loading behavior.

The SD loader checks exact size, a build-generated integrity value, read completion and the space reserved below the external UI before starting M4. The update archive contains matching assets. CaptureThread exposes a stop/join operation and optional writer stack size while retaining upstream's termination/wakeup behavior. Meshtastic and the broad global SD relocation are excluded.

## Measurements

[Validated source](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/commit/d24764597b3496fafde86f21a911e9c2dc2cbfb6)

[Passing build and logs](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45519543490)

| Check | Result |
| --- | ---: |
| Host regression programs | 6 passed |
| Remaining HackRF One flash | 1,280 bytes |
| External UI + radio reserve | 38,792 / 40,960 bytes |
| Repeater capture known heap headroom | 5,504 bytes |
| Recorded audio known heap headroom | 45,948 bytes |
| USTAR updater and matching files | Passed |

The flash margin is tight. The memory checks bound known allocations rather than proving hardware timing or fragmentation behavior. Earlier attempts keeping the new radio modules in SPI exceeded flash; the app-specific SD arrangement resolves that measured failure without moving other apps' basebands.

Would this integration be an acceptable direction to review after hardware testing, or would you prefer an initial PR with a smaller feature set? I would like agreement on scope and the app-specific SD assets before submitting the implementation.

Before a PR, I would supply exact-build physical/RF evidence, screenshots, operating instructions and attribution/license review. Development and preparation used AI assistance and require contributor ownership and human review.

This remains an unsent discussion draft. Craig has requested no upstream PR, issue or maintainer message at this stage.
