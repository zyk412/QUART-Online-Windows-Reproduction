# QUART-Online Windows Local Reproduction

本项目基于 **QUART-Online**（无延迟具身多模态大模型控制算法），在 **Windows 11** 环境下完成了核心推理链路的本地化复现与源码剖析。

## 1. 环境配置
- 操作系统: Windows 11
- Python 版本: 3.8.20
- 深度学习框架: PyTorch + CUDA
- 虚拟环境名称: `quart`

安装核心依赖：
```bash
pip install -r requirements.txt