# Mayhem Firmware - Repeater + PortaMeshRF Fork

## PortaMeshRF branding update

The mesh messaging app is now **PortaMeshRF**, with a new Transceiver menu name, screen title and original three-node icon. Saved channel keys, node identity, internal settings identifiers and the `meshtastic.ppma` filename are retained for upgrade compatibility.

PortaMeshRF is independently developed and compatible with the Meshtastic® protocol. It is not affiliated with, sponsored by or endorsed by the Meshtastic project. Meshtastic® is a registered trademark of Meshtastic LLC. Protocol references and original copyright/license notices remain for compatibility and attribution.

- [Current setup and key-import instructions](docs/h4m/PORTAMESHRF.md)
- [Rebranding candidate with the later receive-window fixes](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/tree/build/portameshrf-branding)
- [PortaMeshRF build checks and matching test downloads](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/workflows/portameshrf-branding.yml)

Existing releases and screenshots retain their original labels. The new candidate needs physical testing of that exact build; no flashing or upstream submission has been performed. The separate repeater-only preparation remains on [upstream/repeater-only](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/tree/upstream/repeater-only).

A fork of [PortaPack Mayhem](https://github.com/portapack-mayhem/mayhem-firmware) with Auto Repeater and experimental PortaMeshRF apps compatible with the Meshtastic protocol for **HackRF One + PortaPack H4M**. The complete modified source, build instructions and credits are included.

**Start here:** [Download and flash](#download-and-install-ar09) | [Auto Repeater quick start](#auto-repeater-quick-start) | [Meshtastic setup](#meshtastic-setup-and-keys) | [Import a key](#import-a-key-from-the-sd-card) | [Troubleshooting](#meshtastic-troubleshooting) | [Changes](CHANGELOG.md)

**Previous H4M test firmware (old app label):** [Download H4M_AR09.ppfw.tar](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/download/ar09/H4M_AR09.ppfw.tar) · [Release notes and checksum](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/tag/ar09). Built on the [November 21 Mayhem nightly](https://github.com/portapack-mayhem/mayhem-firmware/releases/tag/nightly-tag-2026-11-21). GitHub checks the compiled package. On-device confirmation of ar09 is pending.

The [ar06 release](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/tag/ar06) is the previous H4M build with a hardware-confirmed Meshtastic Settings fix.

![Auto Repeater demo](docs/h4m/media/demo-preview.gif)

▶️ **[Watch the full screen walkthrough video (5 min)](docs/h4m/media/H4M-v0.3.1-screen-demo.mp4)**

## What's in this build

This firmware adds two new apps to the HackRF/PortaPack H4M, both found under **Transceivers (TRX)**:

### 📡 Auto Repeater
A store-and-forward "parrot" repeater for the PortaPack. It sits on a receive frequency and listens. When a signal rises above your trigger level, it records it to the SD card. When the signal stops, it waits a short delay and transmits the recording back out, on the same frequency or on a separate TX frequency. Then it rearms for the next one. It works with raw IQ (any signal), with voice modes (NFM, FM, AM, USB, LSB, WFM), and with OOK remotes. In OOK mode it can recognize many common key-fob and sensor protocols live and export Flipper Zero `.sub` files. An **Auto level** button sets the trigger from the background noise for you. **REC / TX / SKIP** counters show what it's doing at a glance.

### 💬 PortaMeshRF (experimental, needs testers!)
An independent PortaMeshRF client compatible with the Meshtastic protocol that runs entirely on the HackRF, using software-defined LoRa with no external LoRa radio. It has **Chat**, **Nodes**, **Data** and **Setup** tabs. You can join a mesh by matching region, modem preset, channel and key with your other nodes, then send and receive text messages, NodeInfo and telemetry.

> **ar05 hardware test:** The H4M imported a 256-bit Base64 channel key and exchanged text in both directions with a LILYGO T3 running Meshtastic 2.7.26. This was a Short Fast bench test at 433.125 MHz. Repeated-delivery reliability and broader hardware/preset coverage need more testing.

## Screenshots

| Auto Repeater | Repeater settings | Transceivers menu |
|:---:|:---:|:---:|
| ![Auto Repeater main screen](docs/h4m/media/01-repeater-ook.png) | ![Auto Repeater settings](docs/h4m/media/02-repeater-settings.png) | ![Transceivers menu with both apps](docs/h4m/media/03-transceivers.png) |

| Meshtastic chat | Meshtastic radio setup |
|:---:|:---:|
| ![Meshtastic chat tab](docs/h4m/media/04-meshtastic-chat.png) | ![Meshtastic radio setup](docs/h4m/media/05-meshtastic-radio.png) |

## Download and install ar09

1. Download [H4M_AR09.ppfw.tar](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/download/ar09/H4M_AR09.ppfw.tar). Keep the TAR intact and copy it into the SD card’s `FIRMWARE` folder. If you download the Actions ZIP instead, extract the ZIP once to get that TAR.
2. On an H4M running this fork’s ar05, ar06 or ar08 firmware, open **Utilities > Flash Utility**, select **H4M_AR09.ppfw.tar**, and let the update finish.
3. After restarting, open **About** and check for **n_261121_ar09**. The TAR includes the matching apps and baseband images.
4. Open **Transceivers (TRX)** and select **Auto Repeater** or **PortaMeshRF** (called Meshtastic in the older release).

Older v0.2.x builds can use the [ar05 Windows USB instructions](#download-and-install-ar05) to install the internal updater first.

## Previous firmware · ar06

1. Download [H4M_AR06.ppfw.tar](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/download/ar06/H4M_AR06.ppfw.tar) and copy it intact into the SD card's `FIRMWARE` folder.
2. On a HackRF One + PortaPack H4M running ar05, open Flash Utility and select the TAR.
3. After reboot, verify that About shows **n_261109_ar06**.

The update includes matching apps and baseband images. The owner confirmed that the Meshtastic Settings fix works on their H4M.

## Download and install ar05

**[Download the complete SD-card and Windows flash package](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/download/ar05/H4M-Meshtastic-ar05-SD-and-Flash.zip)**

Firmware version **`n_261109_ar05`**. This community test package contains matching APPS, BASEBAND, firmware, Windows USB tools/drivers, instructions and checksums. [Release notes](docs/h4m/AR05-RELEASE-NOTES.md) | [Changelog](CHANGELOG.md)

1. Extract the ZIP. Copy everything **inside SD_CARD** to the SD card root. Merge folders and replace matching files while retaining your other data.
2. Open **Utilities > Flash Utility** on the PortaPack and select **H4M_AR05_FIX.ppfw.tar**.
3. Wait for completion, restart, and confirm About shows **n_261109_ar05**.
4. Open **Transceivers / TRX > PortaMeshRF** (called Meshtastic in older releases).

Use the corrected **FIX** archive supplied in the release. Earlier ar05 packaging used extended TAR headers unsupported by the updater.

**Windows USB alternative:** Copy the SD files first. Connect USB, select **HackRF mode** on the PortaPack, and run **USB_FLASH_WINDOWS/START_H4M.bat**. It backs up flash, writes ar05 and verifies a byte-for-byte read-back. Wait for SUCCESS before restarting. Older custom v0.2.x builds require USB because they lack the internal updater.

Use this build's matching **104 PPMA apps**, two standalone apps and BASEBAND files. Mixing builds can cause app compatibility errors. [Previous v0.3.1 release](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/tag/v0.3.1)

## Auto Repeater

- Half-duplex store-and-forward operation with separate RX and TX frequencies, or TX following the received frequency.
- Signal-level trigger, end-silence timer, maximum capture duration, **1–30 second TX delay**, cooldown and automatic rearming.
- Save/discard after successful transmission, record-only mode, repeat count/gap, RX/TX gain and amplifier controls.
- Raw IQ; NFM, FM, AM, USB, LSB and mono WFM voice modes; optional voice monitoring.
- OOK mode adds live frame/protocol recognition where an included decoder recognizes the signal.
- Optional receive-frequency hopping; recording and transmission hold the selected channel.
- Flipper `.sub` **RAW/BinRAW** playback for supported OOK/2FSK presets. Compatible OOK recordings can also export as Flipper RAW `.sub` files.

### Auto Repeater quick start

1. Open **TRX > Auto Repeater**. For a voice check, choose **NFM voice** and enter the receive frequency of your own test radio. Leave hopping off for this first check.
2. Turn on **Save**. Open **Settings > Files**, enable **Record only (no auto TX)** for the first pass, and press **Auto level** while the test radio is quiet. Return with **Done**.
3. Press **START AUTO**, key your test radio briefly, then release it. Watch **REC** and open **Settings > History** to review the event.
4. To test a repeat, stop Auto, turn off **Record only**, choose **TX follows received freq** under **Settings > Radio** or enter a separate TX frequency, set **TX delay**, then start Auto again. Listen on a second receiver. A clean event should count under **TX**, followed by a return to listening. A **SKIP** means the event didn’t transmit.

### v0.3.1 repeater fixes

The Start/Stop caption updates only when it changes. Other text refreshes at most five times per second, reducing redundant LCD writes.

Capture-quality checks cover the retained prebuffer and current event rather than the entire idle listening session. Silence below the selected trigger ends a recording; the optional rearm margin no longer holds a short event open below the noise floor.

A capture with real sample gaps is saved and counted as **SKIP**, then Auto returns to listening after cooldown. It is not automatically transmitted or exported as `.sub`. Clean captures follow the normal delay, transmission and rearm sequence. Actual file/SD errors still stop with their specific error.

For a first test, choose one known RX frequency, disable hopping, keep Save checked, and use **Settings → Auto level** with the remote quiet. Watch the **REC / TX / SKIP** counts.

## Meshtastic setup and keys

### First connection checklist

1. Install the current firmware and matching SD apps, then verify the version in About.
2. Connect a suitable antenna before transmitting and choose a permitted frequency for your location.
3. Open **Transceivers / TRX > PortaMeshRF** (called Meshtastic in older releases) on the PortaPack.
4. In Setup, match the other node's radio settings. Verify the actual center frequency, rather than relying on the channel label alone.
5. On the standard node, an ordinary **CLIENT** role is suitable for chatting. It already acts as a mesh node. A special router role is not needed for this two-radio test.
6. Start with short channel messages addressed to **>All**. Configure a custom channel and the same PSK on both radios for a private channel.
7. Confirm a received text on each radio using the two-way test below.

No account or server registration is needed for direct LoRa messages. The standard web client configures the connected node. MQTT/internet connectivity is optional and separate from local radio communication.

The HackRF can tune a wide range, but the other node's RF hardware and antenna still determine its usable band. A 433/470 MHz LILYGO does not become a 915 MHz node by changing its software region. Our 433.125 MHz bench setting is a test record, not a universal regional default.

### Match both radios

Match the actual frequency, bandwidth, spreading factor and coding rate. A matching modem preset is the easiest starting point. Match the channel name exactly, including capitalization, and use the same key bytes.

Secondary channels share the primary channel's RF frequency. Adding one does not create another frequency. An explicit frequency slot on the standard node can keep the radios aligned.

Our bench test used a secondary channel named `test`, Short Fast and 433.125 MHz on 433 MHz hardware. Choose hardware and settings appropriate to your region and operating authorization.

### Get a key from your existing node

Ask the channel owner to share the channel name and PSK securely, or copy it from a node you own.

With the node connected to **client.meshtastic.org**:

1. Open **Settings > Radio Config > Channels**.
2. Select the channel.
3. Find **Pre-Shared Key** and use **Show password** or **Copy to clipboard**.
4. Copy the Base64 PSK exactly, including trailing `=` padding. Record the exact channel **Name** too.

Use the **channel PSK** from Channels. A node's public key from Security or NodeInfo belongs to direct-message PKC and cannot serve as the channel PSK.

### Generate a new private key

1. In the standard web client's **Settings > Radio Config > Channels**, choose a spare channel.
2. Set the role to **SECONDARY** and enter a short channel name.
3. Select **256 bit** next to the PSK and click **Generate**.
4. Click **Save**, then copy the generated key.
5. Set up a custom channel with that same name and key on the PortaPack.

Share a private PSK only with the people joining that channel. Anyone with that key and matching settings can decode channel traffic. Our bench test used a recognizable test fixture. Generate a fresh key for private use.

### Import a key from the SD card

1. On your computer, create a plain-text file such as **MYKEY.TXT**.
2. Paste **only the PSK** on one line. Include Base64 padding. Use no quotes, spaces, labels or `key=` prefix. A trailing line ending is accepted.
3. Save as ASCII or UTF-8 **without a BOM** and check the filename ends in **.TXT**.
4. Copy the file to your PortaPack's SD card, for example its root.
5. Open **Mesh > Chat**, then press **Ch:** at the bottom to open the channel list.
6. Select an empty custom slot, enter the exact channel name and confirm. The channel becomes enabled and active.
7. Reopen the channel list and highlight that custom channel with the D-pad or encoder.
8. Press **Import key**, browse to the file, highlight it and press Select to open it.
9. Select your custom channel for chat and choose **>All** to test channel messages.

Import loads the key only. Set the name and radio parameters separately. Ar05 silently keeps the previous key if the file cannot be read or parsed. If nothing appears to change, check the encoding, file contents and supported lengths below. An empty file does not clear the key.

The key file stays on the SD card. Protect the card and any copies when using a private PSK.

### Type a key manually

Activate the custom channel, then select it again in the channel list to open the key editor. Type the key and press **OK**. The editor accepts up to 64 characters.

| Format | What to enter |
| --- | --- |
| AES-128 hex | Exactly 32 hex digits, without spaces or a `0x` prefix |
| AES-256 hex | Exactly 64 hex digits, without spaces or a `0x` prefix |
| AES-128 Base64 | Standard padded 24-character PSK |
| AES-256 Base64 | Standard padded 44-character PSK |
| Meshtastic short PSK | Padded 4-character form such as `AQ==`, the well-known default |
| Open custom channel | Leave the typed key empty and confirm |

The hex and Base64 forms must represent the same bytes on both nodes. Select the matching format in your other client.

Other typed text retains this app's legacy passphrase derivation. A passphrase is not automatically a standard Meshtastic PSK. Use valid raw hex or padded Base64 when joining standard nodes. Import accepts supported encoded keys, rather than arbitrary passphrases. Nonzero short-PSK indexes are supported. Use an empty typed key to configure an open channel.

**Rnd key** generates a 128-bit hex key. Generate a new 256-bit key in the standard client and import or type it here.

### Primary channel, padlock and direct messages

This build's primary channel uses the well-known default Meshtastic key. Use a **custom channel** for a private PSK.

A green custom-channel padlock indicates a key is configured. Successful message reception confirms whether the other node matches. The widely known default key does not provide private channel access control.

**Encrypt DMs (PKC)** is a separate direct-message setting. Select your custom channel and **>All** for channel tests. A **key requested** line relates to node public-key exchange, not proof of a matching channel PSK.

### Test sending and receiving

1. Select the same channel on both radios (primary LongFast or a matching custom channel).
2. Send a short, distinctive text from your standard node and confirm the exact text appears on the PortaPack.
3. Press **Write message** in PortaPack chat, type another short message and press **OK**. Confirm it appears on the other node.
4. Repeat several times. A local sent entry or SDR transmission alone does not establish delivery.

**Verified on ar05:** Import of a 256-bit Base64 key, the green custom-channel padlock and text reception in both directions with a LILYGO T3. Manual 256-bit typing, additional keys/presets and DM PKC still need hardware testing. Repeated-delivery reliability remains under investigation.

**Receive limitations:** SF12 reception is disabled. The SF7 ring holds 92 symbols and can truncate long packets. SF8-11 timing and broader RF interoperability need further testing. [Additional Meshtastic background](docs/h4m/MESHTASTIC.md).

### LongFast chat on H4M

Open the primary channel (**Ch:P**) and choose **>All** for a channel broadcast. The separate **All / Msg / Tec** button controls what appears on screen. Choose **Msg** for conversation text or **All** for text and radio events. In ar09 the chat has reserved space in all three views. Background events cannot gradually empty the conversation. New texts can eventually push out old wrapped rows.

**History:** The encoder scrolls chat. **Setup > Chat > Lines** sets the live history size in wrapped screen rows. With SD saving off, switching threads restores recent messages from the app’s 16-message session buffer. For history across restarts, set **Save msgs** above zero and use a writable SD card. **Clear** in chat asks for confirmation and clears the display. **Clear history** under Setup removes saved history.

**Frequency:** Open **Setup > Radio > Freq** for the PortaPack number pad. Use **Load** to pick a saved frequency, then confirm the desired value and unit. Use **Auto** on the Radio page to return to region, preset and slot tuning.

**Navigation:** Use **Write message** along the bottom to compose. Channel, recipient and display filter sit directly above it. Settings pages have a full-width **Back** button near the bottom for D-pad or touch navigation.

On each radio, send a distinct short text and check for those exact words on the other screen. A phone’s **Delivered to mesh** badge alone does not identify the H4M as the receiver. The earlier H4M LongFast test used US slot 17 at 906.125 MHz with the default channel key (`AQ==`); use your node’s actual frequency and channel settings for your own test.

### Meshtastic troubleshooting

| What you see | What to check |
| --- | --- |
| Transmission on an SDR but no received text | Match frequency, bandwidth, SF, coding rate, exact channel name and PSK. Confirm the selected conversation and destination. |
| Location or NodeInfo appears but chat does not | Radio communication is partly working. Check the text channel's name/hash/key and whether you are using a channel or a direct message. |
| Green padlock but no messages | The lock only indicates a configured key. Re-copy the same PSK and verify two-way delivery. |
| Key requested | This concerns the other node's public-key exchange for direct messages. Use your custom channel with >All to test the shared channel PSK separately. |
| Import key does nothing | Highlight an enabled custom channel. Use a key-only .TXT in a supported encoding, without BOM, labels or spaces. Ar05 has no import-error dialog. |
| Open channel cannot decode | Both sides must use a truly empty PSK. The default AQ== public key is still an encryption key and differs from no key. |
| Old or outdated PPMA error | Copy APPS and BASEBAND from the same release as the firmware. |
| BAD FIRMWARE FILE OR W/R ERR during TAR flashing | Use H4M_AR05_FIX.ppfw.tar from the corrected package. Check the download checksum and SD-card copy. The Windows launcher provides an alternative with read-back verification. |
| One direction works or messages arrive intermittently | Check TX/RX mode, antenna, frequency and receive gain. Separate nearby radios to reduce overload. Repeat short messages in each direction and record which ones arrive. |
| Long messages fail while short ones work | Receiver buffering is limited, particularly at SF7. Start with short texts and report preset, length and direction. |

For a bug report, include firmware version, hardware, preset, actual frequency, channel name, key format/length (not the private key itself), direction and the exact error. Describe whether the opposite radio displayed the message. Report results in your test thread or a pull request if repository Issues are unavailable.

## Signal and file limitations

Raw IQ repeats a recorded waveform; protocol recognition is not required for raw recording. OOK recognition identifies supported frame formats, not every manufacturer/model. It does not decrypt or synthesize rolling codes, and replay acceptance is not guaranteed.

`.sub` export is amplitude-sliced OOK RAW, not a universal IQ-to-Flipper conversion. Voice/FSK/arbitrary RF recordings cannot all be exported as OOK. Encoded protocol/key `.sub` files and custom presets are not synthesized by the importer; use supported RAW/BinRAW captures.

## Testing and feedback

Please include these details when sharing test results:

- Hardware and firmware version shown in About.
- Mode, RX/TX frequency, sample rate, trigger and end-silence settings.
- Whether hopping, Save, Record only or an amplifier was enabled.
- REC / TX / SKIP counts and the exact on-screen error, if any.
- Whether a second receiver/node observed the expected transmission.

Build checks cover the 1 MiB firmware checksum and version, the bundled PPMA identifiers/checksums, external-app layout, runtime LoRa memory budget, updater residency and final archive ordering. Host regressions cover repeated automatic cycles, capture-loss windows, UI repaint suppression, file conversion, a synthetic Princeton IQ waveform and imported Meshtastic protocol tests. These checks do not replace physical RF/SD/UI validation.

## Source and building

This repository contains the complete modified firmware source. The original base is Mayhem tag [`nightly-tag-2026-11-09`](https://github.com/portapack-mayhem/mayhem-firmware/releases/tag/nightly-tag-2026-11-09), commit `706fd7f91e0318fc4643e8d31f5087ececb312c4`.

Ar09 includes the November 21 nightly at `afc728338907a1dcbde26daf7f8b96152080015b` and the Meshtastic chat-history change.

Use GNU Arm Embedded **GCC 9.2.1**, Ninja and the dependencies listed in [BUILD.txt](docs/h4m/BUILD.txt):

```sh
git clone --recurse-submodules --branch build/portameshrf-branding https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork.git
cd mayhem-firmware-Repeater-PortaMeshRF-fork
python3 tools/update_external_tier_ld.py
cmake -S . -B build -G Ninja -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DMAYHEM_CUSTOM_VERSION=pmesh_local
cmake --build build --target oci -j6
python3 tests/auto_repeater/check_layout.py build
python3 tests/auto_repeater/check_runtime_memory.py build
python3 tests/auto_repeater/check_install.py build pmesh_local
```

The custom version is cached so CMake regeneration does not silently change app compatibility. The internal flash writer **PFUT** is included in SPI alongside the LoRa and factory images.

## Credits and license

- [PortaPack Mayhem](https://github.com/portapack-mayhem/mayhem-firmware) and its contributors. The original project README is preserved as [README-UPSTREAM.md](README-UPSTREAM.md).
- Experimental Meshtastic software-LoRa implementation by **Alexey Verhogladov**, imported from [`mamapapa1/mayhem-firmware`, `mesh-test-1`](https://github.com/mamapapa1/mayhem-firmware/tree/mesh-test-1), commit `9d028dd349b9f38dcc897ca2a071d91adec3e851`. Existing copyright notices are retained.
- OOK recognizers and their upstream Flipper-related acknowledgements remain in the source headers. LoRa framing sources acknowledge gr-lora_sdr and related research.
- Windows recovery utilities/drivers are redistributed unchanged from the official `n_261109` firmware asset, with provenance in the package credits.

See [LICENSE](LICENSE), [LICENSE.GPL-2.0-or-later](LICENSE.GPL-2.0-or-later), and the individual source-file notices.
