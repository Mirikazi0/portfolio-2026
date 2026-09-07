# Storytelling Plan: Applying Zeel Shah's Framework to Our Case Studies

> **Reference:** `02_Research/Inspiration/Zeel_Shah_Walmart_Africa_Case_Study_Deep_Dive.md`  
> **Goal:** Elevate both case studies from "task-based portfolios" into evidence-led, senior-level product storytelling.

---

## The 6 Zeel Shah Storytelling Patterns We're Borrowing

| Pattern | Zeel Shah Used It As | We Apply It As |
| :--- | :--- | :--- |
| **1. Behavioral Shift Headline** | `From scrolling to shopping.` | Outcome-first, verb-driven title |
| **2. "What this project was and wasn't"** | Enterprise reality & honest scope | Collaborative framing, PM + Designer roles |
| **3. Vanity vs. Value Data Hook** | `49% engaged. 6% shopping.` | Contrast a surface metric with a broken outcome |
| **4. "Before Figma" work** | Power BI exports, Vibey tokens in VS Code | Competitor teardowns, user interviews, copy architecture |
| **5. Component / Evidence Audit** | `EARNS ITS SPOT` vs `LOW CONTRIBUTION` | Section/feature audit with rationale |
| **6. Research Implications** | 5 design principles from competitive synthesis | Design decisions traced back to evidence |

---

## CASE STUDY 1: Interview Query

### The Headline
> **Old:** `Making Interview Query's Value Obvious in 10 Seconds`  
> **New direction:** `From browsing plans to buying one.`  
> *(Captures the same behavioral shift language as "From scrolling to shopping.")*

---

### Section 1: "What this project was and wasn't"
This is where we set expectations honestly and signal cross-functional maturity.

**Draft:**
> My PM brought me a brief: the pricing page wasn't converting the way it should. The sign-up flow was cold. But at a product like Interview Query — one that runs real A/B tests and tracks revenue down to the billing interval — redesigning these flows doesn't get approved on gut feeling. It gets approved on evidence.
>
> So before I opened Figma, I went looking for the case. I ran competitor teardowns on DataLemur, Exponent, and LeetCode. I interviewed users about where they felt uncertain. The PM ran the A/B test architecture. I ran the design.
>
> Most of the shaping work — the competitor breakdowns, the user intent mapping, the tier hierarchy logic — happened before any visual file existed.

**Scope attribution (honest):**
- **I did:** Competitor teardowns, user interviews, information architecture, Figma UI design, copy, pricing hierarchy, coaching add-on interaction design
- **PM did:** A/B test spec (`pricing_page_redesign_v1`), experiment tracking, metrics definition
- **Together:** Problem definition, solution direction

---

### Section 2: The Problem (Vanity vs. Value Hook)
We don't have a hard before metric — so we frame it the way Zeel would: with the structural contradiction.

**Big typographic hook:**
```
Users found the pricing page.
They just couldn't read it.
```

Or more pointed:
```
Two plans.
Zero clarity.
```

**Narrative:**
> Interview Query had two subscription tiers: IQ Coder and IQ Premium. The page existed. Traffic was coming. But users couldn't tell the difference between the plans fast enough to act.
>
> Key features were buried. Long-term plans (Yearly and Lifetime) weren't surfaced. Coaching was a third card competing with the main tiers. The sign-up flow showed the same generic screen to a senior FAANG candidate and an entry-level analyst.
>
> Users were showing up ready to decide. The page wasn't ready to help them.

---

### Section 3: The Evidence — What We Found Before Designing
This mirrors Zeel's "The Evidence" component audit.

**Competitor breakdown (3 columns, card format):**

| Platform | What They Did Right | Design Implication |
| :--- | :--- | :--- |
| **DataLemur** | Clear single-tier "Pro" vs free, no confusion | Fewer tiers = faster decision |
| **Exponent** | "Most Popular" badge + savings callout prominent above fold | Anchor the recommended tier visually |
| **LeetCode** | Feature comparison table directly below pricing cards | Comparison reduces doubt, doesn't add friction |

**User interview signal:**
> Candidates kept asking the same question: *"Do I need Premium or is Coder enough for a FAANG prep?"* The tier names gave no answer. The feature list was too long to scan. They were guessing.

---

### Section 4: The Design Implications (Our Version of Zeel's 5 Principles)

**Four decisions from the research:**

1. **People buy for their goal, not for a feature list.**  
   Reframe each tier around what it gets you (FAANG prep, company-specific guides) not what's technically included.
2. **Default to the plan that wins.**  
   Yearly tab as the default. Users anchor on the first number they see — make that number `$17/mo`, not `$79/mo`.
3. **Add-ons should extend a decision, not force a new one.**  
   Coaching as a radio selector inside Premium means users decide once, not twice.
