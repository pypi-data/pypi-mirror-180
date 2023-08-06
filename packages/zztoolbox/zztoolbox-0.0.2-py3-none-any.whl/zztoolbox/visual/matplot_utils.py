
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
from mpl_toolkits.axisartist.axislines import SubplotZero
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle


SMALL_SIZE = 15
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

# mpl.rcParams["font.family"] = "serif"
mpl.rcParams["font.serif"] = "Times New Roman"
plt.rcParams['patch.linewidth'] = 0
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
# mpl.rcParams['axes.linewidth'] = 1
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


def show_values_on_bars(axs, h_v="v", space=0.4):
    def _show_on_single_plot(ax):
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif h_v == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() # p.get_height()
                value = int(p.get_width())
                ax.text(_x, _y, value, ha="left", va='top')

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)




def common_setting(fig, ax):
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.get_major_ticks()[0].label1.set_visible(False)
    fig.tight_layout()

def plot_hist_simple(save_path, x, num_bins, xlabel, ylabel,figsize=[10.24, 7.68], show = False, show_value = False):
    # sns.set_style("whitegrid", {'grid.linestyle': '--'})
    fig, ax = plt.subplots(figsize=figsize)
    
    # ax.set_axisbelow(True)
    # ax.grid()
    # sns.set_theme()
    
    df = pd.DataFrame({'x': x})
    # sns.set_color_codes('deep')
    sns.histplot(data=df, x="x", bins=num_bins, color=[102/255.,204/255.,1],shrink = 0.9, discrete=True,alpha=1)
    
    
    
    # n, bins, patches = ax.hist(x, num_bins, density=False, rwidth = 0.9, align='left')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    # show_values_on_bars(ax)
    common_setting(fig, ax)
    sns.despine(right=True, top=True)
    if show_value:
        show_values_on_bars(ax,h_v="v",space = 50)
    if show:
        plt.show()
    fig.savefig(save_path)





def plot_bar_simple(save_path, data, xlabel, ylabel,figsize=[10.24, 7.68], angle = 30, show = False, data2 = None):
    names = list(data.keys())
    values = list(data.values())
    if data2 is not None:
        names2 = list(data2.keys())
        values2 = list(data2.values())
    

    fig, ax = plt.subplots(figsize=figsize)
    if data2 is not None:
        
        df2 = pd.DataFrame({ylabel:names2, xlabel:values2}).sort_values(xlabel, ascending=False)
        df = pd.DataFrame({ylabel:names, xlabel:values})
        print(df,df2)
        df = df.loc[df2.index]

        x = df.loc[22:].sort_values(xlabel, ascending=False)

        aa = df.loc[:29].sort_values(xlabel, ascending=False)
        # print(df)
        # print(x)
        # print(aa)
        # cc()
        bb = df2.loc[:29].loc[aa.index]

        df = pd.concat([aa,pd.DataFrame({ylabel:['aaa'], xlabel:[0]}),x])
        df2 = pd.concat([bb,pd.DataFrame({ylabel:['aaa'], xlabel:[0]}),df2.loc[22:]])
        sns.barplot(x=xlabel, y=df[ylabel].values, data=df, palette = sns.color_palette('pastel'))

        sns.barplot(x=xlabel, y=df[ylabel].values, data=df2, palette = sns.color_palette())


    else:
        df = pd.DataFrame({ylabel:names, xlabel:values}).sort_values(xlabel, ascending=False)
        print(df)
        # df = df.drop([27, 12, 8])
        sns.barplot(x=xlabel, y=ylabel, data=df, palette = sns.color_palette())


    show_values_on_bars(ax,h_v="h",space = 50)


    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.invert_yaxis()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # fig.tight_layout()
    if show:
        plt.show()
    fig.savefig(save_path)

def plot_heatmap_simple(save_path, data, xlabel, ylabel, figsize=[20,14], fontsize = 20, show = False):

    mask = np.all(np.isnan(data) | np.equal(data, 0), axis=1)
    data = data[~mask]
    # print(xlabel)
    xlabel_out = []
    for idx, flag in enumerate(mask):
        if ~flag:
            xlabel_out.append(xlabel[idx])


    # print(xlabel_out)

    # cc()
    x = np.arange(data.shape[0])
    y = np.arange(data.shape[1])

    # print(data)
    # cc()
    patches = []
    colors = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # print(np.max(data[i,:]))
            # print(np.sum(data[i,:]))
            width = np.sqrt(data[i][j] / max(np.sum(data[i,:]),1))
            

            rect = Rectangle((x[i] - width/2,y[j] - width/2), width,width)
            patches.append(rect)
            colors.append(width)
        # print(data[i,:]/ max(np.sum(data[i,:]),1))
    # cc()
    fig, ax = plt.subplots(figsize=figsize)
    colors = np.array(colors)
    p = PatchCollection(patches, cmap=plt.get_cmap('OrRd'))
    p.set_array(colors)
    p.set_clim([0, 1])
    ax.add_collection(p)
    ax.set(xlim=(-1./2, data.shape[1] - 1./2), ylim=(-1./2,data.shape[0] - 1./2))
    ax.set_xticks(range(len(xlabel_out)))
    ax.set_xticklabels(xlabel_out, rotation='vertical', fontsize=fontsize)
    ax.set_yticks(range(len(ylabel)))
    ax.set_yticklabels(ylabel, fontsize=fontsize)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_ticks_position('top') 
    ax.yaxis.set_ticks_position('none') 
    # ax.yaxis.set_label_position("right")
    # ax.xaxis.set_label_position('top')
    ax.axis('equal')
    # plt.colorbar(p)

    if show:
        plt.show()
    fig.savefig(save_path)

# plot_heatmap_simple()