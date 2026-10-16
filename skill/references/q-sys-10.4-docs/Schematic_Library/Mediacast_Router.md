# Mediacast Router
> 来源: https://help.qsys.com/Content/Schematic_Library/mc_router_class.htm

The Mediacast Router is a video routing component found in the Video section of the Components palette in Q-SYS Designer. It routes Mediacast video streams between source devices, such as cameras, NV-32 HDMI I/O, and destination devices, such as USB Video Bridges and NVM displays.

The Mediacast Router works as a crosspoint router — think of it as a grid where any input on one side can be independently connected to any output on the other. For example, a 4×2 Mediacast Router has four inputs and two outputs, and each output can independently select which of the four inputs it receives. This lets you switch between camera views on the fly without rewiring your design.

Use the Mediacast Router when you need to:

- Route multiple cameras to USB Video Bridges for conferencing and switch between views.
- Distribute video to NVM (Network Video Matrix) displays in large or multi-zone venues.
- Cascade multiple routers together for complex routing topologies.

## Supported Q-SYS Devices

## Inputs - Sources

These are devices that send Mediacast streams, wired to inputs.

- NC-12x80, NC-20x60 PTZ Conference Cameras
- NC-110 Conference Camera
- NC-90-G2 Network ePTZ Camera
- NC-Pro 15x Network PTZ Camera

- NV-32 HDMI I/O (Mediacast output)
- Other Mediacast Routers (cascading)

## Outputs - Destinations

These are devices that receive Mediacast streams, wired to outputs.

- Any Q-SYS device with a USB Video Bridge. Refer to the USB Video Bridge topic to see a list of supported hardware.
- NVM Decoders (Mediacast input)
- NV-32 HDMI I/O (Mediacast input)
- Other Mediacast Routers (cascading)

## About Mediacast Router and Camera Router

Starting in Q-SYS Designer 10.4, the original Mediacast Router has been renamed to Camera Router , and a new component called Mediacast Router has been introduced. When existing designs are opened in 10.4, any previous Mediacast Router components are automatically migrated and relabeled as Camera Router.

Both components are available in the Components palette and can be used together in the same design. They share the same crosspoint routing concept, but support different device types and capabilities:

| Feature | Mediacast Router (New) | Camera Router |
|---|---|---|
| Route cameras to USB Video Bridges | Yes | Yes |
| Route to NVM Displays | Yes | No |
| Cascade (wire to other routers) | Yes | No |
| Output Enable (mute / unmute output) | Yes | No |
| System Link Tx/Rx | No | No |
| USB Video Bridge camera control proxying (NC-Gen1) | No | Yes |

## Inputs and Outputs

## Input n

Receive incoming Mediacast streams from the Video Output pins of Mediacast-capable components — cameras, NVM displays, or other mediacast routers. The number of inputs is set by the Input Count property (1–255).

## Output n

Send outgoing, routed Mediacast streams to the Video Input pins of Mediacast-capable components — USB Video Bridges, NVM displays, or other mediacast routers. The number of outputs is set by the Output Count property (1–50).

## Properties

## Mediacast Router Properties

For additional properties that are not listed, refer to the Properties Panel help topic for more information.

### Input Count

Sets the number of input pins to receive Mediacast streams. Range: 1–255. Default: 2.

### Output Count

Sets the number of output pins from which to send Mediacast streams. Range: 1–50. Default: 2.

### Outputs per Tab

Sets the number of output columns displayed per tab in the control panel, useful for organizing large output counts. Default: 32.

## Controls

| Control | Type | Description |
|---|---|---|
| Output n Enable | Button | Enables or disables the output. When disabled, the output stops sending its routed stream to the downstream device — similar to a mute button on an audio router. Downstream sink devices behave as if the output has been switched to an unwired source, which triggers their Idle Mode timers. Default: enabled. |
| Output n Select | Selector | Selects which input (1 to n ) is routed to this output. Use the selector control or enter the input number directly. |
| Output n Input n Select | Button | Crosspoint matrix buttons. For each output, click an input's button to route it to that output. Only one input can be active at a time for a given output. |
| RTP Address | Text (read-only) | Displays the multicast RTP address assigned to the Preview stream when enabled. This address comes from Core Manager's Multicast Address range for Cameras. |
| Preview | Display | Displays a live video preview of each output's currently routed source using Media Display technology. You can drag a preview into a UCI to allow live-video-capable rendering devices to display the video at full frame rate. |
| Source Name | Indicator | Displays the name of the video source currently routed to each output (read-only). |

## Control Pins

## Per-Input Pins

### Input n

| Pin Name | Control Type | Value | String | Position | Direction | Description |
|---|---|---|---|---|---|---|
| Source Name | Indicator | — | source name | — | Output | Displays the name of the video source connected to this input. |

## Per-Output Pins

### Output n

| Pin Name | Control Type | Value | String | Position | Direction | Description |
|---|---|---|---|---|---|---|
| Input n Media | Media Stream | — | — | — | Output | Carries the routed video stream for this input / output crosspoint. |
| Input n Select | Toggle | 0 1 | false true | 0 1 | Input / Output | Crosspoint select. Set to 1 to route this input to the output. Only one input can be active per output. |
| Enable | Toggle | 0 1 | false true | 0 1 | Input / Output | Enables or disables the output. When disabled, downstream devices behave as if the output is unwired. |
| Select | Selector | 1 to 255 | 1 to 255 | — | Input / Output | Selects which input number is routed to this output. |
| Source Name | Indicator | — | source name | — | Output | Displays the name of the video source currently routed to this output. |

## Output n Preview

| Pin Name | Control Type | Value | String | Position | Direction | Description |
|---|---|---|---|---|---|---|
| Preview | Text Display | — | preview label | — | Output | Preview label of the currently active source on this output. |

