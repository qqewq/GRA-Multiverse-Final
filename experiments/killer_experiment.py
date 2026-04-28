import yaml
from agents.debate_engine import DebateEngine

def run(config=None):
    if config is None:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)

    engine = DebateEngine(config)
    topic = "Что есть истина в мультивселенной?"
    final_belief, leaders = engine.run_to_emergence(topic)

    print("\n=== РЕЗУЛЬТАТ ===")
    print("Финальное убеждение:")
    print(final_belief)
    print("Лидеры обсуждения:")
    for agent in leaders:
        print(f"- Агент {agent.id}")

if __name__ == '__main__':
    run()