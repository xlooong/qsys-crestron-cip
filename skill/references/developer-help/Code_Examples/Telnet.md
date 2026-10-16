# Telnet 代码示例 / Telnet Code Example

> 来源: `28. Code Examples - Telnet.pdf`
> 用途: Q-SYS 通过 Telnet 协议连接设备（如 Atlona、Extron 切换器）
> 关键模式: TCPSocket + 登录协商 + 命令发送 + 自动重连

---

## Text Controller 设置

拖入 Text Controller，命名为 `Telnet`。添加三个 Text Box：
- `IPAddress`
- `Username`
- `Password`

---

## 完整示例代码

```lua
--Aliases
IPAddress = Controls.IPAddress
Username = Controls.Username
Password = Controls.Password

--Properties
Negotiating = false  -- flag for the state of the telnet session
LoggedIn = false     -- flag for the state of the telnet negotiation
Attempting = false    -- flag for attempting to log in or not

--Initialization
function Initialization()
  print("Initializing plugin")
  Telnet = TcpSocket.New()  -- create new TCP object
  Telnet.ReadTimeout = 5    -- read timeout (seconds)
  Telnet.WriteTimeout = 5   -- write timeout (seconds)
  Telnet.ReconnectTimeout = 5  -- reconnection timeout (seconds)
  -- Line endings, there are a whole slew setup options, these are examples of SOME options.
  Telnet.LineEnding = "\r\n"
  -- Events
  Telnet.EventHandler = TelnetEvent
  Telnet.Data = ParseResponse
end

--Functions
function CredentialsEntered()  -- returns true if IP, username and password have been entered
  return IPAddress.String ~= "" and Username.String ~= "" and Password.String ~= ""
end

function Negotiate()  -- function to tack and send the do/dont/will/wont bits
  print("Attempting Negotiation")
  Attempting = true
  -- IAC DO ECHO, IAC DO SUPPRESS_GO_AHEAD, IAC WILL SUPPRESS_GO_AHEAD
  Telnet:Write(string.char(255,253,1)..string.char(255,253,3)..string.char(255,251,3))
end

function TelnetLogin()  -- function to look for user name and password prompts and send proper credentials
  if string.find(Telnet.Buffer, "login:") or string.find(Telnet.Buffer, "Username:") then
    Telnet:Write(Username.String)
  elseif string.find(Telnet.Buffer, "Password:") then
    print("Sending Password!")
    Telnet:Write(Password.String)
  end
end

function Disconnected()  -- function called when disconnected from the
  print("Disconnected")
  Attempting = false
end

function Connected()  -- function called when the telnet session is first active
  print("Telnet active")
end

function TelnetIsConnected()  -- returns true when the telnet session flag is high
  return Telnet.IsConnected
end

function Connect()
  print("Connecting")
  if CredentialsEntered() then  -- check for login info
    if not TelnetIsConnected() then  -- check if not already connected
      print("Connecting to "..IPAddress.String)
      Telnet:Connect(IPAddress.String,23)
    end
  end
end

function Initialization()  -- function called at start of runtime
  print("Initializing plugin")
  Connect()
end

function ParseResponse()  -- function that parses and prints the TCP socket
  print("Response from socket: "..Telnet.Buffer)
  if not LoggedIn then  -- assign the content of the buffer to a variable
    if string.find(Telnet.Buffer, "login:") or string.find(Telnet.Buffer, "Password:") then
      if not Negotiating then
        Negotiate()
      else
        TelnetLogin()
      end
    elseif string.find(Telnet.Buffer, "Login successful") then
      LoggedIn = true
      Negotiating = false
      print("Login successful!")
    end
    if not TelnetIsConnected then TelnetSetup=false end
  end
end

-- TCP socket callbacks
Telnet.Connected = function()  -- function called when the TCP socket is connected
  print("TCP socket connected")
end
Telnet.Reconnect = function()  -- function called when the TCP socket is reconnected
  print("TCP socket reconnected")
end
Telnet.Closed = function()  -- function called when the TCP socket is closed
  print("TCP socket closed")
  Disconnected()
end
Telnet.Error = function()  -- function called when the TCP socket has an error
  print("TCP socket error")
  Disconnected()
end
Telnet.Timeout = function()  -- function called when the TCP socket times out
  print("TCP socket timeout")
  Disconnected()
end
Telnet.Data = ParseResponse  -- ParseResponse is called when Telnet has data

--Controls
IPAddress.EventHandler = Connect
Username.EventHandler = Connect
Password.EventHandler = Connect

-- Start of runtime
Initialization()  -- calls the initialization function at the start of runtime
```

---

## 关键要点 / Key Points

1. **TCPSocket 对象**: `TcpSocket.New()` 创建，设置 ReadTimeout/WriteTimeout/ReconnectTimeout
2. **Telnet 协商**: 发送 IAC DO ECHO (255,253,1)、IAC DO SUPPRESS_GO_AHEAD (255,253,3)、IAC WILL SUPPRESS_GO_AHEAD (255,251,3)
3. **登录流程**: 检测 "login:" / "Username:" / "Password:" 提示，发送对应凭据
4. **自动重连**: ReconnectTimeout 设置后，断开会自动重连
5. **LineEnding**: 设置为 `\r\n` 匹配大多数设备
6. **Buffer**: `Telnet.Buffer` 包含接收到的数据，用 string.find 解析
7. **回调函数**: Connected/Reconnect/Closed/Error/Timeout/Data

---

## 与 qplug 的集成

在 qplug 中使用时，将上述逻辑放入 `if Controls then` 运行时块中。IP/Port 可通过属性或面板控件配置。连接成功后可发送设备特定命令（如 Extron SIS 协议 `1!`、`2!`）。
