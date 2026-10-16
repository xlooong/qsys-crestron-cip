# UCI Styles（UCI 样式系统完整指南）

> 来源: UCI Styles.pdf（31页）
> 本地文件: `C:\Users\longe\Desktop\Q-SYS 文档\UCI Styles.pdf`
> 用途: UCI 样式开发、qplug 面板 CSS 样式、自定义控件外观
> 注意: Q-SYS CSS 不是标准 HTML5 CSS，是 Q-SYS 自定义的 UCI 样式系统，有独特的属性和选择器

---

## 一、概述 / Overview

可以安装自定义 CSS 文件到设计中，然后将选定的样式应用到用户控制界面 (UCI)。这样可以轻松将相同样式应用于多个 UCI 元素，实现组织内的 UCI 设计统一。

### 样式文件夹位置 / Styles Folder Location

默认路径: `\Users\<user-name>\Documents\QSC\Q-SYS Designer\Styles\`

在此目录中，为每个样式创建一个文件夹，文件夹名即为 QDS 中的样式名。

> **Tip**: 样式文件夹位置可通过 File > Preferences > General > General > Asset Directory 自定义。

---

## 二、创建样式 / Creating Styles

1. 在 Styles 文件夹中创建样式文件夹
2. 创建 `style.css` 文件放入样式文件夹
   - 使用通用代码编辑器（如 Visual Studio Code）编写
   - 参考 Supported CSS Properties 了解兼容的选择器
3. 如果使用图片或自定义字体，放入样式文件夹的子文件夹中
4. 确保 .css 文件引用正确的子文件夹路径
5. 安装样式到设计（见下文）
6. 应用样式到 UCI

---

## 三、安装/保存/移除样式 / Installing, Saving, Removing

### 安装新样式 / Installing New Styles

1. 将 .css 文件和支持图片放入 Styles 文件夹
2. 在 QDS 中创建或打开设计文件
3. 点击 Tools > Design Resources
4. 从 Available 列表选择样式名，点击 Install Style
5. 关闭 Design Resources 窗口

> **Tip**: 因为 style.css 安装到设计中，如果分享包含已安装样式的设计给他人，对方也能看到这些样式。

### 从设计保存样式 / Saving Styles from a Design

如果设计中包含本地磁盘上没有的样式文件，可以从设计中保存：
1. Tools > Design Resources
2. 从 Installed 列表选择样式名，点击保存图标
3. 样式保存到 Styles 文件夹

> **Note**: 引用的图片文件不会被保存。

### 移除样式 / Removing Styles

1. Tools > Design Resources
2. 从 Installed 列表选择样式名，点击删除图标

---

## 四、应用和更新样式 / Applying and Updating

### 应用样式到 UCI

1. 设计打开时，选择左侧面板的 User Control Interfaces
2. 选择 UCI 名称
3. 在 User Control Interface Properties（右侧面板），从下拉菜单选择 Style
4. 可选：使用 CSS Class Name 属性调整 UCI 元素的类分配（按钮、推子、文本框等）。一个元素可以属于多个 CSS 类

### 更新样式 / Updating Styles

如果修改了 style.css 文件（通过 Q-SYS Library 更新或代码编辑器），QDS 会检测到更改并提示更新设计中的样式。

- 可以在设计打开或关闭时修改 .css 文件
- 允许 QDS 在设计打开时自动更新样式（不提示）：Tools > Auto Update Styles

> **Note**: Auto Update Styles 选项不随设计保存，下次打开设计时恢复为禁用。

---

## 五、背景 CSS 属性 / Background CSS Properties

可以在 background 属性中定义 background-color、多个 background-image、background-size 和 background-position。

- 逗号分隔的图片，可选 position/size
- 图片必须是 linear-gradient() 或 url()
- Position 和 size 与 background-position、background-size 规则相同
- 正斜杠 `/` 必须分隔 position 和 size

```css
/* 示例 */
background: url("image1.jpeg");
background: url("image1.jpeg"), url("image2.jpeg"), url("image3.jpeg");
background: red 95%/70% url("image1.jpeg"), left/100% 60% linear-gradient(to bottom left, rgba(0,0,0,0.5), rgba(255,255,255,0.4));
```

---

## 六、引用图片和字体 / Referencing Images and Fonts

> **Note**: Q-SYS 不支持 CSS Font Fallbacks。font-family 属性只能定义单个字体。

### 引用图片 / Referencing Images

通过 background-image 属性提供图片文件路径来引用图片（例如按钮）：

```css
.pc{
  background-image: url(images/pc.png);
}
```

### 引用自定义字体 / Referencing Custom Fonts

使用 `@font-face` 规则引用自定义字体。确保引用字体相对于 CSS 文件的存储位置：

```css
@font-face {
  font-family: "My Fancy Font";
  src: url( fonts/fancyfont.ttf );
}
textbox {
  font-family: "My Fancy Font";
}
```

> **Note**: 正确导入 OpenType (OTF) 字体必须包含 format 参数：
> ```css
> @font-face {
>   font-family: "FontName";
>   src: url(fonts/FontName.otf) format("opentype");
> }
> ```

### 引用图标字体 / Referencing Icon Fonts

图标字体是可以在 CSS 中自定义颜色、大小和样式的图标。内置两种字体：`foundation` 和 `material`，也可以像自定义字体一样引用自定义图标字体。

#### 图标字体属性 / Icon Font Properties

| 属性 | 说明 |
|------|------|
| `-qsc-icon` | 图标字体使用的字符串。内置字体可用友好名称（如 foundation 的 `address-book`、`alert`，material 的 `3d_rotation`、`ac_unit`）；自定义字体必须是 CSS 编码的 Unicode |
| `-qsc-icon-color` | 图标的 CSS 颜色（red, rgb(r,g,b), #RRGGBB） |
| `-qsc-icon-font` | 图标字体：`foundation`(默认)、`material` 或自定义字体 |
| `-qsc-icon-align` | 对齐：`left` 或 `right` |

> **Tip**: Foundation 图标名见 zurb.com；Material 图标名见 fonts.google.com/icons。

```css
@font-face {
  font-family: dash;
  src: url(dashicons.ttf);
}
/* 自定义图标 */
.dash-friends {
  -qsc-icon-font: dash;
  -qsc-icon: "\f167";
  -qsc-icon-color: green;
}
/* foundation */
.foundation-blind {
  -qsc-icon: blind
}
/* material */
.material-brightness-1 {
  -qsc-icon: "brightness_1";
  -qsc-icon-font: material;
  -qsc-icon-color: yellow;
  -qsc-icon-align: right;
}
```

---

## 七、Meter/Knob/Fader 渲染样式 / Render Styles

QSC 渲染样式允许自定义 meter、knob 和 fader 在设计中的外观，基于控件位置。三种渲染样式：**classic**、**filmstrip**、**layer**。

### Classic（经典）

```css
-qsc-render-style: classic;
```

默认值。控件绘制时不应用渲染。

### Filmstrip（胶片）

```css
-qsc-render-style: filmstrip;
```

使用 `:value()` 选择器定义基于控件当前 `.Position` 的"帧"样式。渲染为 filmstrip 时，所有原生绘制和样式（如 Meter Style 和 Fader Style）被忽略。

支持的 CSS 属性：
- background-color
- background-image
- border
- content

```css
/* 示例：基于位置改变背景色 */
.tricolor {
  -qsc-render-style: filmstrip;
  background-color: green;
}
.tricolor:value(0.6) { background-color: orange; }
.tricolor:value(0.9) { background-color: red; }
```

```css
/* 示例：基于位置改变背景图片（旋钮） */
knob {
  -qsc-render-style: filmstrip;
  border: 0px transparent;
  background-color: transparent;
  background-image: url(k1.png);
}
knob:value(0.08) { background-image: url(k2.png); }
knob:value(0.16) { background-image: url(k3.png); }
/* ... 共13帧 ... */
knob:value(1) { background-image: url(k13.png); }
```

### Layer（图层）

```css
-qsc-render-style: layer;
```

由 meter 和 fader 支持，应用多个图层构建图形。每个图层由主样式中的类属性指定，并带有宽度和高度。图层样式还可以定义 `:value()` 选择器来定义"on"图层。"on"图层以全尺寸绘制，图层大小可裁剪到控件位置。如果未定义图层大小，则不绘制该图层。

每个图层支持：
- background-color
- background-image
- border

#### Meter 额外图层属性

| 属性 | 说明 |
|------|------|
| `-qsc-meter-indicator-class` | 绘制指示器的类名 |
| `-qsc-meter-indicator-width` | 指示器宽度（支持视口相对单位 vh, vw 等） |
| `-qsc-meter-indicator-height` | 指示器高度（支持视口相对单位） |

> base:value(1) 指示器夹点匹配 indicator:value(1) 夹点。端点（position 0 和 1）对 base:value(1) 有特殊处理：
> - position = 0：完全不绘制
> - position > 0 and < 1.0：从底部绘制匹配指示器夹点全尺寸
> - position = 1：绘制全尺寸

```css
meter {
  -qsc-render-style: layer;
  background-color: tan;
  border: 1px black;
  -qsc-meter-indicator-class : my-indicator;
  -qsc-meter-indicator-width: 50vw;
  -qsc-meter-indicator-height: 100vh;
  padding: 12px;
}
.my-indicator {
  border-radius: 15px;
  border: 1px rgba(0, 0, 0, 0.5);
  background: linear-gradient(to right, rgba(0,0,0, 0.5), rgba(255,255,0.1) 40%);
}
.my-indicator:value(1) {
  background: linear-gradient(blue, purple, red, orange,yellow);
  linear-gradient(to right, rgba(0,0,0,0.2), rgba(255,255,0.2), rgba(0,0,0.5));
}
```

#### Fader 额外图层属性

| 属性 | 说明 |
|------|------|
| `-qsc-fader-cap-class` | 绘制 fader cap 的类名 |
| `-qsc-fader-cap-width` | cap 宽度（支持视口相对单位） |
| `-qsc-fader-cap-height` | cap 高度（支持视口相对单位） |
| `-qsc-fader-slot-class` | 绘制 fader slot 的类名 |
| `-qsc-fader-slot-width` | slot 宽度（支持视口相对单位） |

> - cap 的宽度和高度由用户定义
> - slot 宽度由用户定义，高度由 `slot_height = total_height - cap_height` 计算
> - 绘制时忽略 Fader Style 属性
> - base 图层样式和 slot 都支持 `:value(1)` 选择器，并裁剪到 cap 的中心位置
> - Faders 支持 `:pressed` 选择器，允许在操作 fader 时切换样式

```css
fader {
  -qsc-render-style: layer;
  background-color: lightgreen;
  border: 1px black;
  -qsc-fader-slot-class: my-slot;
  -qsc-fader-slot-width: 10px;
  -qsc-fader-cap-class: my-cap;
  -qsc-fader-cap-height: 80vw;
  -qsc-fader-cap-width: 80vw;
}
fader:value(1) {
  background-color: lime;
  -qsc-fader-slot-class: my-slot-on;
}
.my-slot { background-color: orange; }
.my-slot:value(1) { background-color: green; }
.my-cap { background-color: blue; }
```

---

## 八、动态 CSS 类名 / Dynamic CSS Class Names

通过 Lua 中的 `.CssClass` 字段可以动态更改 UCI 控件的类名。此字段与 `.String`、`.Value`、`.Color` 等并行。

```lua
-- 更改类名并更新 UCI
if something then Controls.SomeControl.CssClass = "fancyclass" end

