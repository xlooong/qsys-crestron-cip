# mDNS Client Module
> 来源: https://help.qsys.com/DeveloperHelp/Content/Code_Examples/mDNS_Example.htm

The mdnsclient module provides a set of tools for mDNS on the local network. Instantiating the object creates a local handle for a global mDNS UDP socket, shared by all Lua scripts in the design.

> **Note:** If another Lua script creates a UDP socket using port 5353, there will be a conflict, causing one instance not to operate. Because of the shared nature, only one local address can be bound across all uses of the module. To avoid conflicts, do not specify a local address.

## Properties

## mdnsclient.Verbose

Boolean property causes the mdnsclient to send messages to the debug output. Default is false .

## mdnsclient.Filter

Boolean property to use filtering, only returning packets corresponding to the last request. When set to false , all mDNS packets will be forwarded to the EventHandler. Default is true (filter active).

## Functions

## mdnsclient.New()

Create a new instance of the mdnsclient module.

## mdnsclient.EventHandler(data)

Set the EventHandler function for responses to the mDNS search. The function returns an object containing the original Packet and either an Error string or a Records table.

- data
  
  - Error
  - Records
    
    - Name
    - Type
    - Class
    - TTL
    - RawData
    - Value
  - Questions
  - Packet
  - IPV4
  - IPV6
  - Port
  - Target
  - Text

## mdnsclient:Open(localAddress)

Open the mDNS socket for use.

- localAddress Network.Interfaces()

## mdnsclient:Close()

Close the mDNS socket. Note that other instances of mdnsclient may remain open; the socket is only fully closed when all instances execute :Close() .

## mdnsclient:Send(request)

Send an mDNS request to the socket. mdns:Open() must be run first. Accepts a string or an object. There is a 30-second timeout before the same request may be sent again. Allow at least 60 seconds between re-sends of the same request.

request <string> The question string to be sent in the mDNS request, i.e. _http._tcp.local to discover HTTP services available on TCP.

i.e. mdns:Open("_http._tcp.local")

Or as an object:

request <table> Use the table format to control the formatting of the question record being sent.

- Data
- Class
- Type
- Unicast true true
- Header
  
  - Header.Id
  - Header.Flags
  - Header.QCount mdns:Send()
  - Header.ACount
  - Header.Auth
  - Header.Additional mdns:Send()

i.e. mdns:Open({Data = "_http._tcp.local", Class = 0x0001, Type = 0x00FF})

## mdnsclient.CreateQueryString(object)

Generate an mDNS name in the format <name>._<service>._<protocol>.<domain>. Either Name , or Service & Protocol are required to generate a valid query.

- Name
- Service
- Protocol tcp udp
- Domain

## Lookup Tables

## mdnsclient.QueryType

A table of known Resource Record types.

