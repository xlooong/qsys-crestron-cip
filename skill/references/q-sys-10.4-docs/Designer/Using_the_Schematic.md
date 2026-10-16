# Using the Schematic
> 来源: https://help.qsys.com/Content/Q-SYS_Designer/Using_the_Schematic/Using_the_Schematic.htm

The Schematic, in the center of the Q-SYS Designer workspace, is where your Q-SYS system is designed. You organize, connect, and configure Schematic Elements, write scripts, test control logic and audio signal flow, and operate and adjust the system from the Schematic area.

- Inventory Snapshot Controllers
- The term Schematic Element refers to anything after it is in the Schematic.
- You can add multiple pages to your Schematic and link Schematic Elements across pages.

## Topics in This Section

| Basics Moving Around the Schematic Schematic Element Components Adding Components to the Schematic Finding Items Using the Context Finder Selecting Schematic Elements Copying and Pasting Schematic Elements Moving Schematic Elements Deleting Schematic Elements Headers, Text, Boxes, and Other Graphics | Signal Pins and Wiring in the Schematic Traditional Wiring Signal Names Signal Snakes Connection Types Organizing Your Design Labeling Schematic Elements Aligning Schematic Elements Properties Panel Headers, Text, Boxes, and Other Graphics Schematic Pages Coloring in Q-SYS | Using Controls Adjusting Controls Placing Controls in the Schematic Transferring Settings from one Control to Another Identifying Controls in the Schematic |
|---|---|---|

## Moving Around the Schematic

There are several ways to navigate the Schematic when it becomes larger than what can fit on a single Schematic page.

Context Finder

This feature enables quick navigation between associated Schematic Elements.

- Select an item in the Inventory list and press Ctrl+F to display its components as clickable links in the upper-right corner of the Schematic .
- Select a control in a component's control panel; if it is part of a Snapshot Bank, a link to the Snapshot Bank appears in the Snapshots list.
- Select a Signal Name to jump between its source and destination, and back.

> **Note:** Navigation from the Schematic Library to the Schematic is not supported. If an item is obscured by another component or panel, the system will jump to it, but may not be visible.

Panning

Clicking and releasing the mouse's scroll button activates a panning mode—move the mouse in any direction to reposition the Schematic, then click again to exit.

Scrolling

Scroll bars on the right and bottom edges allow vertical and horizontal movement to navigate wide schematic layouts.

The platform-level horizontal bar feature is behavior that is consistent across the Q-SYS Designer application, including all schematic pages, containers (block controllers, text controllers, UCI script), and script editors—both VSCode-based and Legacy script editors. When the content extends beyond the visible width, horizontal scrolling is automatically available and can be activated using standard input methods:

- Touchpad Gestures: Use side-to-side (two-finger) swipes on supported trackpads.
- Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
- Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
- Scroll Bar: Use mouse or arrow keys to drag the bar.

