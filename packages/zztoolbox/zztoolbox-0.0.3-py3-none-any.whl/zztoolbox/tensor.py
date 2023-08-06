import torch
import numpy as np
from zztoolbox.visual.plot_embbed import plot_embbed

def concat(x, axis = 0):

    if type(x[0]) is np.ndarray:
        return np.concatenate(x, axis)

    elif torch.is_tensor(x[0]):
        return torch.cat(x, axis)

def unsqueeze(x, axis = 0):

    if type(x) is np.ndarray:
        return np.expand_dims(x, axis)

    elif torch.is_tensor(x):
        return torch.unsqueeze(x, axis)

def plot_feature(save_path, data, label = None, embbed_type='PCA', **kwargs):
    plot_embbed(save_path, data, label=label, embbed_type=embbed_type, **kwargs)
