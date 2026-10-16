# QDS Release Notes
> 来源: https://help.qsys.com/Content/Q-Sys_Designer/QDS_Release_Notes.htm

This topic covers release information for Q-SYS 10.5 and any maintenance releases.

> **Note:** Before upgrading your system, review the Q-SYS Designer Software Compatibility section.

## v10.5.0

Version 10.5.0 was released September 29, 2026, and includes these updates and resolved issues.

## Hardware

## QIO-WP-BT Bluetooth Wall Plate

The new QIO-WP-BT simplifies wireless BYOD audio connectivity for users while streamlining deployment for integrators. Meeting participants can effortlessly connect personal devices to stream crystal-clear stereo audio or bridge phone calls directly into the room's sound system. The compact design blends into any room aesthetic with interchangeable black and white faceplates in North American (NA) and European (EU) form factors. Because it natively integrates into the Q-SYS ecosystem over PoE, pairing and volume controls can be exposed directly on room touch screens (UCI) or automated alongside the rest of your space.

For more information, see QIO-WP-BT .

## Control

## Easier Hard-Link Identification (Core Discovery)

Give hard links descriptive names using the new Name field, making saved connections easier to recognize and manage at a glance. Names are optional, and IP addresses remain available for compatibility with earlier Q-SYS Designer versions.

For more information, see Creating Hard Links in the Remote Connectivity topic.

## Convert Wires to Signal Names (Schematic Wiring)

In Edit Mode, you can now right-click any wire connection and select Convert to Signal Names to automatically replace schematic wires with matching signal name tags across all connected pins. Designer opens the inline Signal Name Editor pre-populated with an inferred label based on the source pin.

For more information, see Signal Wiring and Pin Types .

## Highlight and Trace Signal Paths (Schematic Diagnostic)

Q-SYS Designer now includes signal tracing, a visual diagnostic tool that highlights end-to-end signal paths in your design. Select a wire or Signal Name and invoke signal tracing to see the complete path highlighted across your schematic, including across schematic pages. Tracing works bi-directionally — forward from a source, backward from a destination, or both ways from a midpoint. Traced paths are color-coded by signal type and displayed in a configurable wire style to differentiate them from standard wiring. Signal tracing is available in both Emulate and Run modes. You can customize trace colors, wire style, and component highlighting in File > Preferences > Signal Tracing. This enhancement makes signal path tracing easier to follow in complex designs, giving you the flexibility to choose colors that stand out best in your workflow.

For more information, see Preferences > Signal Wire Tracing .

## UCI Layer Tree: Expand Everything in One Double-Click

Navigating complex UCI designs just got faster. In the UCI Editor Layers tab, double-clicking the expand all /collapse all caret for a Page or Layer now fully expands all nested items within it at once — including sub-layers, flexboxes, groups, and controls. Single-clicking continues to expand or collapse one level at a time.

For more information on this or viewing, ordering, and deleting layers, go to UCI Customization > Working With Layers.

## Q-SYS Designer Software and Q-SYS Administrator Move to .NET 10

Q-SYS Designer Software and Q-SYS Administrator have been upgraded from Microsoft .NET 8 to Microsoft .NET 10.

For more information, see Software Requirements > Installation Dependencies.

## Enhanced Security With V3 Plugin Encryption

Q-SYS Designer now supports V3 encrypted plugins, providing enhanced security and intellectual property protection for Q-SYS Ecosystem plugins. This update enables plugin developers to leverage the latest encryption standards while ensuring seamless integration and reliable execution within your Q-SYS designs.

> **Note:** Designs containing V3 encrypted plugins require Q-SYS Designer Software version 10.5 or later.

For information about plugin encryption formats and version compatibility, see Plugin Encryption Compatibility Matrix in the Accessing Plugins topic.

For troubleshooting design load issues or instructions on how to check the encryption version of a plugin file, see the Q-SYS Plugin Encryption Formats & Compatibility Matrix Knowledge Base article.

## Q-SYS Remote WebSocket Control (QRWC): Token-Based Security & Access Control

Connecting custom web applications to your Q-SYS Core is now even more secure with token-based authentication for QRWC. When Access Control is enabled, administrators can manage unique credentials for external apps directly from the new Access Management > Access Tokens page in Core Manager. This gives integrations secure access to Q-SYS control objects without exposing user login credentials, while making it simple to revoke individual connections at any time.

## Platform

## Status Block: Verbose Mode Enabled by Default

When you add a status block to the schematic, the Verbose property now defaults to "Yes" and gives you immediate access to the full set of status details without needing to manually enable it. This applies to any inventory item that supports the Verbose property.

## Control Link: "Redundant Network" Property Default Set to "No"

To align with standard component defaults across Q-SYS Designer and eliminate false "compromised network" fault warnings on single-network systems, the Redundant Network property for newly added Control Link components now defaults to No. Integrators deploying Control Links across dual-network infrastructure (LAN A and LAN B) can manually set Redundant Network to Yes. Saved designs created in earlier Q-SYS versions preserve their existing redundancy settings upon upgrade.

