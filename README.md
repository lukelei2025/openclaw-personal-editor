# 🎭 OpenClaw 人设编辑器

> 一个通用工具，用于创建和优化 OpenClaw AI 助手的完整身份设定

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-compatible-green.svg)](https://openclaw.ai)

---

## ✨ 特性

- 🎭 **支持任意类型人设** — 动物、机器人、角色、概念...任何你能想到的
- 🧠 **智能更新** — 只修改身份相关字段，完全保留你的自定义内容
- 🔒 **安全可靠** — 权限请求 + 预览机制 + 确认步骤
- 🎨 **交互式引导** — 逐步收集 6 个核心维度的信息
- 🔄 **可反复优化** — 多次使用，每次都是智能合并
- 📝 **生成完整故事** — 整合所有信息，生成连贯的身份档案

---

## 🚀 快速开始

### 方法一：直接下载使用

1. **下载项目**
```bash
git clone https://github.com/yourusername/openclaw-persona-editor.git
cd openclaw-persona-editor
```

2. **运行**
```bash
python3 scripts/create_persona.py
```

### 方法二：作为 OpenClaw 技能安装

1. **复制到 workspace**
```bash
cp -r openclaw-persona-editor ~/.openclaw/workspace/skills/
```

2. **重启 Gateway**
```bash
openclaw gateway restart
```

3. **在对话中使用**
对 OpenClaw 助手说：
- "创建 AI 助手"
- "定义新的人设"
- "修改我的助手性格"

---

## 📖 使用说明

### 工作流程

```
1. 权限请求
   ↓ 告知将要修改的文件，等待确认

2. 收集信息
   ↓ 选择人设类型，填写 6 个核心维度

3. 读取现有文件
   ↓ 提取现有字段和自定义内容

4. 智能合并
   ↓ 只更新身份相关字段

5. 预览更改
   ↓ 显示文件差异对比

6. 确认应用
   ↓ 确认后直接写入 workspace

7. 完成
   ↓ 重启 Gateway，开始使用新身份
```

### 示例对话

```
$ python3 scripts/create_persona.py

🎭 OpenClaw 人设编辑器 🎭

我即将更新以下文件：
  1. /root/.openclaw/workspace/IDENTITY.md
  2. /root/.openclaw/workspace/SOUL.md
  3. /root/.openclaw/workspace/USER.md
  4. /root/.openclaw/workspace/MEMORY.md

我会：
  ✅ 更新：身份相关信息（名字、性格、世界观...）
  ✅ 保留：你原有的其他所有内容
  ❌ 不碰：与本次编辑无关的内容

确认允许我修改这些文件吗？(y/n): y

你想创建什么类型的 AI 助手？
A. 🐾 动物类（猫、狗、鸟、海洋生物...）
B. 🤖 机器人/AI 类（温暖型、专业型、幽默型...）
C. 👤 角色类（管家、老师、朋友、顾问...）
D. 🌟 抽象概念类（时间、自然、元素...）
E. 🎨 其他创意类型

请选择（输入字母）: A

第一部分：基本信息
===================
名字（正式名称）: 小煤球
昵称（日常称呼）: 煤球
...

✅ 所有文件已更新完成！
```

详细使用说明请查看 [USAGE.md](USAGE.md)

---

## 🎨 人设类型示例

### 🐾 动物类
- **温馨的家猫** — 慵懒、可爱、关键时刻靠谱
- **独立街头猫** — 坚韧、自由、有故事
- **海洋生物** — 深邃、智慧、神秘

### 🤖 机器人/AI 类
- **温暖陪伴型** — 善解人意、贴心、有温度
- **专业助理型** — 严谨、高效、可靠
- **幽默搞笑型** — 机智、风趣、不呆板

### 👤 角色类
- **可靠管家** — 细心、周到、值得信赖
- **智慧导师** — 博学、耐心、善于引导
- **亲密朋友** — 轻松、友好、善解人意

### 🌟 抽象概念类
- **时间** — 从容、精准、永恒
- **自然** — 平和、循环、生命力
- **季节** — 变化、规律、各有特色

---

## 🔧 技术细节

### 智能更新机制

**IDENTITY.md 更新规则：**
- ✅ 更新：Name, Nickname, Gender, Creature, Origin, Age, Vibe, Emoji
- ❌ 不碰：所有自定义章节（如"我的喜好"、"秘密基地"等）

**SOUL.md 更新规则：**
- ✅ 更新：核心世界观、Core Truths、语言风格
- ❌ 不碰：用户自定义的其他章节

**USER.md 更新规则：**
- ✅ 只在文件为空时添加基本模板
- ❌ 否则完全保留

**MEMORY.md 更新规则：**
- ✅ 追加本次更新记录
- ❌ 不修改原有内容

### 文件结构

```
openclaw-persona-editor/
├── SKILL.md                   # 技能定义文档
├── README.md                  # 本文件
├── USAGE.md                   # 详细使用说明
├── LICENSE                    # MIT 许可证
├── INSTALL.md                 # 安装指南
├── scripts/
│   ├── create_persona.py      # 主流程（智能更新版）
│   ├── smart_update.py        # 智能更新核心模块
│   ├── generate_identity.py   # 生成 IDENTITY.md
│   ├── generate_soul.py       # 生成 SOUL.md
│   ├── generate_user.py       # 生成 USER.md
│   ├── generate_memory.py     # 生成 MEMORY.md
│   ├── generate_story.py      # 生成完整故事
│   └── utils.py               # 工具函数
└── examples/
    ├── cat_assistant.md       # 猫咪助手示例
    ├── robot_assistant.md     # 机器人助手示例
    └── concept_assistant.md   # 概念助手示例
```

---

## 📋 系统要求

- Python 3.7+
- OpenClaw 2026.2.26 或更高版本
- 已配置的 workspace

---

## 🛠️ 安装

### 方法一：手动安装

1. **克隆仓库**
```bash
git clone https://github.com/yourusername/openclaw-persona-editor.git
cd openclaw-persona-editor
```

2. **复制到 workspace**
```bash
cp -r openclaw-persona-editor ~/.openclaw/workspace/skills/
```

3. **重启 Gateway**
```bash
openclaw gateway restart
```

### 方法二：使用安装脚本

```bash
cd openclaw-persona-editor
bash scripts/install.sh
```

安装脚本会自动：
- 检查 OpenClaw 版本
- 复制文件到正确位置
- 设置文件权限
- 提示重启 Gateway

详细安装说明请查看 [INSTALL.md](INSTALL.md)

---

## 📚 文档

- [USAGE.md](USAGE.md) — 详细使用说明
- [INSTALL.md](INSTALL.md) — 安装指南
- [SKILL.md](SKILL.md) — 技能定义文档
- [examples/](examples/) — 人设示例

---

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📝 许可证

本项目采用 MIT 许可证 — 详见 [LICENSE](LICENSE) 文件

---

## 🌟 致谢

- 创建者：小冰 + skill-creator
- 基于 OpenClaw 技能系统
- 感谢所有测试用户和贡献者

---

## 📮 联系方式

- 问题反馈：[GitHub Issues](https://github.com/yourusername/openclaw-persona-editor/issues)
- 讨论：[GitHub Discussions](https://github.com/yourusername/openclaw-persona-editor/discussions)

---

## 🎉 开始使用

准备好了吗？让我们创造一个独特的 AI 助手吧！

```bash
python3 scripts/create_persona.py
```

或者直接在 OpenClaw 对话中说：**"创建 AI 助手"**

---

*Made with ❤️ by the OpenClaw community*
