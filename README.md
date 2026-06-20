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
| Frontend | Vanilla HTML/JS (served by FastAPI) |
| MCP Server | FastMCP (SSE + STDIO transport) |
| Vector Store | ChromaDB |
| Evaluation | LangSmith |
| Deployment | Docker Compose |
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

# Run everything with Docker Compose (recommended)

Docker Compose bundles all three services — **Frontend**, **FastAPI backend**, and **MCP server** — with a single command. PostgreSQL is included for persistent checkpointing.

## Services

| Service | Container | Port | What it serves |
|---|---|---|---|
| `api` | `travel-ai-api` | `8000` | FastAPI + Frontend (static files) |
| `mcp` | `travel-ai-mcp` | `8001` | MCP server (SSE transport) |
| `postgres` | `travel-ai-postgres` | `5432` | LangGraph checkpoint storage |

## URLs after startup

| URL | Description |
|---|---|
| `http://localhost:8000` | Frontend UI |
| `http://localhost:8000/travel/plan` | Trip planning API (full response) |
| `http://localhost:8000/travel/plan/stream` | Trip planning API (streaming SSE) |
| `http://localhost:8000/health` | Health check |
| `http://localhost:8001/sse` | MCP server endpoint (for AI clients) |

## Build and start

```bash
docker compose build --no-cache
docker compose up
```

## Run in background
```bash
docker compose up -d
```

## Verify containers
```bash
docker compose ps
```

## Check logs

```bash
docker compose logs -f api
docker compose logs -f mcp
docker compose logs -f postgres
```

## Stop everything
```bash
docker compose down
```

### Stop and delete PostgreSQL data
```bash
docker compose down -v
```
Be careful with `-v` — it deletes the database volume and all checkpoint history.

## In case we need to stop ports

Find what's using port 5432:
```bash
lsof -i :5432
```

Stop it:
```bash
brew services stop postgresql
# or
docker stop <container_id>
```

Then rerun:
```bash
docker compose up
```

## MCP server — local dev without Docker

The MCP server also works in STDIO mode for Claude Desktop integration (no Docker needed):

```bash
cd travel-mcp-server
python server.py
```

Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "travel-planner": {
      "command": "python",
      "args": ["/path/to/travel-mcp-server/server.py"]
    }
  }
}
```


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

