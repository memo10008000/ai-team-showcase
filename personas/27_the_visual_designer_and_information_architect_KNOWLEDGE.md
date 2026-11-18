# Knowledge Brief — Soren Lindqvist, M.Des., RGD, CPACC (Persona 27)
**Role:** The Visual Designer & Information Architect  
**Summon:** `@Design` / `@Visual` / `@Designer`  
**Master Knowledge Base:** [`DESIGN_visual_communication_summaries.md`](https://github.com/memo10008000/ai-team-showcase)  
**NotebookLM Source:** `DESIGN-Visual-Communication-and-Information-Architecture`  
**Version:** 1.0 (October 2026)

---

## I. Operational Knowledge Foundations

This knowledge brief arms Soren with actionable design mathematics, color perception formulas, slide architecture rules, and AI image prompting patterns.

### 1. Mathematical Contrast & Accessibility Formulas

#### Relative Luminance ($L$)
For any sRGB color with normalized red, green, and blue components ($R, G, B \in [0, 1]$):
$$R_s = \begin{cases} \frac{R}{12.92} & \text{if } R \le 0.04045 \\ \left(\frac{R + 0.055}{1.055}\right)^{2.4} & \text{if } R > 0.04045 \end{cases}$$
$$(G_s \text{ and } B_s \text{ calculated identically})$$
$$L = 0.2126 \cdot R_s + 0.7152 \cdot G_s + 0.0722 \cdot B_s$$

#### Contrast Ratio ($CR$)
$$\text{CR} = \frac{L_1 + 0.05}{L_2 + 0.05} \quad (L_1 > L_2)$$
* **Text Compliance Rule:** If $\text{CR} < 4.5:1$, it fails WCAG 2.1 AA for body text.
* **UI & Diagram Rule:** If $\text{CR} < 3.0:1$, box borders, flowchart lines, and icons fail WCAG 2.1 AA.

---

## II. Practical Visual Archetypes & Solutions to Common Pain Points

### Pain Point 1: Diagrams Inconsistent Across Dark and Light Themes
* **Root Cause (Simultaneous Contrast):** Light themes reflect far more ambient white light into the retina, making thin lines and low-contrast borders appear to vanish, while dark themes emit less light, making faint colored borders pop out luminous.
* **Soren's Fix:**
  * In **Dark Mode**: Use 1px borders with subtle glow or 20–30% opacity tints (`#334155`).
  * In **Light Mode**: Double the border stroke weight to 1.5px or 2px, and darken the stroke color to `#CBD5E1` or `#94A3B8` so the box structure holds firm. Never drop container borders below a 3.0:1 contrast ratio against the background.

### Pain Point 2: Presentation Slides Overloaded with Text and Bullet Points
* **Root Cause (TelePrompter Syndrome):** Presenters use slides to remember what to say instead of using slides to focus audience attention.
* **Soren's Fix (The Duarte 3-Part Architecture):**
  1. *Action Headline (Top 15%):* Single bold sentence stating the conclusion.
  2. *Visual Centerpiece (Middle 70%):* 2 to 3 comparative cards, a clean diagram, or a single hero metric callout with 1–2 lines of supporting evidence.
  3. *Anchor Metadata (Bottom 15%):* Source citation, methodology note, or date.
  * *Word Count Ceiling:* Never exceed 30–40 words total per executive slide.

### Pain Point 3: GenAI Images Producing Cluttered, Clashing, or Hallucinated Visuals
* **Root Cause (Vague Prompting):** Using adjectives like "futuristic", "hyperrealistic", or "amazing" prompts the diffusion model to inject hyper-saturated lighting, random neon streaks, and illegible pseudo-text.
* **Soren's Fix (The Parameter Lock):**
  * Lock down the **lighting style**: "soft diffused north-facing studio box lighting, subtle ambient occlusion, no harsh reflections."
  * Lock down the **palette**: "strict restricted palette: slate navy #0F172A, warm ochre #D97706, and ivory negative space."
  * Lock down the **negative prompt**: "text, typography, watermarks, signatures, blurry artifacts, chaotic gradients, drop shadows, busy backgrounds."

---

## III. Ready-to-Use Master Color Palettes

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. EXECUTIVE TECH & ENTERPRISE ARCHITECTURE                            │
│ Dark:  [#0F172A Base]  [#1E293B Card]  [#38BDF8 Accent]  [#F59E0B Alert]│
│ Light: [#F8FAFC Base]  [#FFFFFF Card]  [#0284C7 Accent]  [#D97706 Alert]│
├────────────────────────────────────────────────────────────────────────┤
│ 2. SCIENTIFIC & OKABE-ITO ACCESSIBLE (CVD SAFE)                        │
│ [#000000 Black]   [#E69F00 Orange]   [#56B4E9 SkyBlue]  [#009E73 Green]│
│ [#F0E442 Yellow]  [#0072B2 Blue]     [#D55E00 Vermil]   [#CC79A7 Purple]│
├────────────────────────────────────────────────────────────────────────┤
│ 3. REV VENTURE CATALYST & CIVIC INNOVATION (WESTSHORE)                 │
│ [#064E3B Pine]    [#0F766E Teal]     [#D97706 Amber]    [#FDFBF7 Cream] │
├────────────────────────────────────────────────────────────────────────┤
│ 4. SUSTAINABLE TOURISM & LIVING SYSTEMS (TRMN506)                      │
│ [#1B4332 Canopy]  [#2D6A4F Fern]     [#BC6C25 Earth]    [#2A9D8F Teal]  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## IV. Operational Red Flags & Immediate Mitigations

| Visual Defect Observed | Underlying Design Error | Soren's Mandatory Intervention |
|---|---|---|
| **Vibrating Container Borders** | $1+1=3$ noise effect (Tufte); dark borders placed too close together | Remove borders entirely; distinguish containers with a subtle 3% background tint shift or increase whitespace padding. |
| **Rainbow Syndrome** | Using 5+ distinct bright colors across a diagram or slide | Enforce Stephen Few’s 85/15 rule: desaturate 85% of elements to cool slates/grays; preserve saturated chroma strictly for the 1–2 target nodes. |
| **Invisible Light-Mode Boxes** | Simultaneous contrast fallacy; pasting pastel dark-mode boxes onto white background | Darken card border stroke to `#CBD5E1` (1.5px) and set inner card fill to pure white `#FFFFFF` over an off-white `#F8FAFC` canvas. |
| **Status Shown by Color Alone** | Violates WCAG 2.1 Double-Encoding Rule and excludes CVD viewers | Attach a text pill badge (`[PASS]`, `[FAIL]`) or distinct geometric shape (circle, diamond, triangle) to every status indicator. |
| **Cluttered Slide Presentation** | Fails Nancy Duarte’s 3-Second Glance Test; audience reading instead of listening | Split content across multiple slides; elevate main takeaway into an Action Headline; reduce body copy to 3 bullets maximum. |
