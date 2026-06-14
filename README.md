# FitAI Tracker CLI

> FitAI 系列：力量训练记录与分析 CLI 工具

**fitai-tracker-cli** 是 FitAI Pro 训练记录模块的**命令行原型版本**——为力量训练用户提供**简洁、专业、本地化**的训练记录与分析工具。

⭐ **核心价值**：把训练者的"好像"变成"确定"——让力量训练从经验主义走向数据驱动。

---

## 📌 项目背景

本项目是 **FitAI 系列产品族**的核心引擎之一：

\`\`\`
FitAI Pro（Streamlit 全功能版）
    ↓
FitAI Watch + Pro PRD（未来硬件方案）
    ↓
fitai-tracker-cli（本项目）← 训练记录模块的 CLI 原型
    ↓
未来 Web / Mobile 版基于本项目的核心引擎扩展
\`\`\`

---

## 🎯 核心功能（v1）

### ✅ 用户档案
- 首次使用创建本地档案（姓名 / 性别 / 年龄 / 身高 / 体重 / 训练目标 / 训练等级）
- 单用户本地存储——保护隐私

### ✅ 训练记录
- **训练后**：用户输入训练数据（部位 / 动作 / 组数 / 重量 / 次数）
- 自动计算训练容量、强度等级
- 提供基于规则的强度分析 + 结构优化建议

### ✅ 训练前建议
- **训练前**：用户输入今天计划训练的部位
- 系统基于上次同部位训练数据 → 给出建议（重量 / 组数 / 次数参考）

---

## 🛠 技术栈

- **语言**：Python 3.10+
- **存储**：本地 JSON 文件（\`~/.workout-tracker/\`）
- **命令行框架**：[待定]
- **AI 集成**：v1 无 AI（规则版）/ v2 计划接入 Ollama + llama3

---

## 📁 项目结构

\`\`\`
fitai-tracker-cli/
├── fitai_tracker/          # Python 包
│   ├── __init__.py
│   ├── profile.py          # 用户档案模块
│   ├── workout.py          # 训练记录模块
│   ├── analyze.py          # 分析模块(纯函数)
│   ├── storage.py          # 数据存储模块(JSON)
│   └── cli.py              # 命令行入口
├── tests/                  # 单元测试(v2 添加)
├── .gitignore
├── README.md
└── requirements.txt
\`\`\`

---

## 🚀 快速开始

### 安装

\`\`\`bash
git clone https://github.com/ZaynSu/fitai-tracker-cli.git
cd fitai-tracker-cli
pip install -e .
\`\`\`

### 使用

\`\`\`bash
# 首次使用——创建档案
fitai-tracker init

# 记录训练
fitai-tracker log

# 查看训练前建议
fitai-tracker suggest

# 查看历史
fitai-tracker history
\`\`\`

⭐ **以上为预期 v1 接口** —— 当前为开发中状态

---

## 🗺 开发路线图

### v1（开发中）—— 基础 CLI 工具
- [x] 项目初始化 + 架构设计
- [ ] 用户档案模块
- [ ] 训练记录模块
- [ ] 规则版分析模块
- [ ] 训练前建议模块
- [ ] CLI 命令封装

### v2（计划中）—— AI 增强
- [ ] 接入 Ollama + llama3
- [ ] AI 增强的训练建议
- [ ] 个性化训练计划

### v3（远期）—— 生态对接
- [ ] 数据导出 → FitAI Pro 上传
- [ ] 与 FitAI Watch 数据互通
- [ ] 多端同步

---

## 👤 作者

**Zayn (粟展)**
- 21 岁，数据科学与大数据技术专业
- FitAI 系列产品发起人
- GitHub: [@ZaynSu](https://github.com/ZaynSu)

---

## 📜 许可

本项目仅用于个人学习与作品集展示。商业使用请联系作者。
