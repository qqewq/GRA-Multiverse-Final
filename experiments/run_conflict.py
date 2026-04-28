"""Конфликт целей (v5) – использует мультиверс с разными целями."""
import yaml
from core.multiverse import Multiverse
import numpy as np

def run():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    mv = Multiverse(config)
    # Эмулируем разные цели: разные проекторы
    mv.projectors[0] = np.diag([1, -1, 1, -1])  # какая-то конфликтная цель
    foam = mv.align_level(0)
    print(f"Конфликтная пена после обнуления: {foam:.4f}")

if __name__ == '__main__':
    run()