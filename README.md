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
```

## 2. Quick Start
### 环境自检
运行诊断脚本，确认 PyTorch 及硬件加速状态正常。
```bash
python env_check.py
```
### 运行单步推理
执行核心推理与动作生成测试。
```bash
python test_quart.py
```

## 3. 项目目录结构
```text
QUART-Online-Windows-Reproduction/
├── README.md                  # 项目说明文档
├── requirements.txt           # 核心依赖库列表
├── env_check.py               # 环境与硬件自检脚本
├── test_quart.py              # 核心单步推理与动作生成测试脚本
├── utils.py                   # 核心工具类（包含 RVQ 反量化及输入对齐）
├── ckpts/                     # 模型权重文件夹（权重需按说明自行放置）
├── sample_data/               # 示例数据集
└── gym_eval_scripts/          # 仿真评测与任务加载控制流脚本
```

## 4. 技术方案亮点
**跨平台适配**：针对 Windows 11 环境，绕过了原生强依赖 Linux 的 isaacgym 限制，重点聚焦于模型推理链路与源码剖析。

**显存优化**：借助 accelerate 的 Offload 机制，有效突破大模型（Fuyu-8B 架构）在消费级显卡（如 RTX 4060）上的显存瓶颈。