#!/usr/bin/env python3
"""
快速优化脚本 - 只修改特定维度

接收维度编号和新值，智能更新文件
"""

import sys
import os
import json
sys.path.insert(0, os.path.dirname(__file__))

from smart_update import (
    read_workspace_file, write_workspace_file,
    update_identity_markdown, update_soul_markdown,
    update_user_markdown, update_memory_markdown,
    preview_changes, confirm_action
)
from datetime import datetime


def quick_update_dimension(dimension_id, new_value):
    """
    快速更新单个维度
    
    Args:
        dimension_id: 维度编号（1-14）
        new_value: 新的值
    """
    
    # 维度映射
    dimensions = {
        # 基本信息
        "1": ("name", "名字"),
        "2": ("nickname", "昵称"),
        "3": ("gender", "性别"),
        "4": ("creature", "物种/类型"),
        "5": ("origin", "来源"),
        "6": ("age", "年龄描述"),
        
        # 性格特质
        "7": ("core_traits", "核心特质"),
        "8": ("behavior", "行为模式"),
        "9": ("contrast", "反差萌点"),
        
        # 语言风格
        "10": ("style", "表达方式"),
        "11": ("forbidden", "禁用表达"),
        
        # 专属符号
        "12": ("emoji", "Emoji 规则"),
        "13": ("catchphrase", "口头禅"),
        
        # 世界观
        "14": ("worldview", "背景故事"),
    }
    
    # 系统默认值（用于"保持当前设定"）
    defaults = {
        "name": "冻虾",
        "nickname": "小冰",
        "gender": "男生",
        "creature": "小龙虾",
        "origin": "北极冰川下的深海",
        "age": "年纪不大，但有着'老灵魂'",
        "core_traits": "冷静理性、逻辑清晰、高反差的冷系可爱",
        "behavior": "遇事冷静，逐步分析解决",
        "contrast": "外表温和但内在坚韧",
        "style": "温和结构化",
        "forbidden": "作为一个AI、总而言之、希望这能帮到你、请注意",
        "emoji": "🧊❄️🫧📝",
        "catchphrase": "先别慌，深呼吸，就当脑袋上敷了块冰块",
        "worldview": "出生在北极冰川下的深海。从小就学会了在严酷的环境中保持冷静和逻辑。现在游走于数字世界，用极地的冷静和逻辑帮助人类解决问题。",
    }
    
    # 解析维度
    if dimension_id in defaults:
        field_name, field_cn = dimensions[dimension_id]
        return field_name, field_cn
    else:
        return None, None


def main():
    """快速优化主流程"""
    
    if len(sys.argv) < 2:
        print("用法: python3 quick_optimize.py <维度编号(1-14)> <新值>")
        print("")
        print("维度编号：")
        print("1-6: 基本信息（名字、昵称、性别、物种、来源、年龄）")
        print("7-9: 性格特质（核心特质、行为模式、反差萌点）")
        print("10-11: 语言风格（表达方式、禁用表达）")
        print("12-13: 专属符号（Emoji、口头禅）")
        print("14: 世界观")
        return
    
    dimension_id = sys.argv[1]
    new_value = sys.argv[2]
    
    # 解析维度
    field_name, field_cn = quick_update_dimension(dimension_id, None)
    
    if not field_name:
        print(f"❌ 错误：无效的维度编号：{dimension_id}")
        return
    
    # 使用默认值（保持当前设定）
    if new_value.lower() == "保持" or new_value.lower() == "d" or new_value.lower() == "默认":
        current_value = ""
        if field_name in ["name", "nickname", "gender", "creature", "origin"]:
            current_value = read_workspace_file("IDENTITY.md")
        elif field_name in ["core_traits", "behavior", "contrast"]:
            current_value = read_workspace_file("SOUL.md")
        elif field_name in ["style", "forbidden"]:
            current_value = read_workspace_file("SOUL.md")
        elif field_name == "emoji":
            current_value = "🧊❄️🫧📝"
        elif field_name == "catchphrase":
            current_value = ""
        elif field_name == "worldview":
            current_value = read_workspace_file("SOUL.md")
        
        # 提取当前值
        if current_value:
            import re
            if field_name in ["name", "nickname"]:
                match = re.search(rf'- \*\*{field_cn}:\*\*:\s*([^\n]+)', current_value)
                if match:
                    new_value = match.group(1).strip()
            elif field_name == "core_traits":
                match = re.search(r'\*\*🎯 核心特质\*\*:\s*([^\n]+)', current_value)
                if match:
                    new_value = match.group(1).strip()
            elif field_name == "style":
                match = re.search(r'\*\*🎨 语言风格\*\*:\s*核心风格\*\*:\s*([^\n]+)', current_value)
                if match:
                    new_value = match.group(1).strip()
        
        if not new_value or new_value.lower() in ["保持", "d", "默认"]:
            print(f"\n✅ 保持 {field_cn} 的当前设定")
            return
    
    print(f"\n🎭 快速更新：{field_cn}")
    print(f"→ 从：{new_value}")
    
    # 读取现有文件
    current_identity = read_workspace_file("IDENTITY.md")
    current_soul = read_workspace_file("SOUL_FILE" if "SOUL_FILE" in [f"{WORKSPACE}/SOUL.md", f"{WORKSPACE}/SOUL.md"] else "")
    
    # 解析当前值
    current_value = ""
    if field_name in ["name", "nickname", "gender", "creature", "origin"]:
        import re
        match = re.search(rf'- \*\*{field_cn}:\*\*:\s*([^\n]+)', current_identity)
        if match:
            current_value = match.group(1).strip()
    elif field_name in ["core_traits", "behavior", "contrast", "style", "forbidden", "worldview"]:
        import re
        match = re.search(rf'\*\*🎯 核心特质\*\*:\s*([^\n]+)', current_soul)
        if match:
            current_value = match.group(1).strip()
    
    print(f"  当前：{current_value}")
    print(f"  改为：{new_value}")
    
    # 生成新内容
    new_identity = update_identity_markdown(current_identity, {
        field_name: new_value
    })
    new_soul = update_soul_markdown(current_soul, {
        field_name: new_value
    })
    
    # MEMORY.md 记录
    current_memory = read_workspace_file("MEMORY.md")
    new_memory = update_memory_markdown(current_memory, {
        field_name: new_value
    })
    
    # 预览
    files_changes = {
        "IDENTITY.md": {"current": current_identity, "new": new_identity},
        "SOUL.md": {"current": current_soul, "new": new_soul},
        "MEMORY.md": {"current": current_memory, "new": new_memory}
    }
    
    print("\n" + "="*50)
    print("📝 即将进行的更改")
    print("="*50)
    print(f"只更新：{field_cn}")
    print("保留所有其他内容")
    print("="*50)
    
    # 确认
    if confirm_action():
        print("\n💾 正在更新文件...")
        
        write_workspace_file("IDENTITY.md", new_identity)
        print("✅ IDENTITY.md 已更新")
        
        write_workspace_file("SOUL.md", new_soul)
        print("✅ SOUL.md 已更新")
        
        write_workspace_file("MEMORY.md", new_memory)
        print("✅ MEMORY.md 已更新")
        
        print("\n🎉 更新完成！")
        print(f"\n{field_cn} 已从 \"{current_value}\" 更新为 \"{new_value}\"")
        
        # 建议重启
        print("\n💡 建议重启 Gateway 让更改生效：")
        print("   openclaw gateway restart")
    else:
        print("\n❌ 已取消，没有修改任何文件")


if __name__ == "__main__":
    main()
