# Free Deployment Options

This project uses FastAPI + PostgreSQL + ChromaDB + Docker + MCP server. The options below cover the best free hosting platforms for this stack.

---

## Option 1: Render (Easiest)

Best overall fit for this project.

- **Web Service** (free tier) — deploy the FastAPI app from Docker or Git
- **PostgreSQL** — Render gives a free managed Postgres instance
- **Limitation**: free web services sleep after 15 min of inactivity; ChromaDB volume won't persist on the free tier (use `InMemorySaver` fallback or skip RAG in prod)

**Steps:**
1. Push repo to GitHub
2. Create a Render Web Service pointing to your repo, set build to `Dockerfile`
3. Add environment variables (`GROQ_API_KEY`, `DATABASE_URL` from Render Postgres, etc.)
4. For ChromaDB: either use Render's disk (paid) or switch to `InMemorySaver` and skip RAG for the free tier

---

## Option 2: Railway

- Supports Docker Compose natively — closest to the local setup
- Free tier: $5 of credit/month (enough for light traffic)
- PostgreSQL plugin available
- Persistent volumes for ChromaDB

**Steps:**
1. Connect your GitHub repo to Railway
2. Railway auto-detects `docker-compose.yml`
3. Add a PostgreSQL plugin and link `DATABASE_URL`
4. Set remaining env vars in the Railway dashboard

---

## Option 3: Fly.io

- Docker-native, persistent volumes (3 GB free)
- Free tier: 3 shared-CPU VMs
- ChromaDB can persist on a volume
- Requires splitting `docker-compose.yml` into separate `fly.toml` apps per service

**Steps:**
1. Install the Fly CLI: `brew install flyctl`
2. `fly launch` from the project root (generates `fly.toml`)
3. `fly volumes create chroma_data --size 1` for ChromaDB persistence
4. Deploy the MCP server as a separate Fly app if needed

---

## Option 4: Hugging Face Spaces

- Supports Docker with a `Dockerfile`
- Completely free, always-on (no sleep)
- No PostgreSQL built-in — use `InMemorySaver` fallback instead of Postgres checkpointing

**Steps:**
1. Create a new Space on Hugging Face, choose "Docker" as the SDK
2. Push your repo (the Space uses your `Dockerfile`)
3. Set secrets (`GROQ_API_KEY`, etc.) in Space settings
4. Switch `DATABASE_URL` to empty/unset so the app falls back to `InMemorySaver`

---

## Constraints to Resolve Before Deploying

| Concern | Detail |
|---|---|
| ChromaDB persistence | Needs a persistent disk volume — not free on Render; free on Fly.io (3 GB) |
| MCP server | Separate service — deploy independently or disable for production |
| `GROQ_API_KEY` | Required on all platforms; set as an environment secret |
| PostgreSQL | Free on Render and Railway; use `InMemorySaver` fallback on HuggingFace |

---

## Recommended Path

**Render** (API + Render Postgres) is the fastest path to get running for free.  
**Railway** is the best fit if you want Docker Compose to work with minimal changes.  
**Fly.io** is best if ChromaDB persistence (RAG) is important with no budget.
