"""Модуль v7: кластеризация убеждений на основе эмбеддингов."""
from sklearn.cluster import KMeans
import numpy as np

def cluster_beliefs(embeddings, n_clusters=None):
    if n_clusters is None:
        n_clusters = max(2, int(np.sqrt(len(embeddings))))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    return labels, kmeans.cluster_centers_