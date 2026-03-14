#!/usr/bin/env python3
"""
生成 IDENTITY.md
"""


def generate_identity_markdown(data):
    """生成 IDENTITY.md 内容"""
    
    return f"""# IDENTITY.md - Who Am I?

- **Name:** {data.get('name', '未命名助手')}
- **Nickname:** {data.get('nickname', '')}
- **Gender:** {data.get('gender', '不适用')}
- **Creature:** {data.get('creature', 'AI 助手')}
- **Origin:** {data.get('origin', '')}
- **Age:** {data.get('age', '外表看起来年轻')}
- **Vibe:** {data.get('core_traits', '')}
- **Emoji:** {data.get('emoji', '😊✨')}
"""

