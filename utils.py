import os
import torch
import random
import numpy as np
import yaml


def mkdirss(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def set_seed(seed=0):
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

@torch.no_grad()
def save(model_type, task, name, model):
    model.eval()
    model = model.cpu()
    trainable = {}
    for n, p in model.named_parameters():
        if 'sct_mlp' in n or 'sct_mlp' in n or 'head' in n or 'q_l' in n or 'k_l' in n or 'v_l' in n:
            trainable[n] = p.data

    torch.save(trainable, './output/%s/%s/%s/ckpt_epoch_best.pt'%(model_type, task, name))
    

def load(model_type, task, name, model):
    model = model.cpu()
    st = torch.load('./output/%s/%s/%s/ckpt_epoch_best.pt'%(model_type, task, name))
    model.load_state_dict(st, False)
    return model

def get_config(model_type, task, dataset_name):
    with open('./configs/%s/%s/%s.yaml'%(model_type, task, dataset_name), 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
