# 7 portfolio briefs you can build this weekend

> **pick one. build it saturday. write it up sunday.**

> that's the whole plan. no redesign, no new template, no waiting until you feel ready.

Each brief below has the same shape: the problem, your job, constraints, what you'd measure, and the gotchas. Everything is built around **one weekend** — if it takes longer, you're decorating instead of deciding.

And read the last section before you start. The write-up is what gets you hired, not the screen.

---

# 01 · the empty state

*the screen where the user has nothing yet*

**The problem**

A new user signs up, finishes onboarding, and lands on a screen with nothing in it. Most products show a grey box and the words "No items yet." This is the highest drop-off moment in most products — the user is curious but not invested, and a blank screen gives them nothing to be curious about.

**Your job**

Design the first-use empty state for a real product. Turn a dead screen into the moment that gets them to do the first meaningful thing.

**Constraints**

- One primary action only. Empty states fail when they offer five choices.
- No lorem ipsum — every word is real copy. The writing IS the design here.
- Must work with zero illustration budget. If it's charming with type and layout alone, that's craft.
- Mobile and desktop.

**What you'd measure**

Activation rate (% who complete the first action in session 1) · time to first action · bounce from the empty state.

**Gotchas**

Don't make it cute at the cost of clear — a charming illustration with vague copy converts worse than plain type with a sharp instruction. And don't put the CTA below the fold; the screen is empty, there's no excuse.

**Steal from:** Notion (template suggestions instead of a blank page) · Linear (keyboard hints) · Slack (empty channel prompts the first message)

---

# 02 · the settings page

*bloated, unfindable, and in every product on earth*

**The problem**

Settings pages grow by accretion — every feature ships a toggle, nobody ever removes one, and three years later users can't find how to turn off notifications. It's the least designed screen in most products and one of the most used.

**Your job**

Restructure the settings of a real product so someone can find any given control in under 15 seconds.

**Constraints**

- You may not delete features. Reorganising is the job — hiding things isn't.
- Every group needs a name a normal person would use, not an internal team name.
- Include search. Then design the page well enough that search feels optional.
- Show at least one destructive action (delete account, cancel plan) handled properly.

**What you'd measure**

Time to find a specific setting · support tickets about "where is X" · settings search usage.

**Gotchas**

This is an information architecture problem wearing a UI costume. If your case study is about how it looks, you've missed it — show the grouping logic and why you chose it.

**Steal from:** Linear · Stripe Dashboard · iOS Settings search behaviour

---

# 03 · the error page

*a 404 that actually helps instead of apologising*

**The problem**

Most error pages say "Something went wrong" and offer a home button. The user hit an error mid-task, they're annoyed, and you've given them nothing except a dead end and a mild apology.

**Your job**

Design a 404 or error state that gets the user back to what they were doing.

**Constraints**

- No "Oops!" No apologetic tone. Be useful, not sorry.
- Must offer at least two real recovery paths (search, popular pages, contact, back to previous).
- The illustration, if any, cannot be the main thing. Recovery is.
- Write a version for a broken link and a version for a server error — they need different copy.

**What you'd measure**

% who take a recovery action instead of leaving · bounce rate from error pages · support contacts from error states.

**Gotchas**

Everyone designs the funny 404. Almost nobody designs the *useful* one. Being the second is the harder and more hireable choice — you can still be funny, but the recovery has to work first.

**Steal from:** GitHub · Figma · Notion's error states

---

# 04 · the checkout flow

*find a real store with a bad one*

**The problem**

Checkout is where money either happens or doesn't. Average cart abandonment sits around 70%, and most of it is friction: forced account creation, surprise shipping costs, too many fields, no visible progress.

**Your job**

Redesign the checkout of a real store. Find one in the wild — an actual small brand with an actual bad flow.

**Constraints**

- Guest checkout must exist. No forced account creation.
- Total cost visible before the final step. Surprise fees are the single biggest abandonment cause.
- Cut the field count and justify every field you kept.
- Show the error states — declined card, invalid address, expired session.

**What you'd measure**

Cart abandonment rate · completion time · field-level drop-off · error recovery rate.

**Gotchas**

This one has the clearest business case of any project on this list, so lean into it. If your write-up doesn't mention revenue, you've wasted the best part of the brief.

**Steal from:** Shopify's default checkout · Apple · Stripe Checkout

