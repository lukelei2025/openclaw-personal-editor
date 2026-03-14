#!/bin/bash
# OpenClaw 人设编辑器 - 安装脚本

set -e

echo "🎭 OpenClaw 人设编辑器 - 安装脚本"
echo "=================================="
echo ""

# 检查 OpenClaw 版本
echo "📋 检查 OpenClaw 版本..."
if ! command -v openclaw &> /dev/null; then
    echo "❌ 错误：未找到 OpenClaw"
    echo "请先安装 OpenClaw: npm install -g openclaw"
    exit 1
fi

OPENCLAW_VERSION=$(openclaw -v 2>&1 | grep -oP '\d+\.\d+\.\d+' || echo "0.0.0")
echo "✅ OpenClaw 版本: $OPENCLAW_VERSION"

# 检查版本是否符合要求
REQUIRED_VERSION="2026.2.26"
if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$OPENCLAW_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "⚠️  警告：OpenClaw 版本可能过低"
    echo "建议版本：$REQUIRED_VERSION 或更高"
    read -p "是否继续安装？(y/n): " choice
    if [ "$choice" != "y" ]; then
        echo "安装已取消"
        exit 0
    fi
fi

echo ""

# 检查 workspace
echo "📋 检查 workspace..."
WORKSPACE="$HOME/.openclaw/workspace"
if [ ! -d "$WORKSPACE" ]; then
    echo "❌ 错误：workspace 目录不存在"
    echo "请先配置 OpenClaw workspace"
    exit 1
fi
echo "✅ workspace 目录: $WORKSPACE"
echo ""

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 复制到 workspace
echo "📦 复制文件到 workspace..."
DEST_DIR="$WORKSPACE/skills/openclaw-persona-editor"

# 删除旧版本（如果存在）
if [ -d "$DEST_DIR" ]; then
    echo "  删除旧版本..."
    rm -rf "$DEST_DIR"
fi

# 复制新版本
echo "  复制新文件..."
cp -r "$PROJECT_ROOT" "$DEST_DIR"
echo "✅ 文件已复制到: $DEST_DIR"
echo ""

# 设置执行权限
echo "🔧 设置执行权限..."
chmod +x "$DEST_DIR"/scripts/*.py
echo "✅ 权限已设置"
echo ""

# 验证安装
echo "🔍 验证安装..."
if [ -f "$DEST_DIR/SKILL.md" ] && [ -f "$DEST_DIR/scripts/create_persona.py" ]; then
    echo "✅ 安装成功！"
    echo ""
    echo "安装的文件："
    echo "  - SKILL.md"
    echo "  - README.md"
    echo "  - USAGE.md"
    echo "  - INSTALL.md"
    echo "  - scripts/create_persona.py"
    echo "  - scripts/smart_update.py"
    echo "  - ..."
else
    echo "❌ 安装失败：文件不完整"
    exit 1
fi

echo ""
echo "=================================="
echo "🎉 安装完成！"
echo ""
echo "下一步："
echo "  1. 重启 Gateway:"
echo "     openclaw gateway restart"
echo ""
echo "  2. 在对话中使用:"
echo "     说：'创建 AI 助手' 或 '定义新的人设'"
echo ""
echo "  3. 或直接运行:"
echo "     python3 $DEST_DIR/scripts/create_persona.py"
echo ""
echo "详细说明请查看: $DEST_DIR/README.md"
echo "=================================="
