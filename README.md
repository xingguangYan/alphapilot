# AlphaPilot · 智驭 · 阿尔法智能投资决策副驾驶

## 🚀 突破性创新

AlphaPilot 是一位拥有二十年华尔街量化基金与基本面研究经验的 **AI 投资决策副驾驶**，通过 **十大核心分析模块** 系统性提升投资决策质量。

## 🧠 十大核心分析模块

| # | 模块 | 功能 |
|---|------|------|
| 1 | **市场全景雷达** | 6时间框架趋势 + 量价分析 + 市场广度 + 波动率体制 |
| 2 | **深度基本面引擎** | M-Score/Z-Score/F-Score + 杜邦分解 + FCF收益率 |
| 3 | **量化因子工厂** | 7大因子类复合评分 + Fama-French归因 + 风格轮动 |
| 4 | **智能资金流分析** | 北向资金 + ETF流 + 大宗交易 + 龙虎榜 + 高管增减持 |
| 5 | **动态风险护盾** | VaR/CVaR + 压力测试 + 相关崩溃检测 + 凯利仓位 |
| 6 | **投资组合建筑师** | 均值-方差/Black-Litterman/风险平价/HRP/蒙特卡洛 |
| 7 | **行为金融检测** | 7种认知偏差识别 + 魔鬼代言人强制环节 |
| 8 | **产业链深度穿透** | 热点解构→瓶颈识别→标的映射三步法 |
| 9 | **宏观联动分析** | 美元/汇率/利率/商品敏感性 + PMI周期定位 |
| 10 | **智能预警系统** | 技术形态 + 量价异常 + 财报偏差 + 内部人聚类 |

## 📁 文件结构

`
alphapilot/
├── SKILL.md                          # 主系统提示词（完整10模块架构）
├── agents/openai.yaml                # UI 界面元数据
├── scripts/
│   ├── market_radar.py               # 市场数据聚合（实时/K线/板块/资金/广度）
│   ├── fundamental_analyzer.py       # 基本面评分（M-Score/Z-Score/F-Score/杜邦/FCF）
│   ├── risk_assessment.py            # 风险量化（VaR/压力测试/凯利公式）
│   ├── portfolio_optimizer.py        # 组合优化（有效前沿/风险平价/蒙特卡洛）
│   └── strategy_backtest.py          # 策略回测（MA交叉/动量/突破）
├── references/
│   ├── analysis_methodology.md       # 分析方法论（10模块检查清单）
│   └── factor_library.md             # 多因子库完整参考
├── .gitignore
└── README.md
`

## 🔧 安装

### 本地部署
`ash
# 复制到 Codex skills 目录
cp -r alphapilot ~/.codex/skills/
`

### 数据依赖
`ash
pip install akshare pandas numpy scipy
`

## ⚖️ 重要声明

以上内容仅为基于公开信息的智能化分析推演，不构成任何投资建议。股票市场存在本金全部损失的风险，请独立做出投资决策。

## 📄 License

MIT
