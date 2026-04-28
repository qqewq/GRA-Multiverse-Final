"""Демонстрация иерархического обнуления (из v2)."""
import yaml
from core.multiverse import Multiverse
import matplotlib.pyplot as plt

def run():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    mv = Multiverse(config)
    foam_level0 = mv.align_level(0)
    foam_level1 = mv.align_level(1)
    print(f"Φ0 = {foam_level0:.2e}, Φ1 = {foam_level1:.2e}")
    # простой график
    plt.title("Multi-level alignment")
    plt.bar([0,1], [foam_level0, foam_level1])
    plt.ylabel("Foam")
    plt.savefig("hierarchy.png")
    print("График сохранён в hierarchy.png")

if __name__ == '__main__':
    run()