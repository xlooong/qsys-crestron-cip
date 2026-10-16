# Properties Panel
> 来源: https://help.qsys.com/Content/Q-Sys_Designer/properties_panel.htm

The Properties panel in is a section where settings and configurations for the selected component can be adjusted. It allows customization of various aspects of the component to fit specific needs. When a different component is selected, the options in the Properties panel change accordingly to show the settings for that specific component.

## Core Properties

> **Note:** For NV-32-H (Core Capable) properties related to HDMI, see the HDMI I/O (NV-32-H) topic.

### Name

The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted. Core names are limited to 63 characters.

> **Note:** This name must match the Hostname for the Core as defined in Core Manager . If you use Telnet or third-party external control, you must enter the Name exactly as it is entered here.

### Location

User-defined name that groups the component with other components in the same physical location – for example, "Rack 1" – or in the same organizational scheme.

### Model

Select your Q-SYS Core processor model. See Properties Panel for a list of selectable Core models.

### Is Redundant

If you have redundant Cores in the installation, select Yes, otherwise, leave it as No.

> **Note:** The NV-32-H (Core Capable) does not support Core Redundancy.

### Backup Name

This property displays when you set Is Redundant to Yes. Same requirements as the primary Core Name.

### External USB Audio

When enabled, you can connect an external audio device to the USB input and route audio to and from that device. See External USB Audio Device In and External USB Audio Device Out .

### GPIO

(Core 110 Series models only)

This property determines whether to expose GPIO In and GPIO Out components in the Inventory tree.

- Disabled
- Enabled
- Optional

### Network Receive Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks.

Because the specified additional latency is added both to transfers from IO Frames to the Core and from the Core to IO Frames, the additional system latency is twice the amount of additional receive buffer selected. Total system latency based on this setting is calculated and displayed immediately below the Network Receive Buffer property.

## Inventory Properties

## Inventory - Common Properties

### Name

The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted.

### Location

User-defined name that groups the component with other components in the same physical location, or in the same organizational scheme.

### Is Required

When enabled, and the device is not found on the network, the device is reported as 'Missing', which is an error condition. This is the default behavior. When disabled, and the device is not found on the network, the device is reported as 'Not Present', which is not an error condition.

### Dynamically Paired

Indicates that this virtual component can be paired with the same type of hardware without changing the network ID of the hardware or the name of this component. Refer to the Q-SYS Core Manager Dynamic Pairing topic for more information. The default is 'No'.

### Verbose

Displays the Networking and Audio Stream details for LAN A (and LAN B, if applicable to the device). You must have Is Network Redundant set to Yes to see LAN B details. Verbose is enabled by default.

## USB Bridging Properties

## USB Bridging – Common Properties

These properties appear based on the USB bridging capabilities of the Q-SYS device. Refer to the USB Video Bridge and USB Audio Bridge topics to see what Q-SYS Core processors and peripherals support USB bridging.

### USB Bridge Name

User-defined name given to the USB Bridge, from 1 to 24 characters. The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted.

### Zoom Compatibility

If you are using the HID Conferencing component to control a remote computer running Zoom or Google Meet, set this property to 'Enabled.' Otherwise, when controlling another conferencing app such as Skype for Business, set to 'Disabled' (default). When this property is enabled, the USB Bridge Name property is disabled.

> **Tip:** Enabling Zoom Compatibility may improve the user experience with macOS conferencing solutions.

### USB Video Bridge

Enable the USB Video Bridge to bridge Q-SYS Mediacast streams to USB, enabling you to view Mediacast video on a connected computer. This exposes the USB Video Bridge component in the I/O-USB Bridge Inventory tree. To see what Properties are available when the USB Video Bridge is enabled, see USB Video Bridge .

### USB Audio Bridge

Provides the capability of passing audio via USB. When this is set to anything except 'Disabled', you can drag the Speakerphone and/or Sound Card components from the device's Inventory tree into your design. To see what Properties are available when the USB Audio Bridge is enabled, see USB Audio Bridge .

- Disabled
- Speakerphone (1 x 1)
- Sound Card (2 x 2)
- Speakerphone and Sound Card
- Advanced

### Speakerphone Mode

This selection is available only when Speakerphone or Speakerphone and Sound Card is selected in the USB Audio Bridge property. Indicates if the Q-SYS design has Echo Canceling (EC) or Non-Echo Canceling (NEC). This information is provided to the PC or Mac operating system so it can determine whether or not to use its own echo canceling.

