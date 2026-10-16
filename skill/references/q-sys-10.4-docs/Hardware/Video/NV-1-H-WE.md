# NV-1-H-WE Network Video Endpoint
> 来源: https://help.qsys.com/Content/Hardware/Video/NV-1-H-WE.htm

The Q-SYS NV-1-H-WE wall-mount HDMI encoder enhances and extends the NV Series network video distribution into flexible and reconfigurable spaces, providing a single platform for network video distribution across every room type. The NV-1-H WE can be used alongside other Q-SYS NV Series network video endpoints, providing system design flexibility. Like all Q-SYS products, the NV-1-H-WE offers native integration into the Q-SYS platform, reducing complexity and accelerating deployment by tightly integrating device configuration, control and audio routing capabilities.

> **Note:** This topic provides an overview of the NV-1-H-WE. For complete specifications, installation documentation, and product drawings, see the NV-1-H-WE product page on the Q-SYS website.

## Features

- Single cable solution for video distribution
- Native HDMI video distribution for Q-SYS
- Q-SYS Shift™ adaptive video compression

## Design Components

Add the NV-1-H-WE to your design Inventory from the Video category. The following components are available for the NV-1-H-WE:

### Standard Components

- Status (NV-1-H-WE)
- AV I/O (NV-1-H-WE)

### Related Components

- Generic AV Source

## Connections and Callouts

## Front Panel

1. HDMI In
2. Reset Button
3. Power / ID LED
4. ID Button

## Rear Panel

1. LAN / PoE

## Q-SYS Shift™ Adaptive Bitrate Codec

The NV-1-H-WE uses Q-SYS Shift™ video compression to provide high-quality, low-latency video streaming supporting video formats up to 4k60 4:4:4 over a standard gigabit network. Q-SYS Shift™ leverages DCT and temporal compression technologies, much like those found in H.264 and H.265 video compression codecs. Q-SYS optimized Shift™ to provide flawless image quality from the most demanding content sources. Further, Shift™ intelligently manages and optimizes the resulting network bitrate by only refreshing changes within each frame, allowing for significantly reduced bandwidth usage as compared to other compression codecs.

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

The NV-1-H-WE features a robust 4K60 4:4:4 scaler that can accommodate the most challenging resolution and frame rate conversions from network streams or local HDMI sources. The scaler is capable of operating in three modes (configurable within Q-SYS Designer Software):

- Stretch-to-fit
- Maintain aspect ratio
- 1:1 pixel mapping

## Specifications

For complete product specs, refer to the Specifications Sheet on the NV-1-H-WE product page at qsys.com.

