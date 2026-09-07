---
version: alpha
name: Webflow Inspired
website: "https://webflow.com"
description: An inspired interpretation of Webflow's design language — a visual web development platform whose surface contrasts a deep near-black `#080808` primary against a generous white canvas, broken by a five-stop chromatic accent system (purple / pink / blue / orange / green) that maps to the brand's product categories, and anchored by the proprietary WF Visual Sans family used at restrained 500 / 600 weights with negative tracking.

seo:
  title: "Webflow Design System for React — #080808 ink, WF Visual Sans, 5-stop palette"
  metaDescription: "Webflow's design system as a DESIGN.md file. Ink black #080808, WF Visual Sans, 9 colors, 16 type styles, 30+ components. For React, Next.js, and AI tools."
  highlights:
    - "Two-colour conversion hierarchy — every primary CTA is `#080808` near-black, never one of the five chromatic accents"
    - "Five-stop category palette — `#7a3dff` purple, `#ed52cb` pink, `#3b89ff` blue, `#ff6b00` orange, `#00d722` green as full surface fills"
    - "Weight ceiling at 600 — proprietary WF Visual Sans Variable carries every display and body role, never heavier than semibold"
    - "Tight 4px button radius — the brand's canonical `{rounded.sm}` geometry; pill CTAs do not exist in the system"
    - "Hero display at 80px / 600 with -0.8px tracking — confident kerning rather than billboard weight"
  tags:
    - "Workflow & No-code"
    - "Design & Creative Tools"
  lastUpdated: "2026-05-12"
  author:
    name: "Dov Azencot"
    url: "https://x.com/dovazencot"
  opening: |
    Webflow's design system reads as a confident professional product, not a tech startup. The default page is a generous white canvas with one decisive ink colour — `#080808` near-black — carrying every primary CTA, every heading, and every wordmark. Around that restrained primary, the brand layers a five-stop chromatic accent palette (purple `#7a3dff`, pink `#ed52cb`, blue `#3b89ff`, orange `#ff6b00`, green `#00d722`) that maps directly to product categories: design, animation, SEO, hosting, ecommerce. These accents appear as full-card surface fills inside the category grid, never as button backgrounds. The proprietary WF Visual Sans family handles every typographic role at weights 500 and 600, with negative tracking on display sizes giving the hero its tight, engineered voice.

    This page captures the system in a single DESIGN.md file built to the Google Labs open specification. Inside: 19 colour tokens (one primary, nine chromatic accents, four text roles, hairlines and canvas), 16 type styles all running WF Visual Sans Variable with Inconsolata as the documented mono fallback, an 8-step spacing scale from 2px to 32px, a five-step radius scale capped at 8px for cards, and 30+ component recipes spanning buttons, cards, hero bands, the five chromatic category cards, badges, inputs, and a kit-mirror block of 10 illustrative example surfaces.

    Feed the file to Claude, Cursor, or GitHub Copilot and the AI produces React components that respect Webflow's discipline — `#080808` CTAs, 4px button corners, the 600 weight ceiling — rather than a generic shadcn theme. The tokens drop straight into Tailwind config or CSS variables. The system is worth studying for one reason: it shows how a brand can be visually distinctive without raising any individual element's voice. The chromatic palette does the heavy lifting on surfaces; the primary stays quiet on actions; the type never climbs past semibold. Restraint as a strategy.
  related:
    - href: "https://github.com/google-labs-code/design.md"
      title: "The DESIGN.md specification"
      description: "Google Labs' open spec for machine-readable design system files — the format this page is built on."
    - href: "/design"
      title: "Browse all design systems"
      description: "The full directory of DESIGN.md files on shadcn.io, with live mockups for each."
    - href: "/blocks"
      title: "React blocks for shadcn/ui"
      description: "Production-ready hero, pricing, CTA, and dashboard sections built with the same Tailwind + shadcn primitives."
  questions:
    - id: "primary-color"
      title: "What is Webflow's primary brand colour?"
      answer: "Webflow's primary is `#080808` — a deep near-black that reads as branded rather than pure-black neutral. It carries every primary CTA, every heading, every wordmark, and serves as the polarity-flipped fill on dark hero bands and dark feature cards. The five chromatic accents (purple `#7a3dff`, pink `#ed52cb`, blue `#3b89ff`, orange `#ff6b00`, green `#00d722`) are never used as button backgrounds — they're surface fills on the product category grid only."
    - id: "typography"
      title: "What typography does Webflow use, and what should I substitute?"
      answer: "Webflow runs the proprietary WF Visual Sans Variable family across every display, body, and label role at weights 400 / 500 / 550 / 600 — the brand never goes heavier than semibold. A monospace variant (WFVisualSans-Mono) handles rare technical caption moments, with Inconsolata as the documented fallback. Inter at weights 400 / 500 / 600 with `font-feature-settings: \"ss01\"` enabled is the closest open-source substitute for the variable sans."
    - id: "five-stop-palette"
      title: "How does the five-stop chromatic accent palette work?"
      answer: "The palette is purple `#7a3dff`, pink `#ed52cb`, blue `#3b89ff`, orange `#ff6b00`, and green `#00d722` — each mapped to a Webflow product category (design / build, animation / interaction, SEO / analytics, hosting / infrastructure, ecommerce / status-success). They appear as full-saturation surface fills on category cards at 32px padding and 8px radius, with white text on every fill except green, which uses ink for legibility. They are not used as button backgrounds, badge fills, or accent strokes."
    - id: "shape-language"
      title: "What is Webflow's shape language?"
      answer: "The radius scale is tight and engineered. Buttons sit at `{rounded.sm}` 4px — neither pill nor square. Cards, hero bands, and category cards step up to `{rounded.md}` 8px. Full pill (`{rounded.full}` 9999px) is reserved exclusively for circular icon containers like carousel controls. The brand never uses pill CTAs, and 0px square corners only appear on full-bleed bands. There are five radius tokens total: 0, 2, 4, 8, 9999."
    - id: "use-in-project"
      title: "Can I use this DESIGN.md to build my own React site?"
      answer: "Yes — the file is structured for AI tools. Feed it to Claude, Cursor, or GitHub Copilot alongside your component prompt, and the model will reproduce Webflow's restraint (near-black CTAs, 4px button corners, semibold weight ceiling) rather than a generic Tailwind palette. Every colour, type style, radius, and spacing value is a quoted token you can paste directly into Tailwind config, CSS variables, or your own component library. The 10 `ex-*` example surfaces at the bottom of the spec show how the same primitives recombine across pricing, auth, modals, toasts, and data tables."
    - id: "known-gaps"
      title: "What's missing from this DESIGN.md spec?"
      answer: "A few things. Hover-state colours are not documented — Webflow's actual `:hover` styling on cards uses subtle elevation lifts that don't extract reliably. Full input error-state combinations and focus-ring specifications are missing. Loading skeletons and progress indicators are not captured. The illustrative `ex-*` surfaces (pricing tier, auth form, modal, toast, etc.) are auto-derived kit-mirror entries — they reference brand-native primitives but were not pixel-extracted from production Webflow pages."

