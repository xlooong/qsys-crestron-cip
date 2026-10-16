# Getting Started with Q-SYS Designer
> 来源: https://help.qsys.com/Content/Q-SYS_Designer/002_Getting_Started.htm

## The Design File

The design file contains all the virtual components, their connections and initial DSP settings. The design is created and maintained on a PC running Q-SYS Designer. You can save the design file on your PC, and on the Core. Only one design at a time can be on the Core.

When the design is complete, it is loaded on the Core (Save to Core and Run - F5), tested, and adjustments made. When all adjustments are finalized, the design is saved to the Core and run. It is recommended that you save the design file on your PC as a backup. After creating and saving a design to the Core, Q-SYS Designer is not required to operate the Q-SYS system.

> **Note:** If the entire system should lose power, any settings made to controls 30 seconds (or more) prior to losing power are automatically saved and restored when power is restored to the system.

## Q-SYS Designer Workspace

The Q-SYS Designer workspace can be divided into the following areas: Title Bar, main menu, Left-side Pane, Right-side Pane, and the Schematic.

- Title Bar
- main menu
- Status Bar
  
  - Core name and status - gives the user-defined name of the Core, and the status.Green indicates that communication with the Core is OK, red indicates an issue. Hovering over the Core name displays the communication status, the IP address currently being used by the Core, and all available IP Addresses.
  - If there is a Redundant Core, the status is given for that as well.
  - System Mute icon - loudspeaker with "sound waves" indicates the system is not muted. Click the icon to mute the system, the loudspeaker with the red international "NO" symbol displays, indicating the system is muted. If the Core is stopped and restarted, or you re-deploy the same design, the System Mute state is remembered. If you deploy a new design, the System Mute state is the default state of unmuted.
  - Show Administrator icon - click the icon to open a new tab in Q-SYS Designer showing the Administrator interface. Available in the Run or Emulate mode only.
- The Left-side Pane has accordion bars for: Inventory - adding and configuring hardware proxies, Schematic Pages - to assist in the layout of your design, User Control Interfaces - for designing remote interfaces, Snapshots - for saving sets of control settings to use for different events, Named Controls - to make Q-SYS controls available to Control Change Commands , Control Scripting , and external control systems,
  
  - Inventory
  - Schematic Pages
  - User Control Interfaces
  - Snapshots
  - Named Controls Control Change Commands Control Scripting external control
- Schematic Schematic Pages Signal Names
- Right-side Pane has four main sections: The Schematic Library contains a listing of all the virtual DSP, Control, and Layout components you can add to your system design. For a complete listing of the available components, and information about each one, refer to the Table of Contents > Components and Inventory Reference in this help system. When Q-SYS Designer is in Run/Emulate mode, the Schematic Library is not available. The User Library allows you to drag frequently used, and pre-configured components into the User Library and have them available for use in any design you open. In the Graphic Tools section, there is a Text tool, a Text Box tool, and a Box tool to assist in labeling and organizing your design. The Properties section is available when you have a component selected. The Properties section is used to configure the Schematic Elements, for example, you can set the number of channels available on a Mixer, you can give the Core a specific name and location. A sub-section of Properties is Control Pins . Control Pins give you access to the controls, meters, and so on within a Schematic Element to use in scripts, to control or trigger other controls, and so on. You can select the Control Pins you want to be available for each Schematic Element.
  
  - Properties Control Pins Control Pins Control Pins

## Using the Main Menu

Following is a list of features available on each of the main menu selections and a brief description of each.

## File

- New Design
- Open
  
  - If you open more than one design, multiple instances of Q-SYS Designer are opened.
  - Q-SYS Designer remembers the Schematic Pages you have open from the last time you saved the file. The open pages are remembered by filename, not by the path. If you have multiple copies of a design with the same file name, in different locations, the open pages of the last copy of the file you saved are remembered for any copy you open after that.
- Open Sample Design
- Save Different Versions of Q-SYS Designer
- Save As
- Check Design
- Save to Core & Run
- Load from Core & Connect
- Emulate Emulate Emulate Emulate Save to Core & Run Emulate
- Disconnect Disconnect (F7)
- Recently opened designs
- Design Properties
- Preferences
- Close

## Edit

- Standard Windows edit operations: Cut (Ctrl+X), Copy (Ctrl+C), Paste (Ctrl+V), Delete (Del), Duplicate (Ctrl+D), Select All (Ctrl+A), Undo (Ctrl+Z) and Redo (Ctrl+Y).
- Search and Replace

## View

