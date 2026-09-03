import sys
import importlib.util

def check_package(package_name):
    """检查指定第三方库是否已安装"""
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def main():
    print("=" * 60)
    print("  QUART-Online Windows Local Environment Diagnostic Tool")
    print("=" * 60)
    
    # 1. 基础 Python 信息
    print(f"[1] Python 版本: {sys.version.split()[0]}")
    print(f"    Python 路径: {sys.executable}")
    
    # 2. PyTorch 与 CUDA 硬件环境检测
    try:
        import torch
        print(f"[2] PyTorch 版本: {torch.__version__}")
        
        cuda_available = torch.cuda.is_available()
        print(f"    CUDA 可用性: {'【正常】 (True)' if cuda_available else '【警告】 (False - 仅能使用 CPU)'}")
        
        if cuda_available:
            print(f"    CUDA 版本: {torch.version.cuda}")
            print(f"    当前显卡型号: {torch.cuda.get_device_name(0)}")
            print(f"    显存总量: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")
    except ImportError:
        print("[2] PyTorch: 【未安装】 (请先安装 PyTorch)")

    # 3. 核心依赖库检测
    print("\n[3] 核心依赖库检查:")
    dependencies = [
        "transformers", 
        "accelerate", 
        "numpy", 
        "safetensors", 
        "tqdm", 
        "isaacgym"
    ]
    
    for pkg in dependencies:
        is_installed = check_package(pkg)
        if is_installed:
            try:
                mod = importlib.import_module(pkg)
                version = getattr(mod, "__version__", "未知版本")
                print(f"    - {pkg}: 【已安装】 (版本: {version})")
            except Exception:
                print(f"    - {pkg}: 【已安装】")
        else:
            if pkg == "isaacgym":
                print(f"    - {pkg}: 【未安装/Windows下缺失】 (提示：该仿真引擎通常需 Linux 环境，本地推理可忽略)")
            else:
                print(f"    - {pkg}: 【未安装】 (建议通过 pip 安装)")

    print("=" * 60)
    print("环境检测完成！如果 PyTorch 和 transformers 状态正常，即可开始运行测试。")
    print("=" * 60)

if __name__ == "__main__":
    main()