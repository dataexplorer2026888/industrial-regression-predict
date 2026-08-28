# 🏭 工业级回归预测通用模板

【提供定制服务】机器学习建模、数据清洗、自动化分析报告生成。有需求请邮箱联系，支持全流程定制。

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/sklearn-1.3+-orange.svg)](https://scikit-learn.org/)

> **零数据泄露 · 全自动调参 · 生产级部署 · 一键生成报告**

## ✨ 特性

- 🔒 **零数据泄露**：所有预处理在训练集fit，测试集transform
- 🤖 **7模型自动对比**：Ridge / Lasso / ElasticNet / RF / GBDT / XGBoost / LightGBM
- ⚙️ **RandomizedSearchCV超参搜索**：自动找最优参数
- 📊 **工业级可视化**：残差诊断、特征重要性、模型对比排名
- 📄 **HTML报告生成**：可直接发给客户/导师的精美报告
- 🚀 **生产级API**：`predict()` 支持批量推理 + 特征自动对齐
- 🛡️ **开发模式**：`dev_mode=True` 只看CV，快速调参不碰Test

## 项目效果展示

<p align="center">
  <img src="https://raw.githubusercontent.com/dataexplorer2026888/industrial-regression-predict/main/06_model_comparison.png" width="700">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/dataexplorer2026888/industrial-regression-predict/main/05_feature_importance.png" width="700">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/dataexplorer2026888/industrial-regression-predict/main/04_residual_diagnostics.png" width="700">
</p>

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 一键运行（演示模式）
```bash
python run.py --demo
```

### 使用自己的数据
```bash
python run.py --data ./your_data.csv --target price --output ./output
```

### Python代码调用
```python
from src.pipeline import RegressionPipeline
from src.config import Config
import pandas as pd

cfg = Config(target_col='price', output_dir='./output')
pipeline = RegressionPipeline(cfg)
result = pipeline.run(df)
predictions = pipeline.predict(new_df)
```

## 📁 项目结构

```
├── run.py              # CLI入口
├── config.yaml         # 配置文件
├── src/
│   ├── pipeline.py     # 主流程封装
│   ├── config.py       # 配置中心
│   ├── data_engineering.py  # 数据质量检测+特征工程
│   ├── preprocessing.py     # 零泄露预处理Pipeline
│   ├── modeling.py          # 多模型训练+调参
│   ├── evaluation.py        # 评估与可视化
│   ├── report.py            # HTML报告生成器
│   └── custom_transformers.py
├── examples/
│   ├── california_housing.py
│   └── custom_data.py
└── artifacts/          # 输出产物目录
```

## 📊 输出产物

| 文件 | 说明 |
|------|------|
| `model_artifact.joblib` | 完整Pipeline（可直接部署） |
| `report.html` | 精美分析报告 |
| `06_model_comparison.png` | 模型对比排名图 |
| `04_residual_diagnostics.png` | 残差四合一诊断 |
| `05_feature_importance.png` | 特征重要性 |
| `model_comparison.csv` | 模型指标对比表 |
| `eda_report.json` | 数据质量检测JSON |

## ⚙️ 配置说明

通过 `config.yaml` 或 `Config` 类配置：

```python
cfg = Config(
    target_col='price',           # 目标变量
    target_transform='log1p',     # 目标变换: log1p / none
    cv_folds=5,                   # 交叉验证折数
    n_iter_search=20,             # 超参搜索次数
    dev_mode=False,               # True=只看CV，不评估Test
    models=['XGBoost', 'LightGBM'] # 指定训练模型
)
```

## 🛡️ 数据治理策略

| 问题 | 策略 |
|------|------|
| 缺失值 | SimpleImputer(median) |
| 极端异常 | Winsorizer（训练集分位数截断） |
| 偏度>1 | PowerTransformer(Yeo-Johnson) |
| 目标右偏 | log1p变换 + expm1还原 |
| 高相关特征 | 保留（让模型自动筛选） |
| 低相关特征 | 不删除（Lasso自动处理） |

## 📄 License

MIT License

## 联系作者

- GitHub: [@dataexplorer2026888](https://github.com/dataexplorer2026888)
- 联系邮箱:1057512884@qq.com
- 声明：为了保护客户隐私和商业机密，完整源代码、数据集及核心算法暂不公开。如需定制开发、技术咨询，请通过以邮箱联系我，确认需求后可详谈。感谢理解！

