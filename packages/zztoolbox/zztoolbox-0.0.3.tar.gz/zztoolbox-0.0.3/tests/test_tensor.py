import torch
import numpy as np
import seaborn as sns
from tensor import concat, unsqueeze, plot_feature
def test_concat():
    tensor = torch.ones(100,100)
    assert concat([tensor,tensor]).shape == (200,100)

    array = np.ones((100,100))
    assert concat([array,array]).shape == (200,100)

def test_unsqueeze():
    tensor = torch.ones(100,100)
    assert unsqueeze(tensor).shape == (1,100,100)

    array = np.ones((100,100))
    assert unsqueeze(array).shape == (1,100,100)

def test_plot():

    x = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    label = np.expand_dims(np.array([0,1,0,1]),1)

    plot_feature('test.png', x, label,embbed_type='PCA')