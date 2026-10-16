# NV-21-HU Network Video Endpoint
> 来源: https://help.qsys.com/Content/Hardware/Video/NV-21-HU.htm

The Q-SYS NV Series NV-21-HU is the next evolution for native video distribution on the Q-SYS Platform. The NV-21-HU is a software configurable endpoint offering a comprehensive single-cable solution for audio and video distribution, AV bridging and device charging via USB-C. The NV-21-HU’s compact size and reduced I/O make it ideal for supporting meeting rooms, learning spaces, hospitality and entertainment installations. The NV-21-HU can be used alongside other Q-SYS NV Series video endpoints, providing system design flexibility. Like all Q-SYS products, the NV-21-HU offers native integration and control, simplifying configuration and operation.

> **Note:** This topic provides an overview of the NV-21-HU. For complete specifications, installation documentation, and product drawings, see the NV-21-HU product page on the Q-SYS website.

## Features

- Single cable solution for video distribution, AV bridging, and device charging.
- Native HDMI video and audio distribution for Q-SYS
- Q-SYS Shift™ adaptive video compression
- Software configurable as an encoder or decoder
- HDMI and USB-C Mode selection

> **Note:** An external power supply is required for any device charging over the USB-C connection. See the NV-21-HU Hardware User Manual for power requirements.

## Design Components

Add the NV-21-HU to your design Inventory from the Video category. The following components are available for the NV-21-HU:

### Standard Components

- Status (NV-21-HU)
- AV I/O (NV-21-HU)
- Serial Port (NV-21-HU)
- HID Keyboard
- HID Media
- HID Conferencing
- USB Input
- USB Output

### USB Video Bridge

- USB Video Bridge

### USB Audio Bridge

- USB Audio Bridge – Speakerphone / Sound Card In
- USB Audio Bridge – Speakerphone / Sound Card Out

### Related Components

- Generic AV Source
- Generic HDMI Display

## Connections and Callouts

## Front Panel

1. Power LED
2. ID Button
3. ID LED

## Rear Panel

1. External Power Input
2. LAN / PoE
3. USB-A
4. RS232
5. Reset Button
6. USB-C
7. HDMI In
8. HDMI Out

## Control

### RS-232

Three Pin Euro terminal connection to control third-party devices with Q-SYS Control, user-configurable.

## USB

### USB HID control

Control host PCs with a USB connection using USB HID components in Q-SYS Designer Software.

### Q-SYS AV Bridging

The Q-SYS AV Bridging feature expands the functionality of the NV-21-HU, allowing users to connect their devices via USB-C directly to the network video endpoint to integrate Q-SYS audio and camera feeds for remote meetings easily. The NV-21-HU emulates a webcam (for video streams from Q-SYS network cameras), a speakerphone, and a multichannel soundcard over a single driverless USB connection.

## Audio

### HDMI Audio Input

Receive up to 8 channels of PCM audio from your video source, which are routable within Q-SYS Designer Software.

### USB-C Audio Input

Receive up to 8 channels of PCM Audio from your video source, which are routable within Q-SYS Designer. Additional 1x1 Speakerphone and 2x2 Soundcard options are available with the Q-SYS AV Bridging feature.

### HDMI Audio Output

Embed up to 8 channels of PCM audio from Q-SYS to the HDMI output of the NV-21-HU to utilize the built-in speakers of a display as a Q-SYS audio destination for source audio content or any other audio, including paging, background music, etc.

## Security and Authentication

### AES-128

NV Series supports AES-128 encryption for audio and video signals from encoders to decoders.

### Content Protection

HDCP 1.4 & HDCP 2.3 complaint

### 802.1x

802.1x authentication is available and configurable through Q-SYS Peripheral Manager.

## Q-SYS Shift™ Adaptive Bitrate Codec

The NV-21-HU uses Q-SYS Shift™ video compression to provide high-quality, low-latency video streaming supporting video formats up to 4k60 4:4:4 over a standard gigabit network. Q-SYS Shift™ leverages DCT and temporal compression technologies, much like those found in H.264 and H.265 video compression codecs. Q-SYS optimized Shift™ to provide flawless image quality from the most demanding content sources. Further, Shift™ intelligently manages and optimizes the resulting network bitrate by only refreshing changes within each frame, allowing for significantly reduced bandwidth usage as compared to other compression codecs.

> **Note:** 4k60 formats require Display Stream Compression (DSC) or reduced blanking for USB-C video inputs.

### Modes

Multicast and unicast

### Bitrates

10 Mbps – 800 Mbps

### Streaming Protocol

RTP

## Supported Video Formats 1

| Resolution | Frame Rate (Hz) | Chroma Sampling Level | Bit Depth |
|---|---|---|---|
| 3840 x 2160 (4K UHD) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 3440 x 1440 | 60 | 4:4:4 | 8 bit |
| 2560 x 1600 | 60 | 4:4:4 | 8 bit |
| 2560 x 1440 | 60 | 4:4:4 | 8 bit |
| 2560 x 1080 | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 1920 x 1200 | 60 | 4:4:4 | 8 bit |
| 1920 x 1080 (1080p) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 1280 x 720 (720p) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 640 x 480 | 60 | 4:4:4 | 8 bit |

> **Note:** * All video formats are progressive. 4:2:0 Chroma subsampling and HDR not supported.

> **Note:** 1 This table is a small subset of the most common formats. Many other formats and timings are also supported.

## Scaler

The NV-21-HU features a robust 4K60 4:4:4 scaler that can accommodate the most challenging resolution and frame rate conversions from network streams or local HDMI and USB-C sources. The scaler is capable of operating in three modes (configurable within Q-SYS Designer Software):

- Stretch-to-fit
- Maintain aspect ratio
- 1:1 pixel mapping

## Specifications

For complete product specs, refer to the Specifications Sheet on the NV-21-HU product page at qsys.com.

