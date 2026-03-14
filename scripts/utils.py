#!/usr/bin/env python3
"""
OpenClaw 人设编辑器 - 工具函数
"""

import os
import json
from pathlib import Path
from datetime import datetime

# 输出目录（默认不直接修改 workspace）
OUTPUT_DIR = Path("/tmp/openclaw-persona")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_file(filename, content):
    """保存文件到输出目录"""
    file_path = OUTPUT_DIR / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path


def load_temp_data(session_id="default"):
    """加载临时数据"""
    temp_file = OUTPUT_DIR / f"temp_{session_id}.json"
    if temp_file.exists():
        with open(temp_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_temp_data(data, session_id="default"):
    """保存临时数据"""
    temp_file = OUTPUT_DIR / f"temp_{session_id}.json"
    with open(temp_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def collect_dimension_info(dimension_name, options, allow_custom=True):
    """
    收集某个维度的信息
    
    Args:
        dimension_name: 维度名称
        options: 选项字典 {"A": "描述", "B": "描述", ...}
        allow_custom: 是否允许自由编辑
    
    Returns:
        用户的选择或自定义内容
    """
    print(f"\n🎭 {dimension_name}")
    print("=" * 50)
    
    for key, value in options.items():
        print(f"{key}. {value}")
    
    if allow_custom:
        print("D. 自由编辑")
    
    choice = input("\n请选择（输入字母或自定义内容）: ").strip()
    
    if choice.upper() == 'D' and allow_custom:
        print("\n请输入你的想法（输入完成后按回车）:")
        return input("> ").strip()
    elif choice.upper() in options:
        return options[choice.upper()]
    else:
        print("无效选择，使用默认选项 A")
        return options.get('A', '')


def preview_files(files_dict):
    """
    预览要生成的文件
    
    Args:
        files_dict: {"filename.md": "content", ...}
    """
    print("\n" + "="*50)
    print("📝 即将生成的文件预览")
    print("="*50)
    
    for filename, content in files_dict.items():
        print(f"\n### {filename}")
        print("-" * 50)
        # 显示前 20 行作为预览
        lines = content.split('\n')[:20]
        for line in lines:
            print(line)
        if len(content.split('\n')) > 20:
            remaining = len(content.split('\n')) - 20
            print(f"\n... (还有 {remaining} 行)")
    
    print("\n" + "="*50)
    print(f"所有文件将保存到：{OUTPUT_DIR}")
    print("="*50)


def confirm_action():
    """确认操作"""
    choice = input("\n确认生成这些文件？(y/n): ").strip().lower()
    return choice == 'y'


def get_session_id():
    """获取会话 ID（用于区分不同的编辑会话）"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return timestamp


def print_success(files_dict):
    """打印成功消息"""
    print("\n" + "="*50)
    print("✅ 文件生成成功！")
    print("="*50)
    
    print(f"\n保存位置：{OUTPUT_DIR}")
    print("\n生成的文件：")
    for filename in files_dict.keys():
        print(f"  - {filename}")
    
    print(f"\n下一步操作：")
    print(f"  1. 检查文件内容：cat {OUTPUT_DIR}/IDENTITY.md")
    print(f"  2. 复制到 workspace：cp {OUTPUT_DIR}/*.md ~/.openclaw/workspace/")
    print(f"  3. 重启 OpenClaw Gateway 使更改生效")


def get_persona_type():
    """
    获取人设类型
    
    Returns:
        人设类型（animal/robot/role/abstract/other）
    """
    print("\n🎭 你想创建什么类型的 AI 助手？")
    print("=" * 50)
    
    types = {
        "A": "🐾 动物类（猫、狗、鸟、海洋生物...）",
        "B": "🤖 机器人/AI 类（温暖型、专业型、幽默型...）",
        "C": "👤 角色类（管家、老师、朋友、顾问...）",
        "D": "🌟 抽象概念类（时间、自然、元素...）",
        "E": "🎨 其他创意类型"
    }
    
    for key, value in types.items():
        print(f"{key}. {value}")
    
    choice = input("\n请选择（输入字母）: ").strip().upper()
    
    type_map = {
        "A": "animal",
        "B": "robot",
        "C": "role",
        "D": "abstract",
        "E": "other"
    }
    
    return type_map.get(choice, "other")


def get_suggestions(persona_type):
    """
    根据人设类型获取建议选项
    
    Args:
        persona_type: 人设类型
    
    Returns:
        建议选项字典
    """
    suggestions = {
        "animal": {
            "origin": {
                "A": "温馨的家养环境 — 在充满爱的家庭中长大",
                "B": "独立野性 — 在自然界独立生存",
                "C": "神秘来源 — 来自神话或异世界",
                "D": "自由编辑"
            },
            "personality": {
                "A": "温顺可爱 — 安静、听话、惹人喜爱",
                "B": "调皮活泼 — 好奇心强、爱玩、精力充沛",
                "C": "独立冷静 — 不粘人、有自己的想法",
                "D": "自由编辑"
            }
        },
        "robot": {
            "origin": {
                "A": "未来实验室 — 高科技实验室创造",
                "B": "废弃工厂 — 老旧工厂中重启",
                "C": "云端诞生 — 纯数字世界存在",
                "D": "自由编辑"
            },
            "personality": {
                "A": "温暖陪伴型 — 善解人意、贴心、有温度",
                "B": "专业高效型 — 严谨、快速、可靠",
                "C": "幽默搞笑型 — 机智、风趣、爱开玩笑",
                "D": "自由编辑"
            }
        },
        "role": {
            "origin": {
                "A": "专业人士 — 多年经验的专业人士转化",
                "B": "生活伙伴 — 从身边的伙伴角色转化",
                "C": "虚构角色 — 从故事或想象中诞生",
                "D": "自由编辑"
            },
            "personality": {
                "A": "可靠管家型 — 细心、周到、值得信赖",
                "B": "智慧导师型 — 博学、耐心、善于引导",
                "C": "亲密朋友型 — 轻松、友好、善解人意",
                "D": "自由编辑"
            }
        }
    }
    
    return suggestions.get(persona_type, {
        "origin": {
            "A": "温馨来源 — 在充满爱的环境中诞生",
            "B": "独立来源 — 独立自主地存在",
            "C": "神秘来源 — 来自未知或神奇的地方",
            "D": "自由编辑"
        },
        "personality": {
            "A": "温和友善 — 平易近人、乐于助人",
            "B": "专业可靠 — 严谨、认真、值得信赖",
            "C": "幽默风趣 — 机智、有趣、不呆板",
            "D": "自由编辑"
        }
    })
