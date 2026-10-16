# Q-SYS CSS Class Reference（UCI 样式 CSS 类参考）

> 来源: Q-SYS CSS Class Reference.pdf（4页）
> 本地文件: `C:\Users\longe\Desktop\Q-SYS 文档\Q-SYS CSS Class Reference.pdf`
> 用途: UCI 样式开发、qplug 面板 CSS 类名参考
> 注意: Q-SYS CSS 不是标准 HTML5 CSS，是 Q-SYS 自定义的 UCI 样式系统

---

## Microsoft Teams Rooms 样式类

用于 Microsoft Teams Rooms 控制台上显示的 Q-SYS 房间控制 UCI。

### 按钮类 / Button Classes

| CSS 类名 | 用途 | 样式 |
|----------|------|------|
| `buttonprimary` | 主要用途按钮（功能切换） | 开启时浅紫色填充，关闭时深紫色 |
| `buttonsecondary` | 次要用途按钮（模式选择） | 开启时浅紫色填充，关闭时透明 |
| `buttonsnapshot` | 快照按钮（摄像头位置预设） | 已保存快照时浅紫色，未保存时深紫色 |

### 图标类 / Icon Classes

| CSS 类名 | 用途 |
|----------|------|
| `icondown` / `iconup` / `iconleft` / `iconright` | 方向按钮（摄像头位置控制） |
| `icondownbar` / `iconupbar` | 方向按钮（房间温度控制） |
| `iconeye` | 隐藏可见性按钮（摄像头隐私模式） |
| `iconhome` | 返回主页按钮（摄像头归位） |
| `iconpower` | 电源按钮 |
| `iconvolup` / `iconvoldown` / `iconvoloff` / `iconvolmute` | 音量控制按钮 |
| `iconzoomin` / `iconzoomout` | 摄像头缩放控制 |

### 文本对齐类 / Text Justify Classes

与 `textbodydisplay`、`textheadingdisplay`、`textlabeldisplay`、`texttitledisplay` 组合使用：

| CSS 类名 | 用途 |
|----------|------|
| `justifycenter` | 居中对齐 |
| `justifyleft` | 左对齐 |
| `justifyright` | 右对齐 |

### 文本类 / Text Classes

| CSS 类名 | 用途 | 对齐 |
|----------|------|------|
| `textbody` | 正文文本 | 左对齐 |
| `textbodydisplay` | 正文显示（可组合 justify） | 默认居中 |
| `textboxfader` | 推子标签文本框（紫色填充） | 居中 |
| `textheading` | 标题文本 | 左对齐 |
| `textheadingdisplay` | 标题显示（可组合 justify） | 默认居中 |
| `textlabel` | 标签文本 | 左对齐 |
| `textlabeldisplay` | 标签显示（可组合 justify） | 默认居中 |
| `texttitle` | 大标题文本 | 左对齐 |
| `texttitledisplay` | 大标题显示（可组合 justify） | 默认居中 |

---

## 使用方法 / Usage

在 Q-SYS Designer 的 UCI 中，为控件设置 `ClassName` 属性即可应用对应 CSS 类。在 qplug 的 `GetControlLayout()` 中，通过 `ClassName` 属性指定：

```lua
layout["MyButton"] = {
  Style = "Button",
  ClassName = "buttonprimary",
  Position = {10, 10},
  Size = {100, 40}
}
```

> **注意**: Q-SYS CSS 类名必须完全匹配（大小写敏感），且仅适用于 Q-SYS 提供的 UCI 样式。自定义 CSS 需要通过 UCI Styles 系统实现。
