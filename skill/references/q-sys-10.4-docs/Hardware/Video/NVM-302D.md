# NVM-302D Network Video Monitor
> 来源: https://help.qsys.com/Content/Hardware/Video/NVM-302D.htm

The Q-SYS NVM-302D is a network HDMI decoder that comes pre-installed with a single-channel decode video app. Q-SYS NVM Series network video endpoints deliver high-quality, low-bandwidth network video at scale to a broad range of spaces for hospitality, entertainment, collaboration, government and more.

> **Note:** This topic provides an overview of the NVM-302D. For complete specifications, installation documentation, and product drawings, see the NVM-302D product page on the Q-SYS website.

## Features

- Q-SYS native video decoder
- Mediacast AV routing paradigm enables high-quality, network-efficient video distribution at scale
- Supports resolutions up to 4K60 4:4:4
- RS-232 and IR connectivity for third-party device control
- AV Bridging via USB-C. Supports USB Video Bridging (up to 1080p), USB Audio Bridging, and HID Conferencing. Note: USB Bridging requires a USB 3.0 or higher (SuperSpeed) connection.

## Design Components

Add the NVM-302D to your design Inventory from the Video category. The following components are available for the NVM-302D.

### Standard Components

- Status (NVM-302D)
- Decoder (NVM-302D)
- HDMI AV Display (NVM-302D)
- Serial Port (NVM-302D, NVM-302E)
- HID Keyboard
- HID Media
- HID Conferencing
- USB Input
- USB Output
- USB Video Bridge
- USB Audio Bridge

### Related Components

- Status/Control (NVM Routing Group)
- NVM Proxy

## Connections and Callouts

## Front Panel

1. Power LED – Illuminates blue when the NVM is powered on.
2. ID Button – Locates the NVM in Q-SYS Designer Software and Q-SYS Peripheral Manager.
3. ID LED – Blinks green when placed into ID Mode via ID Button or Q-SYS Peripheral Manager.

## Rear Panel

1. LAN / PoE – RJ-45 connector, 2.5GbE, 802.3at Type 2 Class 4 (30W from PSE, 25.5W at NVM). For connection to Q-LAN.
2. HDMI Out – HDMI 2.0 Output with support for HDCP 2.3 and HDCP 1.4.
3. Reset Button – Use a paper clip, or similar tool, to press and hold the reset button for 10 seconds to reset the NVM to factory values.
4. USB A (x2) – USB 3.0 Type A Host Port. Supports 5VDC (900mA total across all USB A and USB C ports).
5. USB C – USB 3.2 Gen 1x1 (5Gbps) Type C Host/Device Port, supporting DisplayPort Alt-Mode (DP 1.4 Source). Supports 5VDC (900mA total across all USB A and USB C ports).
6. RS232 – Serial Transmit and Receive. Uses the black 3-pin Euro connector.
7. IR TX Port – 3.5mm jack for connection to IR transmitter.

## Supported Video Formats

| Category | Resolution | Frame Rate (Hz) | Chroma Sampling Level | Bit Depth |
|---|---|---|---|---|
| 4K (UHD/DCI) | 3840×2160, 4096×2160 | 23.976/24, 25, 29.97/30, 50, 59.94/60 | 4:4:4 | 8 bit |
| FHD/FHD+ | 1920×1080 (1080p), 1920×1200 | 23.976/24, 25, 29.97/30, 50, 59.94/60 | 4:4:4 | 8 bit |
| HD | 1280×720 (720p) | 23.976/24, 25, 29.97/30, 50, 59.94/60 | 4:4:4 | 8 bit |
| Ultrawide (21:9) | 3440×1440, 2560×1080 | 23.976/24, 25, 29.97/30, 50, 59.94/60 | 4:4:4 | 8 bit |
| PC Resolutions | 2560×1440, 2560×1600 | 60 | 4:4:4 | 8 bit |
| SD (NTSC) | 720×480 | 29.97/30,59.94/60 | 4:4:4 | 8 bit |
| SD (PAL) | 720×576 | 25, 50 | 4:4:4 | 8 bit |
| VGA | 640 × 480 | 59.94/60 | 4:4:4 | 8 bit |

Notes:

- 4:2:2 & 4:2:0 Chroma subsampling supported at some resolutions.
- The scaler is capable of operating in three modes (configurable within Q-SYS Designer Software):
  
  - Stretch-to-fit
  - Maintain aspect ratio
  - 1:1 pixel mapping

## Specifications

For complete product specs, refer to the Specifications Sheet on the NVM-302D product page at qsys.com.

