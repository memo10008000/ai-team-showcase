# 🏗️ SYSTEM_ARCHITECTURE.md — Enterprise Architecture Specification
**Document ID:** ARCH-SPEC-001  
**Version:** 1.0  
**Effective Date:** November 2026  
**Architect:** Adrian Torres, TOGAF 9 L2 (Persona 07 — Enterprise Solution Architect)  
**Co-Authors:** Tariq Al-Mansoor (Persona 23 — Data Engineer), Dr. Kenji Nakamura (Persona 08 — AI Governance & Auditor)  
**Approved By:** Guillermo Granillo (Executive Coordinator)  

---

## 1. Architecture Vision & Objectives

This specification establishes the formal enterprise architecture for Guillermo Granillo's **AI Virtual Advisory Team**. Grounded in **TOGAF 9 / 10 standards**, the architecture decouples cognitive personas from underlying model vendors, establishes clean data and context boundaries, and operationalizes spec-driven agentic engineering.

### Architectural Objectives
1. **Vendor Detachment & Portability:** Complete platform independence across Google Antigravity, Claude Code, GitHub Copilot, Cursor, xAI Grok, and custom orchestration harnesses.
2. **Context Integrity & Zero Drift:** Elimination of multi-session state degradation through deterministic memory structures (`MEMORY.md`, `CHANGE_LOG.md`, `PROJECT_TRACKER.md`).
3. **Model Tiering & Token Economics:** Strict role-to-engine routing (Rule 25) achieving an empirical 76–85% token economy.
4. **Tool & Agent Security:** Hard boundaries enforced via Permissions-over-Instructions (Rule 30) and least-privilege tool contracts.

---

## 2. TOGAF 4-Layer Architectural Blueprint

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             LAYER 1: INTERACTION & WORKSPACE                           │
│  • Antigravity IDE (Gemini 3.8)    • Claude Code CLI      • Cursor / VS Code Copilot  │
│  • Chat UI / Council Mode Prompts   • Sidecar Viewers (Mol*, Compose, Generative UI)  │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│                             LAYER 2: AGENTIC ORCHESTRATION                             │
│  • 31 Autonomous Personas (`personas/*.md`)           • Master Operating Standards     │
│  • Model Tiering & Token Routing Table (Rule 25)      • Council Session Orchestrator   │
│  • CI Auditor Gate (Dr. Kenji Nakamura - Rule 30)     • Process Gate (Rule 29 - CBPP)  │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│                             LAYER 3: CONTEXT, KNOWLEDGE & TOOLS                        │
│  • 38 NotebookLM Knowledge Bases (1,056+ sources)    • MCP Tool Servers (Local/Remote)│
│  • Domain Summaries (`knowledge_bases/*.md`)         • Research Frameworks (Creswell) │
│  • Project Data Dictionaries & Synthetic Traces       • Universal Extraction Prompts   │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│                             LAYER 4: PERSISTENCE & GOVERNANCE                          │
│  • Canonical Memory (`MEMORY.md`)                     • Single Pane Tracker (Rule 28)  │
│  • Immutable Audit Log (`CHANGE_LOG.md`)              • Git Synchronization (Rule 32)  │
│  • Output Document Vault (`outputs/docs/`, `web/`)    • Private GitHub Remote (memo10) │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Layer Specifications

### Layer 1: Interaction & Workspace Environment
* **Primary Environments:**
  * **Google Antigravity:** Primary IDE for deep multi-agent workflow orchestration, generative UI inspection, and sandboxed command execution.
  * **Claude Code CLI:** Rapid terminal-based development and localized refactoring.
  * **GitHub Copilot / Cursor:** In-editor inline code completion and speculative drafting.
