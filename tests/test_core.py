import numpy as np
from core.foam import compute_foam, foam_gradient

def test_foam_orthogonal_vectors():
    v1 = np.array([1,0])
    v2 = np.array([0,1])
    foam = compute_foam([v1, v2])
    assert foam < 1e-10, "Ортогональные векторы должны давать близкую к нулю пену"

def test_foam_identical_vectors():
    v = np.array([1,0])
    foam = compute_foam([v, v])
    assert foam > 0, "Одинаковые векторы дают ненулевую пену"