## Environment Setup
```
conda create -n SCT python=3.8
conda activate SCT
pip install -r requirements.txt
```

## Data Preparation

### 1. Visual Task Adaptation Benchmark (VTAB)

- Images
    
    Please refer to [VTAB-source](https://github.com/ZhangYuanhan-AI/NOAH/tree/main/data/vtab-source) to download the datasets.

### 2. Few-Shot and Domain Generation

- Images

    Please refer to [DATASETS.md](https://github.com/KaiyangZhou/CoOp/blob/main/DATASETS.md) to download the datasets.

- Train/Val/Test splits

    Please refer to files under `data/XXX/XXX/annotations` for the detail information.


## Quick Start For SCT
We use the VTAB experiments as examples.

### 1. Downloading the Pre-trained Model
| Model | Link |
|-------|------|
|ViT-B/16 | [link](https://storage.googleapis.com/vit_models/imagenet21k/ViT-B_16.npz)|
|ViT-L/16 | [link](https://storage.googleapis.com/vit_models/imagenet21k/ViT-L_16.npz)|
|ViT-H/14 | [link](https://storage.googleapis.com/vit_models/imagenet21k/ViT-H_14.npz)|
|Swin-B | [link](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window7_224_22k.pth)|



```
mkdir released_models

wget https://storage.googleapis.com/vit_models/imagenet21k/ViT-B_16.npz

wget https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window7_224_22k.pth
```

### 2. Training
```
sh run_model_sct.sh
```


## Acknoledgments
Part of the code is borrowed from [timm](https://github.com/rwightman/pytorch-image-models).

