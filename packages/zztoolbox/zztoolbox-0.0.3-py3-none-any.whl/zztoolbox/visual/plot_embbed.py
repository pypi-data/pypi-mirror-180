import numpy as np
import umap
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from zztoolbox.visual.matplot_utils import *

def embbed_data(data, embbed_type='PCA', components = 2, **kwargs):
    if embbed_type == 'PCA':
        pca = PCA(components, **kwargs)
        pca.fit(data.T)
        return pca.components_.T
        
    elif embbed_type == 'TSNE':
        return TSNE(components, **kwargs).fit_transform(data)

    elif embbed_type == 'UMAP':
        return umap.UMAP(**kwargs).fit_transform(data)

def common_setting(fig, ax):
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.yaxis.get_major_ticks()[0].label1.set_visible(False)
    # fig.tight_layout()

def plot_embbed(save_path, data, label=None, x_label = "component 1", y_label = "component 2", figsize=[10.24, 7.68], embbed_type='TSNE', show=False, **kwargs):
    fig, ax = plt.subplots(figsize=figsize)
    common_setting(fig, ax)
    sns.despine(right=True, top=True)

    new_data = embbed_data(data, embbed_type, **kwargs)

    df = pd.DataFrame({x_label:new_data[:,0], y_label:new_data[:,1], 'label':label})

    sns.scatterplot(data=df, x=x_label, y=y_label, hue= 'label' if label is not None else None)

    if show:
        plt.show()
    fig.savefig(save_path)

def scatter2d(save_path, data, label=None, x_label = 'x', y_label = 'y', figsize=[10.24, 7.68], show=False):
    fig, ax = plt.subplots(figsize=figsize)
    common_setting(fig, ax)
    sns.despine(right=True, top=True)

    df = pd.DataFrame({x_label:data[:,0], y_label:data[:,1]})
    sns.scatterplot(x=x_label, y=y_label, data=df, hue= 'label' if label is not None else None, palette = sns.color_palette())

    if show:
        plt.show()
    fig.savefig(save_path)





