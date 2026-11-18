"""AI Team Model Context Protocol (MCP) Server.

Exposes the 31-persona AI virtual team council, curated knowledge bases,
project tracker, and governance standards to external AI agents via standard MCP.
"""

from pathlib import Path
import re
from typing import Any, Dict, List, Optional
from mcp.server.mcpserver import MCPServer

# Initialize server
server = MCPServer(
    name="ai-team-mcp",
    instructions=(
        "You are connected to the AI Virtual Team Council MCP Bridge. "
        "Use this server to discover team personas, summon expert personas, "
        "query domain knowledge bases, and inspect project governance and sprint status."
    ),
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PERSONAS_DIR = REPO_ROOT / "personas"
KB_DIR = REPO_ROOT / "knowledge_bases"
ROSTER_FILE = REPO_ROOT / "TEAM_ROSTER.md"
TRACKER_FILE = REPO_ROOT / "PROJECT_TRACKER.md"
GOVERNANCE_FILE = REPO_ROOT / "AI_GOVERNANCE_AND_ETHICS.md"


@server.tool(
    name="list_personas",
    description="Lists all 31 specialized AI personas in the virtual team council, including their ID, name, role, summon triggers, and core domain anchor.",
)
def list_personas() -> str:
    """Read and format the complete team roster."""
    if not ROSTER_FILE.exists():
        # Fallback: scan personas directory
        files = sorted(PERSONAS_DIR.glob("[0-9][0-9]_*.md"))
        out = ["# AI Team Roster (Directory Scan)", ""]
        for f in files:
            if not f.name.endswith("_KNOWLEDGE.md"):
                out.append(f"- **{f.stem}**")
        return "\n".join(out)

    content = ROSTER_FILE.read_text(encoding="utf-8")
    # Extract table from TEAM_ROSTER.md
    match = re.search(r"(\| # \| Name \| Role \|.*?\n\n)", content, re.DOTALL)
    if match:
        return f"# 👥 AI Virtual Team Roster (31 Personas)\n\n{match.group(1).strip()}"
    return content[:4000]


@server.tool(
    name="summon_persona",
    description="Retrieves the detailed persona specification, cognitive posture, system prompt, and instructions for a specific team member by ID (01-31), name, or summon tag (e.g., '07', 'adrian', '@Tech').",
)
def summon_persona(identifier: str, include_knowledge_base: bool = False) -> str:
    """Retrieve full system instructions and prompt for a given persona."""
    clean_id = identifier.strip().lower().lstrip("@")
    
    # Try finding matching persona file
    target_file: Optional[Path] = None
    target_kb_file: Optional[Path] = None

    all_files = list(PERSONAS_DIR.glob("[0-9][0-9]_*.md"))
    
    # Check if number provided
    num_match = re.search(r"\b([0-9]{1,2})\b", clean_id)
    if num_match:
        padded = f"{int(num_match.group(1)):02d}"
        for f in all_files:
            if f.name.startswith(padded) and not f.name.endswith("_KNOWLEDGE.md"):
                target_file = f
                kb_candidate = PERSONAS_DIR / f"{f.stem}_KNOWLEDGE.md"
                if kb_candidate.exists():
                    target_kb_file = kb_candidate
                break
    
    # If not found by number, search by keyword in filename
    if not target_file:
        for f in all_files:
            if f.name.endswith("_KNOWLEDGE.md"):
                continue
            if clean_id in f.name.lower():
                target_file = f
                kb_candidate = PERSONAS_DIR / f"{f.stem}_KNOWLEDGE.md"
                if kb_candidate.exists():
                    target_kb_file = kb_candidate
                break

    # If still not found, search inside TEAM_ROSTER.md for the summon trigger/name
    if not target_file and ROSTER_FILE.exists():
        roster_text = ROSTER_FILE.read_text(encoding="utf-8")
        for line in roster_text.splitlines():
            if line.startswith("|") and clean_id in line.lower():
                cols = [c.strip() for c in line.split("|")]
                if len(cols) > 2 and cols[1].isdigit():
                    padded = f"{int(cols[1]):02d}"
                    for f in all_files:
                        if f.name.startswith(padded) and not f.name.endswith("_KNOWLEDGE.md"):
                            target_file = f
                            kb_candidate = PERSONAS_DIR / f"{f.stem}_KNOWLEDGE.md"
                            if kb_candidate.exists():
                                target_kb_file = kb_candidate
                            break
                if target_file:
                    break

    if not target_file or not target_file.exists():
        return (
            f"❌ Persona '{identifier}' not found in council roster.\n"
            "Use `list_personas()` to see available personas (01 through 31)."
        )

    response = [f"# 👤 Persona Specification: {target_file.stem}", ""]
    response.append(target_file.read_text(encoding="utf-8"))

    if include_knowledge_base and target_kb_file and target_kb_file.exists():
        response.append("\n---\n")
        response.append(f"# 📚 Persona Knowledge Base: {target_kb_file.stem}\n")
        response.append(target_kb_file.read_text(encoding="utf-8"))

    return "\n".join(response)


@server.tool(
    name="get_project_status",
    description="Returns the current single-pane-of-glass execution state from PROJECT_TRACKER.md (Active Sprints, Open Decisions, Backlog WBS, Verification Gates).",
)
def get_project_status(section: str = "all") -> str:
    """Retrieve active status from PROJECT_TRACKER.md."""
    if not TRACKER_FILE.exists():
        return "❌ PROJECT_TRACKER.md not found in repository root."

    content = TRACKER_FILE.read_text(encoding="utf-8")
    sec_lower = section.strip().lower()

    if sec_lower in ("all", "dashboard", "overview"):
        # Return first 3500 chars (Executive overview + active tables)
        return content[:4000]

    # Filter by specific pillar
    patterns = {
        "decisions": r"## 🎯 Pillar 1: Open Decisions.*?(?=##|\Z)",
        "questions": r"## ❓ Pillar 2: Pending Questions.*?(?=##|\Z)",
        "tasks": r"## 📋 Pillar 4: Team Task Board.*?(?=##|\Z)",
        "wbs": r"## 📋 Pillar 4: Team Task Board.*?(?=##|\Z)",
        "verification": r"## 🧪 Pillar 5: Test & Verification.*?(?=##|\Z)",
    }

    if sec_lower in patterns:
        match = re.search(patterns[sec_lower], content, re.DOTALL)
        if match:
            return match.group(0).strip()

    return content[:4000]


@server.tool(
    name="query_knowledge_base",
    description="Searches across the curated knowledge_bases/ directory for specific topics, frameworks, literature summaries, and citations.",
)
def query_knowledge_base(query: str, max_results: int = 3) -> str:
    """Search knowledge bases for relevant snippets."""
    if not KB_DIR.exists():
        return "❌ knowledge_bases/ directory not found in repository root."

    keywords = [k.lower() for k in query.split() if len(k) > 2]
    if not keywords:
        # Return index of available files
        files = [f"- **{f.name}** ({f.stat().st_size // 1024} KB)" for f in KB_DIR.glob("*.*")]
        return "# 📚 Available Knowledge Base Files:\n\n" + "\n".join(files)

    matches: List[Dict[str, Any]] = []

    for file_path in KB_DIR.glob("*.*"):
        if file_path.suffix not in [".md", ".txt"]:
            continue
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        lines = text.splitlines()
        file_hits = 0
        snippets: List[str] = []

        for i, line in enumerate(lines):
            line_lower = line.lower()
            if any(kw in line_lower for kw in keywords):
                file_hits += 1
                start = max(0, i - 1)
                end = min(len(lines), i + 3)
                snippet = "\n".join(lines[start:end])
                if snippet not in snippets and len(snippets) < 2:
                    snippets.append(snippet)

        if file_hits > 0:
            matches.append({
                "file": file_path.name,
                "hits": file_hits,
                "snippets": snippets,
            })

    matches.sort(key=lambda x: x["hits"], reverse=True)
    top_matches = matches[:max_results]

    if not top_matches:
        return f"No direct matches found for '{query}' in knowledge_bases/. Try searching with broader keywords."

    out = [f"# 🔍 Knowledge Base Search Results for: '{query}'", ""]
    for m in top_matches:
        out.append(f"### 📄 `{m['file']}` ({m['hits']} hits)")
        for s in m["snippets"]:
            out.append("```text\n" + s.strip() + "\n```")
        out.append("")

    return "\n".join(out)


@server.tool(
    name="get_governance_rule",
    description="Retrieves official team governance rules and compliance standards (e.g. Rule 30 Permissions-over-Instructions, Rule 28 SPG-PETS, Rule 31 Plain-Language Text, Rule 32 Git Sync) from AI_GOVERNANCE_AND_ETHICS.md.",
)
def get_governance_rule(rule_query: str) -> str:
    """Retrieve governance and ethics standards."""
    if not GOVERNANCE_FILE.exists():
        return "❌ AI_GOVERNANCE_AND_ETHICS.md not found in repository root."

    content = GOVERNANCE_FILE.read_text(encoding="utf-8")
    query_clean = rule_query.strip().lower()

    # Search for matching section or rule
    lines = content.splitlines()
    matched_blocks: List[str] = []
    current_block: List[str] = []
    recording = False

    for line in lines:
        if line.startswith("#"):
            if query_clean in line.lower():
                recording = True
                if current_block:
                    matched_blocks.append("\n".join(current_block))
                    current_block = []
            elif recording and line.startswith(("## ", "# ")):
                recording = False
                if current_block:
                    matched_blocks.append("\n".join(current_block))
                    current_block = []

        if recording:
            current_block.append(line)

    if current_block:
        matched_blocks.append("\n".join(current_block))

    if matched_blocks:
        return "\n\n---\n\n".join(matched_blocks)

    return f"Rule matching '{rule_query}' not specifically isolated. Overview excerpt:\n\n" + content[:3000]


# Main execution entry point
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Virtual Team MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="Transport protocol to run server with (default: stdio)",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host address for HTTP/SSE transport (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port number for HTTP/SSE transport (default: 8000)",
    )

    args = parser.parse_args()

    if args.transport == "stdio":
        server.run(transport="stdio")
    else:
        print(f"🚀 Starting AI Team MCP Server over {args.transport.upper()} on http://{args.host}:{args.port}/sse ...")
        server.run(transport=args.transport, host=args.host, port=args.port)

