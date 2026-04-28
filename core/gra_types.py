import numpy as np

class GRATypeSelector:
    @staticmethod
    def determine(eigenvalues, lyapunov1, lyapunov_max):
        reals = [np.real(ev) for ev in eigenvalues]
        if all(r < -1e-9 for r in reals):
            return "static"
        if any(abs(r) < 1e-9 for r in reals) and lyapunov1 < 0:
            return "cyclic"
        if lyapunov_max > 1e-9:
            return "chaotic"
        return "hybrid"