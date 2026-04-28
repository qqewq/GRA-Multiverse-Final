import numpy as np
from .foam import compute_foam, foam_gradient

class Multiverse:
    def __init__(self, config):
        mconf = config['multiverse']
        self.levels = mconf['levels']
        self.subsystems = mconf['subsystems']
        self.gra_types = mconf.get('gra_types', ['static'] * self.levels)
        self.hp = mconf['hyperparams']
        self.states = []
        # инициализация случайными комплексными векторами
        for l in range(self.levels):
            dim = 4  # можно сделать настраиваемым
            self.states.append([np.random.randn(dim) + 1j*np.random.randn(dim) for _ in range(self.subsystems[l])])
        self.projectors = [np.eye(dim) for _ in range(self.levels)]  # заглушка

    def align_level(self, level, eta=0.05, max_iter=200):
        """Обнуление пены на одном уровне (градиентный спуск)."""
        P = self.projectors[level]
        for it in range(max_iter):
            foam = compute_foam(self.states[level], P)
            if foam < 1e-9:
                break
            grad = foam_gradient(self.states[level], P)
            for i in range(len(self.states[level])):
                self.states[level][i] -= eta * grad[i]
            # нормировка
            self.states[level] = [v / np.linalg.norm(v) for v in self.states[level]]
        return foam

    def get_consensus_vector(self, level):
        """Возвращает усреднённый вектор уровня (грубый консенсус)."""
        return np.mean(self.states[level], axis=0)