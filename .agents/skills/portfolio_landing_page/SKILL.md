---
name: generate_portfolio_landing_page
description: Generates a high-end Minimal SaaS / B2B Agency landing page with specific neobrutalist and glassmorphic aesthetics.
---

# Portfolio Landing Page Generation

When a user asks you to generate a portfolio landing page or use the `generate_portfolio_landing_page` style, follow these exact design instructions.

## 1. Core Visual Aesthetic
The target style is **Minimal SaaS combined with Premium Agency**. It is characterized by high-contrast sections, distinctive pill-shaped elements, crisp borders, and bright accent colors.

### 1.1 Color Palette
- **Primary Background**: Off-white/cream (`#FDFDFD` or `#FAFAFA`).
- **Inverted/Dark Background**: Deep Black (`#0A0A0A` or `#111111`) used for contrast sections (like the footer or CTA block).
- **Text**: Pitch black (`#000000`) on light backgrounds, pure white (`#FFFFFF`) on dark backgrounds.
- **Accents**: 
  - Vivid Blue (`#4F46E5` or `#2563EB`)
  - Bright Orange/Coral (`#FF6B6B` or `#F97316`)
  - Highlight Yellow (`#FBBF24` or `#FDE047`)

### 1.2 Typography
- Use a modern geometric sans-serif font. `Inter`, `Outfit`, or `Plus Jakarta Sans` via Google Fonts.
- **Headings**: Heavy, tight letter-spacing. Use variable font weights (700-800 for emphasis).
- **Body**: Clean, legible, looser line-height (1.6).

### 1.3 UI Elements & Shapes
- **Buttons & Tags**: Strictly pill-shaped (`border-radius: 9999px`).
- **Cards & Containers**: Slightly rounded corners (`border-radius: 12px` to `16px`).
- **Borders**: Elements like feature cards, pricing tables, and even buttons should have a distinct `1px` or `2px` solid black/dark grey border to give it a slight neobrutalist structural feel.
- **Shadows**: Use clean, offset drop shadows (e.g., `box-shadow: 4px 4px 0px 0px rgba(0,0,0,1)`) exclusively on interactive elements or floating cards to give them physical presence.

## 2. Layout & Composition Requirements

When structuring the layout, ensure you include these specific architectural elements and sections:

### 2.1 Navigation (Sticky)
- **Style**: A floating inner-container (pill-shaped) nav bar, not a full-width block. It should sit slightly below the top edge of the viewport.
- **Content**: Logo on the left (bold text), minimal links in center, "Contact" pill button on the right.

### 2.2 Hero Section
- **Composition**: Centered alignment.
- **Headline**: Massive display text, e.g., "Unlimited design for your startup". Important words should be highlighted with a pill-shaped background (e.g., "Unlimited" with a vivid blue background and white text, slightly rotated for dynamism).
- **CTAs**: Primary solid pill button, and a secondary outline pill button next to it.
- **Graphics**: Include abstract 3D or flat illustration elements floating around the headline (glassmorphic shapes, floating browser windows, UI cards). Do NOT use empty gray placeholders. Generate SVGs or dynamic CSS shapes.

### 2.3 Services / Features
- **Heading**: "We offer a wide range of [highlighted: design] services."
- **Layout**: A 3-column masonry or even grid of cards.
- **Card Style**: White background, 1px solid border, containing a vibrant, minimal 2-color icon.
- **Section Detail**: A bold statement banner directly below: "We are an extension of your team."

### 2.4 Portfolio Presentation (Bento Box)
- **Heading**: "Our fitting projects"
- **Layout**: An asymmetrical bento-grid. 
- **Content**: Project thumbnails must use solid vibrant background colors (Dark Blue, Bright Blue, Orange, Purple) containing floating UI elements (mockups of apps, browser windows, abstract graphics). Use CSS to generate these geometric compositions instead of blank images.

### 2.5 Testimonials
- **Style**: Overlapping rectangular chat-bubble style cards.
- **Visual Connector**: An SVG or CSS dotted/dashed line connecting the cards across the layout to map a "user journey".

### 2.6 Pricing & CTA
- **Pricing Cards**: Side-by-side cards. 
  - *Standard*: White background with black text. 
  - *Premium*: Vivid blue background with white text. 
  - *Details*: Checkmark lists, bold pricing numbers.
- **Bottom CTA**: Dark mode section (Black background). Centered white text. "Let's work together". A stylized SVG of a pointing hand or greeting icon.

## 3. Implementation Rules
1. **No External Frameworks** (unless specified): Use Vanilla HTML, CSS, and JS.
2. **Icons**: Use inline SVGs for all icons.
3. **Animations**: Add subtle CSS hover states (e.g., the offset drop shadow shifts when a button is clicked, or cards elevate slightly on hover).
4. **Resilience**: The layout must be fully responsive and gracefully degrade on mobile (e.g., stack the bento box and services grid).
