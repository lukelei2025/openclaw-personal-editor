#!/usr/bin/env python3
"""
收集单个维度的信息 - 分步交互版本

改进点：
- 每个问题单独显示
- 提供选项后等待确认
- 更清晰的视觉分隔
- 支持自由编辑
"""

import time


def show_header(title):
    """显示标题"""
    print("\n" + "="*60)
    print(f"🎭 {title}")
    print("="*60)
    time.sleep(0.3)


def show_options(options):
    """显示选项"""
    for key, value in options.items():
        print(f"  {key}. {value}")
    print()


def wait_for_continue():
    """等待用户按回车继续"""
    input("\n💡 按回车继续...")


def ask_question_with_pause(question, options=None, allow_custom=True):
    """
    询问单个问题并等待回答
    
    Args:
        question: 问题文本
        options: 选项字典 {"A": "描述", "B": "描述", ...}
        allow_custom: 是否允许自由编辑
    
    Returns:
        用户的选择或自定义内容
    """
    show_header(question)
    
    if options:
        print("可选选项：")
        show_options(options)
        if allow_custom:
            print("  D. 自由编辑")
        wait_for_continue()
    
    while True:
        answer = input("\n你的选择（输入字母或自定义内容）: ").strip()
        
        if not answer:
            print("❌ 不能为空，请重新输入")
            continue
        
        # 如果是选项，返回对应值
        if options and answer.upper() in options:
            selected = options[answer.upper()]
            print(f"\n✅ 已选择：{selected}")
            return selected
        
        # 如果是自由编辑（或没有选项）
        if allow_custom:
            if answer.upper() == 'D' and options:
                print("\n请输入你的想法：")
                custom_input = input("> ").strip()
                if custom_input:
                    return custom_input
            else:
                return answer
        else:
            return answer
        
        # 如果是无效选项
        if options:
            print("❌ 无效选择，请输入 A-D 的字母")
        else:
            return answer


def ask_freeform(question, placeholder=""):
    """
    询问自由形式的问题
    
    Args:
        question: 问题文本
        placeholder: 占位符提示
    
    Returns:
        用户输入的内容
    """
    show_header(question)
    
    if placeholder:
        print(f"提示：{placeholder}")
    
    while True:
        answer = input("\n你的回答: ").strip()
        if answer:
            return answer
        print("❌ 不能为空，请重新输入")


def ask_yes_no(question):
    """
    询问是/否问题
    
    Args:
        question: 问题文本
    
    Returns:
        bool: True(yes)/False(no)
    """
    show_header(question)
    
    while True:
        answer = input("\n你的选择 (y/n): ").strip().lower()
        if answer in ['y', 'yes', '是']:
            return True
        elif answer in ['n', 'no', '否']:
            return False
        else:
            print("❌ 请输入 y 或 n")


def ask_multiline(question):
    """
    询问多行输入
    
    Args:
        question: 问题文本
    
    Returns:
        str: 用户输入的多行内容
    """
    show_header(question)
    print("（输入完成后，在新的一行输入 'END' 结束）")
    
    lines = []
    while True:
        line = input("> ")
        if line.strip() == 'END':
            break
        lines.append(line)
    
    return '\n'.join(lines).strip()


def show_summary(collected_data):
    """
    显示已收集的信息摘要
    
    Args:
        collected_data: 已收集的数据字典
    """
    print("\n" + "="*60)
    print("📋 已收集的信息摘要")
    print("="*60)
    
    for key, value in collected_data.items():
        if value:
            print(f"  • {key}: {value}")
    
    print("="*60)
    print()
