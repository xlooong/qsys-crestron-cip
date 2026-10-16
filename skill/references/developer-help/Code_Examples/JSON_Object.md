# JSON Object 代码示例 / JSON Object Code Example

> 来源: `16.Code Examples - JSON Object.pdf`
> 用途: Q-SYS 中 JSON 编解码和文件读写（如 Atlona JSON-RPC API）
> 关键库: `rapidjson`（推荐），旧版 `json`

---

## Encode/Decode（编解码）

### Text Controller 设置

- Combo Box 命名 `Type`（Encode/Decode）
- Text Box 命名 `Input`、`Name`、`Version`
- Text Indicator 命名 `Output`

### 示例代码

```lua
--Include
rapidjson = require("rapidjson")  -- include the rapidjson library

--Aliases
Type = Controls.Type
Input = Controls.Input
Name = Controls.Name
Version = Controls.Version
Output = Controls.Output

--Properties
JSONChoices = {"Encode","Decode"}  -- combobox choices

--Functions
function ShowWhereInfo()  -- gets and prints JSON version to text boxes
  Name.String = rapidjson._NAME  -- get rapidjson name
  Version.String = rapidjson._VERSION  -- get rapidjson version
end

function TypeChange()  -- set the combobox choices
  Type.Choices = JSONChoices
  Type.String = JSONChoices[1]
end

function ProcessData()  -- process the string in the input textbox
  if Input.String ~= "" then
    if Type.String == "Encode" then
      Output.String = rapidjson.encode(Input.String)  -- encode the string in the input textbox
    elseif Type.String == "Decode" then
      local dec = rapidjson.decode(Input.String)  -- decode the string in the input textbox
      if dec ~= nil then
        Output.String = dec  -- print the result in output textbox
      else
        Output.String = "Error in string"  -- print data is invalid or error if nil
      end
    end
  end
end

function Initialization()  -- function called at the start of runtime
  ShowWhereInfo()
  TypeChange()
  ProcessData()
end

--EventHandlers
Type.EventHandler = ProcessData  -- calls process data when type eventhandler is called
Input.EventHandler = ProcessData  -- calls process data when input eventhandler is called

--Start of runtime
Initialization()  -- calls initialization at the start of runtime
```

---

## Read/Write Files（文件读写）

### Text Controller 设置

- Text Box 命名 `Input`、`Name`
- Combo Box 命名 `Location`（media/design）
- Text Indicator 命名 `Output`

### 示例代码

```lua
--Include
rapidjson = require("rapidjson")  -- include the rapidjson library

--Aliases
Name = Controls.Name
Location = Controls.Location
Input = Controls.Input
Output = Controls.Output

--Properties
LocationChoices = {"media","design"}  -- location choices
Writing = false  -- set to true when writing that can run in emulation mode

--Functions
function WriteJSON(location)  -- write JSON file
  local fileName = Name.String
  local data = Input.String
  if location == "media" then
    rapidjson.dump(data, "media/"..fileName)  -- write JSON file to the location file path
  elseif location == "design" then
    rapidjson.dump(data, "design/"..fileName)  -- write JSON file to the location file path
  end
  Timer.CallAfter(ReadJSON, 0.5, location)  -- call the ReadJSON function after .5 seconds and pass location
end

function ReadJSON(location)  -- read JSON file
  local fileName = Name.String
  if location == "media" then
    local data = rapidjson.load("media/"..fileName)  -- read JSON file and print it in the output textbox
    Output.String = data
  elseif location == "design" then
    local data = rapidjson.load("design/"..fileName)  -- read JSON file and print it in the output textbox
    Output.String = data
  end
end

function ToggleReadWrite()  -- function that set controls disable by state and throws warnings if in emulation mode
  if Location.String == "media" then
    if System.IsEmulating then  -- check if emulating
      Output.String = "Warning: using Location.string = media only works when not in emulation mode"
    else
      if Writing then ReadJSON(Location.String) else WriteJSON(Location.String) end  -- show warnings if in emulation mode
    end
  elseif Location.String == "design" then
    if Writing then ReadJSON(Location.String) else WriteJSON(Location.String) end
  end
end

function Initialization()  -- function called at the start of runtime
  if not IsInDesign() then
    Location.Choices = LocationChoices
    Location.String = LocationChoices[1]
  end
  ToggleReadWrite()
end

--EventHandlers
Input.EventHandler = ToggleReadWrite
Name.EventHandler = ToggleReadWrite
Location.EventHandler = ToggleReadWrite

--Start of runtime
Initialization()  -- calls initialization at the start of runtime
```

---

## 关键 API / Key API

| 函数 | 说明 |
|------|------|
| `rapidjson.encode(table)` | Lua 表 → JSON 字符串 |
| `rapidjson.decode(string)` | JSON 字符串 → Lua 表 |
| `rapidjson.dump(data, path)` | 写入 JSON 文件 |
| `rapidjson.load(path)` | 读取 JSON 文件 |
| `rapidjson._NAME` | 库名称 |
| `rapidjson._VERSION` | 库版本 |

---

## Atlona JSON-RPC 应用示例

```lua
-- 发送 Atlona USB 切换查询
local request = rapidjson.encode({
  jsonrpc = "2.0",
  id = "test",
  method = "UsbSwitch.Get"
})
http:Download{
  Url = "http://192.168.101.99/api",
  Method = "POST",
  Headers = {["Content-Type"] = "application/json"},
  Body = request
}
```

> **Note**: 文件读写示例在 Emulation 模式下不工作（media 路径）。