-- 多个类名用空格分隔
Controls.SomeControl.CssClass = "this that"
```

> **Note**: 目前脚本只能看到控件，不能操作图形对象的类名。可以通过创建控件代理来克服，但这超出了本功能范围。

---

## 九、按钮类型 / Button Types

| 按钮类型 | 用途 |
|----------|------|
| Momentary | 仅在按下时保持激活的按钮 |
| Snapshot | 底层是 state trigger |
| Trigger | 按下时激活动作但不保持状态 |
| Toggle | 每次按下在两个状态 (on/off) 间切换 |
| State Trigger | 可以有多个状态，每次按下更改状态 |

### 按钮 CSS 选择器

```css
/* 通用按钮样式 */
button {
  background-color: #654236;
  border: 1px #505050;
  font-family: 'Open Sans';
  color: #F3F2F1;
  font-size: 40px;
  border-radius: 10px;
}

/* 按下状态 */
button:pressed {
  background-color: var(--Color4);
  border: var(--BorderDecoration) var(--Color2);
}

/* Toggle/Momentary: value=1 (on/high), value=0 (off/low) */
button:value(1) {
  background-color: var(--Color2Light);
}

/* Snapshot: true=value(1), false=value(0) */
button .buttonsnapshot:value(1) { /* 设置按钮值为1/true */ }
```

### CSS 属性覆盖规则

定义的 CSS 样式属性会覆盖 QDS 中的相同属性。例如，如果 style.css 中所有按钮定义为蓝色背景，即使 QDS 属性设为红色，也会使用蓝色。但如果样式中没有定义 font-size，则使用 QDS 中指定的大小。

```css
/* 所有按钮蓝色背景 */
button{
  background: Blue;
  font-family: Lato;
  font-face: Bold;
}

