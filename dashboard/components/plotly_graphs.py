"""Дополнительные функции для визуализации."""
import plotly.graph_objects as go

def plot_foam_curve(foam_values):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=foam_values, mode='lines+markers'))
    fig.update_layout(xaxis_title="Итерация", yaxis_title="Пена", title="Обнуление пены")
    return fig