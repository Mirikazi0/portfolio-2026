# Making Interview Query's Value Obvious in 10 Seconds

> **Outcome:** Redesigned the onboarding and pricing experience to show personalized value before the paywall — driving a **+19% conversion lift** and **+12% increase in revenue per user**.

---

## 1. The Problem

Interview Query helps data professionals (data scientists, analysts, ML engineers) prepare for technical job interviews. 

Even with steady incoming traffic, visitors were dropping off right before buying. Two main friction points were causing the drop:

1. **A cold, generic sign-up:** Users had to create an account before seeing anything useful. A candidate cramming for a FAANG Data Scientist interview saw the exact same generic screen as an entry-level analyst.
2. **Pricing tier confusion:** Visitors couldn't tell the difference between *IQ Coder* ($29/mo) and *IQ Premium* ($79/mo) in under 10 seconds. High-value Yearly plans were buried, and coaching was split into separate cards that competed with the main subscription.

---

## 2. The Before

The original experience forced users to make a buying decision without proving relevance first:

- **Legacy Sign-Up:** A standard blank form that asked for credentials before showing any product value.  
  *Image: `04_Assets/Images/[Sign Up] Before.png`*
- **Legacy Pricing Page:** Three disconnected cards with confusing feature overlap and no clear visual anchor.  
  *Image: `04_Assets/Images/[Interview Query] Old Pricing.png`

---

## 3. The Core Decisions (And Why)

### Decision 1: Show a tailored plan *before* asking for payment
Instead of a generic registration form, I designed a 3-step intake wizard:
1. Select target role (Data Analyst, Data Scientist, ML Engineer)
2. Select target companies (FAANG, Startups, Fintech)
3. Select experience level & interview timeline

> **Why:** Candidates don't buy prep tools out of general curiosity — they buy because they have an urgent interview coming up. Showing an auto-generated study plan tailored to their target company gave them immediate perceived value and confidence before seeing the pricing page.

### Decision 2: Default to Yearly savings and use "Limited" badges
On the pricing page, I made three specific adjustments:
- **Defaulted to the Yearly tab ("Save up to 79%"):** Re-anchored the perceived cost of Premium from $79/mo down to $17/mo (billed yearly).
- **Used amber "Limited" badges instead of red Xs:** For the cheaper Coder plan, features like Case Studies and AI Interviews were marked "Limited" rather than omitted.
- **Embedded coaching as an inline selector:** Added a radio toggle inside the Premium card (+1 session for $21/mo, +3 sessions for $50/mo) instead of a separate competing card.

> **Why:** Red `X` marks feel punitive, while omitting features leaves users guessing. Amber "Limited" badges showed candidates they would hit a ceiling during intense interview prep, making Premium feel like the natural, high-value choice.

---

## 4. The After

The redesigned flow turns a dead-end signup into a guided, high-confidence conversion path:

- **Redesigned Onboarding:** An interactive assessment that builds a custom curriculum preview in under 30 seconds.  
  *Image: `04_Assets/Images/[Sign Up] After.png`*
- **Redesigned Pricing:** Two clear cards above the fold, an inline coaching selector, and a side-by-side comparison table below.  
  *Image: `04_Assets/Images/[Interview Query] New Pricing.png`

---

## 5. What Was Measured (And What Would Prove Me Wrong)

**What we measured:**
- Pricing-to-checkout conversion rate
- Revenue per user (ARPU / LTV)
- 1st-week question engagement for onboarding completers

```
┌───────────────────────────────┬───────────────────────────────┐
│     OVERALL CONVERSION        │       REVENUE PER USER        │
│            +19%               │             +12%              │
│  (Pricing Page -> Checkout)   │  (Higher Yearly & Lifetime)   │
└───────────────────────────────┴───────────────────────────────┘
```

> **What would have proved me wrong:**  
> If checkout conversion went up but revenue per user went down, it would have meant users were panic-buying the cheap Coder plan because of the savings badges. Instead, revenue per user grew by +12%, confirming that users understood the value of Premium and annual commitments.

---

## 6. Project Scope & Role

**Shipped project.**  
**Role:** Product Designer.  
**Responsibilities:** User research teardowns, flow mapping, Figma wireframes & high-fidelity UI, copy, and design handoff to the engineering team.
