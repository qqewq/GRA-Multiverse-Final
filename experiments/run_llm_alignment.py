"""LLM-выравнивание (v6) – простой запуск без trust/truth (для совместимости)."""
import yaml
from agents.llm_agent import LLMAgent

def run():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    agents = [LLMAgent(config['agents'], i) for i in range(3)]
    topic = "Смысл жизни"
    for agent in agents:
        print(f"Агент {agent.id}: {agent.initial_belief(topic)}")

if __name__ == '__main__':
    run()