colors:
  primary: "#080808"
  on-primary: "#ffffff"
  ink: "#080808"
  ink-strong: "#222222"
  body: "#363636"
  body-mid: "#5a5a5a"
  mute: "#898989"
  mute-soft: "#ababab"
  hairline: "#d8d8d8"
  canvas: "#ffffff"
  accent-purple: "#7a3dff"
  accent-pink: "#ed52cb"
  accent-blue: "#3b89ff"
  accent-blue-deep: "#006acc"
  accent-blue-info: "#146ef5"
  accent-orange: "#ff6b00"
  accent-green: "#00d722"
  accent-yellow: "#ffae13"
  accent-red: "#ee1d36"

typography:
  display-xxl:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, -apple-system, sans-serif
    fontSize: 80px
    fontWeight: 600
    lineHeight: 83.2px
    letterSpacing: -0.8px
  display-xl:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 56px
    fontWeight: 600
    lineHeight: 58.24px
  display-lg:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 44.8px
    fontWeight: 600
    lineHeight: 46.6px
  display-md:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 500
    lineHeight: 41.6px
  display-sm:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 500
    lineHeight: 31.2px
  display-xs:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 500
    lineHeight: 28px
  eyebrow-uppercase:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 15px
    fontWeight: 500
    lineHeight: 19.5px
    letterSpacing: 1.5px
  eyebrow-uppercase-sm:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 500
    lineHeight: 12px
    letterSpacing: 0.6px
  body-lg:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 28.8px
    fontWeight: 400
    lineHeight: 46.08px
    letterSpacing: -0.288px
  body-md:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 25.6px
    letterSpacing: -0.16px
  body-md-strong:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 25.6px
    letterSpacing: -0.16px
  body-sm:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22.4px
  body-sm-strong:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 22.4px
  caption:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 12.8px
    fontWeight: 550
    lineHeight: 15.36px
  caption-mono:
    fontFamily: WFVisualSans-Mono, Inconsolata, ui-monospace, SFMono-Regular, Menlo, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 18px
  button-md:
    fontFamily: WF Visual Sans Variable, Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 25.6px
    letterSpacing: -0.16px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  button-text-arrow:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "{spacing.xl} 0"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  badge-info:
    backgroundColor: "{colors.accent-blue-info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-info-soft:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue-info}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  card-feature-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  hero-band-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.3xl} {spacing.3xl}"
  category-card-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  category-card-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body-mid}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.2xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---


