import streamlit as st
import yaml
import numpy as np
import plotly.graph_objects as go
from agents.debate_engine import DebateEngine
from core.multiverse import Multiverse

# Загрузка конфига
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

st.set_page_config(page_title="GRA Multiverse Live", layout="wide")
st.title("🌌 GRA Multiverse — Абсолютный когнитивный вакуум")

# Боковая панель управления
st.sidebar.header("Параметры дебатов")
topic = st.sidebar.text_input("Тема обсуждения", "Является ли вселенная вычислимой?")
use_real_llm = st.sidebar.checkbox("Использовать настоящий LLM", value=config['agents']['use_llm'])
config['agents']['use_llm'] = use_real_llm

# Запуск дебатов
if st.sidebar.button("Запустить дебаты"):
    engine = DebateEngine(config)
    with st.spinner("Агенты спорят... ищут истину..."):
        final_belief, leaders = engine.run_to_emergence(topic)
    st.success("Консенсус достигнут!")
    st.subheader("Финальное убеждение")
    st.write(final_belief)
    st.subheader("Лидеры обсуждения")
    for agent in leaders:
        st.write(f"🤖 Агент {agent.id} (влияние: высокое)")

# Визуализация симуляции (заглушка с динамикой пены)
st.sidebar.header("Визуализация")
if st.sidebar.button("Показать демо-график сходимости"):
    # генерация фейковых данных пены
    rounds = np.arange(1, 11)
    foam = np.exp(-0.5 * rounds) + np.random.normal(0, 0.02, len(rounds))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rounds, y=foam, mode='lines+markers', name='Φ'))
    fig.update_layout(xaxis_title="Раунд", yaxis_title="Пена Φ", title="Сходимость к истине")
    st.plotly_chart(fig, use_container_width=True)

    # аттрактор Лоренца для красоты
    from core.lorenz import generate_trajectory
    traj = generate_trajectory(3000)
    fig3d = go.Figure(data=[go.Scatter3d(x=traj[:,0], y=traj[:,1], z=traj[:,2],
                                        mode='lines', line=dict(width=1))])
    fig3d.update_layout(title="Аттрактор Лоренца (хаос)")
    st.plotly_chart(fig3d, use_container_width=True)