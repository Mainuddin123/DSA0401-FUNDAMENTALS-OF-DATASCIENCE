import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


np.random.seed(0)
n_samples = 300
data = np.random.randn(n_samples, 2)  # Replace with your own customer data


k = 3


kmeans = KMeans(n_clusters=k, random_state=0)
clusters = kmeans.fit_predict(data)


plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Cluster Centers')
plt.xlabel('Amount Spent')
plt.ylabel('Visits')
plt.title('Customer Segmentation')
plt.legend()
plt.show()

