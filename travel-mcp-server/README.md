# Travel Planner MCP Server

A learning project for understanding and implementing the **Model Context Protocol (MCP)**.

This project exposes travel-related capabilities as MCP tools, resources, and prompts so they can be consumed by MCP-compatible clients such as:

- Claude Desktop
- Cursor
- VS Code
- LangGraph applications
- CrewAI
- AutoGen
- Custom AI agents

---

## 🎯 Learning Goals

This project demonstrates:

- MCP fundamentals
- MCP server architecture
- Tools, resources, and prompts
- stdio transport
- Connecting Claude Desktop to MCP
- Reusing capabilities across AI applications
- Integrating MCP with LangGraph

---

## 🏗️ Architecture

```text
Claude Desktop / Cursor / LangGraph
                  │
                  ▼
            MCP Client
                  │
                  ▼
           MCP Protocol
                  │
                  ▼
      Travel Planner MCP Server
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 Hotels Tool  Flights Tool  Weather Tool

```

## 📂 Project Structure

travel-mcp-server/
├── server.py
├── requirements.txt
├── README.md
│
├── tools/
│   ├── __init__.py
│   ├── hotels.py
│   ├── flights.py
│   └── weather.py
│
├── resources/
│   ├── __init__.py
│   └── guides.py
│
└── prompts/
    ├── __init__.py
    └── itinerary.py


## 🚀 Features
Tools
Search hotels
Search flights
Get weather information
Resources
Travel guides
Destination information
Prompts
Itinerary generation templates
🛠️ Tech Stack
Python 3.12+
MCP Python SDK
FastMCP

# 📦 Installation

Clone the repository:
```
git clone <repository-url>

cd travel-mcp-server
```

Create a virtual environment:
```
python -m venv .venv
```

Activate the environment:

macOS / Linux
```
source .venv/bin/activate
```
Windows
```
.venv\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```

## ▶️ Running the Server

Start the MCP server:
```
python server.py
```

The server runs using the default MCP transport:
```
stdio
```

This allows MCP-compatible clients to communicate with it.

# 🔧 Example Tools

## Search Hotels
```
search_hotels(city="Tokyo")
```

### Example response:
```
[
  "Hotel Sakura",
  "Tokyo Inn",
  "Shibuya Stay"
]
```

## Search Flights
```
search_flights(
    origin="Colombo",
    destination="Tokyo"
)
```

### Example response:
```
[
  "Flight A",
  "Flight B"
]
```

## Get Weather
```
get_weather(city="Tokyo")
```

### Example response:
```
{
  "temperature": 24,
  "condition": "Sunny"
}
```

# 📚 Example Resources

## Resource URI:
```
travel://tokyo-guide
```

### Example content:

- Visit Shibuya Crossing
- Explore Akihabara
- Experience cherry blossom season

# ✍️ Example Prompts
```
itinerary_prompt(destination="Tokyo")
```

## Example output:

Create a 5-day itinerary for Tokyo focused on anime, food, and cultural experiences.

# 🔌 Claude Desktop Integration

## Open the Claude Desktop configuration file:

macOS
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

Add:
```
{
  "mcpServers": {
    "travel-planner": {
      "command": "/absolute/path/to/.venv/bin/python",
      "args": [
        "/absolute/path/to/server.py"
      ]
    }
  }
}
```

Restart Claude Desktop.
The available tools will automatically appear.

# 🔗 Future LangGraph Integration

Instead of directly creating tools inside LangGraph:

```
@tool
def search_hotels():
    ...
```

LangGraph can consume MCP tools through an MCP client.

```
LangGraph
    ↓
MCP Client
    ↓
Travel Planner MCP Server
```

## Benefits:

Tool reuse
Standardized integrations
Framework independence

# 🧠 Key MCP Concepts

## MCP Client

The AI application consuming capabilities.

Examples:

Claude Desktop
Cursor
LangGraph

## MCP Server

Exposes capabilities to clients.

Examples:

Travel Planner MCP Server
GitHub MCP Server
PostgreSQL MCP Server

## Tools

Executable actions.

Examples:

search_hotels()
search_flights()

## Resources

Read-only information.

Examples:

travel://tokyo-guide

## Prompts

Reusable prompt templates.

Examples:

itinerary_prompt()