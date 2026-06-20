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

## Update requirements file
```
pip freeze > requirements.txt
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
```
python -m app.main
```

# Set up progressql
Step 1: Verify Docker
```
docker --version
```

If Docker isn't installed:

Docker Desktop for Mac

Install and start Docker Desktop.

Step 2: Run PostgreSQL - only once in initial setup
```
docker run --name travel-postgres \
  -e POSTGRES_USER=travel_user \
  -e POSTGRES_PASSWORD=travel_password \
  -e POSTGRES_DB=travel_ai \
  -p 5432:5432 \
  -d postgres:17
```

Start docker container 
```
docker start travel-postgres
```

Verify:
```
docker ps
```

You should see:

travel-postgres

Test Connection
```
psql postgresql://travel_user:travel_password@localhost:5432/travel_ai
```

Expected:

travel_ai=#

Exit:
```
\q
```

## Start persitant memory - progressql
```
python -m app.memory.setup
```

# Ingest files to RAG
```
python -m app.rag.ingest
```


# Run fastapi app
```
uvicorn app.api.app:app --reload
```

# Run the application using docker

## build the dockerfile
```
docker build -t travel-ai .
```

## Run using docker
```
docker run -p 8000:8000 travel-ai
```

# Use docker compose becuase we need to use local host for both progress and main app but we cannot do it when we use onluy dockerfile

## build compose
```
docker compose build --no-cache
```

## start the applicaiton
```
docker compose up
```

## or run in background 
```
docker compose up -d
```

## Verify containers
```
docker compose ps
```

## check logs

API
```
docker compose logs -f api
```
Postgres
```
docker compose logs -f postgres
```

## Stop everything
```
docker compose down
```

### Stop and delete PostgreSQL data
```
docker compose down -v
```
Be careful with -v because it deletes the database volume.

## In case we need to stop ports
stop the process using port 5432

Find what's using it:

lsof -i :5432

Example output:

COMMAND     PID   USER
postgres   1234  supunimanamperi

Stop it:

brew services stop postgresql

or:

docker ps
docker stop <container_id>

Then rerun:

docker compose up


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

# Real usage

![alt text](image.png)

# 👨‍💻 Author

Supuni Manamperi

Senior Software Engineer | AI Engineering Learner

