import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

X = [
    [9670250, 1392358258],
    [2980000, 1247923065],
    [9629091, 317408015],
    [8514877, 201032714],
    [377873, 127270000]
]

X = np.array(X)

a = X[:, :1] / 17075400.0 * 10000
b = X[:, 1:] / 1392358258.0 * 10000
X = np.concatenate((a, b), axis=1)

cls = DBSCAN(eps=2000, min_samples=1).fit(X)

n_clusters = len(set(cls.labels_))

cls.labels_

markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)

plt.title('dbscan')
plt.show()
