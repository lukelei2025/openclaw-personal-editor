# 安装指南

本指南将帮助你安装 OpenClaw 人设编辑器。

## 📋 前置要求

在安装之前，请确保你已经：

1. ✅ 安装了 OpenClaw
   ```bash
   openclaw -v
   # 应显示版本号，如 2026.2.26 或更高
   ```

2. ✅ 配置了 workspace
   ```bash
   ls ~/.openclaw/workspace
   # 应该能看到这个目录
   ```

3. ✅ Python 3.7+ 已安装
   ```bash
   python3 --version
   # 应显示 Python 3.7 或更高版本
   ```

---

## 🚀 安装方法

### 方法一：自动安装脚本（推荐）

1. **克隆或下载项目**
```bash
git clone https://github.com/yourusername/openclaw-persona-editor.git
cd openclaw-persona-editor
```

2. **运行安装脚本**
```bash
bash scripts/install.sh
```

安装脚本会自动完成所有步骤，包括：
- ✅ 检查 OpenClaw 版本
- ✅ 复制文件到 workspace/skills/
- ✅ 设置执行权限
- ✅ 验证安装
- ✅ 提示重启 Gateway

### 方法二：手动安装

1. **克隆项目**
```bash
git clone https://github.com/yourusername/openclaw-persona-editor.git
cd openclaw-persona-editor
```

2. **复制到 workspace**
```bash
cp -r openclaw-persona-editor ~/.openclaw/workspace/skills/
```

3. **设置执行权限**
```bash
chmod +x ~/.openclaw/workspace/skills/openclaw-persona-editor/scripts/*.py
```

4. **验证安装**
```bash
ls ~/.openclaw/workspace/skills/openclaw-persona-editor/
# 应该能看到 SKILL.md, README.md 等文件
```

5. **重启 Gateway**
```bash
openclaw gateway restart
```

---

## ✅ 验证安装

安装完成后，你可以通过以下方式验证：

### 方法一：命令行测试

```bash
cd ~/.openclaw/workspace/skills/openclaw-persona-editor
python3 scripts/create_persona.py
```

应该能看到欢迎信息。

### 方法二：在 OpenClaw 对话中测试

对你的 OpenClaw 助手说：
```
创建 AI 劥手
```

如果助手开始询问人设类型，说明安装成功！

---

## 🔄 更新

如果已经安装了旧版本，更新方法：

### 方法一：使用 git pull

```bash
cd ~/.openclaw/workspace/skills/openclaw-persona-editor
git pull origin main
```

### 方法二：重新下载

```bash
# 删除旧版本
rm -rf ~/.openclaw/workspace/skills/openclaw-persona-editor

# 重新克隆
git clone https://github.com/yourusername/openclaw-persona-editor.git ~/.openclaw/workspace/skills/openclaw-persona-editor

# 设置权限
chmod +x ~/.openclaw/workspace/skills/openclaw-persona-editor/scripts/*.py

# 重启 Gateway
openclaw gateway restart
```

---

## ❌ 卸载

如果不再需要这个技能：

```bash
# 删除技能目录
rm -rf ~/.openclaw/workspace/skills/openclaw-persona-editor

# 重启 Gateway
openclaw gateway restart
```

---

## 🐛 故障排除

### 问题 1：找不到 openclaw 命令

**解决方案：**
```bash
# 检查 OpenClaw 是否安装
which openclaw

# 如果没有，安装 OpenClaw
npm install -g openclaw
```

### 问题 2：权限错误

**解决方案：**
```bash
# 使用 sudo（如果需要）
sudo cp -r openclaw-persona-editor ~/.openclaw/workspace/skills/

# 或者检查文件所有者
ls -la ~/.openclaw/workspace/
```

### 问题 3：技能没有触发

**解决方案：**
1. 检查 SKILL.md 是否存在
2. 检查描述是否正确
3. 重启 Gateway
4. 查看 Gateway 日志：`openclaw gateway logs`

---

## 📞 获取帮助

如果遇到问题：

1. 查看 [USAGE.md](USAGE.md) 详细使用说明
2. 查看 [README.md](README.md) 项目概述
3. 在 GitHub 提交 Issue：[github.com/yourusername/openclaw-persona-editor/issues](https://github.com/yourusername/openclaw-persona-editor/issues)

---

## 🎉 安装完成后

安装成功后，你可以：

1. **创建新人设**
   ```bash
   python3 scripts/create_persona.py
   ```

2. **在对话中使用**
   对 OpenClaw 助手说："创建 AI 助手"

3. **查看示例**
   查看 `examples/` 目录中的人设示例

4. **阅读文档**
   - [USAGE.md](USAGE.md) — 使用说明
   - [README.md](README.md) — 项目概述

---

**祝你创造出独特的 AI 助手！** 🎭
