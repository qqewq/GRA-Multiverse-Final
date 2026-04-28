"""
GRA Multiverse Final – главная точка входа.
Запускает killer-эксперимент (поиск истины) или любой другой из experiments/.
"""
import yaml
import argparse
from experiments import killer_experiment

def main():
    parser = argparse.ArgumentParser(description='GRA Multiverse Final')
    parser.add_argument('--experiment', type=str, default='killer',
                        choices=['killer', 'hierarchy', 'modes', 'lorenz', 'conflict', 'llm_alignment'],
                        help='какой эксперимент запустить')
    args = parser.parse_args()

    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    if args.experiment == 'killer':
        killer_experiment.run(config)
    # Здесь можно добавить вызовы других экспериментов по аналогии
    else:
        print(f"Эксперимент {args.experiment} пока не подключён к main.py, запустите напрямую из experiments/")

if __name__ == '__main__':
    main()