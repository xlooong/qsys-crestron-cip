# Networked Audio Design
> 来源: https://help.qsys.com/Content/Q-Sys_Designer/Networked_Audio_Design.htm

Audio Channels and Streams are created by wiring to and from networked I/O devices. Using efficient wiring, and the capabilities of the Q-SYS Core, you can maximize the capabilities of your Q-SYS system. This topic explains the principals of Network Audio Channels (NAC) and Network Audio Streams (NAS), and how to wire the components in your design to achieve maximum efficiency in your Q-SYS system.

## Core Channel Capacities

> **Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the Licensing topic for more information.

Network Audio Streams vs. Channels

Each Q-SYS Core has separate limits for Network Audio Channels and Network Audio Streams. These limits apply to the total Network Audio I/O pool across all network audio transports (QLAN, AES67, Software Dante, SMPTE ST-2110, and System Link). A single stream may carry one or more audio channels. In many cases, you will reach the stream limit before you hit the channel limit.

For most Core models, the maximum number of Network Audio Streams (Tx and Rx) is half of the maximum Network Audio Channels. Notable exceptions:

- Server Core X50r: supports up to 1024x1024 Network Audio Streams and 4096 x 4096 Network Audio Channels when configured for 10 Gbps; at 1 Gbps it supports 256 x 256 streams and 512 x 512 channels. These totals are shared across QLAN, AES67, Software Dante, SMPTE ST‑2110, and System Link.

- Core 510i and Core 510c: support 256 x 256 streams and 256 x 256 channels.
- Core 610: supports 256 x 256 streams and up to 384 x 384 channels (with capacity scaling license); applying a capacity scaling license does not increase the stream limit.

The Check Design window in Q-SYS Designer always shows the authoritative maximum for both Network Audio Channels and Network Audio Streams for the selected Core model.

| Core Model | Local I/O Channels | Network Audio Channels 5 | Network Audio Streams | Software Dante Audio Channels 4 | AEC Processors 5 | Multitrack Audio Players | Local I/O Card Capacity | VoIP Instances |
|---|---|---|---|---|---|---|---|---|
| NV-32-H (Core Capable) Network Video Endpoint | HDMI (8-ch per port) Stereo 3.5 mm (1 x 1) | 64 x 64 | 32 x 32 | Up to 32 x 32 (none included) | 8 | 16 | N/A | 1 |
| Core Nano | 8x8 USB audio | 64 x 64 (128 x 128 w/ Licensing ) | 32 x 32 (64 x 64 w/ Licensing ) | Up to 32 x 32 (8 x 8 included) | 8 | 16 (upgradable to 32) | N/A | 2 |
| Core 8 Flex | 8 flex, 8x8 USB audio | 64 x 64 (128 x 128 w/ Licensing ) | 32 x 32 (64 x 64 w/ Licensing ) | Up to 32 x 32 (8 x 8 included) | 8 | 16 (upgradable to 32) | N/A | 2 |
| Core 24f | 24 (8 analog in, 8 analog out, 8 analog flex in/out) | 160 x 160 | 80 x 80 | Up to 64 x 64 (8 x 8 included) | 24 | 4 | N/A | 8 |
| Server Core X10 | N/A | 256 x 256 | 128 x 128 | Up to 128 x 128 (8 x 8 included) | 64 | 128 | N/A | 32 |
| Server Core X20r | N/A | 384 x 384 | 192 x 192 | Up to 256 x 256 (8 x 8 included) | 128 | 256 | N/A | 64 |
| Server Core X50r | N/A | 4096 x 4096 @10 Gbps 512 x 512 @ 1 Gbps | 1024 x 1024 @ 10 Gbps 256 x 256 @ 1Gbps | Up to 512 x 512 (8 x 8 included) | 256 | 16 (upgradable to 256) | N/A | 96 |
| Discontinued |  |  |  |  |  |  |  |  |
| Core 110c | 24 (8 analog in, 8 analog out, 8 analog flex in/out), 16 x 16 USB audio | 128 x 128 1 |  | N/A | 4 | 16 (upgradable to 32) | N/A | 1 |
| Core 110f | 24 (8 analog in, 8 analog out, 8 analog flex in/out), 16x16 USB audio | 128 x 128 1 | 64 x 64 | Up to 32 x 32 (8 x 8 included 3 ) | 16 | 16 (upgradable to 32) | N/A | 4 |
| Core 510c | Up to 32 analog, 128 x 128 (AES/CobraNet/Dante/AVB cards) | 256 x 256 |  | N/A | 64 | 16 (upgradable to 128) | 8 | 4 |
| Core 510i | Up to 32 analog, 128x128 (AES/CobraNet/Dante/AVB cards) | 256 x 256 | 256 x 256 | Up to 128 x 128 (8 x 8 included 2 ) | 64 | 16 (upgradable to 128) | 8 | 64 |
| Core 610 | N/A | 256 x 256 (384 x 384 with Licensing) | 256 x 256 (streams stay fixed) | Up to 256 x 256 (8 x 8 included) | 64 | 16 (upgradable to 128) | N/A | 64 |
| Core 5200 | N/A | 512x512 | 256 x 256 | Up to 512 x 512 (8 x 8 included 2 ) | 160 | 16 (upgradable to 128) | N/A | 64 |
| Core 6000 CXR | N/A | 256 x 256, upgradeable to 512 x 512 |  | Up to 512 x 512 (8 x 8 included) | 80, upgradeable to 160 | 16 (upgradable to 128) | N/A | 64 |