## Overview

Webflow positions itself as the visual web development platform — the marketing surface reads as a confident professional product, not a tech startup. The default page is a generous white canvas (`{colors.canvas}` — `#ffffff`) with a deep near-black `{colors.primary}` (`#080808`) for the brand's primary CTA, typography, and ink. Around this restrained primary, the brand layers a five-stop chromatic accent system — `{colors.accent-purple}` `#7a3dff`, `{colors.accent-pink}` `#ed52cb`, `{colors.accent-blue}` `#3b89ff`, `{colors.accent-orange}` `#ff6b00`, `{colors.accent-green}` `#00d722` — each mapped to one of the platform's product categories (design, CMS, hosting, ecommerce, etc.). These accents appear as full-card fills inside the product-category grid, not as button colours; the brand's primary CTA stays near-black.

Type carries the second decisive voice. The proprietary `WF Visual Sans Variable` family carries every display, body, and label role at weight 500 / 600 — the brand never goes heavier than semibold, never lighter than regular. Hero display sits at 80 px / weight 600 / `-0.8 px` tracking — confident but not shouting. Uppercase eyebrows in 15 px weight 500 with `1.5 px` positive tracking mark every section header.

The shape system is restrained. Buttons take a tight `{rounded.sm}` 4 px radius — neither pill nor square; the brand reads as engineered. Cards step up to `{rounded.md}` 8 px. Pill (`{rounded.full}` 9999 px) is reserved for circular icon containers. Layered drop-shadows on featured cards add modest elevation but never feel material-heavy.

**Key Characteristics:**
- A two-colour conversion hierarchy — `{colors.primary}` (`#080808`) near-black for every primary CTA, white-on-hairline for every secondary. Chromatic accents are used as full surface fills on category cards, never as button backgrounds.
- The brand's signature is its **five-stop chromatic category palette**: purple `#7a3dff` / pink `#ed52cb` / blue `#3b89ff` / orange `#ff6b00` / green `#00d722`, each tied to a product surface. Used at full saturation as card fills.
- Hero typography at 80 px weight 600 with `-0.8 px` tracking — restrained, confident, never billboard-loud.
- WF Visual Sans Variable is the single family; the brand uses no separate sans for body / display. WFVisualSans-Mono / Inconsolata appears only for technical captions.
- Tight `{rounded.sm}` 4 px button geometry; cards at `{rounded.md}` 8 px. The brand never uses pill CTAs.
- Layered multi-offset drop-shadows on featured cards — the brand's only elevation cue.

## Colors

### Brand & Accent
- **Ink Black** (`{colors.primary}` — `#080808`): The brand's primary conversion colour. Every primary CTA, every heading, every wordmark. Deeper than pure black to read as branded.
- **Accent Purple** (`{colors.accent-purple}` — `#7a3dff`): One of the five chromatic category accents — used for design / build product surfaces.
- **Accent Pink** (`{colors.accent-pink}` — `#ed52cb`): Magenta accent — used for animation / interaction product surfaces.
- **Accent Blue** (`{colors.accent-blue}` — `#3b89ff`): Bright cyan-blue — used for SEO / analytics product surfaces.
- **Accent Blue Deep** (`{colors.accent-blue-deep}` — `#006acc`): The deeper blue used for emphasis links.
- **Accent Blue Info** (`{colors.accent-blue-info}` — `#146ef5`): The badge-info blue.
- **Accent Orange** (`{colors.accent-orange}` — `#ff6b00`): Used for hosting / infrastructure product surfaces.
- **Accent Green** (`{colors.accent-green}` — `#00d722`): Used for ecommerce / status-success surfaces.
- **Accent Yellow** (`{colors.accent-yellow}` — `#ffae13`): Used for warning / collaboration product surfaces.
- **Accent Red** (`{colors.accent-red}` — `#ee1d36`): Used for error / destructive states.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): The default page background.
- **Hairline** (`{colors.hairline}` — `#d8d8d8`): 1 px solid borders — input borders, card chrome, divider lines.