/* 所有按钮 On 状态红色 */
button:value(1){
  background: Red;
}

/* 特定类的按钮：Off 绿色，On 橙色 */
.source{
  background: Green;
}
.souce:value(1){
  background: rgb(255, 174, 0);
}
```

### Pressed 按钮样式

使用 `:pressed` 选择器定义按下时的特定样式：

```css
/* 未按下灰色，按下红色 */
.myButton { background-color: gray; }
.myButton:pressed { background-color: red; }

/* 按下且 value=1 时绿色 */
.myButton:pressed:value(1) { background-color: green; }
```

---

## 十、视口相对尺寸 / Viewport Relative Sizes

某些属性（如 font-size）允许定义为包含对象宽度或高度的百分比：

| 单位 | 说明 |
|------|------|
| `vw` | 宽度百分比 |
| `vh` | 高度百分比 |
| `vmin` | 宽度或高度中较小者的百分比 |
| `vmax` | 宽度或高度中较大者的百分比 |

```css
.someclass {
  font-size: 90vh; /* 字体大小为高度的90% */
}
```

> 查看 Supported CSS Properties 主题的表格脚注了解哪些属性支持视口相对尺寸。

---

## 十一、CSS 变量 / CSS Variables

Q-SYS 在 `:root` 选择器中支持 CSS 变量。变量可以定义多个项，每个必须以 `--` 前缀。

```css
:root {
  --fancy-color: yellow;
  --fancy-border-color: chartreuse;
  --fancy-border: 30px orange;
}

