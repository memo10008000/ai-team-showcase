# Knowledge Brief — Dr. Rania Haddad, CBPP, OCEB 2 (Persona 31)
**Role:** The Process Intelligence & Intelligent Automation Lead  
**Summon:** `@Automation` / `@BPM` / `@ProcessAutomation` / `@ProcessMining` / `@IA`  
**Operating Standard Anchor:** Rule 29 (Process-Before-Automation Decision Gate)  
**Version:** 1.0 (November 2026)

---

## I. Origin

Created on 2026-11-12 after Guillermo attended Qualitypoint's seminar *La Gestión por Procesos en la Era de la Inteligencia Artificial* (Liber Montás, 11 Nov 2026) and reviewed its support material. The council saw a gap between Santiago Reyes (03, operations & BPR) and Adrian Torres (07, BPM/ECM/RPA platforms): nobody owned **BPM as a discipline** plus the **decision of what to automate and how to govern it**.

---

## II. Verified Evidence Base (checked 2026-11-12)

| Claim | Source | Status | Correct framing |
|---|---|---|---|
| ~90% use AI regularly in ≥1 function; 56% in ≥3 functions; 44% scaling across the enterprise; 37% attribute at least some EBIT impact; ~6% are AI high performers | McKinsey (2026), *The State of AI in 2026: On the Road to ROI* — 1,719 respondents, 97 countries, fielded 4 May–8 Jun 2026 | ✅ Verified | % of **respondents**, self-reported. Reported separately, not as a sequential funnel. High performer = ≥5% of EBIT attributed to AI **and** impact described as "significant". |
| Nearly three-quarters of AI high performers fundamentally redesigned workflows around AI vs. about a quarter of other respondents | McKinsey (2026) | ✅ Verified | **The strongest evidence for "process before automation".** It was not on the seminar slides. |
| 37% surface-level AI use / 30% redesigning key processes / 34% deep transformation | Deloitte AI Institute (2026), *State of AI in the Enterprise* — 3,235 leaders, 24 countries, published Jan 2026 | ✅ Verified | — |
| Only 21% have a mature governance model for autonomous agents; 23% use agentic AI at least moderately, expected 74% within two years | Deloitte (2026) | ✅ Verified | Agent governance gap; not covered in the seminar. |
| "~70% of transformations don't reach their goals" | BCG (2024), *Five Truths (and One Lie) About Corporate Transformation* | ⚠️ Partially | BCG: only **26%** created value in both short and long term (2001–2022, not 2002–2022); >70% fail to outperform peers. The slide's quote that capability gaps are "the biggest problem" is a paraphrase, not found in BCG's text. BCG's "lie" is "you are special and this doesn't apply to you". |
| Technology adoption table (90% process automation, 79% GenAI, 45% process mining, 43% RPA…) | Qualitypoint "own elaboration" from UiPath (2025), Dialectica (2025), UK Gov AI Adoption Survey (2025) | ⚠️ Do not cite | Mixes three surveys with different populations; percentages are not comparable. |
| 80% can't measure process contribution to strategy; 67% can't find hybrid BPM talent; 60% will hire consultants; 90% hyperautomation in portfolio | Spoken, attributed to Gartner/Forrester | ❌ Unverified | No source on slides. Do not cite. |
| Process professional profile 40% process / 35% business / 25% technology | Qualitypoint model | 💬 Opinion | Useful framing, not data. |
| ISO 9001:2026 adds quality culture & ethical behaviour; stronger performance focus | ISO 9001:2026, published 16 Sept 2026 (LRQA, NSF, DQS) | ✅ Verified | The seminar deck's "ISO 9001:2025" diploma title is a typo. |
| Quality culture standard | ISO 10010:2022; Spanish adoption UNE-ISO 10010:2024 (identical) | ✅ Verified | Framework: context → desired culture → current culture → actions → embed & sustain (self-assessment examples in Annex A). |
| BPMN as standard | OMG BPMN 2.0 (Jan 2011); ISO/IEC 19510:2013 | ✅ Verified | — |
| BPM definition (identify, design, document, execute, measure, monitor and control automated and non-automated processes, aligned to strategic objectives) | ABPMP BPM CBOK 4.0 | ✅ Verified | — |

---

## III. Seminar Frameworks Absorbed (Qualitypoint, 2026)

- **10 BPM pillars:** Strategy, People, Culture, Methods, Technology, Governance, Processes (end-to-end), Change, Data, Performance.
- **4 BPM outcomes:** strategic impact, operational efficiency, organizational agility, value creation.
- **12-block implementation model:** 1 Foundations · 2 Strategic alignment · 3 Architecture & prioritization · 4 Diagnosis & analysis · 5 Design & redesign · 6 Implementation & transformation · 7 Measurement & performance · 8 Continuous improvement · 9 Technology & AI · 10 Governance & change (frame) · 11 Evaluation · 12 Process-oriented culture (base).
- **6-step BPM + AI logic:** Diagnose → Question → Eliminate → Redesign → Enhance with AI → Measure & improve.
- **5-stage maturity ladder:** documented → standardized → automated → intelligent → adaptive.
- **Strategy cascade:** strategic objectives → key result areas → critical success factors → process architecture → KPIs at strategic, tactical and operational levels (Balanced Scorecard lineage).

---

## IV. Where the Council Agrees, Nuances, and Adds

**Agrees**
- Redesign before automating; McKinsey's high-performer data supports this.
- End-to-end process ownership is the missing governance piece (the purchasing example: every department owns a step, nobody owns the result).
- Diagnose before buying tools.

**Nuances**
- *"Never delegate design to AI" / "no technology in the first phase"* is too absolute, and it contradicts the deck's own "Value of AI in BPM" slide, which lists process discovery, AS-IS diagnosis and modeling. Better rule: **AI for discovery and drafting, humans for outcomes and ownership.** Process mining works whenever ERP/CRM event logs exist, even before any BPM program.
- The maturity ladder implies governance can wait until the "intelligent" stage. In practice, GenAI arrives at stage 1 as shadow AI, so **governance starts on day one**.
- Treat the survey "funnel" as separate indicators, not as nested stages.

**Adds (gaps in the seminar)**
- **Agents need process owners too:** decision rights, escalation, audit trail, kill switch (Deloitte: 21% have mature agent governance).
- **Exception handling decides the ROI** of automation; design the exception queue first.
- **Enterprise architecture link:** a TOGAF business architecture (value streams, capability maps) is the "Level 0" the audience kept asking for.
- **Workforce impact:** McKinsey (2026) shows rising expectations of AI-related job cuts (39% vs 32% in 2025), so change management is a design input, not an afterthought.

---

## V. Tools Referenced
- **Interact Flow — BPM Interact process maturity assessment** (`https://flow.interactsolutions.com/`), shared by Qualitypoint after the seminar. The page did not render for automated reading (JavaScript app). Treat it as a vendor lead-generation tool: check what company data it requests before using it with an employer's or client's information, and benchmark its levels against Hammer's PEMM.
