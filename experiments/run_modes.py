"""Демо трёх режимов (static, cyclic, chaotic) – v3."""
import numpy as np
from core.gra_types import GRATypeSelector

def run():
    # статический: отрицательные действительные части
    ev_static = [-1.0, -2.0]
    mode = GRATypeSelector.determine(ev_static, 0, 0)
    print(f"Собств.значения {ev_static} -> режим: {mode}")

    # циклический: чисто мнимые
    ev_cyclic = [1j, -1j]
    mode = GRATypeSelector.determine(ev_cyclic, -0.1, 0)
    print(f"Собств.значения {ev_cyclic}, Lyap1=-0.1 -> режим: {mode}")

    # хаотический: положительный Ляпунов
    ev_chaos = [-1, 0.5]
    mode = GRATypeSelector.determine(ev_chaos, 0, 0.1)
    print(f"Собств.значения {ev_chaos}, Lyap_max=0.1 -> режим: {mode}")

if __name__ == '__main__':
    run()