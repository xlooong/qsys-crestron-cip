# Wake on LAN
> 来源: https://help.qsys.com/DeveloperHelp/Content/Code_Examples/Wake_On_LAN_Example.htm

Wake-on-LAN (WoL) is a network-based power-on behavior. It typically uses a UDP transport to deliver a magic packet to a sleeping device. A WoL-capable device keeps enough of its NIC active to detect the packet while the system is off (soft-off/sleep).

The magic packet payload is:

1. 6 bytes of 0xFF
2. Followed by 16 repetitions of the target MAC address (6 bytes each)

WoL is commonly sent over these UDP destination ports:

- 9 (most common default)
- 7 (also very common)
- 0 (used by some tools/devices)
- Configurable vendor-specific ports (for example, some deployments use high ports such as 40000)

Most WoL-enabled devices can wake from either unicast or broadcast delivery. In practice:

- Unicast can fail when the target IP is no longer reachable in ARP/DHCP state while the device is asleep.
- Broadcast is often more reliable on local segments.
- Directed broadcast (for example 192.168.1.255 for a /24) is usually preferred over global broadcast.
- Global broadcast (255.255.255.255) may be filtered by switch/router policy.

In Q-SYS Lua, UdpSocket can send the packet with this basic flow:

1. Construct the magic packet
2. Open UDP on the desired local interface (or allow automatic interface selection)
3. Send to the chosen unicast or broadcast destination and WoL port
4. Close the socket

WoL traffic is typically one-way (fire-and-forget). Do not expect a reply from the target.

## Text Controller Setup

Drag in a Text Controller and edit the script. The simplest version is to send a general broadcast WoL packet:

## Wake-on-LAN General Broadcast Example Code


```
DeviceIP = 
"192.168.1.100"

DeviceMAC = 
"0f:0e:0d:0c:0b:0a"

-- Generate the magic Packet

MacClean = DeviceMAC:
gsub
(
"[%:%-/%s%.]"
, 
""
)

MagicPacket = 
""

for
 i = 
1
, 
12
, 
2
 
do

  MagicPacket = MagicPacket .. 
string
.
char
(
tonumber
(MacClean:
sub
(i, i + 
1
), 
16
))

end

MagicPacket = 
"\xff\xff\xff\xff\xff\xff"
 .. MagicPacket:
rep
(
16
)

-- Send the magic packet

Udp = UdpSocket.New()

Udp:Open()

Udp:Send(
"255.255.255.255"
, 
9
, MagicPacket)

Udp:Close()
```

When no interface is specified, the Q-SYS Core processor chooses the local interface based on routing/interface state. If you need deterministic behavior, open on a specific NIC and send to either unicast or directed broadcast. This targets a specific local interface and sends directly to the device IP:

## Wake-on-LAN Targeting Unicast to Specific Address


```
DeviceIP = 
"192.168.1.100"

DeviceMAC = 
"0f:0e:0d:0c:0b:0a"

-- Generate the magic Packet

MacClean = DeviceMAC:
gsub
(
"[%:%-/%s%.]"
, 
""
)

MagicPacket = 
""

for
 i = 
1
, 
12
, 
2
 
do

  MagicPacket = MagicPacket .. 
string
.
char
(
tonumber
(MacClean:
sub
(i, i + 
1
), 
16
))

end

MagicPacket = 
"\xff\xff\xff\xff\xff\xff"
 .. MagicPacket:
rep
(
16
)

-- Find local NIC by name (example: LAN A)

LocalNIC = 
nil

for
 name, nic 
in
 
pairs
(Network.Interfaces()) 
do

  
if
 name == 
"LAN A"
 
then

    LocalNIC = nic.Address

    
break

  
end

end

-- Send the magic packet

Udp = UdpSocket.New()

Udp:Open(LocalNIC)

Udp:Send(DeviceIP, 
9
, MagicPacket)

Udp:Close()
```

An alternative is to calculate the broadcast address for the device's subnet, then send there. This helps when the sleeping device no longer responds as a unicast endpoint. This computes a subnet-directed broadcast (for example, 192.168.1.255 on a /24). If no matching NIC is found, it falls back to global broadcast:

## Wake-on-LAN Calculating Network and Broadcast Range


```
DeviceIP = 
"192.168.1.100"

DeviceMAC = 
"0f:0e:0d:0c:0b:0a"

-- Generate the magic Packet

MacClean = DeviceMAC:
gsub
(
"[%:%-/%s%.]"
, 
""
)

MagicPacket = 
""

for
 i = 
1
, 
12
, 
2
 
do

  MagicPacket = MagicPacket .. 
string
.
char
(
tonumber
(MacClean:
sub
(i, i + 
1
), 
16
))

end

MagicPacket = 
"\xff\xff\xff\xff\xff\xff"
 .. MagicPacket:
rep
(
16
)

-- Calculate subnet broadcast address

DeviceIPValue = 
0

for
 octet 
in
 DeviceIP:
gmatch
(
"%d+"
) 
do

  DeviceIPValue = (DeviceIPValue << 
8
) + 
tonumber
(octet)

end

-- Find the interface that is on the same network segment

LocalNIC = 
nil

Destination = 
"255.255.255.255"

for
 _, nic 
in
 
pairs
(Network.Interfaces()) 
do

  
local
 NicIPValue = 
0

  
for
 octet 
in
 nic.Address:
gmatch
(
"%d+"
) 
do

    NicIPValue = (NicIPValue << 
8
) + 
tonumber
(octet)

  
end

  
local
 MaskValue = 
0

  
for
 octet 
in
 (nic.Netmask 
or
 
"255.255.255.0"
):
gmatch
(
"%d+"
) 
do
  
-- Sometimes the netmask may not be available. This assumes 8 bit network for a fallback

    MaskValue = (MaskValue << 
8
) + 
tonumber
(octet)

  
end

  
if
 (NicIPValue & MaskValue) == (DeviceIPValue & MaskValue) 
then

    LocalNIC = nic.Address

    
-- Calculate broadcast: (IP & Mask) | ~Mask

    
local
 BroadcastValue = (DeviceIPValue & MaskValue) | (
0xFFFFFFFF
 - MaskValue)

    Destination = 
string
.
format
(
"%d.%d.%d.%d"
, 

      (BroadcastValue >> 
24
) & 
0xFF
,

      (BroadcastValue >> 
16
) & 
0xFF
,

      (BroadcastValue >> 
8
) & 
0xFF
,

      BroadcastValue & 
0xFF
)

    
break

  
end

end

Udp = UdpSocket.New()

Udp:Open(LocalNIC)

Udp:Send(Destination, 
9
, MagicPacket)

Udp:Close()
```
