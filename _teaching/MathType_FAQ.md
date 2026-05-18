---
title: "MathType 常见问题解答（FAQ）"
collection: teaching
type: "Tutorial"
permalink: /teaching/2024-fall-teaching-5
excerpt: ""
venue: "by Prof. Zhang"
date: 2026-05-18
location: "Beijing, China"
---

# MathType 常见问题解答（FAQ）

---

### Q1：求和/积分符号如何自动拉伸，以匹配内部较高的公式？

**A：** 在 MathType 编辑器中，**按住 Shift 键**的同时点击求和（Σ）或积分（∫）模板。这样 MathType 会根据内部公式的高度自动计算并拉伸符号，使其与被求和/积分的表达式完美匹配。

---

### Q2：将 MathType 公式从 Word 复制到另一个 Word 后，公式与文字不在同一行（错位），如何批量修复？

**A：** 这是目标文档的 MathType 格式偏好与源文档不一致导致的。批量修复步骤如下：

1. 在**目标 Word 文档**中，点击 **MathType** 选项卡；
2. 选择 **Format Equations**（格式化公式）；
3. 在弹出对话框中设置：
   - **Range**: `Whole document`（整篇文档）
   - **Format**: `MathType's 'New Equation' preferences`（或你保存的正常偏好设置）
4. 点击 **Format**。

此操作会按照当前文档的样式设置重新格式化**所有**公式，一次性修复嵌入位置和对齐问题。

---

### Q3：如何在 MathType 中开启 LaTeX 输入模式？

**A：** 按以下步骤启用：

1. 在 MathType 编辑器中，点击 **Preferences** → **Cut and Copy Preferences**；
2. 勾选 **Allow TeX language on the equation editor**（允许在公式编辑器中使用 TeX 语言）；
3. 确认后，在编辑器中按 **Alt + \\**（反斜杠）即可进入 LaTeX 输入模式；
4. 直接键入 LaTeX 代码（如 `\frac{a}{b}`），按 **Enter** 即可自动转换为可视化公式。

---

### Q4：如何实现公式编号按章节/段落自动编排？有哪些技巧？

**A：** MathType 支持自动编号并与 Word 标题样式联动。操作方法：

1. 点击 **MathType** 选项卡 → **Insert Number** → **Format**；
2. 在编号格式对话框中配置：
   - **编号样式**：如 `(1.1)`、`(2.3)`、`[1.1]` 等；
   - **章节划分依据**：选择按 **Heading 1**、**Heading 2** 等标题样式分隔；
   - **是否包含章节号**：勾选后编号会随章节自动重置（如第 2 章变为 2.1, 2.2...）。
3. 编辑时，使用 **Insert Right/Left Numbered Equation** 插入带编号的公式；
4. 若增删公式导致编号错乱，点击 **MathType** → **Update Equation Numbers** 即可全文自动更新。

* 确保 Word 的章节标题已应用正确的 **Heading 样式**，否则 MathType 无法识别章节边界。