1. When using the Core 110f on-board USB Device Port for video bridging, the Q-LAN / AES67 maximum audio channel count is 80 x 64 (Q-SYS version 9.7 and later) or 64 x 64 (Q-SYS version 9.6 and earlier).

2. For units shipped after January 1, 2021. See Licensing .

3. For units shipped after March 31, 2020. See Licensing .

4. Software Dante channels count towards Network Audio Channels.

5. The maximum number of third-party microphone AEC Processors and input Network Audio Channels is affected by the quantity of Q-SYS NM-T1 microphones in the design. See NM-T1 Quantity and AEC Channel Limits .

## Network Audio Channel Fan-out

Fan-out is the distribution of a single Network Audio Channel (NAC) to multiple outputs. In Q-SYS Designer you can distribute the output several ways. This topic describes fan-out, and how to incorporate it in a Q-SYS design in the most efficient way.

Network Audio Channels are made up of virtual and physical connections.

The Q-SYS Core and I/O Frames are physically connected via the Ethernet. Each I/O Frame has four available slots for I/O cards. The I/O cards are identified in Q-SYS Designer by I/O Frame and Slot within the I/O Frame. When you make a connection in Q-SYS Designer from a Gain DSP component, for example, to a representation of an I/O card, like a Line Out card, you are telling Q-SYS that "this Gain output" is going to Channel 1 of the card in "Slot x " of "I/O Frame xyz ". In a Q-SYS Designer Schematic, the physical Ethernet connection between components is not shown, neither are the I/O Frame or Core; it is the virtual connection that is shown. The virtual connections shown in this topic are more like assignments from a DSP component running on one physical piece of hardware, to a DSP component running on a card within another physical piece of hardware.

## Network Audio Channel Definition

- A unique, point to point, audio signal on the network.
- Can be connected between Cores in multi-system installations.

## Counting Network Audio Channels in Your Design

You can determine the number of Input NACs and Output NACs by pressing Shift+F6. The Check Design dialog box displays the number of Input and Output NACs along with other information.

- When counting Input NACs, the system counts all signal pins on all input cards that are in the design and wired to another component in the schematic. If you put one Mic/Line Input card into your design, and wire all the signal pins, the Input NAC count is four because it has four connectors.
- When counting Output NACs, the system counts all the signal pins on any of the output cards that are placed in the design and wired to another component.
- When an input or output card is installed in the Core, there are no NACs because the connection is internal to the Core, and not on the network.

## Wiring in Q-SYS Designer

### Network Fan-out

Fan-out on the network is one audio signal from the Core going to multiple I/O Frames on the network. This method uses multiple NACs, and the audio signal is sent multiple times. Input signals always use one NAC per input because they are all unique, whereas an output can be the same signal going multiple places.

In this example, the signal from the Core is the same, but because it is going to two separate I/O Frames, it requires two NACs.

> **Note:** The two network connections also represent two Output Network Audio Streams because the signals go to different I/O Frames.

### I/O Frame Fan-out

Fan-out in the I/O Frame is one audio signal from the Core going to a single I/O Frame. Inside the I/O Frame the audio signal is fanned-out to a possible 16 output channels. In this case, only one NAC is used on one NAS.

The top example is how the design looks in Q-SYS Designer, the bottom is a network representation. In the example, there are 16 channels from one source, going to a single I/O Frame with four 4-channel Line Out cards, using only one NAC because it is only going to one I/O Frame.

> **Note:** The one network connection also represents one Output Network Audio Stream because the signal goes to only one I/O Frame.

## Fan-out Gain Control

### Output to Amplifiers

When one NAC is fanned-out into multiple channels, there is an individual gain control for each channel. The available controls with the Q-SYS output cards vary depending on the card.

### Loudspeakers

When QSC DataPort amplifiers, and QSC loudspeakers are used in a design, there are individual gain controls for each loudspeaker , including multi-way loudspeakers.

## Network Audio Stream

A Network Audio Stream (NAS) is a bundle of one or more NACs going to or from a single peripheral connected to the Q-LAN network, and wired in the design running on the Core.

Hardware peripherals include I/O Frames and Page Stations. A Q-LAN Receiver or Transmitter does not represent physical hardware, and needs only to be in a design (not wired) to be counted as an NAS with NACs. The Q-SYS Touchscreen and DataPort Amplifier Backup panel peripherals do not count against the NAS count.

The maximum number of NACs in a single NAS is 16 because you can only have 16 inputs or outputs.

> **Note:** An I/O Frame with four AES3 Input / Output cards installed has one Input NAS with 16 channels, and one Output NAS with 16 channels giving a total of 32 channels for a single peripheral.

## Example 1

The example shows the different types of NASs. There is one NAS for all inputs going to a single peripheral, and one NAS for all outputs going to a single peripheral. All components must be wired in the design with the exception of the Q-LAN Transmitter and Receiver.

## Example 2

This example has two I/O Frames with 16 channels each going to the Core. For each I/O Frame, there is one NAS; a total of two NASs.

## Example 3

In this example, each of two I/O Frames have both input and output cards, resulting in two input streams and two output streams. While this has the same I/O Frame count and audio channel count as the previous example, it is less efficient because more streams are required.

