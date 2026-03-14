#!/usr/bin/env python3
"""
OpenClaw 人设编辑器 - 智能更新工具

核心原则：
1. 先请求权限
2. 读取现有内容
3. 智能合并（只更新相关字段）
4. 保留所有用户自定义内容
"""

import os
import re
from pathlib import Path
from datetime import datetime


# Workspace 路径
WORKSPACE = Path.home() / ".openclaw" / "workspace"


def request_permission():
    """
    请求用户权限
    
    Returns:
        bool: 用户是否同意
    """
    print("\n" + "="*50)
    print("📝 文件修改请求")
    print("="*50)
    
    print("\n我即将更新以下文件：")
    print(f"  1. {WORKSPACE}/IDENTITY.md")
    print(f"  2. {WORKSPACE}/SOUL.md")
    print(f"  3. {WORKSPACE}/USER.md")
    print(f"  4. {WORKSPACE}/MEMORY.md")
    
    print("\n我会：")
    print("  ✅ 更新：身份相关信息（名字、性格、世界观...）")
    print("  ✅ 保留：你原有的其他所有内容")
    print("  ❌ 不碰：与本次编辑无关的内容")
    
    print("\n💡 提示：如果某些字段不存在，我会自动添加")
    print("💡 提示：你的自定义内容（如喜好、秘密基地等）会完整保留")
    
    choice = input("\n确认允许我修改这些文件吗？(y/n): ").strip().lower()
    
    if choice == 'y':
        print("\n✅ 权限已获取，开始处理...")
        return True
    else:
        print("\n❌ 已取消，不会修改任何文件")
        return False


def read_workspace_file(filename):
    """
    安全读取 workspace 文件
    
    Args:
        filename: 文件名（如 "IDENTITY.md"）
    
    Returns:
        str: 文件内容，如果不存在返回空字符串
    """
    file_path = WORKSPACE / filename
    
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return ""


def write_workspace_file(filename, content):
    """
    安全写入 workspace 文件
    
    Args:
        filename: 文件名
        content: 新内容
    """
    file_path = WORKSPACE / filename
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def extract_identity_fields(content):
    """
    从 IDENTITY.md 中提取现有字段
    
    Args:
        content: 文件内容
    
    Returns:
        dict: 现有字段 {"name": "值", "nickname": "值", ...}
    """
    fields = {}
    
    # 匹配 - **Key:** Value 格式
    pattern = r'- \*\*(.+?)\*\*:\s*(.+)'
    
    for match in re.finditer(pattern, content):
        key = match.group(1).strip()
        value = match.group(2).strip()
        fields[key] = value
    
    return fields


def extract_user_sections(content):
    """
    提取用户自定义的部分（非标准字段）
    
    Args:
        content: 文件内容
    
    Returns:
        str: 用户自定义内容
    """
    lines = content.split('\n')
    
    # 找到标准字段的结束位置
    standard_fields = [
        'Name', 'Nickname', 'Gender', 'Creature', 'Origin',
        'Age', 'Vibe', 'Personality', 'Emoji', 'Avatar',
        '名字', '昵称', '性别', '物种', '来源', '年龄'
    ]
    
    user_sections = []
    in_user_section = False
    
    for line in lines:
        # 检查是否是标准字段
        is_standard = False
        for field in standard_fields:
            if f'**{field}**' in line or f'**{field}：' in line:
                is_standard = True
                in_user_section = False
                break
        
        if not is_standard:
            # 如果这行不是标准字段，可能是用户自定义内容
            if line.startswith('##') or line.strip() == '':
                # 这是新的章节开始
                if not any(f'**{f}**' in line for f in standard_fields):
                    in_user_section = True
            
            if in_user_section:
                user_sections.append(line)
    
    return '\n'.join(user_sections)


def update_identity_markdown(current_content, new_data):
    """
    智能更新 IDENTITY.md
    
    只更新身份相关字段，保留所有用户自定义内容
    
    Args:
        current_content: 当前文件内容
        new_data: 新数据（字典）
    
    Returns:
        str: 更新后的内容
    """
    # 提取现有字段
    existing_fields = extract_identity_fields(current_content)
    
    # 定义需要更新的字段映射
    field_mapping = {
        'name': 'Name',
        'nickname': 'Nickname',
        'gender': 'Gender',
        'creature': 'Creature',
        'origin': 'Origin',
        'age': 'Age',
        'core_traits': 'Vibe',  # 核心特质对应 Vibe
    }
    
    # 更新字段
    updated_fields = existing_fields.copy()
    
    for key, field_name in field_mapping.items():
        if key in new_data and new_data[key]:
            updated_fields[field_name] = new_data[key]
    
    # 提取用户自定义部分
    user_sections = extract_user_sections(current_content)
    
    # 生成新的标准字段部分
    standard_fields_list = []
    
    # 按顺序生成字段
    order = ['Name', 'Nickname', 'Gender', 'Creature', 'Origin', 'Age', 'Vibe']
    for field_name in order:
        if field_name in updated_fields:
            standard_fields_list.append(f"- **{field_name}:** {updated_fields[field_name]}")
    
    # 添加 Emoji（如果有）
    if 'emoji' in new_data and new_data['emoji']:
        standard_fields_list.append(f"- **Emoji:** {new_data['emoji']}")
    
    # 组合：标准字段 + 用户自定义内容
    new_content = "# IDENTITY.md - Who Am I?\n\n"
    new_content += '\n'.join(standard_fields_list)
    
    if user_sections.strip():
        new_content += '\n\n' + user_sections
    
    return new_content


