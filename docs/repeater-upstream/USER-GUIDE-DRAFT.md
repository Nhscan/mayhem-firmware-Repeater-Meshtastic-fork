# Auto Repeater user guide draft

This describes the full-feature candidate's controls. The initial isolated build exceeded the HackRF One flash limit. A revision moves only the extra repeater radio modules to SD and is undergoing validation; do not treat this branch as an installable release. Existing working fork releases remain separate.

## Automatic recording and playback

1. Open **Transceiver > Auto Repeater**.
2. Set **Receive** to the source frequency and **Transmit** to the intended playback frequency.
3. Choose the receive mode. **IQ** records the signal for replay without demodulating it. Audio modes record demodulated voice and transmit it using the configured voice TX mode.
4. Set the trigger above the idle noise level and below the level of the signal you want to capture. The meter shows signal level and trigger position. **Settings > Auto level** samples the noise and sets the trigger 10 dB above its average; check the result before starting.
5. Set **TX delay** from 1 to 30 seconds. Select whether to keep recordings and whether to enable the TX amplifier.
6. Select **START AUTO**. The status shows listening, recording, processing, delay, transmission and rearming. Automatic mode stays enabled until stopped or an error occurs.
7. Select **STOP AUTO** to stop. Opening another screen also halts operation.

HackRF alternates RX and TX; it does not receive while transmitting. This app records a signal before replaying it, rather than acting as a simultaneous duplex voice repeater.

## Settings

| Page | Controls |
| --- | --- |
| Radio | RX LNA/VGA, TX gain, audio gain, voice TX mode, RX amplifier, receive-audio monitoring, TX follows received frequency |
| Timing | Trigger hold, end silence, rearm margin, maximum recording duration, cooldown, repeat count, gap, wait for quiet |
| Files | IQ sample rate, prebuffer, SUB threshold, optional SUB export, record-only mode, event log |
| RX hopping | End frequency, step, dwell and enable; the main RX field supplies the start frequency |

Start with hopping disabled for a reproducible test. Higher IQ rates and longer recordings require more SD space and sustained write speed. The app checks free space and reports SD errors. Captures with detected sample loss are retained and rejected for automatic replay.

## Manual playback and files

Select **Open** to browse recordings, then **Send** for manual playback. Selecting a file does not immediately transmit it.

Recordings are stored under **SAMPLES/REPEATER**. IQ recordings use C16 with metadata and a repeater mode sidecar; audio recordings use WAV. Event logging, when enabled, uses **LOGS/REPEATER.TXT**. Interrupted recordings may be retained as TMP files.

SUB import handles supported RAW/BinRAW pulse data and OOK/FSK presets. It does not accept every Flipper protocol-specific file. Optional SUB export requires a clean OOK capture; arbitrary IQ, FSK and voice recordings are not interchangeable with an OOK SUB file. An export failure does not establish that the original IQ recording was lost.

## Initial hardware validation

Use a known signal and a separate receiver. Confirm capture, the chosen delay, playback on the correct TX frequency and return to listening over several cycles. Check stop/cancel, app exit/re-entry and saved-file playback. Record the exact firmware commit, hardware model, radio settings and SD contents alongside screenshots or video.

The six host regression programs exercise controller, conversion, recognition and quality/UI logic. RF performance, gain settings and timing still require physical validation of the final firmware.
