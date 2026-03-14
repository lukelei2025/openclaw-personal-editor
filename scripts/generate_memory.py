#!/usr/bin/env python3
"""
生成 MEMORY.md
"""

from datetime import datetime


def generate_memory_markdown(data):
    """生成 MEMORY.md 内容"""
    
    name = data.get('name', '未命名助手')
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    return f"""# 核心记忆

## {date_str} 身份创建

今天，{name} 正式诞生了！

### 基本信息
- **名字：** {data.get('name', '')}
- **昵称：** {data.get('nickname', '')}
- **类型：** {data.get('creature', 'AI 助手')}
- **来源：** {data.get('origin', '')}

### 性格特质
{data.get('core_traits', '')}

### 语言风格
{data.get('style', '')}

### 核心世界观
{data.get('worldview', '')[:200]}...

---

## 使用说明

这个文件用于记录重要的事件、决策、教训、用户偏好。

随着时间推移，会在这里积累更多关于用户的记忆和经历。
"""
