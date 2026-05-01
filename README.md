# 🌌 GRA Multiverse — Final
## GRA‑Multiverse — Final
https://github.com/vm32/GR-Project

**Многоуровневая GRA Мета‑обнулёнка в мультивселенной** — фреймворк для согласования иерархических систем через минимизацию «пены» (Φ).  
**GRA Multiverse — Final** is a hierarchical **GRA Meta‑obnulёнka (Meta‑Reset)** framework operating in a multiverse, designed to reconcile complex systems by minimizing “foam” (Φ) across scales.

**Финальная версия** объединяет все наработки (v1–v8) и добавляет поиск истины, динамическое доверие, эмерджентных лидеров и живой дашборд.  
The **final release** consolidates all versions (v1–v8) and adds **truth‑finding**, **dynamic trust**, **emergent leaders**, and a **live dashboard**.

---

## Quick links / Быстрые ссылки

- [ORCID profile](https://orcid.org/0009-0004-1872-1153) – [ORCID аккаунт](https://orcid.org/0009-0004-1872-1153)  
- [Zenodo record](https://doi.org/10.5281/zenodo.19844482) – [Ресурс Zenodo](https://doi.org/10.5281/zenodo.19844482)

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--1872--1153-green)](https://orcid.org/0009-0004-1872-1153)  
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.19826433-blue)](https://doi.org/10.5281/zenodo.19826433)  
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

---

## Что внутри? / What’s inside?

- **Иерархия мультивселенной** – уровни доменов, мета‑систем и мультиверса.  
  **Multiverse hierarchy** – nested levels of domains, meta‑systems, and the multiverse core.  
- **4 режима GRA** – статический, циклический, хаотический (Лоренц) и гибридный.  
  **4 GRA modes** – static, cyclic, chaotic (Lorenz), and hybrid configurations.  
- **LLM‑дебаты** – настоящие языковые агенты (OpenAI / локальная симуляция).  
  **LLM‑debates** – real language agents (OpenAI / local simulation).  
- **Trust Graph** – динамическая матрица доверия, эмерджентные лидеры.  
  **Trust Graph** – dynamic trust matrix and emergent leaders.  
- **Поиск истины** – алетическая метрика, убивающая компромиссы.  
  **Truth‑finding** – alethic metric that eliminates compromises.  
- **Живой дашборд** – Streamlit с графиками сходимости и аттракторами.  
  **Live dashboard** – Streamlit interface with convergence plots and attractors.

---

## Быстрый старт / Quick start

1. Установите зависимости / Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Настройте ключи (если используете настоящие LLM) / Configure keys (if using real LLMs):
   ```bash
   cp .env.example .env
   # отредактируйте .env, вставьте OPENAI_API_KEY
   # edit .env and insert OPENAI_API_KEY
   ```

   Запустите дашборд / Run the dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```

   или через Docker / or via Docker:
   ```bash
   docker-compose up
   ```

   Для запуска экспериментов из командной строки / To run experiments from CLI:
   ```bash
   python main.py
   # или напрямую / or directly:
   python experiments/killer_experiment.py
   ```

---

## Эволюция версий (путь к финалу) / Version evolution (path to Final)

| Версия / Version | Ключевое улучшение / Key improvement |
|------------------|--------------------------------------|
| v1 | Базовая иерархия и пена / Basic hierarchy and foam |
| v2 | Визуализация сходимости / Convergence visualization |
| v3 | Режимы: статика/цикл/хаос / Modes: static / cyclic / chaos |
| v4 | Хаос Лоренца, показатели Ляпунова / Lorenz chaos, Lyapunov exponents |
| v5 | Конфликт целей + мета‑агент / Goal conflict + meta‑agent |
| v6 | LLM‑агенты (первые шаги) / LLM agents (first steps) |
| v7 | Эмбеддинги и кластеризация убеждений / Embeddings and belief clustering |
| v8 | Настоящая LLM‑автосходимость / Real LLM auto‑convergence |
| **Final** | 🔥 Убийца компромиссов: истина, доверие, лидеры, дашборд / 🔥 The compromise‑killer: truth, trust, leaders, dashboard |

---

## Структура репозитория / Repository structure

```text
├── config.yaml            # все настройки мультивселенной
├── main.py                # точка входа для запуска экспериментов
├── core/                  # математика: пена, мультиверс, режимы GRA, Лоренц
├── agents/                # LLM-агенты, дебаты, доверие, истина
├── experiments/           # готовые сценарии (killer_experiment.py – главный)
├── dashboard/             # Streamlit-интерфейс
├── tests/                 # юнит-тесты
├── docs/                  # LaTeX-статья
```

```text
├── config.yaml            # multiverse configuration
├── main.py                # entry point for experiments
├── core/                  # math: foam, multiverse, GRA modes, Lorenz
├── agents/                # LLM agents, debates, trust, truth‑finding
├── experiments/           # ready‑made scenarios (killer_experiment.py is central)
├── dashboard/             # Streamlit interface
├── tests/                 # unit tests
├── docs/                  # LaTeX paper
```

---

## Философия / Philosophy

Мы не ищем компромисс – мы обнуляем несогласие на всех уровнях абстракции.  
**We are not seeking compromise – we reset disagreement at every level of abstraction.**

Конечная цель: состояние абсолютного когнитивного вакуума – пространство, свободное от интерпретационных артефактов.  
The final goal: **absolute cognitive vacuum** – a space free from interpretational artifacts.

---

## Лицензия / License

MIT
