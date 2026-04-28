import numpy as np
from .llm_agent import LLMAgent
from .trust_graph import TrustGraph
from .truth_evaluator import TruthEvaluator

class DebateEngine:
    def __init__(self, config):
        self.config = config['agents']
        self.num_agents = self.config['num_agents']
        self.agents = [LLMAgent(self.config, i) for i in range(self.num_agents)]
        self.trust_graph = TrustGraph(self.num_agents)
        self.truth_evaluator = TruthEvaluator(self.config.get('truth_threshold', 0.8))
        self.rounds = self.config['debate_rounds']

    def text_to_vec(self, text):
        """Примитивное преобразование текста в вектор (для симуляции)."""
        # реально нужно использовать эмбеддинги (v7), здесь просто хэш
        seed = sum(ord(c) for c in text) % 1000
        np.random.seed(seed)
        return np.random.randn(4)

    def run_to_emergence(self, topic):
        print(f"🚀 Запуск дебатов по теме: {topic}")
        # 1. Получение начальных убеждений
        beliefs_text = [agent.initial_belief(topic) for agent in self.agents]
        belief_vecs = [self.text_to_vec(t) for t in beliefs_text]
        consensus = np.mean(belief_vecs, axis=0)

        # 2. Раунды дебатов
        for rnd in range(self.rounds):
            # оценка истинности
            truth_scores = [self.truth_evaluator.evaluate(t) for t in beliefs_text]

            # вычисление кастомной пены = Φ_agreement + λ * (1 - mean_truth)
            phi_agree = sum(np.linalg.norm(v - consensus)**2 for v in belief_vecs) / len(belief_vecs)
            phi_truth = 1.0 - np.mean(truth_scores)
            total_phi = phi_agree + 0.5 * phi_truth

            print(f"Раунд {rnd+1}: Φ_agree={phi_agree:.4f}, Φ_truth={phi_truth:.4f}, total={total_phi:.4f}")
            if total_phi < 0.02:
                break

            # обновление доверия
            self.trust_graph.update(belief_vecs, consensus, truth_scores)

            # градиентный шаг: смещаем векторы в сторону взвешенного консенсуса (упрощённо)
            weighted_consensus = self.trust_graph.get_weighted_consensus(belief_vecs)
            for i in range(self.num_agents):
                belief_vecs[i] += 0.1 * (weighted_consensus - belief_vecs[i])
                belief_vecs[i] /= np.linalg.norm(belief_vecs[i])

            # обновление текстов (агенты "пересматривают" свои мнения)
            beliefs_text = [agent.revise_belief(topic, v) for agent, v in zip(self.agents, belief_vecs)]
            consensus = np.mean(belief_vecs, axis=0)

        # 3. Определение лидеров
        leaders_idx = self.trust_graph.get_leaders(top_k=2)
        # финальное убеждение (текст) – берём самого доверенного лидера
        final_belief = beliefs_text[leaders_idx[-1]]
        print("🏆 Лидеры:", [f"Агент {i}" for i in leaders_idx])
        return final_belief, [self.agents[i] for i in leaders_idx]