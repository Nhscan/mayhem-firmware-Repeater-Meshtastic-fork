# Draft: Add Auto Repeater external Transceiver app

Status: preparation only. Do not submit until the exact candidate compiles, passes layout/memory checks and has been physically tested and reviewed by the contributor.

## Brief description

Adds an external Auto Repeater interface for triggered RX recording followed by delayed TX playback. Users can configure separate RX/TX frequencies, threshold, delay, repeat count and cooldown; retain recordings; or select a recording for manual playback. The controller returns to listening after automatic playback.

The app supports IQ capture/replay and recorded AM/FM/SSB audio using existing radio facilities plus a recorded-audio TX baseband. Optional IQ-envelope recognition and RAW/BinRAW SUB import/export are included in this initial candidate; their final scope depends on footprint and maintainer review.

The UI is external. Engine and file-worker code are currently internal. ARSV reserves the largest switched radio image beneath the UI to prevent overlap. Normal built-in baseband storage and the existing global loader remain unchanged. Only repeater capture recognition and recorded-audio TX load from matching, integrity-checked SD modules.

Meshtastic and combined-fork updater/release changes are excluded. This contribution was developed with AI assistance and needs contributor ownership and detailed human review before submission.

## Proof it compiles

Pending: successful final ARM build, final flash-space summary, external app size/reserve check and runtime memory assessment. A successful host test is not a successful firmware build.

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
