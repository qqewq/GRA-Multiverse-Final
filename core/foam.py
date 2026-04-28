import numpy as np

def compute_foam(vectors, P=None):
    """Φ = Σ_{a≠b} |⟨ψ_a|P|ψ_b⟩|^2"""
    if P is None:
        P = np.eye(len(vectors[0]))
    foam = 0.0
    n = len(vectors)
    for a in range(n):
        for b in range(n):
            if a != b:
                foam += np.abs(np.vdot(vectors[a], P @ vectors[b]))**2
    return foam

def foam_gradient(vectors, P=None):
    """Градиент пены по каждому вектору."""
    if P is None:
        P = np.eye(len(vectors[0]))
    n = len(vectors)
    grad = []
    for i in range(n):
        g = np.zeros_like(vectors[i])
        for j in range(n):
            if i != j:
                g += 2 * np.conj(np.vdot(vectors[i], P @ vectors[j])) * (P @ vectors[j])
        grad.append(g)
    return grad