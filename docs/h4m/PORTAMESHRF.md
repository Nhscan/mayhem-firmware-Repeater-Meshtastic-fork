# PortaMeshRF: setup, channels and keys

> [!WARNING]
> **Before transmitting (TX):** check the radio rules for your country, state/province and local area. Make sure the frequency, power, mode and antenna setup are permitted, and obtain any required licence or authorization. You are responsible for lawful operation; this experimental firmware does not guarantee regulatory compliance.

Open **Transceiver > PortaMeshRF**. The app is independent and compatible with the Meshtastic® protocol; it is not an official Meshtastic product.

## Connect to another node

1. In Setup/Radio, select the region appropriate to your hardware and location. Both devices must use compatible frequency hardware.
2. Match the modem preset, actual frequency/frequency slot, bandwidth, spreading factor and coding rate. Use preset defaults for an initial test.
3. Match the primary channel name and channel PSK. A channel's position in a client list is not by itself its over-air channel identity.
4. Set distinct node IDs. Existing node identity and saved settings carry over after this rename.
5. Start by sending to **All** on the shared channel. Receiving a signal on an SDR proves RF activity, not successful decoding or message delivery.

## Channel encryption

In the official node's Meshtastic web/mobile client, open the relevant channel settings and obtain its PSK/key. Keep private channel keys private. Some clients provide a Base64 key or a channel-sharing URL/QR instead of a plain text key field; use the client's channel export/share controls where appropriate.

Open PortaMeshRF's channel/key controls and enter the **same Base64 PSK** or use **Import key** with a plain-text key file on the SD card. The importer accepts a supported Base64 PSK or a 32/64-character raw hexadecimal AES key. A complete channel-sharing URL or QR payload is not a raw PSK; extract the actual key from the node configuration instead of pasting the URL. Use the file selector to choose the key file. See the full guide for the exact controls in your build.

AES-128 uses a 16-byte key; AES-256 uses a 32-byte key. A one-byte Base64 value is an indexed-key shorthand, not an 8-bit AES cipher. For example, the conventional public default key shorthand is `AQ==`; a publicly known default does not provide private-channel secrecy. For a private channel, generate a random key with the node's client and import that same key on PortaMeshRF.

Unencrypted channel testing also requires both sides to select **no encryption**. Turning off **Encrypt DMs (PKC)** affects direct messages and is not the same as disabling channel encryption.

## Direct messages and requested keys

An encrypted direct message needs the destination node's public key in addition to compatible radio settings. **Key requested** means the app requested peer information/key material; it does not confirm a reply arrived. Announcing NodeInfo may help discovery, but channel PSKs and node public/private keys serve different purposes.

First prove **All** channel messages work in both directions. Then test a specific peer. Match settings, ensure the peer has announced its identity/key, and check the delivery/acknowledgement status. Do not assume every preset, device or encrypted-DM case has passed testing.

## Typing and delivery

Use the compose/keyboard control at the bottom of Chat (the `»` control on older layouts). Choose the channel and destination, type a short message and send. Receipt/ACK indicators provide more evidence than RF activity alone; a broadcast without a peer response does not prove reception by a particular device.

See [the full guide](MESHTASTIC.md) for the node list, channel configuration and display controls. Older screenshots may show the previous app name. The internal `meshtastic.ppma` filename and settings namespace are retained so existing SD installations and saved keys can migrate without duplicate menu entries.

Meshtastic® is a registered trademark of Meshtastic LLC. PortaMeshRF is not affiliated with or endorsed by the Meshtastic project.
