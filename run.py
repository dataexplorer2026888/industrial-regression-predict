#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
工业级回归预测Pipeline —— 一键运行入口

用法:
    python run.py --data data.csv --target price --config config.yaml
    python run.py --demo  # 使用California Housing数据集演示
"""
import argparse
import os
import sys

# 添加src到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from src.pipeline import RegressionPipeline
from src.config import Config


def parse_args():
    parser = argparse.ArgumentParser(
        description='工业级回归预测Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 使用California Housing数据集运行演示
  python run.py --demo

  # 使用自己的CSV文件
  python run.py --data ./my_data.csv --target price

  # 使用配置文件
  python run.py --data ./my_data.csv --config ./config.yaml

  # 开发模式（只看CV，不评估Test）
  python run.py --data ./my_data.csv --target price --dev
        """
    )
    parser.add_argument('--data', type=str, help='输入CSV文件路径')
    parser.add_argument('--target', type=str, default='target', help='目标列名')
    parser.add_argument('--config', type=str, help='配置文件路径（YAML）')
    parser.add_argument('--output', type=str, default='./artifacts', help='输出目录')
    parser.add_argument('--demo', action='store_true', help='使用California Housing数据集演示')
    parser.add_argument('--dev', action='store_true', help='开发模式（跳过Test评估）')
    parser.add_argument('--models', type=str, nargs='+', 
                       default=['Ridge', 'Lasso', 'ElasticNet', 'RandomForest', 
                               'GradientBoosting', 'XGBoost', 'LightGBM'],
                       help='要训练的模型列表')

    return parser.parse_args()


def main():
    args = parse_args()

    # 加载配置
    if args.config and os.path.exists(args.config):
        cfg = Config.from_yaml(args.config)
        print(f'✅ 从 {args.config} 加载配置')
    else:
        cfg = Config(
            target_col=args.target,
            output_dir=args.output,
            dev_mode=args.dev,
            models=args.models
        )
        print('✅ 使用默认配置')

    # 加载数据
    if args.demo:
        print('🎯 演示模式：加载California Housing数据集')
        from sklearn.datasets import fetch_california_housing
        housing = fetch_california_housing()
        df = pd.DataFrame(housing.data, columns=housing.feature_names)
        df['MedHouseVal'] = housing.target
        cfg.target_col = 'MedHouseVal'
        # 设置该数据集的winsorize参数
        cfg.winsorize_limits = {
            'AveRooms': 0.995,
            'AveBedrms': 0.995,
            'AveOccup': 0.995,
            'Population': 0.99
        }
    elif args.data:
        if not os.path.exists(args.data):
            print(f'❌ 数据文件不存在: {args.data}')
            sys.exit(1)
        df = pd.read_csv(args.data)
        print(f'✅ 加载数据: {args.data} ({df.shape[0]}行 × {df.shape[1]}列)')
    else:
        print('❌ 请提供 --data 或 --demo')
        sys.exit(1)

    # 运行Pipeline
    pipeline = RegressionPipeline(cfg)
    result = pipeline.run(df)

    print('\n' + '='*70)
    print('✨ 执行完成！')
    print(f'   最优模型: {result["best_model_name"]}')
    if result.get('metrics'):
        print(f'   R² Score: {result["metrics"]["R2"]:.4f}')
    print(f'   产物目录: {result["output_dir"]}')
    print('='*70)


if __name__ == '__main__':
    main()