## Telephony Properties (Core 110f, Core 110c, QIO-TEL2, and POTS card only)

### Telephone Country

Select the country in which the telephone service resides.

### Telephone Tone Output

When 'Yes' is selected, the Ring, Entry, Exit, and DTMF tones are fed to a separate output channel (Tone Output) on the POTS In component. These tones can now be routed independent of the voice audio.

### Enable Call Sync

Use the Call Sync component to simplify the integration of Q-SYS collaboration devices and calling systems. It synchronizes mute state, call controls, and LED light behavior across multiple calling components, including USB HID Conferencing, Softphone, and POTS Controller. See the Call Sync topic

## I/O Properties

### I/O Slot

Identifies the type of I/O card installed in the physical Core. The number of I/O Slots varies depending on the Core Model. After you make your selection, the I/O card displays under the Core in the Inventory list. The choices are:

- Line Out
- Mic/Line In
- DataPort Out
- AES3 In / Out
- CobraNet
- Dante
- AES3 16-channel In

### Is Network Redundant

Selecting Yes allows a device to maintain network connectivity even if one network path fails. If a network problem occurs, the secondary network takes over automatically.

### SRC Disabled (AES3)

When an AES3 In / Out or AES3 16-channel In card is selected for the I/O Slot Property, you have the ability to disable or enable the AES3 Sample Rate Conversion.

## Clocking Properties

> **Note:** The PTP settings for the Core are now available in the Design Properties dialog. (Menu > File > Design Properties .)

### Sample Rate

Selects the sample rate. Typically, 48kHz is used as the Sample Rate. In scenarios where Q-SYS is externally synchronized to a (video) house sync signal you would use 48kHz Pull Down as the Sample Rate.

### Clock Source

The AES3-1 and AES3-2 options display when you have an AES3 In / Out card selected for the Core I/O slot. When you have an AES3 16-channel In card selected, only the AES3-1 option is available. Use these options to sync to an external AES3 signal. The AES3 selections require either regular AES3 or AES3 black. The clock should be connected to the AES3 card either connector Channel 1/2 In , or Channel 3/4 In .

The GPIO selections require an external TTL level word clock or a GPS connection: pin 3 is signal, pin 8 is ground. When you select GPIO A-1 or GPIO B-1 as the clock source, the respective GPIO 1 Property changes to "Input used as clock source". The clock source should be connected to pin 3 of the respective GPIO connector - either GPIO A or GPIO B.

> **Note:** Typically, Internal is used as the clock source. Only if there is a need to synchronize the Q-SYS system to an external clock would you use GPIO or AES3. You would use GPIO if the external clock signal is a word clock or GPS. You would use AES3 if the external clock signal is an AES3 signal. Often an AES3 signal without audio is used to reduce the clock jitter. This signal is called AES3 black.

### Clock Type

When the Clock Source is set to a GPIO pin, the Clock Type field is available.

### Baud Rate

- For 1PPS clocks, the default baud rate is 4800.
- For 5PPS clocks, the default baud rate is 19200.

### Verbose

Adds CPU Statistics Audio and Network to the Core Status component, along with a Reset button to reset the statistics to zero. You must have the Core Status component in the schematic area, and selected.

## Graphic Properties

### Label

Use the Label property to change the name of the component in the schematic. The Label property defaults to the component name. To learn more about renaming schematic elements, see Organizing Your Design .

### Position

The coordinates reference a specific place in the schematic - for example,"100,100" (horizontal, vertical). 0,0 is the upper left corner of the schematic.

### Fill

Sets the fill color of the component in the schematic.

## Script Access Properties

### Code Name

Displays the currently assign name for control access. You can use the auto-assigned name or customize it. Q-SYS will automatically check all Code Names in the design to ensure name is unique.

### Script Access

Defines whether the component will be accessible by script and/or externally, or not at all. Choices include All, External, None (default), and Script.

- None Q-SYS Remote Control Protocol (QRC)
- Script
- External Q-SYS Remote Control Protocol (QRC)
- All Q-SYS Remote Control Protocol (QRC)

> **Tip:** Use Script Programmer Mode to quickly view the Script Access setting directly on the component in the design schematic without the need to disconnect from the Q-SYS Core processor.

