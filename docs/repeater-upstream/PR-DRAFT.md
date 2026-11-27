# Draft: Add Auto Repeater external Transceiver app

Status: preparation only. Software checks passed; physical testing and contributor review remain pending. Craig has explicitly requested no upstream submission.

## Brief description

Adds an external Auto Repeater interface for triggered RX recording followed by delayed TX playback. Users can configure separate RX/TX frequencies, threshold, delay, repeat count and cooldown; retain recordings; or select a recording for manual playback. The controller returns to listening after automatic playback.

The app supports IQ capture/replay and recorded AM/FM/SSB audio using existing radio facilities plus a recorded-audio TX baseband. Optional IQ-envelope recognition and RAW/BinRAW SUB import/export are included in this initial candidate; their final scope depends on footprint and maintainer review.

The UI is external. Engine and file-worker code are currently internal. ARSV reserves the largest switched radio image beneath the UI to prevent overlap. Normal built-in baseband storage and the existing global loader remain unchanged. Only repeater capture recognition and recorded-audio TX load from matching, integrity-checked SD modules.

Meshtastic and combined-fork updater/release changes are excluded. This contribution was developed with AI assistance and needs contributor ownership and detailed human review before submission.

## Proof it compiles

[Passing build](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45519543490), source `d24764597b3496fafde86f21a911e9c2dc2cbfb6`, identifier `rpt_d247645`.

```text
Space remaining in flash ROM: 1280 bytes (0.1%)
PASS external UI: 15572 bytes + 23220 bytes radio reserve / 40960
PASS built-in capture/replay/audio/updater/factory images retained
PASS capture known heap: 72592/78732 bytes, 6140 bytes headroom
PASS repeater_capture known heap: 73228/78732 bytes, 5504 bytes headroom
PASS recorded audio known heap: 33888/79836 bytes, 45948 bytes headroom
PASS firmware: 1 MiB, checksum valid, USTAR update with exact apps/radio files before firmware
```

All six host regression programs passed. Flash margin is small and must be rechecked after any rebase. These checks do not establish physical RF performance.

## Proof of physical device testing

Pending on this isolated candidate. Earlier combined-fork tests are background only.
After testing, provide the exact commit, build identifier, PortaPack model, SD contents and screenshots/video. Only then include the required physical-test statement from AGENT.md.

## Real emitter/receiver test plan

1. Configure a known lab source and separate receiver. Record RX/TX frequencies, modulation, rate and gains.
2. Demonstrate threshold-triggered capture, the configured delay, one complete TX and automatic return to RX.
3. Repeat multiple cycles and demonstrate maximum duration, cooldown and stop/cancel.
4. Verify retained IQ/WAV playback, file-import errors, SD-write failure reporting and app exit/re-entry.
5. Check normal Capture, Replay and Audio RX apps after the capture-thread/DSP changes.
6. Attach RF evidence from the receiver or spectrum display and a view of the PortaPack UI.

## Documentation and licensing

- [ ] Contributor reviewed the final code and can maintain it.
- [ ] Exact candidate physically tested, with screenshots/video and real RF evidence.
- [ ] Compile, flash/RAM and external layout evidence attached.
- [ ] Attribution and GPL-3.0-compatible contribution rights verified.
- [ ] Contributing guidelines reviewed and wiki documentation commitment accepted.
- [ ] Final scope and description approved before opening upstream PR.

See PREPARATION.md for current validation and integration details.