* **Workspace Invariants:**
  * Canonical root: `C:\Users\gsanc\AI Team`
  * Forward-slash URI convention (`https://github.com/memo10008000/ai-team-showcase) for universal cross-platform hyperlinking.

### Layer 2: Agentic Orchestration & Engine Tiering (Rule 25)
To balance cognitive reasoning against inference cost and latency, workloads are routed according to the codified 4-tier model allocation strategy:

| Tier | Model Category | Exemplar Engines | Assigned Roles / Personas | Workload Characteristics |
|---|---|---|---|---|
| **Tier 1: Frontier / Architect** | Heavy Frontier Reasoning | Claude 3.5 Sonnet / Opus, Gemini 3.8 Pro | Adrian Torres (`@Tech`), Dr. Kenji Nakamura (`@AIGov`), Dr. Vivienne Zhao (`@Strategy`), Dr. Vance (`@PI`) | Architecture design, CI gate auditing, complex econometric proofs, meta-governance. |
| **Tier 2: Mid-Tier Workhorse** | Balanced Instruction Following | Claude 3.5 Sonnet, Gemini 3.8 Flash | Lucas Morales (`@PM`), Dr. Natasha Kowalski (`@DataAnalyst`), Tariq Al-Mansoor (`@DataEngineer`), Dr. Maya Lin (`@DataScientist`) | Code implementation, SQL generation, project tracker updates, data pipeline transformations. |
| **Tier 3: Specialized Domain** | Domain-Tuned / Structured | Gemini 3.8 Flash, GPT-4o-mini | Isabelle Renaud (`@Tourism`), Mateo Valenzuela (`@Venture`), Ariella Stern (`@Virtuoso`), Soren Lindqvist (`@Design`) | Structured rubric scoring, Lean Canvas iterations, slide outline schemas, itinerary mapping. |
| **Tier 4: Lightweight / Utility** | Ultra-Fast / Low Latency | Gemini Flash Lite, Haiku 3.5 | Memoria (`@Scribe`), Prof. Elara Whitfield (`@Coach`) | Markdown formatting, text linting, APA 7 citation audits, changelog formatting. |

---

## 4. Context Engineering & Memory Architecture

To prevent context drift and eliminate hallucinations across multi-turn sessions, the architecture implements a **Deterministic Tri-Store Memory Hierarchy**:

```
                                  CONVERSATION INPUT
                                          │
                                          ▼
                         ┌──────────────────────────────────┐
                         │      SESSION CONTEXT WINDOW      │
                         │   (Dynamic Ingestion / Active)   │
                         └────────────────┬─────────────────┘
                                          │
                  ┌───────────────────────┼───────────────────────┐
                  ▼                       ▼                       ▼
      ┌───────────────────────┐ ┌───────────────────┐ ┌───────────────────────┐
      │   EPISODIC TRACKER    │ │  SEMANTIC MEMORY  │ │   AUDIT TRAIL STORE   │
      │   PROJECT_TRACKER.md  │ │     MEMORY.md     │ │     CHANGE_LOG.md     │
      │  (Rule 28 — Active)   │ │  (Stable Profile) │ │  (Immutable History)  │
      └───────────────────────┘ └───────────────────┘ └───────────────────────┘
```

1. **Episodic Execution Layer (`PROJECT_TRACKER.md`):** Manages volatile, session-to-session tasks, decisions, questions, and backlog items. Solved items are archived immediately to prevent token bloat.
2. **Semantic Knowledge Layer (`MEMORY.md`):** Stores durable facts—Guillermo's GPA, academic records, career targets, key contacts, and codified decisions.
3. **Audit Verification Layer (`CHANGE_LOG.md`):** An append-only, chronologically indexed ledger recording every structural change, persona modification, and framework ingestion.

---

## 5. Tool Integration & Model Context Protocol (MCP) Design

### 5.1 Local vs. Remote Tool Integration
The architecture strictly enforces **Permissions-over-Instructions (Rule 30)**:
* Hard access controls (scopes, accounts, API keys) dictate tool capabilities—not prompt instructions.
* Tools are registered with explicit JSON schemas and run inside sandboxed subprocesses.

### 5.2 External AI Accessibility via MCP Bridge
To expose the AI Team knowledge base and persona council to external AI agents (e.g., cloud Copilot, mobile Gemini, web ChatGPT) without requiring local disk access, the architecture defines the **`ai-team-mcp` Sidecar Interface**:

```
   [External AI Client] (Copilot / Web Gemini / ChatGPT)
             │
             │ HTTPS / SSE / stdio
             ▼
   ┌────────────────────────────────────────────────────────┐
   │             AI-TEAM MCP SERVER (Bridge)                │
   │  • Endpoints: `get_persona`, `query_knowledge`         │
   │  • Authentication: Bearer Token / Role-Based Scopes    │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │         LOCAL REPOSITORY STORE (Sanitized)             │
   │   `personas/*.md`  |  `knowledge_bases/*.md`           │
   └────────────────────────────────────────────────────────┘
```

* **Core MCP Tools Exposed:**
  * `list_personas()`: Returns the 31-persona roster and triggers.
  * `summon_persona(persona_id, query)`: Retrieves specialized domain guidance.
  * `search_knowledge_base(topic)`: Returns semantic chunks from curated knowledge bases.
  * `get_project_status()`: Returns active items from `PROJECT_TRACKER.md`.

---

## 6. Security, Reliability & Quality Assurance

1. **Independent CI Gatekeeper:** Dr. Kenji Nakamura (`@AIGov` / `@Auditor`) conducts automated code and document reviews against ISO/IEC 25010 standards prior to commit.
2. **Model Stability Check:** Before any build or workflow execution, models and versions are audited (pinned vs. vendor-managed) with redundant failovers identified.
3. **Automated Git Synchronization (Rule 32):** Ingress auto-pull (`git pull --rebase`) and egress auto-commit/push with semantic tags (`[C-XXX]`, `[KL-XXX]`) preserve state synchronization across devices.

---

*Authored by Adrian Torres, TOGAF (`@Tech`) & Tariq Al-Mansoor (`@DataEngineer`). Canonical specification maintained under version control.*
