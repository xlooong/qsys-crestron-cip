# Reserved Notification Names
> 来源: https://help.qsys.com/DeveloperHelp/Content/Standards_Definitions/Reserved_Notifications_Names.htm

This is a companion reference for the Q-SYS Lua Notifications API . It defines the vocabulary for cross-compatible plugins.

## Compliance

Type is required. A compliant plugin must use one of the Type names below as its Notification channel type. This is what ensures two independently-developed plugins can address each other.

Commands are optional and extensible. A plugin need not implement every command listed for its type. Cross-compatibility between plugins relies on using the same names for the same operations. Custom commands may be added freely; they will simply be ignored by plugins that do not know them.

## Standard Types

These are the Q-SYS Reflect types used as Notification channel types.

| Type | Description |
|---|---|
| Amplifier | Power amplifiers and zone amplifiers |
| AudioIO | Audio I/O and signal routing devices |
| Calendar | Room calendaring and scheduling systems |
| Camera | PTZ and fixed cameras |
| CaptureDevice | Recording and capture hardware |
| Conferencing | Video conferencing endpoints and codecs |
| ControlIO | GPIO, relay, and general control I/O |
| DigitalSignage | Digital signage players and displays |
| Display | Monitors and flat panel displays |
| HVAC | Heating, ventilation, and air conditioning |
| Interface | Touch panels and control interfaces |
| Lighting | Lighting dimmers and switched loads |
| MediaPlayer | Media playback devices |
| MediaServer | Media servers and content distribution |
| Microphone | Microphones and microphone systems |
| Network | Network infrastructure devices |
| Power | Power distribution units and outlet controllers |
| Presentation | Presentation switching and control systems |
| Projector | Projectors |
| Sensors | Environmental and occupancy sensors |
| Shades | Motorized window shades and blinds |
| Speaker | Speakers and playback-only audio devices |
| VideoDistribution | Video distribution and extension systems |
| VideoSwitching | Video matrices and routing switchers |
| Other | Custom or unclassified device types |

## Commands

All standard command names, their expected data, and the types that should support them.

| name | data | Direction | Description | Supported Types (examples) |
|---|---|---|---|---|
| InputSelect | string | Set, Query, Publish | Switch to input by number | CaptureDevice, Display, Projector, VideoDistribution |
|  | Strings will be a port type+index. e.g. DVI2 is the second DVI port Types: HDMI, DVI, DISPLAYPORT, AV, HDBASET, COMPONENT, RGB, ATV, CATV, DTV, STREAM Indexes: 1-[n] for as many are available. i.e HDMI port 3 is HDMI3. All strings have an index (even if just 1) |  |  |  |
| MuteOff | - | Set | Unmute | Amplifier, AudioIO, Display, Microphone, Projector, Speaker |
| MuteOn | - | Set | Mute | Amplifier, AudioIO, Display, Microphone, Projector, Speaker |
| MuteToggle | boolean | Set, Query, Publish | Toggle mute | Amplifier, AudioIO, Microphone, Speaker |
| Next | - | Set | Next track or item | MediaPlayer |
| Pause | - | Set | Pause playback | MediaPlayer, MediaServer |
| Play | - | Set | Begin playback | DigitalSignage, MediaPlayer, MediaServer, Presentation |
| PowerOff | - | Set | Turn off | Amplifier, DigitalSignage, Display, HVAC, Power, Projector |
| PowerOn | - | Set | Turn on | Amplifier, DigitalSignage, Display, HVAC, Power, Projector |
| PowerToggle | boolean | Set, Query, Publish | Toggle power | Display, Power, Projector |
| PowerLevel | number:0-100 | Set, Query, Publish | Set Light power level | Lighting |
| Previous | - | Set | Previous track or item | MediaPlayer |
| Privacy | boolean | Set, Query, Publish | Set privacy mode | Camera |
| Reboot | - | Set | Reboot or power-cycle device | Network, Power, Display |
| RoomInUse | boolean | Query, Publish | Set room in-use state | Conferencing |
| RoomInCall | boolean | Query, Publish | Set room in-call state | Conferencing |
| RoomMicsMute | boolean | Set, Query, Publish | Set room microphones muted | Conferencing |
| RoomSpeakersMute | boolean | Set, Query, Publish | Set room speakers muted | Conferencing |
| Stop | - | Set | Stop playback or movement | DigitalSignage, MediaPlayer, MediaServer, Presentation, Shades |
| Volume | number:0–100 | Set, Query, Publish | Set volume | Amplifier, AudioIO, Speaker, Display |
|  | Translating 0-100 to the device audio level scale is the responsibility of the implementing code. |  |  |  |
