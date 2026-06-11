# ✈️ Travel Planner AI

An end-to-end AI Travel Planning Assistant built to learn and demonstrate modern AI Engineering concepts using:

- LangChain
- LangGraph
- LLMs (Groq, OpenAI, Anthropic)
- Tool Calling
- AI Agents
- Memory
- RAG
- Streaming
- LangSmith
- Evaluation
- FastAPI
- Docker
- CI/CD

This project starts as a simple travel planning assistant and evolves into a production-grade AI system through incremental development.

---

# 🎯 Project Goals

This project is designed to learn and implement:

## LangChain Core

- Models
- Messages
- Prompt Templates
- Structured Output

## LangChain Advanced

- Tools
- Tool Calling
- Agents
- Memory
- Streaming
- Event Streaming

## LangGraph

- State Management
- Nodes
- Edges
- Conditional Routing
- Loops
- Checkpointing
- Multi-Agent Systems

## AI Engineering

- RAG
- Evaluation
- Observability
- Tracing
- Cost Optimization
- Model Routing
- Deployment
- Monitoring

---

# 🏗️ High Level Architecture

Current Phase:

```text
User
  |
Prompt
  |
LLM
  |
Structured Output
```

Target Architecture:

```text
                    ┌─────────────┐
                    │   User      │
                    └──────┬──────┘
                           │
                           ▼
                ┌───────────────────┐
                │ Planner Agent     │
                └──────┬────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼

 Flights Tool    Hotels Tool    Weather Tool

        └──────────────┼──────────────┘
                       ▼

                Budget Validator
                       │
                       ▼

                Itinerary Generator
                       │
                       ▼

                  Final Plan
```

Future LangGraph Architecture:

```text
START
   |
Planner
   |
Route Decision
 /    |    \
Flights Hotels Weather
  \      |      /
   \     |     /
      Budget
         |
      Generate
         |
        END
```

---

# 📂 Project Structure

```text
travel-planner-ai/
│
├── app/
│   │
│   ├── models/
│   │   └── llm.py
│   │
│   ├── prompts/
│   │   └── planner_prompt.py
│   │
│   ├── schemas/
│   │   └── travel_plan.py
│   │
│   ├── services/
│   │   └── travel_planner.py
│   │
│   └── main.py
│
├── tests/
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

```text
travel-planner-ai/
│
├── app/
│   ├── models/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── agents/
│   ├── graphs/
│   └── main.py
│
├── tests/
├── docs/
├── notebooks/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Framework | LangChain |
| Orchestration | LangGraph |
| LLM Provider | Groq |
| Validation | Pydantic |
| API Layer | FastAPI |
| Evaluation | LangSmith |
| Vector Store | TBD |
| Deployment | Docker |
| CI/CD | GitHub Actions |

---

# 🚀 Setup

## Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate:

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 🧪 Run Project

```bash
python3 app/main.py
```

---

# 🗺️ Learning Roadmap

## Phase 1 - LangChain Core

- [ ] Models
- [ ] Messages
- [ ] Prompt Templates
- [ ] Structured Output

---

## Phase 2 - LangChain Components

- [ ] Tools
- [ ] Tool Calling
- [ ] Agents
- [ ] Memory

---

## Phase 3 - Production Features

- [ ] Streaming
- [ ] Event Streaming
- [ ] LangSmith Tracing
- [ ] Evaluation

---

## Phase 4 - LangGraph

- [ ] State
- [ ] Nodes
- [ ] Edges
- [ ] Conditional Routing
- [ ] Loops

---

## Phase 5 - Advanced LangGraph

- [ ] Multi-Agent Systems
- [ ] Human-in-the-Loop
- [ ] Checkpointing
- [ ] Supervisor Pattern

---

## Phase 6 - RAG

- [ ] Document Loading
- [ ] Embeddings
- [ ] Vector Stores
- [ ] Retrieval
- [ ] Hybrid Search

---

## Phase 7 - Deployment

- [ ] FastAPI
- [ ] Docker
- [ ] GitHub Actions
- [ ] Monitoring

---

# 📚 Key Learning Outcomes

By the end of this project, I should be able to:

- Build production-ready AI applications
- Design AI workflows using LangGraph
- Implement AI agents and tool calling
- Build RAG systems
- Evaluate AI applications
- Deploy AI systems to production
- Explain AI architecture decisions in interviews

---

# 👨‍💻 Author

Supuni Manamperi

Senior Software Engineer | AI Engineering Learner