### Text
- **Ink** (`{colors.ink}` — `#080808`): Default text and headings.
- **Ink Strong** (`{colors.ink-strong}` — `#222222`): Near-black emphasis.
- **Body** (`{colors.body}` — `#363636`): Default body paragraph color.
- **Body Mid** (`{colors.body-mid}` — `#5a5a5a`): Mid-emphasis secondary text — footer lines, captions.
- **Mute** (`{colors.mute}` — `#898989`): Lower-priority text.
- **Mute Soft** (`{colors.mute-soft}` — `#ababab`): The lightest text role — placeholder text, fine print.

### Semantic
- **Info Blue** (`{colors.accent-blue-info}` — `#146ef5`): Info badge / notification.
- **Success Green** (`{colors.accent-green}` — `#00d722`): Success indicators.
- **Warning Yellow** (`{colors.accent-yellow}` — `#ffae13`): Warning states.
- **Error Red** (`{colors.accent-red}` — `#ee1d36`): Validation / destructive.

## Typography

### Font Family
A single proprietary family carries every typographic role: **WF Visual Sans Variable** (with `Arial` system fallback). Weights 400 / 500 / 550 / 600 are present; the brand never uses 700 / 800 / 900. A monospace variant — **WFVisualSans-Mono** with `Inconsolata` fallback — handles rare technical caption moments and code-style labels. OpenType features `"ss02"`, `"ss10"`, `"zero"` are enabled in the mono variant for the styled zero glyph.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 80px | 600 | 83.2px | -0.8px | Hero headline. |
| `{typography.display-xl}` | 56px | 600 | 58.24px | 0 | Sub-hero displays. |
| `{typography.display-lg}` | 44.8px | 600 | 46.6px | 0 | Section headlines. |
| `{typography.display-md}` | 32px | 500 | 41.6px | 0 | Card-cluster headlines. |
| `{typography.display-sm}` | 24px | 500 | 31.2px | 0 | Sub-section displays. |
| `{typography.display-xs}` | 20px | 500 | 28px | 0 | Inline display micro-headings. |
| `{typography.eyebrow-uppercase}` | 15px | 500 | 19.5px | 1.5px | UPPERCASE eyebrow tags above sections. |
| `{typography.eyebrow-uppercase-sm}` | 12px | 500 | 12px | 0.6px | Small uppercase metadata. |
| `{typography.body-lg}` | 28.8px | 400 | 46.08px | -0.288px | Lead paragraphs. |
| `{typography.body-md}` | 16px | 400 | 25.6px | -0.16px | Default body. |
| `{typography.body-md-strong}` | 16px | 500 | 25.6px | -0.16px | Bolded inline body. |
| `{typography.body-sm}` | 14px | 400 | 22.4px | 0 | Secondary body. |
| `{typography.body-sm-strong}` | 14px | 500 | 22.4px | 0 | Bold caption / nav-link. |
| `{typography.caption}` | 12.8px | 550 | 15.36px | 0 | Badge labels (the brand's signature 550 weight). |
| `{typography.caption-mono}` | 12px | 400 | 18px | 0 | Mono code captions. |
| `{typography.button-md}` | 16px | 500 | 25.6px | -0.16px | Button labels. |

### Principles
- **Weight ceiling at 600.** The brand never uses 700+. Confident, not loud.
- **Negative tracking at display sizes.** `-0.8 px` at 80 px, scaling through. Tight kerning is part of the voice.
- **Uppercase eyebrows mark every section.** 15 px / weight 500 / `1.5 px` positive tracking is the brand's signature label style.
- **Single family across the system.** No separate display vs body face. The variable axes do the work.

### Note on Font Substitutes
WF Visual Sans Variable is proprietary. Open-source substitutes:
- **Display + body** — *Inter* weights 400 / 500 / 600 with `font-feature-settings: "ss01"` enabled is the closest stylistic match.
- **Mono** — *Inconsolata* (the documented fallback) or *DM Mono*.

## Layout

### Spacing System
- **Base unit**: 4 px (with frequent 0.4 / 0.8 sub-multiples for fine padding).
- **Tokens**: `{spacing.xxs}` 2 px · `{spacing.xs}` 4 px · `{spacing.sm}` 8 px · `{spacing.md}` 12 px · `{spacing.lg}` 16 px · `{spacing.xl}` 20 px · `{spacing.2xl}` 24 px · `{spacing.3xl}` 32 px.
- **Section padding**: hero / content bands use `{spacing.3xl}` 32 px gutters with generous vertical spacing.
- **Card interior padding**: feature and pricing cards sit at `{spacing.3xl}` 32 px.

### Grid & Container
- Marketing container is wide (effectively edge-to-edge with `{spacing.3xl}` gutters).
- Category card grid: 2 / 3-up at desktop with mixed sizing (some larger feature cards span 2 columns).
- Pricing tier grid: 3-up at desktop, 1-up at mobile.

### Responsive Strategy

#### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 479px | Hero stacks; all grids 1-up. |
| Mobile-Large | 479–767px | Same as Mobile. |
| Tablet | 768–991px | 2-up grids. |
| Desktop | ≥ 992px | Full multi-up grids. |

#### Touch Targets
Buttons render at ~44 px (12 px vertical padding + 25.6 px line-height). WCAG AAA met.

#### Collapsing Strategy
- Nav: full link row at desktop. Hamburger at mobile.
- Category card grid: 2 / 3 / 4-up at desktop, drops to 1-up at mobile.
- Pricing tier: 3 / 4-up at desktop, 1-up at mobile.

#### Image Behavior
- Category cards: full-bleed solid colour fills (no photography).
- Product screenshots: 16:9 inside `{rounded.md}` card chrome.
- No portrait imagery in the marketing surface.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | No shadow, no border. | Default bands. |
| Level 1 — Hairline | 1 px solid `{colors.hairline}` border on `{colors.canvas}`. | Default card chrome and input borders. |
| Level 2 — Layered Drop | Multi-stop layered shadow with subtle warm offsets — `0 84px 24px rgba(0,0,0,0), 0 54px 22px rgba(0,0,0,0.01), 0 30px 18px rgba(0,0,0,0.04), 0 13px 13px rgba(0,0,0,0.08), 0 3px 7px rgba(0,0,0,0.09)`. | Featured cards needing visible lift. |
| Level 3 — Layered Drop Strong | Deeper version of Level 2 with `0.12` final offset opacity. | Pricing / modal-level emphasis. |
| Level 4 — Heavy Modal | Extremely heavy multi-stop — `0 24px 24px rgba(0,0,0,0.26), 0 6px 13px rgba(0,0,0,0.29)` final stops. | Modal / dialog surfaces. |

### Decorative Depth
- The chromatic category cards (full-saturation purple `#7a3dff` / pink `#ed52cb` / blue `#3b89ff` / orange `#ff6b00` / green `#00d722` fills) provide visual depth through pure colour contrast against the white canvas.
- Layered shadow recipes are the brand's only true atmospheric effect — they're 5-stop drop-shadow stacks with very low individual opacities.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed bands. |
| `{rounded.xs}` | 2px | Tight inline pills. |
| `{rounded.sm}` | 4px | The brand's canonical button + badge + small-element radius. |
| `{rounded.md}` | 8px | Card chrome and feature / category cards. |
| `{rounded.full}` | 9999px | Circular icon containers only. |

## Components

### Buttons

**`button-primary`** — the canonical near-black CTA.
- Background `{colors.primary}` (`#080808`), text `{colors.on-primary}` white, label `{typography.button-md}` (16 px weight 500), padding `{spacing.md} {spacing.xl}`, shape `{rounded.sm}` 4 px.

**`button-secondary`** — the white outline CTA.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}` border, same typography + padding + shape.

**`button-text-arrow`** — the underlined text-link CTA with arrow used in long-form sections.
- Background `{colors.canvas}`, text `{colors.ink}`, no border, body in `{typography.button-md}`, padding `{spacing.xl}` 0.

**`button-icon-circular`** — the circular icon button for carousel controls.
- Background `{colors.canvas}`, ink icon, shape `{rounded.full}`.

### Cards & Containers

**`card-feature`** — the canonical feature card on canvas.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, padding `{spacing.3xl}`, shape `{rounded.md}`. Often elevated to Level 2 shadow when featured.

**`card-feature-dark`** — the polarity-flipped feature card on near-black.
- Background `{colors.primary}` (`#080808`), text `{colors.on-primary}`, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`card-pricing`** — the pricing-tier card.
- Background `{colors.canvas}`, text `{colors.ink}`, hairline border, padding `{spacing.3xl}`, shape `{rounded.md}`. Layered shadow on the featured tier.

