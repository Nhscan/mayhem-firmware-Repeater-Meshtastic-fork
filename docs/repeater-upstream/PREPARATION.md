# Auto Repeater upstream preparation

This branch separates Auto Repeater from Meshtastic for review against Mayhem next at `5bc230848cb17c666f34d07b70062bed682da1a2`.
Source was extracted from Nhscan's tested combined fork at `d2113491810f9877a087c0d43bea785d93bfecbd`.

## Current scope

- External Transceiver app UI: receive/transmit frequencies, trigger threshold, delay, repeat/cooldown controls, recording/file playback, gain controls and status.
- Internal engine and file workers: circular prebuffer, capture quality checks, metadata, RAW/BinRAW SUB conversion and playback scheduling.
- CaptureThread: explicit stop/join while retaining counters and optional writer stack size. Existing upstream shutdown/wakeup fixes remain intact; normal callers keep the 1024-byte default.
- Capture DSP: optional IQ-envelope protocol recognition in a separate SD module (PRCP); the normal built-in Capture image excludes it.
- Recorded audio TX baseband: AM/FM/SSB playback using existing modulators in SD module PRAT.
- ARSV reserve image: keeps the external UI above the largest baseband it switches to in the shared 40 KiB code region.

This candidate preserves normal built-in baseband SPI storage. Only PRCP/PRAT are app-specific SD modules; their size and build-generated integrity hash are checked before startup. It excludes Meshtastic, the global SD-loading fallback, updater alterations, combined-fork release packages and README replacements.
The UI is external, but the engine and file workers remain internal for this first measurement. This is not yet a fully external implementation or a stock-firmware-compatible app download.

## Validation

All five existing portable regression programs passed locally before and after formatting, and on the hosted Linux build:

- Control: 1,000 automatic cycles, timing, quiet mode, repeats/gaps, cancellation and timer wrap.
- SUB parsing: RAW/BinRAW, modulation presets, malformed/unsupported input.
- OOK: generated IQ-envelope waveform decoded as a known Princeton packet; decoding disabled in normal raw mode.
- Quality/UI: retained prebuffer/drop accounting and repaint throttling.
- Files: real conversion routines, pulse timing, circular-buffer reorder and error cleanup.

The host compiler identified an uninitialized array in the existing upstream Security+ v1 decoder when assigning a temporary during repeater decoder reset. The candidate now initializes that array. Passing host tests do not establish all protocol decoders are correct.

The first hosted ARM run compiled and linked the application and radio images, then failed final SPI image generation:

| Item | Result |
| --- | ---: |
| Required final firmware image | 1,066,628 bytes |
| HackRF One flash limit | 1,048,576 bytes |
| Overflow | 18,052 bytes |
| External UI linked section | 14,984 bytes |
| Capture radio linked flash | 24,608 bytes |
| Recorded audio TX linked flash | 18,496 bytes |

[Initial measurement run](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork/actions/runs/45514616884), commit bd4ac213a5c2d435471ba78dddb67828cf183aa0.
That is a failed firmware package, not a passing build. Additional validation reports app relocation/checksum and retained SPI images even if the final firmware exceeds flash. The decoder-array initialization is a subsequent change.
No firmware from this isolated branch has been flashed or physically tested.

## Before asking maintainers to review code

1. Complete ARM compilation and verify flash, M0/M4 memory and external UI/radio overlap limits.
2. Resolve any integration failures and review the decoder warning.
3. Review whether internal engine/file-code footprint is acceptable or a smaller external feature set is needed.
4. Check runtime allocations, capture shutdown, file-worker teardown and radio changes against existing apps.
5. Build a matching install package and test this exact candidate on physical PortaPack hardware and real RF peers.
6. Add current screenshots/video, clear operating instructions, limitations and attribution/license review.
7. Present the final diff and description to Craig for review before opening an upstream PR.

The original fork has user-reported successful hardware tests. Those do not substitute for testing this isolated candidate.
No upstream issue, maintainer message or PR has been submitted for this branch.

## App-specific SD radio revision

After the initial size failure, PRCP capture recognition and PRAT audio TX moved to BASEBAND on SD. The repeater loader checks exact image length, available reserved memory, read completion and a build-generated FNV-1a integrity value before starting M4. Failures return an app error before RX/TX enable. Normal built-in Capture, Replay and audio loading is unchanged. The updater package includes the matching SD modules and uses USTAR. A sixth host regression exercises the actual copy/integrity helper and rejects corrupt, truncated and oversized images. All six host programs passed locally. ARM build and packaging results for this revision are pending.
