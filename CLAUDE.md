# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Run the app
```bash
# Direct Python entry point
python -m app.main

# FastAPI server (primary API)
uvicorn app.api.app:app --reload
```

### One-time setup tasks
```bash
# Initialize PostgreSQL checkpointer schema (requires running postgres)
python -m app.memory.setup

# Ingest documents into ChromaDB vector store
python -m app.rag.ingest
```

### Run tests (manual invocation — no test runner configured)
```bash
python -m app.tests.test_agents
python -m app.tests.test_memory
python -m app.tests.test_model
python -m app.tests.test_streaming
python -m app.tests.test_tools
```

### Docker (all services)
```bash
docker compose build --no-cache
docker compose up          # foreground — starts api, postgres, and mcp
docker compose up -d       # background
docker compose down        # stop
docker compose down -v     # stop + delete postgres volume
```

Logs per service:
```bash
docker compose logs -f api
docker compose logs -f mcp
docker compose logs -f postgres
```

## Service URLs (when running via docker compose)

| URL | Service |
|---|---|
| `http://localhost:8000` | Frontend UI |
| `http://localhost:8000/travel/plan` | FastAPI — full trip plan |
| `http://localhost:8000/travel/plan/stream` | FastAPI — SSE streaming |
| `http://localhost:8000/health` | FastAPI — health check |
| `http://localhost:8001/sse` | MCP server — SSE endpoint |

## Environment Variables

Copy `.env.template` to `.env`:

| Variable | Purpose |
|---|---|
| `GROQ_API_KEY` | Required — Groq LLM API key |
| `MODEL_PROVIDER` | `groq` (only supported provider) |
| `MODEL_NAME` | Default: `llama-3.3-70b-versatile` |
| `TEMPERATURE` | Default: `0.2` |
| `MAX_TOKENS` | Default: `1024` |
| `DATABASE_URL` | PostgreSQL URI for persistent checkpointing |
| `LANGSMITH_API_KEY` | Optional — LangSmith tracing |
| `LANGSMITH_TRACING` | `true` to enable tracing |

## Architecture

This is a LangGraph-based multi-agent travel planning system exposed via FastAPI.

### Request Flow

```
POST /travel/plan  →  travel_service.py  →  LangGraph graph  →  itinerary string
POST /travel/plan/stream  →  SSE stream of graph update events
```

`travel_service.py` creates the initial `TravelState` dict, invokes the graph with a `thread_id` config (for checkpointing), and returns `result["itinerary"]`.

### Shared State

All agents communicate through a single `TravelState` TypedDict (`app/graphs/state.py`). Fields with `Annotated[list, add]` reducers (`warnings`, `travel_advice`) support concurrent writes from multiple nodes — all other fields are last-writer-wins.

### Graph Variants

Multiple graph implementations exist for different patterns (most recent one is used in production):

| File | Pattern |
|---|---|
| `graph.py` | Fan-out/fan-in with subgraphs; `InMemorySaver` checkpointing |
| `llm_supervisor_graph.py` | LLM-powered supervisor decides which agents to run; PostgreSQL checkpointing |
| `rag_graph.py` | Supervisor + RAG retrieval step before itinerary generation |
| `long_memory_graph.py` | RAG + long-term user memory (load/save memory nodes) |
| `planner_graph.py` | LLM planner generates a task list; executor runs tasks sequentially |
| `llm_planner_graph.py` | Variant of planner pattern |
| `shared_state_graph.py` | Multi-agent shared state collaboration |
| `graph_single.py` | Single-agent variant |

**Currently active**: `travel_service.py` imports from `rag_graph.py`.

### Subgraphs

Each domain (flights, hotels, weather, itinerary) has its own subgraph under `app/graphs/subgraphs/`. These are compiled separately and registered as nodes in the parent graph.

### Nodes

`app/graphs/nodes/` contains individual node functions. Key nodes:

- `llm_supervisor.py` — uses structured output (`SupervisorDecision`) to decide `next_agents`
- `router.py` (`route_agents`) — conditional edge function routing to the supervisor's chosen agents
- `retrieve_context.py` — queries ChromaDB via `app/rag/retriever.py`
- `load_memory.py` / `save_memory.py` — read/write JSON user profiles from `app/memory/users/{user_id}.json`
- `itinerary.py` — final node that assembles the itinerary string from state

### LLM

`app/models/llm.py` exports `get_llm()` — reads `MODEL_PROVIDER`/`MODEL_NAME` from env, currently only supports Groq.

### Memory Systems

Two distinct memory mechanisms:

1. **Short-term (checkpointing)**: `app/memory/checkpointer.py` — uses `PostgresSaver` for persistent conversation state across requests, keyed by `thread_id`. Falls back gracefully to `InMemorySaver` in some graph variants.

2. **Long-term (user profiles)**: `app/memory/long_term.py` — JSON files in `app/memory/users/{user_id}.json` storing user preferences across sessions.

### RAG Pipeline

- Documents in `data/` (markdown files: `visa_rules.md`, `hotels.md`, `attractions.md`, `transportation.md`, `tokyo_guide.md`)
- Embedded with `all-MiniLM-L6-v2` (HuggingFace) and stored in ChromaDB at `./db/travel/`
- Run `python -m app.rag.ingest` to rebuild the vector store after changing source documents

### MCP Server

`travel-mcp-server/` is a standalone FastMCP server (`server.py`) that exposes the same tools (hotels, flights, weather) as MCP tools/resources/prompts. Has its own `requirements.txt`.

Transport is controlled by the `MCP_TRANSPORT` environment variable:
- **STDIO** (default, no env var) — for Claude Desktop; run `python server.py` from `travel-mcp-server/`
- **SSE** (`MCP_TRANSPORT=sse`) — HTTP mode used in Docker; listens on `MCP_PORT` (default `8001`)

In Docker, the `mcp` service starts automatically with SSE transport and is reachable at `http://localhost:8001/sse`.
