import numpy as np; np.random.seed(42)
import matplotlib.pyplot as plt
import seaborn as sns

def upper_rugplot(data, height=.05, ax=None, **kwargs):
    from matplotlib.collections import LineCollection
    ax = ax or plt.gca()
    kwargs.setdefault("linewidth", 1)
    segs = np.stack((np.c_[data, data],
                     np.c_[np.ones_like(data), np.ones_like(data)-height]),
                    axis=-1)
    lc = LineCollection(segs, transform=ax.get_xaxis_transform(), **kwargs)
    ax.add_collection(lc)

fig, ax = plt.subplots()

data = np.random.normal(0, 0.1, 100)
sns.distplot(data, rug=False, hist=False, ax=ax)

upper_rugplot(data, ax=ax)

plt.show()