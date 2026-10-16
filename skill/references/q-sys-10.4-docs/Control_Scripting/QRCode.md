# QRCode

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/QRCode.htm

Use the QRCode library to generate a QR code graphic that links to a specified URL.

## QRCode.GenerateSVG

Generate a QR code SVG graphic.

Syntax: `QRCode.GenerateSVG('url', ['mode'])`

### Arguments
- **url**: The URL string to encode.
- **mode**: Optional error correction mode string. low/medium/quartile/high. Defaults to "medium".
  - low = Level L, up to 7% error correction
  - medium = Level M, up to 15% error correction
  - quartile = Level Q, up to 25% error correction
  - high = Level H, up to 30% error correction
