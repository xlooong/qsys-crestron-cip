# Emulate Mode
> 来源: https://help.qsys.com/Content/Q-SYS_Designer/003_Emulate_Mode.htm

There are three modes of operation available in Q-SYS Designer: Run , Design , and Emulate .

- Run
- Design Run Emulate
- Emulate

> **Note:** Even if you are connected to a network and have a Core available, using the Emulate mode does not connect Q-SYS Designer to the Core.

Emulate mode is used during the design phase of your system to:

- Run Emulate Save to Core & Run
- test control logic such as User Control Interfaces (UCI), control scripts, and so on.

## Emulating a Design

To enter the Emulate mode, open a design in Q-SYS Designer and press the F6 button, or select File > Emulate from the main menu.

In Emulate mode the Schematic Library, and Component Properties are not available. The Inventory, Schematic Pages, User Control Interfaces, Snapshots, and Named Controls accordion bars are available you can not add or delete items from those areas. In addition you cannot move any components in the Schematic.

Open any of the component's control panels to make adjustments to controls, test external controls, UCIs, and so on.

## Limitations

Since the design is open in Q-SYS Designer on your PC, and not connected to a Core, there is no DSP taking place - the DSP takes place on the Core. As a result, there is functionality that does not work in the Emulate mode.

### General

During Emulation, there is no audio or information from physical hardware, being passed through the design. In general, the following items do not work in the Emulate mode. Some of these items may be populated with default information or values in the Emulate mode.

- Meters
- Status
- LEDs indicating signal, or status from hardware.
- Crossover Responsalyzer RTA - Band-Pass Dynamic Equalizers Filters
- Control Scripts Emulate
- Script plugin command button

### Specific Instances

There are some components that are unique in their operation in the Emulate mode.

- Audio Player
  
  - Play Stop Pause Loop Loop
  - You cannot load a file.
- Crossfader
  
  - Xfade to Gain Position
- Gain Ramp
  
  - Ramp To Gain
  - Time Rate dB/s
- Listen Amplifier Loudspeaker
  
  - Run Listen Listen Amplifier Loudspeaker Emulate

## Errors

Following are a few examples of errors that may occur when you attempt to Emulate a design.

You can have multiple Q-SYS designs open on a PC at one time, but you can only Emulate one design at a time. If you attempt to Emulate more than one design, Q-SYS displays the following error message.

If you attempt to Emulate a design that has invalid connections in the design, Q-SYS Designer displays an error message similar to the following.

The message shown above indicates that the design has a multi-port DataPort amplifier connected to either a Core and one or more I/O Frames, or two or more I/O Frames.