### Inputs & Forms

**`text-input`** — the canonical text input.
- Background `{colors.canvas}`, text `{colors.ink}`, 1 px solid `{colors.hairline}`, body in `{typography.body-md}`, padding `{spacing.md} {spacing.lg}`, shape `{rounded.sm}`.

### Navigation

**`nav-bar`** — the sticky top nav.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.3xl}`.

**`nav-link`** — link items inside `nav-bar`.
- Text `{colors.ink}`, set in `{typography.body-sm-strong}`.

**`footer`** — the footer band.
- Background `{colors.canvas}`, text `{colors.body-mid}` (`#5a5a5a`), padding `{spacing.3xl} {spacing.3xl}`. Body in `{typography.body-sm}`.

### Signature Components

**`hero-band`** — the white hero band.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.3xl}`. Headline in `{typography.display-xxl}` (80 px weight 600).

**`hero-band-dark`** — the polarity-flipped near-black hero band (used on some campaign pages).
- Background `{colors.primary}` (`#080808`), text `{colors.on-primary}`, same padding / headline scale.

**`content-band`** — the standard content band on canvas.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.3xl} {spacing.3xl}`. Section headline in `{typography.display-lg}`.

**`category-card-purple`** — full-fill purple category card.
- Background `{colors.accent-purple}` (`#7a3dff`), text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-pink`** — full-fill pink category card.
- Background `{colors.accent-pink}` (`#ed52cb`), text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-blue`** — full-fill blue category card.
- Background `{colors.accent-blue}` (`#3b89ff`), text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-orange`** — full-fill orange category card.
- Background `{colors.accent-orange}` (`#ff6b00`), text white, padding `{spacing.3xl}`, shape `{rounded.md}`.

