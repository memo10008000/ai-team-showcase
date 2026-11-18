# 🛡️ AI_GOVERNANCE_AND_ETHICS.md — AI Governance, Ethics & Compliance Framework
**Document ID:** GOV-ETH-001  
**Version:** 1.0  
**Effective Date:** November 2026  
**Lead Authors:** Dr. Kenji Nakamura, Ph.D. (Persona 08 — AI Governance & Independent Auditor) & Dr. Amara Osei, J.D. (Persona 05 — Ethics & Corporate Law)  
**Approved By:** Guillermo Granillo (Executive Coordinator & Decision Authority)  

---

## 1. Executive Statement & Scope

This framework establishes the operational governance, regulatory compliance, and ethical operating policies for Guillermo Granillo's **AI Virtual Advisory Team**. 

As enterprise AI adoption transitions from speculative experimentation to regulated business operations, this team serves as a production benchmark for **Responsible, Transparent, and Governed Co-Intelligence**. The framework maps directly to international standards (**ISO/IEC 42001**, **NIST AI RMF 1.0**), Canadian privacy legislation (**BC PIPA**, **PIPEDA**, **Bill C-27 / AIDA**), and Indigenous Data Sovereignty (**First Nations OCAP® Principles**).

---

## 2. Regulatory Alignment & Compliance Matrix

| Standard / Law | Scope & Mandate | Implementation in AI Team Operations | Verification Owner |
|---|---|---|---|
| **ISO/IEC 42001:2023** | Artificial Intelligence Management System (AIMS) | Structured lifecycle governance, documented persona roles, risk assessment, change control (`CHANGE_LOG.md`). | Dr. Kenji Nakamura (08) |
| **NIST AI RMF 1.0** | AI Risk Management Framework (Govern, Map, Measure, Manage) | Continuous bias testing, hallucination cross-checks against NotebookLM sources, vulnerability tracking. | Dr. Rafael Montoya (12) & Dr. Kenji Nakamura (08) |
| **BC PIPA & PIPEDA** | Personal Information Protection Act (British Columbia) | Zero storage of confidential 3rd-party PII; strict local data isolation; sanitized public showcase standards. | Dr. Amara Osei (05) |
| **First Nations OCAP®** | Ownership, Control, Access, Possession (Indigenous Data) | **Rule 20 (Ethical Research Pivot):** Strict decoupling of unsolicited policy prescriptions on Indigenous lands without authentic co-design. | Dr. Amara Osei (05) & Dr. Rosalind Vance (18) |
| **EU AI Act / AIDA** | Risk Classification & High-Risk AI System Safeguards | Classification of advisory outputs as Low/Medium Risk decision-support with mandatory human oversight. | Dr. Kenji Nakamura (08) |

---

## 3. The Human-in-the-Loop (HITL) Authority Model

The core tenet of this governance model is that **AI personas possess advisory privilege, never executive authority**.

```
   ┌────────────────────────────────────────────────────────┐
   │                  AI TEAM ADVISORY COUNCIL              │
   │  • Multi-perspective analysis    • Draft generation    │
   │  • Risk identification           • Model predictions   │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ▼ [Advisory Output Only]
   ┌────────────────────────────────────────────────────────┐
   │             MANDATORY HUMAN-IN-THE-LOOP GATE           │
   │             (Guillermo Granillo Sign-Off)              │
   └───────────────────────────┬────────────────────────────┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
    [APPROVED & EXECUTED]            [REVISED / REJECTED]
```

### Core HITL Safeguards
1. **No Autonomous Commits to Third Parties:** No persona or automated script may send emails, publish social posts, or submit documents to employers, academic portals, or clients without Guillermo's explicit sign-off.
2. **Financial & Legal Isolation:** Personas provide financial modeling and legal risk reviews, but have zero programmatic access to financial accounts, credit cards, or legal signature instruments.
3. **Kill Switch & Override Mandate:** Guillermo can instantly terminate, silence, or override any persona, workflow, or background task at any time.

---

## 4. Permissions-over-Instructions Standard (Rule 30)

Prompts are not security boundaries. Relying solely on system prompt instructions (e.g., *"Do not delete files"*) is architecturally flawed. The team enforces **Rule 30 (Permissions-over-Instructions — PoI)**:

1. **Access-Layer Hard Limits:** Boundaries are enforced via execution sandboxes, filesystem permissions, scoped API tokens, and command timeouts.
2. **The "Must Not" Test:** If an agent *must not* access private files, those files are physically excluded from the tool environment or placed in `.gitignore`—never just hidden by prompt requests.
3. **Five-Part Job Card Standard:** Every autonomous task or subagent is scoped with:
   * **Job:** Precise functional outcome.
   * **Tools:** Strict whitelist of necessary tools.
   * **Rules:** Explicit operational bounds.
   * **Approval:** Named human checkpoint for irreversible actions.
   * **Report:** Standardized completion log.
4. **Model Stability Check:** Pinned vs. vendor-managed model versions are logged, redundant fallbacks established, and regression plans enacted after platform updates.

---

## 5. Indigenous Data Sovereignty & OCAP® Protocol (Rule 20)

When research or advisory work touches First Nations, Métis, or Inuit territories, communities, or ecological knowledge:

1. **The Four OCAP® Pillars:**
   * **Ownership:** Cultural knowledge and community data belong exclusively to the First Nation.
   * **Control:** First Nations communities must control research design and data usage.
   * **Access:** First Nations have the right to access and manage information about their peoples.
   * **Possession:** Physical stewardship of data should reside within community governance.
2. **The Ethical Research Pivot Protocol:**
   * Non-Indigenous researchers must **never publish unsolicited policy recommendations, land classifications, or regulatory mandates** over Indigenous lands without authentic co-authorship and formal partnership.
   * If regional open data (e.g. GBIF, Open-Meteo) covers traditional territories, researchers must decouple unsolicited policy prescriptions and refocus strictly on biophysical/spatial science, including a respectful territorial acknowledgement without claiming jurisdictional authority.

---

## 6. Algorithmic Integrity & Hallucination Prevention

To guarantee scholarly and executive credibility:

1. **Source Grounding Invariant:** Every factual assertion must link to an indexed NotebookLM source (38 notebooks / 1,056+ sources) or a verified external database listed in `AUTHORIZED_DATABASES.md`.
2. **Deficiencies Scaffolding (Creswell 4th Ed):** Academic drafts follow Creswell's 5-part deficiency model:
   $$\text{Problem} \longrightarrow \text{Past Studies} \longrightarrow \text{Deficiencies} \longrightarrow \text{Stakeholder Significance} \longrightarrow \text{Purpose Statement}$$
3. **Plain-Language Text Audit (Rule 31):** Every public post, article, or executive brief is reviewed by Prof. Elara Whitfield (15) to eliminate double negatives, obscure jargon, and ungrounded claims.

---

*Authored by Dr. Kenji Nakamura, Ph.D. (`@AIGov`) & Dr. Amara Osei, J.D. (`@Ethics`). Canonical compliance document maintained under version control.*