- ["A"] = 0x0001 (IPv4 address)
- ["NS"] = 0x0002
- ["MD"] = 0x0003
- ["MF"] = 0x0004
- ["CNAME"] = 0x0005 (Canonical Name)
- ["SOA"] = 0x0006
- ["MB"] = 0x0007
- ["MG"] = 0x0008
- ["MR"] = 0x0009
- ["NULL"] = 0x000A
- ["WKS"] = 0x000B
- ["PTR"] = 0x000C (Instance name pointer)
- ["HINFO"] = 0x000D
- ["MINFO"] = 0x000E
- ["MX"] = 0x000F
- ["TXT"] = 0x0010
- ["RP"] = 0x0011
- ["AFSDB"] = 0x0012
- ["X25"] = 0x0013
- ["ISDN"] = 0x0014
- ["RT"] = 0x0015
- ["NSAP"] = 0x0016
- ["NSAP-PTR"] = 0x0017
- ["SIG"] = 0x0018
- ["KEY"] = 0x0019
- ["PX"] = 0x001A
- ["GPOS"] = 0x001B
- ["AAAA"] = 0x001C (IPv6 address)
- ["LOC"] = 0x001D
- ["NXT"] = 0x001E
- ["EID"] = 0x001F
- ["NB"] = 0x0020
- ["SRV"] = 0x0021
- ["ATMA"] = 0x0022
- ["NAPTR"] = 0x0023
- ["KX"] = 0x0024
- ["CERT"] = 0x0025
- ["A6"] = 0x0026
- ["DNAME"] = 0x0027
- ["SINK"] = 0x0028
- ["OPT"] = 0x0029
- ["APL"] = 0x002A
- ["DS"] = 0x002B
- ["SSHFP"] = 0x002C
- ["IPSECKEY"] = 0x002D
- ["RRSIG"] = 0x002E
- ["NSEC"] = 0x002F
- ["DNSKEY"] = 0x0030
- ["DHCID"] = 0x0031
- ["NSEC3"] = 0x0032
- ["NSEC3PARAM"] = 0x0033
- ["TLSA"] = 0x0034
- ["HIP"] = 0x0037
- ["NINFO"] = 0x0038
- ["RKEY"] = 0x0039
- ["TALINK"] = 0x003A
- ["CDS"] = 0x003B
- ["SPF"] = 0x0063
- ["UINFO"] = 0x0064
- ["UID"] = 0x0065
- ["GID"] = 0x0066
- ["UNSPEC"] = 0x0067
- ["NID"] = 0x0068
- ["L32"] = 0x0069
- ["L64"] = 0x006A
- ["LP"] = 0x006B
- ["TKEY"] = 0x00F9
- ["TSIG"] = 0x00FA
- ["IXFR"] = 0x00FB
- ["AXFR"] = 0x00FC
- ["TMAILB"] = 0x00FD
- ["MAILA"] = 0x00FE
- ["*"] = 0x00FF (All)
- ["URI"] = 0x0100
- ["CAA"] = 0x0101
- ["DNSSECTA"] = 0x8000
- ["DNSSECDLV"] = 0x8001

## mdnsclient.QueryClass

Array containing Query Class types in name:value pairs.

- ["IN"] = 0x0001 (Internet — almost always used)
- ["CS"] = 0x0002
- ["CH"] = 0x0003 (Chaos)
- ["HS"] = 0x0004
- ["*"] = 0x00FF (Any)

## Example Usage

## Setup

Follow these steps to add the mdnsclient module to your Q-SYS design.

1. Q-SYS Library
2. Tools > Design Resources
3. Available Design Resources Install Module

> **Note:** The mdnsclient module does not function in Emulation mode, as it requires a live UDP socket on port 5353.

## Using the Examples

Call mdns:Open() before sending any requests. Use mdns.EventHandler to process incoming responses. The Target , IPV4 , IPV6 , Port , and Text fields in the response table provide the most commonly needed service discovery information.

## Single mDNS Request


```
-- Include

mdnsclient = 
require
(
"mdnsclient"
)  
-- include the mdnsclient library

-- Create Instance

mdns = mdnsclient.New()  
-- create a new instance of the mdns client

-- EventHandler

mdns.EventHandler = 
function
(tbl)  
-- set the event handler for responses

    
print
(
"mDNS response from"
, tbl.Target, tbl.IPV4)

end

-- Open and Send

mdns:Open()  
-- open the mdns socket

mdns:Send(
"_http._tcp.local"
)  
-- search for http services over tcp on the local network

-- Close after 5 seconds

Timer.CallAfter(
function
() 
mdns:Close
() 
end
, 5)  
-- close the socket after 5 seconds
```

## Using CreateQueryString


```
-- Include

mdnsclient = 
require
(
"mdnsclient"
)  
-- include the mdnsclient library

-- Create Instance

mdns = mdnsclient.New()  
-- create a new instance of the mdns client

-- Build Query String

myQuery = mdns.CreateQueryString({  
-- generate a formatted mdns query string

    Service = 
"ipp"
,

    Protocol = 
"tcp"

})

print
(myQuery)  
-- Prints "_ipp._tcp.local."

-- EventHandler

mdns.EventHandler = 
function
(tbl)  
-- set the event handler for responses

    
print
(
"Service found:"
, tbl.Target, tbl.IPV4, tbl.Port)

end

-- Open and Send

mdns:Open()  
-- open the mdns socket

mdns:Send(myQuery)  
-- send the generated query

-- Close after 5 seconds

Timer.CallAfter(
function
() 
mdns:Close
() 
end
, 5)  
-- close the socket after 5 seconds
```
