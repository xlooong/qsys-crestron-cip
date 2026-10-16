# Check Design
> 来源: https://help.qsys.com/Content/Q-SYS_Designer/016_Check_Design.htm

Use File > Check Design (or Shift+F6) to view calculated signal processing and network usage, as well as Q-SYS Core and Q-SYS Reflect license requirements based on the design. You can check your design in the Design, Emulate, and Run modes. Check Design gives a numeric quantity or percentage of each measured parameter. The bar graph is green when the reading is within the limits and red when the limits are exceeded.

> **Note:** While Check Design can report usage and limits for DSP components (quantity of channels and streams) based on the Core model, it cannot predict usage for non-real-time functionality, including Lua scripting, plugins, audio file playback and recording, Softphone usage, Media Stream and WAN streaming, peripheral management, firmware management, Reflect connectivity, logging, and other general Q-SYS OS operations. This is because the loads placed on the Core by many of these features are dependent on external connections and formats that are not known to Q-SYS until design deployment.

> **Tip:** You can view real-time calculated usage of Core memory, as well as Control, Process, and Lua compute usage, within the Core Status component's control panel in your running design when Verbose mode is set to 'Yes' in the Properties panel. See the Status (Core) topic for more information.

## Signal Processing and Network Usage

### Total Signal Processing

This is the percentage of DSP cycles used on the Core.

- Signal Processing usage is based on the number, size, and type of DSP Components in your design.
- All of the Components in the Schematic Library are DSP Components, and all DSP Components placed in your design count against the DSP usage.
- The actual amount of DSP available depends on the model of the Core.

### Signal Processing by Category

There are two types or categories of DSP:

- Cat 1 is standard DSP – all components in the Schematic Library except the Acoustic Echo Canceler (AEC) and Notch Feedback Controller (NFC).
- Cat 2 is for the AEC (including NM-T1), NFC, and the speech-detection processing in the Voice Activity Detector (VAD).

> **Note:** Cat 2 components share the same processing resources. Designs with many AEC channels and VAD components can exceed the Cat 2 limit. See Voice Activity Detector .

### Audio Player Channels

This is the combined number of channels in all the Audio Player components in your design.

### Peripherals

This is the combined number of peripherals in use by the Core.

### Network Audio Input

This is the number of network channels into the Q-SYS Core.

- Inputs are counted when an input card is in the design and wired. Only wired input connectors on the card are counted.
- Input cards in the Q-SYS Core are not counted against the Network Audio count.
- If Loudspeaker Monitoring is used, there is one additional network input channel per DataPort card.

### Network Audio Output

This is the number of network channels from the Q-SYS Core.

- Outputs are counted when an output card is in the design and wired to a source.
- Output cards in the Q-SYS Core are not counted against the Network Audio count.

### Input Network Bandwidth

This is the bandwidth, in megabits per second, used on the network by the audio streams into the Q-SYS Core.

### Output Network Bandwidth

This is the bandwidth, in megabits per second, used on the network by the audio streams out of the Q-SYS Core.

## Q-SYS Core Licenses

This section lists the Q-SYS Feature Licenses, if any, that are required for the design to be deployed to a Q-SYS Core.

For a list of features and design components requiring a license for deployment, see Licensing .

> **Note:** Licensed features can always be run in Emulate Mode.

## Q-SYS Reflect Licenses

This section lists the number of System (Q-SYS Core) and Peripheral licenses required for monitoring with Q-SYS Reflect.

> **Tip:** You can easily sort your Inventory list to see which devices require a license to be monitored with Q-SYS Reflect. From the Inventory pane, click { } > Group by Q-SYS Reflect .

