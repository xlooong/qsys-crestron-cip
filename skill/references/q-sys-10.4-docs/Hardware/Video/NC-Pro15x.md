# NC-Pro15x Conference Camera
> 来源: https://help.qsys.com/Content/Hardware/Video/NC-Pro15x.htm

The NC-Pro15x expands the Q-SYS camera portfolio to bring broadcast-quality video to high-impact spaces that require elevated production-grade elements. Built by Canon, the NC-Pro15x is a network PTZ camera that delivers smooth and responsive pan, tilt, and zoom performance to enhance the VisionSuite Presenter Spotlight experience. Driven by the Q-SYS Full Stack AV Platform, the NC Series integrate seamlessly into any Q-SYS system, allowing for easy camera feed routing anywhere on the network without the need for complicated programming or video matrix hardware. These camera video feeds are delivered to any modern video conferencing applications via any Q-SYS AV bridging peripheral.

> **Note:** This topic provides an overview of the NC-Pro15x camera. For related documentation, including installation instructions, see the NC-Pro15x product page on the QSC website.

## Features

- Network PTZ built by Canon
- 15x optical zoom with 73° horizontal field of view
- 1-inch 4K UHD CMOS image sensor with Dual Pixel Autofocus
- Canon image processing offers advanced performance and high image quality
- Built-in ND (neutral density) filter
- Integrated tally light
- Optional HDMI, SDI, NDI outputs
- Simultaneous output via 3G-SDI, HDMI, and IP feeds
- Power over Ethernet (PoE)
- Compatible with Canon PTZ camera controllers

## Design Components

The following components are available for the NC-Pro15x.

### Standard Components

- Status/Control (Cameras)

### Related Components

- USB Video Bridge
- Camera Router
- VisionSuite (VisionSuite Designer)

## Connections and Callouts

## Front Panel

1. Camera head
2. Base
3. Air intake vent
4. Tally lamp (see Lamp Status )
5. Lens
6. STATUS indicator (see Lamp Status )
7. POWER indicator (see Lamp Status )
8. Logo plate

## Rear Panel

1. QLAN network connection (RJ-45 connector). The built-in PoE+ (Power over Ethernet+) function allows the camera to be powered by a PoE+ switch that complies with IEEE 802.3at Type 2. Use a category 5e or higher STP (shielded type) LAN cable, up to 100 m (328 ft.) in length.
2. USB port. For future expansion.
3. Memory card slot. For future expansion.
4. RESET pinhole button. To restore the NC-Pro15x network settings to default, including the network name:
  
  1. Disconnect power.
  2. Press and hold the RESET button.
  3. While pressing and holding the RESET button, reconnect power and continue holding for 10 seconds. The reset will take a few minutes.
5. HDMI OUT port. For connection to an HDMI output device.
6. SERVICE switch. For service purposes only.
7. 3G-SDI OUT port. For 3G-SDI output (BNC).
8. GEN-LOCK port. For synchronization of BNC video signals between the camera and external devices. If the reference signal is unstable, external synchronization is not possible. Subcarriers do not synchronize.
9. INPUT1, INPUT2 ports. For XLR audio input connection. These can be used for microphone / line input.
  
  - Microphone input: Input impedance 600 Ω ±10%, phantom power 48 V ±1 V, bias resistance 6.8 Ω ±1%
  - Line input: Input impedance 10k Ω ±10%
10. LED for phantom power supply. Turns blue when phantom power is supplied.
11. MIC port. Stereo 3.5 mm (0.14 in.) terminal for audio input. It can be used for microphone / line input.
  
  - Microphone input: Input impedance 1.5k Ω or higher, power 2.4 V ±0.2 V, bias resistance 2.2 k Ω ±5%
  - Line input: Input impedance 1.5 k Ω or higher
12. RS-422 port. Serial terminal (RJ-45 connector) for RS-422. Connect the GNDs on both ends to stabilize the voltage level of the signal. Use category 5e or higher STP cables. See RS-422 Port Pinout .
13. DC IN 24V port. For connection of AC adapter power supply.
14. GND port. Ground terminal.
15. Cable clamp. For prevention of cord disconnection. Pass the AC adapter cord through this clamp.

## Lamp Status

| Lamp | Lamp Status | Status |
|---|---|---|
| STATUS lamp | Orange light ON | Standby Power shortage |
| Orange light BLINKING | PT position error Firmware being updated Device failure |  |
| POWER lamp | Orange light ON | Standby |
| Orange light BLINKING | ID mode |  |
| Green light ON | Power on |  |
| Green light BLINKING | Initializing (starting and restarting) Moving to or returning from standby Device failure |  |
| Tally lamp | Red light ON | Distributing data |
| Green light ON | Preparing to distribute data |  |

## RS-422 Port Pinout

| Pin Number | Function |  |
|---|---|---|
| 1 | TX- | Output (-) |
| 2 | TX+ | Output (+) |
| 3 | RX- | Input (-) |
| 4 | GND | — |
| 5 | GND | — |
| 6 | RX+ | Input (+) |
| 7 | NC | — |
| 8 | NC | — |

## Specifications

Refer to the NC-Pro15x product page for product specifications.

