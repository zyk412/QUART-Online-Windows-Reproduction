# QUART-Online Model Checkpoints Directory

This directory is designated for storing pre-trained model weights, fine-tuned checkpoints, and related neural network parameters required for the QUART-Online project.

## Important Note on File Sizes
Due to GitHub and general storage constraints, large pre-trained checkpoint files (such as Fuyu-8B weights, Action Encoders, and RVQ models) are **NOT** included directly in this repository.

## Instructions for Setup
1. **Download Checkpoints**: Obtain the official pre-trained checkpoint package provided by the QUART-Online project maintainers.
2. **Directory Placement**: Extract and place the weight files/folders directly into this `ckpts/` directory. 
3. **Verification**: Ensure the paths match those expected by the inference and evaluation scripts (e.g., `test_quart.py`).

## Expected Directory Structure Example
ckpts/
├── README.txt
└── quart_online/
    ├── config.json
    ├── model.safetensors.index.json
    └── ...