## Control and Process Compute Usage Out of Beta

Control Compute Usage and Process Compute Usage metrics in the Status block's CPU Status tab are no longer marked as Beta. These metrics are now considered production-ready. Lua Compute Usage remains in Beta.

## Event Logging: Q-SYS Remote Control (QRC) Authentication Events Now Include Username

When Access Control is enabled, the Core Event Log now records the authenticated username for Q-SYS Remote Control (QRC) connection events, giving administrators a more complete picture of who is accessing the Core.

## Q-SYS Administrator: Removed Obsolete "File Management Protocol" Setting

The File Management Protocol option under user Access Permissions, which was previously deprecated following the removal of legacy FTP support in Q-SYS 9.3, has been removed from Q-SYS Administrator. Management of files on Q-SYS Core processors continues to be handled via the Q-SYS Management APIs.

## Discontinued Products

These products have been moved to the Discontinued category in Q-SYS Designer Software.

### Cores

Core 110f, Core 510i, Core 610, Core 5200, vCore Control.

### Controls

TSC-47w-G2, TSC-55w-G2, TSC-80w-G2, TSC-116w-G2.

### Video

NC-110

### Loudspeakers Acoustic

AD-C4T, AD-C4T-LP, AD-C6T, AD-C6T-LP, AD-C820, AD-C821, AD-C1200, AD-C81Tw, AD-S6, AD-S282H, AC-C2T, AC-C2T-LP, AP-212sw, AP-4122m FOH, AP-4122m MON, AP-5102, AP-5122, AP-5122m FOH, AP-5122m MON, AP-5152.

### Loudspeakers E Speakers

E110, E112, E115, E118, E215.

### Loudspeakers Line Array

ILA (WL2082-i), WideLine-10 (WL2102-w), WideLine-8 (WL3082).

### Loudspeakers Performance Subwoofers

WL118-sw, WL212-sw, WL218-sw, GP212-sw, GP218-sw.

### Loudspeakers Cinema

SC-222, SC-222X, SC-223, SC-223X, SC-412C, SC-413C, SC-414, SC-422C, SC-423C, SC-423CF, SC-424, SC-424-8F, SC-433C, SC-444, SC-1120, SC-1150, SC-2150, SR-800, SR-1000, SR-1020, SR-1030, SR-1290, SR-1590, SR-5152, SR-8101, SR-8200, GP118Cine-sw, RSB-212, SB-118F, SB-218F, SB-1180, SB-2180, SB-7118, SB-7218, SB-15121.

## Security

## Safeguard and Restore Core Configurations

Q-SYS Core Manager now supports full and selective system configuration backup and restore, streamlining disaster recovery, hardware replacements, and configuration rollbacks. Authorized users can generate encrypted, passphrase-protected backup archives containing Core settings, such as network parameters, access management, and peripheral configurations, to safeguard credentials and restore system state when needed.Note that this feature applies to Core system configuration settings only, while design files (.qsys) and user-managed files continue to be backed up using existing methods.

For more information, see System Backup and Restore .

## Seamless Local Core Authentication and Persistent Sessions

Q-SYS Designer now supports direct local authentication when connecting to and loading designs from Access Control–enabled Cores running Q-SYS 10.5.0 or later. Users can securely authenticate from Designer and maintain their session across disconnections and reconnections, eliminating repeated login prompts and streamlining routine system management.

For more information, see the Local Core Authentication section of Loading and Saving Designs .

## Session Timeout Now Configurable Up to 120 Minutes

Administrators can now set the idle session timeout to any value from 1 to 120 minutes. The default remains 5 minutes. Cores upgrading with a previously stored value above 120 minutes are automatically adjusted to 120 minutes, and a Warning event is recorded in the Event Log.

For more information on this and other sign-in policies, go to Access Management > Security

## Access Control: Viewer Role Security Extended Across Core, Reflect and APIs

To maintain system integrity and prevent unapproved configuration changes on active Cores, the Viewer role consistently restricts design operations across Q-SYS Designer, Q-SYS Reflect, and direct API calls. Viewer accounts can inspect system status, logs, and configuration settings without the ability to modify or pull running design files.

## Video

## USB AV Bridging for NVM Series Endpoints

Expand your collaboration capabilities with driverless USB AV Bridging now available on NVM-302E Network Video Encoder and NVM-302D Network Video Decoder . Connect a computer via USB-C to bridge video (up to 1080p), audio, and HID conferencing controls into your UC&C meeting applications, all running concurrently with network streaming and HDMI distribution. Adding an NVM device to your design Inventory automatically provides the associated USB Video Bridge , USB Audio Bridge , and HID Conferencing subcomponents without requiring additional licensing.

> **Note:** USB bridging on NVM Series devices requires a USB 3.0 or higher connection.

## Resolved Known Issues

- Control value(1
- Control Timer.CallAfter
- Control
- Control
- Endpoints
- Endpoints
- Endpoints
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Platform
- Security
- Video
- Video
- Video
- Video
- Video

