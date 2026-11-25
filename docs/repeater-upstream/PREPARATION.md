# Auto Repeater upstream preparation

This branch separates Auto Repeater from Meshtastic for review against Mayhem next at `5bc230848cb17c666f34d07b70062bed682da1a2`.
Source was extracted from Nhscan's tested combined fork at `d2113491810f9877a087c0d43bea785d93bfecbd`.

## Current scope

- External Transceiver app UI: receive/transmit frequencies, trigger threshold, delay, repeat/cooldown controls, recording/file playback, gain controls and status.
- Internal engine and file workers: circular prebuffer, capture quality checks, metadata, RAW/BinRAW SUB conversion and playback scheduling.
- CaptureThread: explicit stop/join while retaining counters and optional writer stack size. Existing upstream shutdown/wakeup fixes remain intact; normal callers keep the 1024-byte default.
- Capture DSP: optional IQ-envelope protocol recognition, disabled unless the repeater explicitly configures it.
- Recorded audio TX baseband: AM/FM/SSB playback using existing modulators.
- ARSV reserve image: keeps the external UI above the largest baseband it switches to in the shared 40 KiB code region.

This candidate preserves normal built-in baseband SPI storage. It excludes Meshtastic, the global SD-loading fallback, updater alterations, combined-fork release packages and README replacements.
The UI is external, but the engine and file workers remain internal for this first measurement. This is not yet a fully external implementation or a stock-firmware-compatible app download.

## Validation

All five existing portable regression programs passed locally before formatting:

- Control: 1,000 automatic cycles, timing, quiet mode, repeats/gaps, cancellation and timer wrap.
- SUB parsing: RAW/BinRAW, modulation presets, malformed/unsupported input.
- OOK: generated IQ-envelope waveform decoded as a known Princeton packet; decoding disabled in normal raw mode.
- Quality/UI: retained prebuffer/drop accounting and repaint throttling.
- Files: real conversion routines, pulse timing, circular-buffer reorder and error cleanup.

The host compiler reports an uninitialized-state warning in an existing upstream Security+ v1 decoder when assigning a temporary during repeater decoder reset. That needs review before submission; passing host tests do not establish all protocol decoders are correct.

Hosted ARM build, flash size and external app layout validation are pending. The matching workflow records build logs and maps. No firmware from this isolated branch has been flashed or physically tested.

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
