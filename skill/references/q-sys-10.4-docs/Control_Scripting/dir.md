# dir (Directory)

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/dir.htm
> 入库时间: 2026-10-16
> 用途: Q-SYS Lua 目录操作（media/ 和 design/）

## 概述 / Overview

使用目录命令在文件系统的 `media/` 或 `design/` 位置列出文件夹和文件、创建文件夹、删除文件夹。出于安全和稳定性考虑，**这是 Lua 库唯一可访问的两个位置**。

- **media/** — 所有媒体文件的位置
- **design/** — 设计在 Q-SYS Core 上模拟或运行时，未压缩设计配置文件所在位置（**不用于存储用户创建的设计文件，且不可远程访问**）

## dir.get()

按以下条件列出 media/ 或 design/ 路径中的目录和文件：

- 指定文件夹不存在 → 返回 nil
- 文件夹存在但为空 → 返回空表
- 文件夹存在且有内容 → 返回表，每个文件/目录为独立子表，含三个参数：

| 参数 | 说明 |
|------|------|
| name | 文件或目录名称 |
| type | "file"（文件）或 "directory"（目录） |
| size | 条目大小（字节） |

### 语法

```lua
dir.get(path)
```

### 参数

- **path**: String。必须以 `/media` 或 `/design` 开头。路径用引号包围。

### 示例

```lua
temp = dir.get("media/Audio")
```

调试输出:

```
2025-09-08T09:18:39.526 Starting Script
2025-09-08T09:18:39.527 file Speech Off.wav 188460
2025-09-08T09:18:39.527 file Speech On.wav 147500
2025-09-08T09:18:39.527 directory Test 4096
```

## dir.create()

在 media/ 或 design/ 路径中创建新文件夹。

### 语法

```lua
dir.create(path)
```

### 参数

- **path**: String。必须以 `/media` 或 `/design` 开头。路径用引号包围。

### 示例

```lua
dir.create("media/Audio/New")
```

## dir.remove()

删除 media/ 或 design/ 路径中的空文件夹。

### 语法

```lua
dir.remove(path)
```

### 参数

- **path**: String。必须以 `/media` 或 `/design` 开头。路径用引号包围。

> **注意**: 要删除的文件夹**必须为空**。见下方迭代删除示例。

### 示例（先删文件再删文件夹）

```lua
directory = "media/Audio/New"
temp = dir.get(directory)
for v in os.listdir(temp) do
  os.remove(directory .. "/" .. v.name)
end

-- 然后删除空文件夹
dir.remove(directory)
```

## 要点 / Key Points

- 仅可访问 `media/` 和 `design/` 两个位置
- `dir.get()` 返回条目表：name/type/size
- 删除文件夹前必须先用 `os.remove()` 清空内容
- 路径必须以 `/media` 或 `/design` 开头
