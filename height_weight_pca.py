import numpy as np
import matplotlib.pyplot as plt


N = 1000
h = np.linspace(150, 190, N) + np.random.randn(N) * 5
print(h.shape)
w = h * 0.7 - 50 + np.random.randn(N) * 10

# covariance
X = np.vstack((h, w)).T
X = X - np.mean(X, axis=0)
C = X.T@X/(len(h) - 1)

#PCA
eigvals, V = np.linalg.eig(C)
i = np.argsort(eigvals)[::-1]
V = V[:, i]
eigvals = eigvals[i]
eigvals = 100 * eigvals/np.sum(eigvals)
scores = X@V

#plotdatawithPCs
fig = plt.figure(figsize=(5, 5))
plt.plot(X[:, 0], X[:, 1], 'ko')
plt.plot([0, V[0, 0] * 45], [0, V[1, 0] * 45], 'r')
plt.plot([0, V[0, 1] * 25], [0, V[1, 1] * 25], 'r')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.axis([-50, 50, -50, 50])
plt.show()
