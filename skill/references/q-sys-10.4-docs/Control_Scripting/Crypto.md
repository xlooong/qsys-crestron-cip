# Crypto

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Crypto.htm

Use the Crypto commands to encode and decode ASCII text strings to and from Base64, as well as obtain CRC16, HMAC, and MD5 values for specified strings.

## Methods

| Method | Description |
|--------|-------------|
| Crypto.Base64Encode | Compute the Base64 of a specified string. |
| Crypto.Base64Decode | Convert the Base64 of a specified value to a string. |
| Crypto.CRC16Compute | Compute the CRC16 of a specified value. |
| Crypto.Cipher | Table with values for supported ciphers. |
| Crypto.Decrypt | Block-based decryption. Will raise error on failure. |
| Crypto.Digest | Compute the message digest of specified data using a specified hashing algorithm. |
| Crypto.Encrypt | Block-based encryption. Will raise error on failure. |
| Crypto.GetRandomBytes | Create a series of random bytes. |
| Crypto.Hash | Table with values for supported hash functions. |
| Crypto.HMAC | Compute the message authentication code of specified data using a specified hashing algorithm and key. |
| Crypto.MD5Compute | Compute the MD5 hash of a specified value. |
| Crypto.PBKDF2 | Implementation of Password-Based Key Derivation Function 2. |
