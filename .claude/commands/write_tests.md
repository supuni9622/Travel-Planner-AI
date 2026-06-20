---
description: Write comprehensive tests for FastAPI + LangChain + LangGraph Python app
allowed-tools: Read, Grep, Glob, Bash(pytest:*), Bash(find:*), Bash(cat:*)
---

Write comprehensive pytest tests for: $ARGUMENTS

## Testing conventions:
- Use **pytest** with **pytest-asyncio** for async endpoints
- Place test files in a `tests/` directory at the project root, mirroring the source structure
- Name test files as `test_[filename].py`
- Use `from app.[module] import ...` for imports
- Mock LLM calls with `unittest.mock.patch` or `pytest-mock` — never hit real LLM APIs in tests
- Mock LangChain/LangGraph chains, agents, and graph nodes as needed
- Use `httpx.AsyncClient` with FastAPI's `ASGITransport` for endpoint testing
- Use `pytest.fixture` for shared setup (app client, mock LLM responses, sample states)

## Coverage:

### FastAPI Endpoints
- Happy path: valid request returns expected status + response shape
- Validation errors: missing/wrong fields return 422
- Service errors: when LLM/chain raises, endpoint returns 500
- Streaming endpoints: verify `text/event-stream` content-type and SSE format

### LangChain Chains & Tools
- Test chain invocation with mocked LLM returning controlled outputs
- Test prompt templates render correctly with given inputs
- Test tool functions independently with valid and invalid inputs
- Test output parsers handle well-formed and malformed LLM responses

### LangGraph Graphs & Nodes
- Test each node function independently with mock state
- Test graph transitions: verify correct next node is selected per state
- Test conditional edges with all branch conditions
- Test full graph execution end-to-end with mocked LLM
- Test interrupt/resume flows if using human-in-the-loop

### Error & Edge Cases
- Empty inputs, None values, empty lists
- LLM timeout or API error propagation
- Malformed LLM output that fails parsing
- State missing required keys mid-graph
- Concurrent requests if applicable

## Test file structure to follow:
```
tests/
  conftest.py          # shared fixtures (app client, mock LLM, sample states)
  test_api.py          # FastAPI endpoint tests
  test_chains.py       # LangChain chain/tool tests
  test_graph.py        # LangGraph node and graph tests
  test_[module].py     # any other module-specific tests
```

## Example fixture pattern to use:
```python
@pytest.fixture
def mock_llm(mocker):
    mock = mocker.patch("app.chains.llm")
    mock.invoke.return_value = AIMessage(content="mocked response")
    return mock

@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
```

All tests must run without a live LLM, database, or .env file. Use mocks and fixtures for all external dependencies.