To zoom within Q-SYS Designer, use the following menu items or the Zoom to selector at the bottom of the Q-SYS Designer canvas. Each schematic page or UCI page can have an independent zoom level.

- Zoom In (Ctrl++)
- Zoom Out (Ctrl+-)
- Actual Size (Ctrl+0)
- Fit To Screen (Ctrl+9)
- Reset All Zooms - resets the zoom level across all pages to 100%.
- Find (Ctrl+F)
- Application Application Zoom In (Ctrl+Shift++) (zooms the entire user interface) Application Zoom Out (Ctrl+Shift+-) (zooms the entire user interface) Application Zoom Actual Size (Ctrl+Shift+Backspace)
  
  - Application Zoom In (Ctrl+Shift++) (zooms the entire user interface)
  - Application Zoom Out (Ctrl+Shift+-) (zooms the entire user interface)
  - Application Zoom Actual Size (Ctrl+Shift+Backspace)

- Reset View

## Tools

- Group
- Ungroup
- Align
  
  - Horizontal Align Left (Ctrl+L)
  - Horizontal Align Center
  - Horizontal Align Right (Ctrl+R)
  - Horizontal Center in Page
  - Vertical Align Top (Ctrl+T)
  - Vertical Align Center
  - Vertical Align Bottom (Ctrl+B)
  - Vertical Center in Page
- Distribute
  
  - Horizontal Distribute Center
  - Horizontal Distribute Equally Spaced
  - Vertical Distribute Center
  - Vertical Distribute Equally Spaced
- Pack
  
  - Pack Left (Ctrl+Shift+L)
  - Horizontal Pack Center
  - Pack Right (Ctrl+Shift+R)
  - Pack Top (Ctrl+Shift+T)
  - Vertical Pack Center
  - Pack Bottom (Ctrl+Shift+B)
- Order
  
  - Bring to Front (Ctrl+])
  - Send to Back (Ctrl+[)
- UCI Operations Remap UCI Controls [BETA] Relink UCI Controls [BETA] Import and Export UCIs Update UCI From Bundle Import and Export UCI Variables
  
  - Remap UCI Controls [BETA]
  - Relink UCI Controls [BETA]
  - Import and Export UCIs
  - Update UCI From Bundle
  - Import and Export UCI Variables
- Component Controls
  
  - Copy Component Controls
  - Paste Component Controls
- Lock
- Unlock All
- Script Programmer Mode
- View Component Controls Info...
- Extract Named Controls...
- Show Design Resources...
- Auto Update Styles
- Open Q-SYS Library...
- Show Asset Installer...
- NVM Show NVM Manager Show NVM Designer
  
  - NVM Manager
  - NVM Designer
- Show Configurator...
- Show Administrator...
- Show Core Manager...

## Help (F1)

- Help
- Download Offline Help
- QSC Communities for Developers
- QSC Training Website
- About

## Icons

### Administrator

Quickly connects to the Administrator page. Only accessible when in Run or Emulate Mode. For more information, visit Administrator .

### Configurator

Quickly connects to Q-SYS Configurator. For more information, visit Configurator .

### Q-SYS Library

Quickly connects to Q-SYS Library to manage and download available assets. For more information, visit Q-SYS Library .

### Q-SYS Reflect Sign In

Quickly connects to the Q-SYS Reflect platform. For more information, visit Q-SYS Reflect .

### Light/Dark Theme [BETA]

Toggling between light and dark themes allows you to switch the visual appearance of your interface to either a bright or a dark color scheme.

### Window Control

Minimize: This button reduces the window to an icon on the taskbar, allowing you to keep the application running in the background without taking up screen space.

Restore: This button toggles the window between its maximized state (full screen) and its previous size and position. If the window is already maximized, clicking this button will restore it to its original size.

Close: This button closes the window and terminates the application, removing it from the taskbar and freeing up system resources.

### Mute All Audio

Toggles between muted and unmuted audio within the design. Only accessible while in Run or Emulate Mode. When selected, the icon will turn red with a slash through it.

### Auto-Hide

Each of the panes offer an Auto-Hide icon that will minimize the pane from the screen. The arrows may face the other way, depending on left or right pane.

## Using the Left-side Pane

Each accordion bar in the Left-side Pane has different characteristics, purposes, and procedures. Refer to the following topics for information.

- Using Inventory
- Using Schematic Pages
- User Control Interfaces
- Snapshots
- Named Controls
- Inspector

## Using the Schematic

Refer to Using the Schematic .

## Using the Right-side Pane

Refer to:

- Schematic Library
- Graphic Tools
- Accessing Plugins