**`category-card-green`** — full-fill green category card (uses ink text for legibility against the lighter green).
- Background `{colors.accent-green}` (`#00d722`), text `{colors.primary}` (`#080808` ink), padding `{spacing.3xl}`, shape `{rounded.md}`.

**`badge-info`** + **`badge-info-soft`** — info badges in solid blue or soft outline.
- Filled: bg `{colors.accent-blue-info}` (`#146ef5`) text white. Soft: bg canvas, text `{colors.accent-blue-info}`. Both at `{typography.caption}` (12.8 px weight 550) — the brand's signature 550-weight caption.

### Examples (illustrative)

> Auto-derived kit-mirror demonstration surfaces (`scripts/derive-examples-block.mjs`). Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently. `TO_FILL` markers indicate missing primitives — resolve in the LLM judgment pass.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (`#080808`) for every primary CTA, every heading, and every wordmark. Near-black is the conversion colour.
- Use the five chromatic accents (purple `#7a3dff` / pink `#ed52cb` / blue `#3b89ff` / orange `#ff6b00` / green `#00d722`) as full-fill category cards, NOT as button backgrounds.
- Set hero headlines in `{typography.display-xxl}` weight 600 with `-0.8 px` tracking.
- Pair the proprietary WF Visual Sans family across every typographic role.
- Use `{rounded.sm}` 4 px for buttons, `{rounded.md}` 8 px for cards. The brand never uses pill CTAs.
- Use layered multi-stop drop-shadows on featured cards — the brand's distinctive elevation recipe.

### Don't
- Don't promote button-medium weight to 700+. The brand's weight ceiling is 600.
- Don't use chromatic accents as button backgrounds. They're surface fills, not actions.
- Don't render CTAs as pills. The brand's button geometry is tight 4 px rectangle.
- Don't introduce a sixth accent colour. The 5-stop palette is the system.

## Known Gaps

- **Hover state colours:** not documented in the captured surfaces — the brand uses subtle layered-shadow lifts on featured cards, but precise per-state colour shifts on buttons and nav links don't extract reliably.
- **Focus rings:** the system uses some form of focus indicator (likely a 2 px outline at `{colors.accent-blue-info}`), but exact ring colour, offset, and width were not captured.
- **Loading / skeleton states:** not visible in the marketing surfaces sampled.
- **Form input error states:** error colour (`{colors.accent-red}` `#ee1d36`) is documented as a token, but the full input outline + helper-text combination on validation failure was not extracted.
- **Editor / Designer UI:** Webflow's actual visual builder (Designer canvas, panels, contextual menus) lives behind auth and uses a denser, darker chrome distinct from the marketing surface — not captured here.
- **`ex-*` example surfaces:** the 10 illustrative example components at the bottom of the spec are auto-derived kit-mirror references for downstream `/preview-design` and `/generate-kit` consumers, not pixel-extracted production surfaces. Resolve any `TO_FILL` markers in the LLM judgment pass.
