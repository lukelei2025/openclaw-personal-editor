# 贡献指南

感谢你有兴趣贡献 OpenClaw 人设编辑器！

## 🤝 如何贡献

### 报告问题

如果你发现了 bug：
1. 在 [GitHub Issues](https://github.com/yourusername/openclaw-persona-editor/issues) 搜索是否已有相同问题
2. 如果没有，创建新 Issue，包含：
   - 清晰的标题
   - 详细的问题描述
   - 复现步骤
   - 预期行为
   - 实际行为
   - 环境信息（OpenClaw 版本、Python 版本、操作系统）

### 提出新功能

1. 先在 [GitHub Discussions](https://github.com/yourusername/openclaw-persona-editor/discussions) 讨论
2. 创建 Issue 描述你的想法
3. 等待维护者反馈

### 提交代码

1. **Fork 本仓库**
2. **创建特性分支**
   ```bash
   git checkout -b feature/YourAmazingFeature
   ```

3. **编写代码**
   - 遵循现有代码风格
   - 添加注释（如果需要）
   - 更新文档（如果需要）

4. **运行测试**
   ```bash
   python3 scripts/create_persona.py
   # 确保没有错误
   ```

5. **提交更改**
   ```bash
   git add .
   git commit -m "Add some AmazingFeature"
   ```

   提交信息格式：
   - feat: 添加新功能
   - fix: 修复 bug
   - docs: 更新文档
   - style: 代码格式调整
   - refactor: 代码重构
   - test: 添加测试
   - chore: 构建/工具更新

6. **推送到分支**
   ```bash
   git push origin feature/YourAmazingFeature
   ```

7. **开启 Pull Request**
   - 填写 PR 模板
   - 等待代码审查

---

## 📋 代码规范

### Python 代码

- 使用 4 空格缩进
- 函数和类使用 docstring
- 变量命名：snake_case
- 类名：PascalCase
- 常量：UPPER_SNAKE_CASE

### 文档

- Markdown 格式
- 清晰的章节结构
- 提供示例（如果适用）

---

## 🎯 优先事项

我们特别欢迎以下贡献：

### 高优先级
- 🐛 Bug 修复
- ✨ 新的人设类型支持
- 📝 文档改进
- 🌍 国际化支持

### 中优先级
- 🎨 UI 改进（如果有）
- 🔧 工具函数增强
- 📊 示例扩展

### 低优先级
- ♻️ 代码重构
- 🧪 测试覆盖

---

## 📝 PR 模板

提交 PR 时，请包含：

### 描述
简要描述这个 PR 做了什么

### 类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 文档更新
- [ ] 代码重构
- [ ] 其他

### 变更内容
- 列出主要的变更
- 说明为什么需要这些变更

### 测试
- 如何测试这些变更
- 测试环境

### 截图（如果适用）
- 展示新功能的截图

### 检查清单
- [ ] 代码遵循项目规范
- [ ] 已自我审查代码
- [ ] 已添加文档（如果需要）
- [ ] 已更新示例（如果需要）
- [ ] 已测试更改
- [ ] 无新增警告

---

## 🙋 行为准则

- 尊重所有贡献者
- 建设性讨论
- 接受反馈并改进
- 关注最适合的方案，而不是你认为最好的方案

---

## 📧 联系方式

有任何问题？
- 在 [GitHub Discussions](https://github.com/yourusername/openclaw-persona-editor/discussions) 讨论
- 或创建 [GitHub Issue](https://github.com/yourusername/openclaw-persona-editor/issues)

---

**感谢你的贡献！** 🎉
