import numpy as np

class TrustGraph:
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.weights = np.ones((num_agents, num_agents)) / num_agents

    def update(self, belief_vectors, consensus_vector, truth_scores=None):
        """Обновление весов доверия на основе когерентности с консенсусом и истинности."""
        for i in range(self.num_agents):
            coherence = 1.0 - np.linalg.norm(belief_vectors[i] - consensus_vector)
            if truth_scores is not None:
                coherence *= truth_scores[i]
            self.weights[i, :] += 0.1 * coherence
        # нормализация строк
        row_sums = self.weights.sum(axis=1, keepdims=True)
        self.weights = self.weights / np.where(row_sums == 0, 1, row_sums)

    def get_leaders(self, top_k=2):
        influence = self.weights.sum(axis=0)
        leaders = np.argsort(influence)[-top_k:]
        return list(leaders)

    def get_weighted_consensus(self, belief_vectors):
        """Консенсус с учётом влияния агентов (столбцовые суммы)."""
        influence = self.weights.sum(axis=0)
        weighted = np.average(belief_vectors, axis=0, weights=influence)
        return weighted