import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = []
f = open('city.txt', encoding='utf-8')
for v in f:
    x.append([float(v.split(',')[1]), float(v.split(',')[2])])

X = np.array(x)
n_clusters = 5

cls = KMeans(n_clusters).fit(X)

markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)

plt.title('')
plt.show()