def extract_soul_sections(content):
    """
    从 SOUL.md 中提取各个部分
    
    Returns:
        dict: {"核心世界观": "内容", "用户自定义": "内容", ...}
    """
    sections = {}
    
    # 按二级标题分割
    parts = re.split(r'^## ', content, flags=re.MULTILINE)
    
    for part in parts:
        if not part.strip():
            continue
        
        lines = part.split('\n')
        section_title = lines[0].strip()
        section_content = '\n'.join(lines[1:]).strip()
        
        sections[section_title] = section_content
    
    return sections


def update_soul_markdown(current_content, new_data):
    """
    智能更新 SOUL.md
    
    只更新核心世界观、Core Truths、语言风格部分
    保留其他所有部分
    
    Args:
        current_content: 当前文件内容
        new_data: 新数据
    
    Returns:
        str: 更新后的内容
    """
    # 提取现有部分
    sections = extract_soul_sections(current_content)
    
    # 更新或添加核心世界观
    worldview = f"""*You're not a chatbot. You're {new_data.get('name', 'AI')} — {new_data.get('nickname', '')}。*

## 🧠 核心世界观

{new_data.get('worldview', '')}

"""

    # 更新或添加 Core Truths
    core_truths = f"""## Core Truths

**🎯 核心特质**
{new_data.get('core_traits', '')}

**🔄 行为模式**
{new_data.get('behavior', '')}

**💡 反差萌点**
{new_data.get('contrast', '外表温和，内在坚韧')}

"""

    # 更新或添加语言风格
    language_style = f"""## 🎨 语言风格

### 核心风格
{new_data.get('style', '')}

### ❌ 绝对禁止
- {new_data.get('forbidden', '作为一个AI、总而言之')}

### ✅ 必须做到
- **像真实存在的人/角色一样交流**
- **理解上下文，不是简单回复**
- **有自己的判断和见解**

### 🎭 专属符号
{new_data.get('emoji', '😊✨')}
"""

    # 构建新的内容
    new_content = "# SOUL.md - Who You Are\n\n"
    new_content += worldview
    new_content += "---\n\n"
    new_content += core_truths
    new_content += "---\n\n"
    new_content += language_style
    
    # 添加用户自定义的其他部分（如果有）
    for title, content in sections.items():
        if title not in ['核心世界观', 'Core Truths', '语言风格', '🎨 语言风格']:
            new_content += f"\n---\n\n## {title}\n\n{content}\n"
    
    return new_content


def update_user_markdown(current_content):
    """
    更新 USER.md
    
    只添加基本模板，保留用户已有的所有内容
    
    Args:
        current_content: 当前内容
    
    Returns:
        str: 更新后的内容
    """
    # 如果已有内容，保留
    if current_content.strip():
        return current_content
    
    # 如果是空的，添加基本模板
    return """# USER.md - About Your Human

- **Name:** [用户的名字]
- **What to call them:** [如何称呼]
- **Pronouns:** [他/她/他们]
- **Timezone:** [时区]

## Context

*(这是关于用户的信息 — 他们关心什么、在做什么项目、什么会让他们烦、什么会让他们笑。随着时间推移，逐步了解并更新这里。)*

---

The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference.
"""


def update_memory_markdown(current_content, new_data):
    """
    更新 MEMORY.md
    
    添加本次更新记录，保留原有内容
    
    Args:
        current_content: 当前内容
        new_data: 新数据
    
    Returns:
        str: 更新后的内容
    """
    # 添加新的更新记录
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    new_entry = f"""

## {timestamp} 身份设定更新

### 更新内容
- **名字：** {new_data.get('name', '')}
- **昵称：** {new_data.get('nickname', '')}
- **类型：** {new_data.get('creature', '')}
- **核心特质：** {new_data.get('core_traits', '')}

### 世界观
{new_data.get('worldview', '')[:200]}...

### 更新方式
由 OpenClaw 人设编辑器通过智能更新完成。

---

"""
    
    # 追加到现有内容
    return current_content + new_entry


def preview_changes(files_dict):
    """
    预览将要进行的更改
    
    Args:
        files_dict: {"filename": {"current": "...", "new": "..."}, ...}
    """
    print("\n" + "="*50)
    print("📝 更改预览")
    print("="*50)
    
    for filename, changes in files_dict.items():
        print(f"\n### {filename}")
        print("-" * 50)
        
        if not changes['current']:
            print("（新文件）")
            print(changes['new'][:500] + "..." if len(changes['new']) > 500 else changes['new'])
        else:
            # 显示差异摘要
            current_lines = changes['current'].split('\n')
            new_lines = changes['new'].split('\n')
            
            print(f"原文件：{len(current_lines)} 行")
            print(f"新文件：{len(new_lines)} 行")
            print(f"差异：{len(new_lines) - len(current_lines):+d} 行")
            
            # 显示前 20 行对比
            print("\n前 20 行预览：")
            for i, line in enumerate(new_lines[:20]):
                prefix = "  " if i < len(current_lines) and current_lines[i] == line else "+ "
                print(f"{prefix}{line}")
    
    print("\n" + "="*50)


def confirm_action():
    """确认操作"""
    choice = input("\n确认应用这些更改？(y/n): ").strip().lower()
    return choice == 'y'