---

# 05 · onboarding

*for an app that drops you in with no context*

**The problem**

A user downloads an app, opens it, and is immediately looking at an interface they don't understand. Either there's no onboarding, or there's a five-screen carousel of feature descriptions everyone skips.

**Your job**

Design onboarding for a real product that gets someone to their first moment of value as fast as possible.

**Constraints**

- Maximum three screens before the user is *doing* something.
- No feature tours. Teach by having them do the thing, not by describing it.
- Include a skip. Design for the person who skips too.
- Show what the second session looks like — onboarding isn't over after day one.

**What you'd measure**

Time to first value · completion rate of onboarding · day-2 return rate · skip rate.

**Gotchas**

The temptation is to explain everything. The good version explains almost nothing and makes the first action obvious. Cutting is the skill being demonstrated here.

**Steal from:** Duolingo (you're learning before you've signed up) · Figma · Superhuman's guided setup

---

# 06 · the cancel flow

*that doesn't hide the cancel button*

**The problem**

Most subscription cancellation is deliberately hostile — buried in settings, five confirmation screens, a phone call. It works short-term and destroys trust permanently. Users who cancel easily come back. Users who had to fight tell everyone.

**Your job**

Design a cancel flow that's genuinely easy, while still giving the business a fair chance to retain the user.

**Constraints**

- Cancel must be findable in two clicks from account settings.
- You get exactly one retention offer. One. Not a gauntlet.
- Ask why they're leaving — but make it skippable, and make the options useful for the product team.
- Confirm clearly what happens: when access ends, what data is kept, how to come back.

**What you'd measure**

Completion rate · retention offer acceptance · reactivation rate within 90 days · support tickets about cancelling.

**Gotchas**

This is the most senior-signalling project on the list, because it requires arguing for the user against short-term business incentive — and doing it with a business case, not a moral one. Frame it as reactivation and lifetime value, not "dark patterns are bad."

**Steal from:** Netflix · Spotify · anything that lets you leave in under a minute

---

# 07 · the notification centre

*for an app that spams you*

**The problem**

Notifications start useful and end up noise. Once a user mutes everything or turns push off entirely, you've permanently lost a channel — and most products design notifications as a growth lever instead of a user need.

**Your job**

Design the notification centre and preferences for a real product that over-notifies.

**Constraints**

- Group notifications by type or source, not just reverse-chronologically.
- Granular controls — the user shouldn't have to choose between everything and nothing.
- Include a batching or quiet-hours option.
- Design the empty state too (nice tie-in with brief 01).

**What you'd measure**

Notification opt-out rate · open rate per notification type · % of users using granular settings vs turning everything off.

**Gotchas**

The interesting decision isn't the UI, it's which notifications you'd *delete entirely*. Say so in the write-up — knowing what not to build is the thing AI can't do and hiring managers can't teach.

**Steal from:** Slack's notification granularity · GitHub · Linear

---

# how to write it up (this is the part that gets you hired)

The design is maybe 30% of the value. The framing is the rest. Most people build something decent and then freeze at the case study, so here's the shape:

**1. Title it with an outcome, not a task**

- ❌ "Settings Page Redesign"
- ✅ "Making 40 settings findable in under 15 seconds"

**2. Open with the problem, in numbers if you can defend them**

> "Checkout abandonment averages ~70% industry-wide. This store forces account creation before showing shipping costs — two of the top three abandonment causes, stacked."

**3. Show the before.** Screenshot the real thing. Honesty reads as confidence.

**4. State ONE decision and why**

> "I chose to show total cost on step one rather than optimise the form layout, because surprise fees cause more abandonment than field count does."

**5. Show the after.** Mobile and desktop.

**6. Name what you'd measure and what would prove you wrong**

> "I'd track field-level drop-off and test the cost-transparency change before the visual one. If abandonment didn't move, the problem is trust, not friction."

**7. Be honest about scope at the bottom**

> "Self-initiated project. Not shipped — built to show how I approach checkout friction."

That last line doesn't weaken anything. It makes everything above it more credible.

---

# the weekend rule

Saturday: build it. Sunday: write it up. Monday: it's in your portfolio.

If you're on day four still adjusting spacing, you've stopped designing and started hiding. Ship it slightly worse and start the next one — the second project teaches you more than the extra polish on the first ever will.
