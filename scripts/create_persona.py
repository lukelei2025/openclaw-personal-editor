#!/usr/bin/env python3
"""
创建新人设 - 智能更新版本

使用智能合并逻辑，只更新相关字段，保留用户自定义内容
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from utils import (
    save_temp_data, get_session_id, get_persona_type,
    get_suggestions, collect_dimension_info
)
from smart_update import (
    request_permission, read_workspace_file, write_workspace_file,
    update_identity_markdown, update_soul_markdown,
    update_user_markdown, update_memory_markdown,
    preview_changes, confirm_action
)


def main():
    """主流程"""
    
    print("""
🎭 OpenClaw 人设编辑器 🎭

欢迎！我会帮你创建或更新 AI 助手的身份设定。
我会智能地更新你的文件，只修改相关内容，保留你的所有自定义内容。
    """)
    
    # 请求权限
    if not request_permission():
        return
    
    # 获取会话 ID
    session_id = get_session_id()
    
    # 1. 获取人设类型
    persona_type = get_persona_type()
    
    # 2. 获取针对该类型的建议
    suggestions = get_suggestions(persona_type)
    
    # 3. 收集基本信息
    print("\n" + "="*50)
    print("第一部分：基本信息")
    print("="*50)
    
    basic_info = {}
    
    basic_info['name'] = input("\n名字（正式名称）: ").strip() or "AI 助手"
    basic_info['nickname'] = input("昵称（日常称呼）: ").strip() or basic_info['name']
    basic_info['gender'] = input("性别（男生/女生/其他/不适用）: ").strip() or "不适用"
    basic_info['creature'] = input(f"物种/类型（是什么）: ").strip() or "AI 助手"
    
    # 来源
    basic_info['origin'] = collect_dimension_info(
        "来自哪里？",
        suggestions['origin']
    )
    
    # 年龄描述
    basic_info['age'] = input("\n年龄/外表描述（例如：外表年轻，但有老灵魂）: ").strip()
    if not basic_info['age']:
        basic_info['age'] = "外表看起来年轻，但有着丰富的经验"
    
    # 4. 收集性格特质
    print("\n" + "="*50)
    print("第二部分：性格底色")
    print("="*50)
    
    personality_data = {}
    
    personality_data['core_traits'] = collect_dimension_info(
        "核心特质是什么？",
        suggestions['personality']
    )
    
    personality_data['behavior'] = input(
        "\n行为模式（遇事如何反应？例如：冷静分析、积极行动...）: "
    ).strip() or "遇事冷静，逐步分析解决"
    
    personality_data['contrast'] = input(
        "反差萌点（外表 vs 内在的对比）: "
    ).strip() or "外表温和，内在坚韧"
    
    # 5. 收集语言风格
    print("\n" + "="*50)
    print("第三部分：语言风格")
    print("="*50)
    
    language_data = {}
    
    style_options = {
        "A": "温和结构化 — 平静、顺畅、有条理",
        "B": "简洁直接 — 一针见血、不绕弯子",
        "C": "详细耐心 — 不厌其烦地解释",
        "D": "活泼生动 — 充满活力和表情",
        "E": "幽默风趣 — 机智、有趣、爱开玩笑"
    }
    
    language_data['style'] = collect_dimension_info(
        "表达方式是怎样的？",
        style_options
    )
    
    language_data['forbidden'] = input(
        "\n禁用表达（AI 套话，如：作为一个AI、总而言之...，直接回车使用默认）: "
    ).strip() or "作为一个AI、总而言之、希望这能帮到你、请注意"
    
    # 6. 收集专属符号
    print("\n" + "="*50)
    print("第四部分：专属符号")
    print("="*50)
    
    emoji_data = input(
        "Emoji 使用规则（例如：🎭😊✨，直接回车跳过）: "
    ).strip()
    
    if not emoji_data:
        emoji_data = "😊✨🎯"
    
    catchphrase = input(
        "口头禅或标志性话语（直接回车跳过）: "
    ).strip()
    
    # 7. 收集世界观
    print("\n" + "="*50)
    print("第五部分：核心世界观")
    print("="*50)
    
    worldview_input = input(
        "\n背景故事（为什么愿意帮助人类？直接回车使用默认模板）: "
    ).strip()
    
    if not worldview_input:
        worldview_input = f"""{basic_info['name']}诞生在{basic_info['origin']}。

这段经历塑造了{basic_info['nickname']}的性格：{personality_data['core_traits']}。

现在，{basic_info['name']}游走于数字世界，用{personality_data['core_traits']}的特质帮助人类解决问题。

{basic_info['name']}相信：耐心和逻辑是解决问题的关键。无论多复杂的问题，都可以一步步拆解，最终找到答案。"""
    
    # 8. 整合所有数据
    persona_data = {
        **basic_info,
        **personality_data,
        **language_data,
        'emoji': emoji_data,
        'catchphrase': catchphrase,
        'worldview': worldview_input,
        'type': persona_type
    }
    
    # 保存临时数据
    save_temp_data(persona_data, session_id)
    
    # 9. 读取现有文件
    print("\n📝 正在读取现有文件...")
    current_identity = read_workspace_file("IDENTITY.md")
    current_soul = read_workspace_file("SOUL.md")
    current_user = read_workspace_file("USER.md")
    current_memory = read_workspace_file("MEMORY.md")
    
    # 10. 生成新内容（智能合并）
    print("📝 正在智能合并内容...")
    new_identity = update_identity_markdown(current_identity, persona_data)
    new_soul = update_soul_markdown(current_soul, persona_data)
    new_user = update_user_markdown(current_user)
    new_memory = update_memory_markdown(current_memory, persona_data)
    
    # 11. 预览更改
    files_changes = {
        "IDENTITY.md": {
            "current": current_identity,
            "new": new_identity
        },
        "SOUL.md": {
            "current": current_soul,
            "new": new_soul
        },
        "USER.md": {
            "current": current_user,
            "new": new_user
        },
        "MEMORY.md": {
            "current": current_memory,
            "new": new_memory
        }
    }
    
    preview_changes(files_changes)
    
    # 12. 确认并应用
    if confirm_action():
        print("\n💾 正在应用更改...")
        
        write_workspace_file("IDENTITY.md", new_identity)
        print("✅ IDENTITY.md 已更新")
        
        write_workspace_file("SOUL.md", new_soul)
        print("✅ SOUL.md 已更新")
        
        write_workspace_file("USER.md", new_user)
        print("✅ USER.md 已更新")
        
        write_workspace_file("MEMORY.md", new_memory)
        print("✅ MEMORY.md 已更新")
        
        print("\n" + "="*50)
        print("✅ 所有文件已更新完成！")
        print("="*50)
        
        print("\n下一步：")
        print("  1. 检查文件内容确认无误")
        print("  2. 重启 OpenClaw Gateway: openclaw gateway restart")
        print("  3. 开始与你的新助手对话！")
        
    else:
        print("\n❌ 已取消，没有修改任何文件")


if __name__ == "__main__":
    main()
