# Camera Router
> 来源: https://help.qsys.com/Content/Schematic_Library/video_router.htm

Use this component to route Mediacast video streams between source devices, such as cameras and NV-32 HDMI I/O, and destinations like USB Video Bridges. It works as a crosspoint router, which means any input can be independently connected to any output, like a grid. A 4×2 configuration, for example, gives you four inputs and two outputs, where each output can pull from whichever input you choose. This makes it easy to switch between camera views on the fly without rewiring your design.

This component is a great fit when you want to route multiple cameras to USB Video Bridges for conferencing, take advantage of USB Video Bridge proxying for NC-Gen1 camera controls, or build designs that handle video distribution across divisible or multipurpose rooms.

> **Tip:** The Camera Router configuration can easily be added to a Snapshot Bank for a simple and intuitive way to create presets.

## Supported Q-SYS Devices

## Inputs - Sources

These are devices that send Mediacast streams, wired to inputs.

- NC-12x80, NC-20x60 PTZ Conference Cameras
- NC-110 Conference Camera
- NC-90-G2 Network ePTZ Camera
- NC-Pro 15x Network PTZ Camera
- NV-32 HDMI I/O (Mediacast output)

## Outputs - Destinations

These are devices that receive Mediacast streams, wired to outputs.

- Any Q-SYS device with a USB Video Bridge. Refer to the USB Video Bridge topic to see a list of supported hardware.
- NV-32 HDMI I/O (Mediacast input).

## Wiring Constraints

The Camera Router can only be wired to the devices listed above. It cannot be wired to:

- NVM displays.
- Other Camera Routers or Mediacast Routers (no cascading).
- System Link components.

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

## Inputs

### Input n

Receive incoming Mediacast streams from the Video Output pins of Q-SYS cameras. The number of inputs is set by the Input Count property (1–255).

## Outputs

### Output n

Send outgoing, routed Mediacast streams to the Video Input pins of USB Video Bridge–capable devices or NV-32 HDMI I/O components. The number of outputs is set by the Output Count property (1–50).

## Properties

For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Camera Router Properties

### Input Count

Sets the number of camera input pins to receive Mediacast streams. Range: 1–255. Default: 2.

### Output Count

Sets the number of output pins from which to send Mediacast streams. Range: 1–50. Default: 1.

### Image Buttons

When set to Yes, a 1 fps thumbnail of the camera's current image is displayed on each crosspoint button. Default: false.

## Controls

| Control | Type | Description |
|---|---|---|
| Output n Select | Selector | Selects which input (1 to n ) is routed to this output. Use the combo box or enter the input number directly. |
| Output n Input n Select | Button | Crosspoint matrix buttons. For each output, click a camera input's button to route it to that output. Only one input can be active at a time for a given output. When Image Buttons is enabled, each button displays a 1 fps thumbnail of the camera's current image. |
| Input n Source Name | Indicator | Displays the name of the video source currently streaming on each camera input (read-only). |
| Output n Source Name | Indicator | Displays the name of the video source currently routed to each output (read-only). |
| Output n Preview | Display | Displays a preview label or thumbnail for the currently selected source on each output. |

## Control Pins

| Pin Name | Control Type | Value | String | Position | Direction | Description |
|---|---|---|---|---|---|---|
| Source Name | Indicator | — | source name | — | Output | Displays the name of the camera source connected to this input. |

## Per-Output Pins

### Output n

| Pin Name | Control Type | Value | String | Position | Direction | Description |
|---|---|---|---|---|---|---|
| Input n Select | Toggle | 0 1 | false true | 0 1 | Input / Output | Crosspoint select. Set to 1 to route this input to the output. Only one input can be active per output. |
| Select | Selector | 1 to 255 | 1 to 255 | — | Input / Output | Selects which input number is routed to this output. |
| Source Name | Indicator | — | source name | — | Output | Displays the name of the video source currently routed to this output. |

## Output n Preview

| Pin Name | Control Type | Value | String | Position | Direction | Description |
|---|---|---|---|---|---|---|
| Preview | Text Display | — | preview label | — | Output | Preview label of the currently active source on this output. |

