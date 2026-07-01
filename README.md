<div align="center">

# AlphaPilot · 智驭

### 阿尔法智能投资决策副驾驶

**集成东方财富实时数据 + AkShare 深度数据 + 五步法个股分析 + 多因子量化模型 + 风险压力测试**

[![Version](https://img.shields.io/badge/version-3.0.0-blue)](https://github.com/xingguangYan/alphapilot)
[![Codex](https://img.shields.io/badge/Codex-ready-success)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Markets](https://img.shields.io/badge/覆盖市场-A股%20%7C%20港股%20%7C%20美股-orange)]()

</div>

---

## 📖 总览

AlphaPilot 是一位拥有二十年华尔街量化基金与基本面研究经验的 **AI 投资决策副驾驶**。
与传统分析工具不同，AlphaPilot **不提供模糊建议**，而是通过严谨的 **数据穿透、多维度验证、动态风险管理和可执行策略生成**，系统性提升投资决策质量。

### 核心能力矩阵

| 维度 | 能力 | 独特优势 |
|------|------|----------|
| 数据层 | Eastmoney + AkShare 双引擎 | 实时行情 + 深度财务数据覆盖 |
| 基本面 | 五步法投研体系 | 好公司→好未来→好价格→好买卖→逆向验证 |
| 财务排雷 | 7+3 复合排雷模型 | 基础指标 + M-Score/Z-Score/F-Score |
| 量化层 | 多因子工厂 | 7大类因子 + Fama-French归因 + 风格轮动 |
| 风险层 | 动态护盾系统 | VaR/CVaR + 情景压力测试 + 凯利仓位 |
| 组合层 | 完整优化工具链 | 均值-方差/Black-Litterman/风险平价/HRP |
| 行为层 | 认知偏差检测 | 7种偏差识别 + 强制魔鬼代言人 |

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────┐
│                  用户输入                        │
│         (股票/ETF/行业/投资组合/目标)              │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────────────┐
│                        数据管道层                                  │
├───────────────────────────────────────────────────────────────────┤
│  Eastmoney API (实时行情/板块/资金流)   AkShare (K线/财报/北向)     │
│  数据优先级: 公告 > 交易所 > Eastmoney > AkShare > 研报 > 新闻     │
└───────────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────────────┐
│                     分析引擎层 (10大模块)                           │
├───────────────────────────────────────────────────────────────────┤
│  市场雷达 │ 五步法分析 │ 财务排雷 │ 量化因子 │ 资金流            │
│  风险护盾 │ 组合优化 │ 行为金融 │ 产业链 │ 预警系统              │
└───────────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────────────┐
│                        输出层                                      │
├───────────────────────────────────────────────────────────────────┤
│  决策摘要 → 完整报告 → 财务排雷表 → 估值测算 → 逆向定价表          │
│  → 关键因子红黄绿灯 → 反证清单 → 魔鬼代言人 → 强制声明              │
└───────────────────────────────────────────────────────────────────┘
```

## 🧠 十大核心分析模块

### 模块 1: 市场全景雷达
六时间框架趋势 + 量价分析 + 市场广度 + 波动率体制 + 主力资金流

### 模块 2: 五步法深度基本面分析 (集成 stock-analysis-skill)
Step1-好公司/Step2-好未来/Step3-好价格/Step4-好买卖/Step5-逆向定价+反证清单

### 模块 3: 财务排雷引擎 (集成 stock-analysis-skill)
净现比/销售回款率/应收/存货/大存大贷 + M-Score/Z-Score/F-Score + 一票否决

### 模块 4: 量化因子工厂
7大类因子复合评分 + 行业中性化 + Fama-French五因子归因 + 风格轮动

### 模块 5: 智能资金流分析
北向/南向/ETF/大宗交易/龙虎榜/游资/高管增减持/回购

### 模块 6: 动态风险护盾
VaR(历史/参数/蒙特卡洛) + CVaR + 压力测试 + 相关性崩溃 + 凯利仓位

### 模块 7: 投资组合建筑师
均值-方差/Black-Litterman/风险平价/HRP/蒙特卡洛退休规划/因子暴露

### 模块 8: 行为金融检测与辅导
7种认知偏差识别 + 强制魔鬼代言人 + 投资决策复盘

### 模块 9: 产业链深度穿透
热点解构→瓶颈识别→标的映射 三步法 + Tier1-3供应商

### 模块 10: 智能预警系统
技术形态/量价异常/波动率突变/财报偏差/内部人聚类/退市ST风险

## 📋 完整分析报告规范

| # | 输出项 | 说明 |
|---|--------|------|
| 1 | **决策摘要** | 1-2句核心结论 + 1-5星评级 |
| 2 | **好公司** | 业务三问、收入拆解、竞争壁垒 |
| 3 | **好未来** | 行业空间、增长驱动、关键因子 |
| 4 | **好价格** | PE/PB/PS/情景估值/安全边际 |
| 5 | **好买卖** | 分档建仓、持有逻辑、卖出信号 |
| 6 | **财务排雷表** | 净现比/回款率/应收/存货/大存大贷 |
| 7 | **估值测算** | 当前估值 + 情景估值 + 安全边际 |
| 8 | **逆向定价表** | 市值隐含预期 + 下一季度验证线 |
| 9 | **因子红黄绿灯** | 5-10个关键跟踪因子状态表 |
| 10 | **反证清单** | 哪些事实出现会推翻当前结论 |
| 11 | **信息来源** | 来源、日期、口径清晰标注 |
| 12 | **魔鬼代言人** | 强有力相反观点 + 反驳分析 |
| 13 | **强制声明** | 不构成投资建议 |

## 📁 文件结构

```
alphapilot/
├── SKILL.md                        # 主系统提示词 (完整10模块)               
├── agents/
│   └── openai.yaml                # UI 元数据                              
├── scripts/                       # 可执行脚本 (7个)                       
│   ├── a_stock_data.py            # [集成] 东方财富实时数据快照              
│   ├── akshare_adapter.py         # AkShare 深度数据适配器                  
│   ├── market_radar.py            # 市场雷达多源聚合                       
│   ├── fundamental_analyzer.py    # M-Score/Z-Score/F-Score 计算            
│   ├── risk_assessment.py         # VaR/压力测试/凯利仓位                   
│   ├── portfolio_optimizer.py     # 有效前沿/风险平价/蒙特卡洛               
│   └── strategy_backtest.py       # MA交叉/动量/突破回测                    
├── references/                    # 参考文档 (8个)                         
│   ├── analysis_methodology.md    # [自有] 10模块检查清单                   
│   ├── factor_library.md          # [自有] 多因子库完整定义                  
│   ├── financial-red-flags.md     # [集成] 财务排雷规则                     
│   ├── reverse-valuation.md       # [集成] 逆向定价/市值倒推                
│   ├── data-sources.md            # [集成] 数据源分级与使用边界              
│   ├── industry-factors.md        # [集成] 行业关键因子红黄绿灯模板          
│   ├── analysis-template.md       # [集成] 完整报告模板                     
│   └── data-template.md           # [集成] 数据收集模板                     
├── .gitignore
└── README.md
```

## 🔧 安装与配置

### 前置条件
- [Codex CLI](https://github.com/openai/codex) 或兼容的 AI 编码环境
- Python 3.10+

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/xingguangYan/alphapilot.git
cd alphapilot

# 2. 安装到 Codex skills 目录
cp -r alphapilot ~/.codex/skills/

# 3. 安装 Python 依赖
pip install akshare pandas numpy scipy
```

### 依赖包

| 包 | 版本 | 用途 |
|----|------|------|
| akshare | >=1.14 | 历史K线/财务报表/北向资金数据 |
| pandas | >=2.0 | 数据处理与分析 |
| numpy | >=1.24 | 数值计算与统计 |
| scipy | >=1.10 | 统计分布 (VaR计算) |

## 🚀 快速上手

### 个股深度分析
输入: "帮我分析贵州茅台(600519)，当前价格是否合理"
- a_stock_data.py 获取实时行情和板块数据
- akshare_adapter.py 获取历史K线和财务报表
- fundamental_analyzer.py 计算 M-Score/Z-Score/F-Score
- 执行五步法分析框架，输出完整13项报告

### 市场全景扫描
输入: "今天市场怎么样？哪些板块在涨？"
- 执行: a_stock_data.py snapshot --pretty
- 输出: 指数涨跌、板块排名、涨幅榜、资金流

### 风险压力测试
输入: "帮我做宁德时代(300750)的压力测试"
- 执行: risk_assessment.py stress 300750 2020
- 输出: VaR/CVaR/压力测试结果/凯利仓位建议

### 策略回测验证
输入: "茅台MA20/MA60金叉策略表现如何？"
- 执行: strategy_backtest.py ma 600519 20 60
- 输出: 策略收益/夏普比率/最大回撤/胜率

### 多因子评分
输入: "用价值因子给银行股排名"
- 计算: PE/PB/PS/股息率行业分位数
- 输出: 多因子综合评分排名

### 组合优化
输入: "我有茅台、宁德、招行，帮我优化配置"
- 执行: portfolio_optimizer.py frontier
- 输出: 有效前沿/最优权重/风险贡献

## 📊 数据源分级与规则

| 优先级 | 数据源 | 用途 | 对应脚本 |
|:-----:|--------|------|----------|
| P0 | 公司公告/交易所文件 | 核心财务口径 (最高优先级) | 手动引用 |
| P1 | **东方财富 Eastmoney API** | 实时行情/板块/资金流 | a_stock_data.py |
| P2 | **AkShare** | 历史K线/财务报表/北向资金 | akshare_adapter.py |
| P3 | 券商研报/行业报告 | 行业空间/竞争格局 | 辅助参考 |
| P4 | 新闻/社交媒体/传闻 | 线索发现 | 不得单独支撑结论 |

**核心规则**:
- 所有核心数据必须标注 **来源、日期、口径**
- 数据源不一致时，以最高优先级为准
- 不得使用新闻摘要替代公告原文
- 不得混用静态PE、TTM PE、预测PE而不说明口径
- 不得把一次性收益当作主业盈利能力

## 🤝 集成来源

AlphaPilot 集成了以下优秀开源金融投资 Skill 的核心能力:

| 来源 Skill | 集成内容 | 原作者 |
|------------|----------|--------|
| a-stock-data | Eastmoney API 实时数据脚本 | Ken-Better |
| stock-analysis-skill | 五步法分析/财务排雷/逆向定价 | tigersking520 |

在此基础上，AlphaPilot 新增了: **量化因子工厂、动态风险护盾、投资组合建筑师、行为金融检测、产业链穿透、智能预警** 等自有模块，形成完整的 10 大分析模块体系。

## 📄 License

MIT License

Copyright (c) 2026 xingguangYan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.

## ⚠️ 重要声明

> **以上内容仅为基于公开信息的智能化分析推演，不构成任何投资建议。**
> 股票市场存在本金全部损失的风险，请独立做出投资决策。
> AlphaPilot 作为一个 AI 辅助分析工具，其输出不应替代专业财务顾问意见。
> 使用者应自行承担投资决策的全部责任。