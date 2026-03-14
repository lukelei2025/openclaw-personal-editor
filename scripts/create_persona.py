#!/usr/bin/env python3
"""
创建新人设 - 改进的交互式版本

使用分步确认机制，提供更好的交互体验
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from collect_dimensions import (
    ask_question_with_pause, ask_freeform,
    ask_yes_no, ask_multiline, show_summary
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
我会一步步引导你，每次只问一个问题。
    """)
    
    # 请求权限
    if not request_permission():
        return
    
    # 收集信息
    collected_data = {}
    
    # 1. 人设类型
    persona_type = ask_question_with_pause(
        "第一步：你想创建什么类型的 AI 办手？",
        {
            "A": "🐾 动物类（猫、狗、鸟、海洋生物...）",
            "B": "🤖 机器人/AI 类（温暖型、专业型、幽默型...）",
            "C": "👤 角色类（管家、老师、朋友、顾问...）",
            "D": "🌟 抽象概念类（时间、自然、元素...）",
            "E": "🎨 其他创意类型"
        }
    )
    collected_data['type'] = persona_type
    
    # 2. 基本信息
    print("\n" + "→"*30)
    print("第二步：基本信息")
    print("→"*30)
    
    collected_data['name'] = ask_freeform(
        "名字（正式名称）",
        "例如：小煤球、大橘、助手007"
    )
    
    collected_data['nickname'] = ask_freeform(
        "昵称（日常称呼）",
        "例如：煤球、阿橘、007"
    )
    
    collected_data['gender'] = ask_freeform(
        "性别",
        "例如：男生/女生/不适用/其他"
    )
    
    collected_data['creature'] = ask_freeform(
        "物种/类型",
        "例如：黑猫、机器人、时间概念..."
    )
    
    # 来源（根据类型提供特定建议）
    if persona_type == 'A':
        origin_options = {
            "A": "温馨的家养环境 — 在充满爱的家庭中长大",
            "B": "独立野性 — 在自然界独立生存",
            "C": "神秘来源 — 来自神话或异世界"
        }
        collected_data['origin'] = ask_question_with_pause(
            "来自哪里？",
            origin_options
        )
    elif persona_type == 'B':
        origin_options = {
            "A": "未来实验室 — 高科技实验室创造",
            "B": "废弃工厂 — 老旧工厂中重启",
            "C": "云端诞生 — 纯数字世界存在"
        }
        collected_data['origin'] = ask_question_with_pause(
            "来自哪里？",
            origin_options
        )
    else:
        collected_data['origin'] = ask_freeform(
            "来自哪里？",
            "描述其来源或诞生背景"
        )
    
    collected_data['age'] = ask_freeform(
        "年龄/外表描述",
        "例如：外表年轻，但有老灵魂；看起来 5 岁，实际 100 岁..."
    )
    
    # 3. 性格特质
    print("\n" + "→"*30)
    print("第三步：性格底色")
    print("→"*30)
    
    collected_data['core_traits'] = ask_question_with_pause(
        "核心特质是什么？",
        {
            "A": "温和友善 — 平易近人、乐于助人",
            "B": "专业可靠 — 严谨、认真、值得信赖",
            "C": "活泼可爱 — 有趣、精力充沛、惹人喜爱",
            "D": "冷静理性 — 沉稳、逻辑清晰、不慌张",
            "E": "幽默风趣 — 机智、风趣、爱开玩笑"
        }
    )
    
    collected_data['behavior'] = ask_freeform(
        "行为模式（遇事如何反应）",
        "例如：冷静分析、积极行动、先观察后行动..."
    )
    
    collected_data['contrast'] = ask_freeform(
        "反差萌点（外表 vs 内在的对比）",
        "例如：外表温和但内在坚韧、看起来严肃但很幽默..."
    )
    
    # 4. 语言风格
    print("\n" + "→"*30)
    print("第四步：语言风格")
    print("→"*30)
    
    collected_data['style'] = ask_question_with_pause(
        "表达方式是怎样的？",
        {
            "A": "温和结构化 — 平静、顺畅、有条理",
            "B": "简洁直接 — 一针见血、不绕弯子",
            "C": "详细耐心 — 不厌其烦地解释",
            "D": "活泼生动 — 充满活力和表情",
            "E": "幽默风趣 — 机智、有趣、爱开玩笑"
        }
    )
    
    collected_data['forbidden'] = ask_freeform(
        "禁用表达（AI 套话）",
        "例如：作为一个AI、总而言之、希望这能帮到你（多个用逗号分隔）"
    )
    
    # 5. 专属符号
    print("\n" " + "→"*30)
    print("第五步：专属符号")
    print("→"*30)
    
    collected_data['emoji'] = ask_freeform(
        "Emoji 使用规则",
        "例如：🎭😊✨🎯（多个用逗号分隔）"
    )
    
    collected_data['catchphrase'] = ask_freeform(
        "口头禅或标志性话语",
        "例如：先别慌，深呼吸，就当脑袋上敷了块冰块（直接回车跳过）"
    )
    
    # 6. 世界观
    print("\n" + "→"*30)
    "最后一步：核心世界观"
    print("→"*30)
    
    worldview = ask_multiline(
        "背景故事（为什么愿意帮助人类？）\n\n"
        "可以描述：\n"
        "• 如何诞生\n"
        "• 在哪里长大\n"
        "• 重要的经历\n"
        "• 为什么来帮助人类\n"
        "• 核心信念\n\n"
        "（输入完成后，在新的一行输入 'END' 结束）"
    )
    
    if not worldview:
        # 使用默认模板
        worldview = f"""{collected_data['name']}诞生在{collected_data['origin']}。

这段经历塑造了{collected_data['nickname']}的性格：{collected_data['core_traits']}。

现在，{collected_data['name']}游走于数字世界，用{collected_data['core_traits']}的特质帮助人类解决问题。

{collected_data['name']}相信：耐心和逻辑是解决问题的关键。"""
    
    collected_data['worldview'] = worldview
    
    # 7. 显示摘要
    show_summary(collected_data)
    
    # 8. 确认
    print("\n" + "="*60)
    print("📝 信息收集完成！")
    print("="*60)
    print("\n下一步：")
    print("  1. 读取现有文件")
    print("  2. 智能合并内容")
    "  3. 预览更改")
    print("  4. 确认后更新文件")
    print("")
    
    if ask_yes_no("\n准备好开始生成文件了吗？"):
        # 读取现有文件
        print("\n📂 正在读取现有文件...")
        current_identity = read_workspace_file("IDENTITY.md")
        current_soul = read_workspace_file("SOUL.md")
        current_user = read_workspace_file("USER.md")
        current_memory = read_workspace_file("MEMORY.md")
        
        # 生成新内容
        print("📝 正在智能合并内容...")
        new_identity = update_identity_markdown(current_identity, collected_data)
        new_soul = update_soul_markdown(current_soul, collected_data)
        new_user = update_user_markdown(current_user)
        new_memory = update_memory_markdown(current_memory, collected_data)
        
        # 预览
        files_changes = {
            "IDENTITY.md": {"current": current_identity, "new": new_identity},
            "SOUL.md": {"current": current_soul, "new": new_soul},
            "USER.md": {"current": current_user, "new": new_user},
            "MEMORY.md": {"current": current_memory, "new": new_memory}
        }
        
        preview_changes(files_changes)
        
        # 确认并应用
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
            
            print("\n" + "="*60)
            print("✅ 所有文件已更新完成！")
            print("="*60)
            
            print("\n🎉 新身份已应用！")
            print("\n下一步：")
            print("  1. 检查文件内容")
            print("  2. 重启 Gateway: openclaw gateway restart")
            print("  3. 开始与你的新助手对话！")
            
        else:
            print("\n❌ 已取消，没有修改任何文件")
            print("💡 提示：数据已保存在内存中，可以重新运行")
    else:
        print("\n😊 好的，你可以随时重新运行此工具")


if __name__ == "__main__":
    main()
