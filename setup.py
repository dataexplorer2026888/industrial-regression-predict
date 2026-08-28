from setuptools import setup, find_packages

setup(
    name="industrial-regression-template",
    version="1.0.0",
    author="dataexplorer2026888",
    description="工业级回归预测通用模板",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.12.0",
        "joblib>=1.2.0",
        "pyyaml>=6.0",
        "xgboost>=1.7.0",
        "lightgbm>=4.0.0",
        "scipy>=1.9.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
