# 🔌 `ai-team-mcp` — AI Virtual Team Council MCP Server

**Version:** 0.1.0 (MCP 2.x Architecture)  
**Standard:** Model Context Protocol (Anthropic MCP Standard)  
**Lead Custodian:** Adrian Torres, TOGAF (Persona 07 — The Enterprise Tech Architect)  
**Project Manager:** Lucas Morales, PMP, PMI-ACP (Persona 30)  

---

## 📖 Overview

`ai-team-mcp` is the official Model Context Protocol (MCP) sidecar interface for Guillermo Granillo's 31-persona AI Virtual Team Council.

It exposes the team's cognitive personas, domain knowledge bases, single-pane-of-glass execution tracker, and governance standards to any MCP-compliant AI client (e.g., Claude Desktop, Antigravity, Cursor, VS Code Copilot, or remote web agents).

---

## 🛠️ Exposed MCP Tools

| Tool Name | Parameters | Description |
|---|---|---|
| `list_personas` | None | Lists all 31 specialized AI personas with their IDs, names, roles, summon tags (`@Tech`, `@PM`, `@Strategy`), and domain anchors. |
| `summon_persona` | `identifier` (str), `include_knowledge_base` (bool, default `False`) | Retrieves the full system prompt, cognitive posture, and operational instructions for any persona by number (`01`-`31`), name, or summon tag (e.g. `'07'`, `'adrian'`, `'@Tech'`). |
| `get_project_status` | `section` (str, default `'all'`) | Retrieves active execution status from `PROJECT_TRACKER.md` (e.g. `'dashboard'`, `'decisions'`, `'tasks'`, `'wbs'`, `'verification'`). |
| `query_knowledge_base` | `query` (str), `max_results` (int, default `3`) | Semantically searches curated markdown knowledge bases across strategy, data engineering, systems thinking, tourism, and venture economics. |
| `get_governance_rule` | `rule_query` (str) | Extracts official compliance rules from `AI_GOVERNANCE_AND_ETHICS.md` (e.g. Rule 30 Permissions-over-Instructions, Rule 28 SPG-PETS, Rule 31 Plain Language, Rule 32 Git Sync). |

---

## 🚀 Local Quickstart (Phase 1 — `stdio`)

### 1. Prerequisites
* Python 3.10+ (managed via `uv` or system Python)
* Virtual environment configured in `mcp/.venv`

### 2. Running the Server Locally

#### A. Local stdio mode (for Claude Desktop, Antigravity, VS Code Copilot):
```powershell
& "C:\Users\gsanc\AI Team\mcp\.venv\Scripts\python.exe" "C:\Users\gsanc\AI Team\mcp\server.py"
```

#### B. HTTP / SSE Web Server mode (for Gemini, Remote Copilot, or Web Agents):
```powershell
& "C:\Users\gsanc\AI Team\mcp\.venv\Scripts\python.exe" "C:\Users\gsanc\AI Team\mcp\server.py" --transport sse --port 8000
```
This runs an HTTP/SSE server accessible at `http://127.0.0.1:8000/sse` with message endpoint at `http://127.0.0.1:8000/messages/`.


### 3. Running Verification Tests
To run the automated integration test suite:

```powershell
& "C:\Users\gsanc\AI Team\mcp\.venv\Scripts\python.exe" "C:\Users\gsanc\AI Team\mcp\test_server.py"
```

---

## ⚙️ Client Configuration Snippets

### Claude Desktop (`claude_desktop_config.json`)
Add this block under `"mcpServers"` in `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ai-team": {
      "command": "C:\\Users\\gsanc\\AI Team\\mcp\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\gsanc\\AI Team\\mcp\\server.py"
      ]
    }
  }
}
```

### Antigravity (`~/.gemini/antigravity/mcp_servers.json`)
```json
{
  "ai-team-mcp": {
    "command": "C:\\Users\\gsanc\\AI Team\\mcp\\.venv\\Scripts\\python.exe",
    "args": [
      "C:\\Users\\gsanc\\AI Team\\mcp\\server.py"
    ]
  }
}
```

---

## 🗺️ Roadmap to Phase 2 (SSE / Cloud Hosting)
When ready to expose this server to external AI agents over the web:
1. `server.run(transport="sse")` exposes an HTTP/SSE server via Starlette/Uvicorn.
2. Deploy as a lightweight container to Render / Fly.io / HuggingFace Spaces.
3. Configure Bearer Token authentication to restrict tool calls to authorized agents only.