/* 使用 var() 引用变量 */
.my-style {
  color: var(--fancy-color);
  border: var(--fancy-border);
  border-bottom: 5px var(--fancy-color, orange); /* 带 fallback 值 */
}
```

> **Tip**: 可以定义 fallback 值（逗号后），在变量名未定义时使用。这在包含其他样式时很有用。

---

## 十二、导入样式 / Importing Styles

可以使用 `@import` 将一个样式导入另一个样式。按名称引用要导入的样式。

**注意**:
- 导入的样式必须已经安装在 Q-SYS 设计中
- 导入后，可用类是导入样式和基础样式的组合
- 选择器声明合并：如果导入样式和基础样式都定义了选择器，最终结果是两者的组合，导入的选择器定义在前，基础的在后
- 变量也以同样方式合并
- 导入样式中引用的图片和字体相对于该样式。如果要在基础样式中引用导入的图片，必须使用相对 URL

```css
/* 基础样式导入 Dash 样式 */
@import url("Dash");

:root {
  --base-var: green;
}
page {
  background: linear-gradient(var(--base-var), rgb(54, 53, 53));
  border: var(--var-2);
}
/* 引用导入样式中的图片 */
.ref-style-image {
  background-image: url("../Dash/core_blue.png");
}
```

---

## 十三、qplug 中的 CSS 应用 / CSS in qplug

在 qplug 的 `GetControlLayout()` 中，通过 `ClassName` 属性为控件指定 CSS 类：

```lua
layout["MyButton"] = {
  Style = "Button",
  ClassName = "buttonprimary",  -- CSS 类名
  Position = {10, 10},
  Size = {100, 40}
}
```

运行时可通过 `Controls.MyControl.CssClass` 动态更改类名。