4. **Show candidates what they'll hit before they hit it.**  
   Amber "Limited" badges on Coder features signal the ceiling without punishing the tier.

---

### Impact (Keep it simple, attribute it honestly)

```
+19%   Pricing → Checkout Conversion
+12%   Revenue per Subscribed User
```

> *Self-note for interviews: These numbers came from the A/B test post-launch. The test spec was written by the PM. The design decisions that produced them were mine.*

---

---

## CASE STUDY 2: Lesson Planner PH

### The Headline
> **Old:** `Designing a Zero-to-One Landing Experience for Lesson Planner PH`  
> **New direction:** `From a product nobody could explain to one that opened doors.`  
> *(Zero-to-one + clarity + real-world outcome in one line.)*

---

### Section 1: "What this project was and wasn't"
This is where Lesson Planner PH's story gets *especially* strong — because the constraints were wider than Interview Query. The brief was essentially: *"Here's the product. Make people get it."*

**Draft:**
> The brief I was handed was three words: *highlight the value.* No wireframes. No existing website. No reference UI. Just a product that helped Filipino teachers generate lesson plans in minutes — and a team that needed the world to understand why that mattered.
>
> What this meant in practice: I had to figure out the architecture before the aesthetics. I had to decide what story to tell, in what order, for two completely different audiences — individual teachers and school administrators — without losing either of them.
>
> I started with structure. I wireframed the narrative sequence, presented it to the PM and engineers, iterated on copy and flow through one round of feedback, and then moved into high-fidelity design.

**Scope attribution (honest):**
- **I did:** Full narrative architecture, wireframing, stakeholder presentation, Figma design, responsive UI, copy
- **Engineers did:** Technical implementation, product direction
- **Constraint given:** "Highlight the value" — everything else was my call

---

### Section 2: The Problem (The Invisible Product Problem)
This case study doesn't have a funnel metric. Its tension is different: **the product existed but nobody outside the team could explain it.**

**Typographic hook:**
```
A product that worked.
A page that didn't exist.
```

**Narrative:**
> Lesson Planner PH was already helping teachers generate structured lesson plans faster. The problem wasn't the product. The problem was that without a landing page, non-teaching users — administrators, institutional buyers, international visitors — had no way to understand what it was, why it mattered, or whether to trust it.
>
> The landing page had to do two jobs simultaneously: give individual teachers an emotional reason to try it, and give institutions a rational reason to recommend it.

---

### Section 3: The Audience Tension (Our Version of the "Evidence" Section)
Instead of a component audit, this case study's "evidence" is the dual-audience architecture problem.

**Two audiences. One page. Different jobs:**

| Audience | Primary Need | What Fails Them on Generic Pages |
| :--- | :--- | :--- |
| **Filipino Teachers** | *"Will this actually save me time?"* | Tech jargon, feature lists, no emotional hook |
| **School Administrators** | *"Can we trust this for our institution?"* | Informal tone, no compliance signals, no contact path |

**The structural decision:**
> I built a 4-stage narrative sequence: problem acknowledgment → how-it-works → proof → dual CTA. The sequence had to earn teacher trust first, then institutional credibility second — because administrators follow teacher adoption, not the other way around.

---

### Section 4: Design Implications (3 Principles)

1. **Lead with the problem, not the product.**  
   "Your Sunday nights back" lands harder than "AI-powered lesson planning." Teachers don't buy tools — they buy relief.
2. **Structure before aesthetics.**  
   Every wireframe review meeting was about information flow, not visual style. The copy and sequence were locked before a single color was chosen.
3. **Framing outcomes serves both audiences.**  
   Saying "compliant with DepEd standards" serves the institution. Saying "done in minutes" serves the teacher. The same design can do both without compromising either.

---

### Impact (Lead with the Qualitative — It's Stronger Here)

> After launch, the engineering team shared direct feedback:
>
> *"It makes it tremendously easier for non-teaching users to know what the product is about and see the relevant impact in metrics, testimonials, and events."*
>
> *"This makes it easier for facilitating discussions b2b and other kinds of stakeholders."*
>
> *"Also helpful to cater to folks that discover this platform — we have international users as well."*

> The page became the foundation for early B2B outreach, institutional conversations, and international discovery — none of which existed before it shipped.

---

## Implementation Priority

| Task | For Which Case Study | Status |
| :--- | :--- | :--- |
| Rewrite headline to behavioral shift format | Both | 🔲 To Do |
| Add "What this project was and wasn't" section | Both | 🔲 To Do |
| Add vanity vs. value typographic hook | IQ | 🔲 To Do |
| Add invisible product hook | LPPH | 🔲 To Do |
| Add competitor/audience evidence table | Both | 🔲 To Do |
| Add research design implications (3–4 principles) | Both | 🔲 To Do |
| Update HTML files to match | Both | 🔲 To Do |
