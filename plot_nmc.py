"""
=============================================
NMC
=============================================

Plot an NMC classifier. Data is generated from two Gaussians with different centers and covariance matrices.
"""

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt


class NMC:
    
    def fit(self, X_train, Y_train):
        self.labels = sorted(list(set(Y_train)))
        self.nr_classes = len(self.labels)
        self.mu = [None] * self.nr_classes
        for i in range(self.nr_classes):
            idx = [j for j in range(len(Y_train)) if Y_train[j] == self.labels[i]]
            self.mu[i] = X_train[idx,:].mean(axis=0)
  

    def predict(self, X_test):
        n,d = X_test.shape 
        scores = np.zeros((n,1))
        for i in range(n):
            x = X_test[i,:]
            min_d = 1e6
            pred = 0
            for k in range(self.nr_classes):
                d = sum([ (v1-v2)**2 for v1,v2 in zip(x,self.mu[k])])
                if d < min_d:
                    min_d = d
                    pred = self.labels[k]
            scores[i] = pred        
        return scores


n_samples = 500

# generate random sample, two components
np.random.seed(0)

# generate spherical data centered on (20, 20)
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])



# generate zero centered stretched Gaussian data
C = np.array([[0., -0.7], [3.5, .7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# concatenate the two datasets into the final training set
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
Y_train = [1] * len(shifted_gaussian) + [-1] * len(stretched_gaussian)
clf = NMC()
clf.fit(X_train, Y_train)



# display predicted scores by the model as a contour plot
num = 500
x0 = np.linspace(-20.0, 30.0, num)
x1 = np.linspace(-20.0, 40.0, num)

X0, X1 = np.meshgrid(x0, x1)
XX = np.array([X0.ravel(), X1.ravel()]).T

Z = clf.predict(XX)
Z = Z.reshape(X0.shape)
#CS = plt.contour(X, Y, Z)
plt.contourf(X0, X1, Z, cmap=plt.cm.Paired, alpha=0.8)

plt.scatter(shifted_gaussian[:, 0], shifted_gaussian[:, 1], s=20,  c='r', marker='o')
plt.scatter(stretched_gaussian[:, 0], stretched_gaussian[:, 1], s=30,  c='b', marker='^')

plt.title('An NMC classifier built on 2d guass points')
plt.axis('tight')
plt.savefig(__file__ + '.png')
#plt.show()
