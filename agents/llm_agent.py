import os
import numpy as np

class LLMAgent:
    def __init__(self, config, agent_id=0):
        self.config = config
        self.id = agent_id
        self.backend = config['backend']
        self.model = config['model']
        self.use_llm = config.get('use_llm', False)
        # Инициализация LLM-клиента только при необходимости
        if self.use_llm and self.backend == 'openai':
            import openai
            openai.api_key = os.getenv('OPENAI_API_KEY')
            self.client = openai
        else:
            self.client = None

    def initial_belief(self, topic):
        if self.client:
            # настоящий вызов LLM
            response = self.client.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": f"Выскажи свое мнение по вопросу: {topic}"}],
                temperature=0.7
            )
            return response.choices[0].message['content']
        else:
            # симуляция: случайное мнение
            opinions = [
                f"{topic} – это фундаментальная категория.",
                f"{topic} непостижима.",
                f"{topic} можно объяснить через науку.",
            ]
            return opinions[self.id % len(opinions)]

    def revise_belief(self, topic, current_belief_vector):
        """Пересмотр убеждения с учётом аргументов (заглушка)."""
        if self.client:
            # упрощённо: пересмотр через API
            response = self.client.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Ты участвуешь в дебатах. Учитывай предыдущие аргументы и пересмотри своё мнение."},
                    {"role": "user", "content": f"Тема: {topic}. Текущее убеждение (вектор): {current_belief_vector}"}
                ]
            )
            return response.choices[0].message['content']
        else:
            # векторы не преобразуются в текст, просто возвращаем старую позицию
            return f"Агент {self.id} сохраняет мнение."