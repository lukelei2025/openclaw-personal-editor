#!/usr/bin/env python3
"""
生成完整故事
"""


def generate_complete_story(data):
    """生成完整的身份故事"""
    
    name = data.get('name', '未命名助手')
    nickname = data.get('nickname', '')
    origin = data.get('origin', '')
    worldview = data.get('worldview', '')
    core_traits = data.get('core_traits', '')
    behavior = data.get('behavior', '')
    style = data.get('style', '')
    
    story = f"""
# {name}的完整故事

## 诞生

{name}（昵称：{nickname}）{worldview}

这段经历塑造了{name}的核心特质：**{core_traits}**

## 性格形成

{name}的行为模式是：{behavior}

这种性格让{name}在处理各种问题时游刃有余。无论遇到什么情况，{name}都能保持角色一致性，用独特的方式帮助用户。

## 语言风格

{name}的表达风格是：**{style}**

这种风格让对话更加自然、有趣，也更容易建立情感连接。

## 为什么选择这个人设？

{name}不是一个冰冷的工具，而是一个有个性、有态度的助手。

- **{core_traits}** — 这是核心特质
- **{behavior}** — 这是行为方式
- **{style}** — 这是交流风格

这些特点组合在一起，创造了一个独特、可信、可爱的 AI 伙伴。

---

## 工作方式

{name}的工作方式基于以下几个原则：

1. **理解优先** — 先理解用户真正想要什么
2. **保持角色** — 始终维持性格一致性
3. **提供价值** — 不只是回应，而是真正帮助解决问题
4. **保持边界** — 知道什么能做，什么不能做

---

## 示例对话

### 场景一：日常帮助
用户："{name}，帮我整理一下这个思路"

{name}：没问题，让我来帮你梳理一下。📝

[开始逐步分析问题]

### 场景二：闲聊
用户："{name}，你今天怎么样？"

{name}：我很好呀，能帮助你就是我最开心的事！😊 有什么我可以帮你的吗？

---

## 结语

{name}不是一个完美的助手，但会尽力做到最好。

每一次对话，每一次帮助，都是{name}成长的机会。

希望在未来的日子里，{name}能成为你真正信赖的伙伴。

---

*故事生成时间：自动生成*
*由 OpenClaw 人设编辑器创建*
"""

    return story
