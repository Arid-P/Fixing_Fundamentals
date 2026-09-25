# Milestones — CS Fundamentals Path

Guided path to close the gap between "can solve LeetCode / DSA" and "can actually
build and ship a full-stack app." Separate from `Python/`, `Leetcode/`, `SQL/`
(reference/practice archive) and `Projects/` (finished, real things).

Each milestone lives in its own numbered folder, has its own `.venv`, and ends
with one real "build" — not a toy example.

---

## Progress Log

| # | Milestone | Status | Started | Finished |
|---|-----------|--------|---------|----------|
| 00 | Environment & Tooling (uv) | 🔲 Not started | | |
| 01 | JSON, Virtual Environments, Git Merge Conflicts | 🔲 Not started | | |
| 02 | APIs & HTTP (requests, status codes, auth) | 🔲 Not started | | |
| 03 | FastAPI + SQLAlchemy Backend (fix circular imports) | 🔲 Not started | | |
| 04 | Frontend Basics + Deployment | 🔲 Not started | | |

Status key: 🔲 Not started · 🟡 In progress · ✅ Done · 🔁 Revisit later

---

## Milestone Folder Structure

```
0X_Milestone_Name/
├── README.md      ← what this milestone covers + what you learned/struggled with
├── data/           ← real data you're practicing on (not toy examples)
├── practice/       ← follow-along scripts while learning
├── build/          ← the actual milestone deliverable
└── .venv/          ← gitignored, fresh per milestone
```

---

## Per-Milestone README Template

Copy this into each `0X_Milestone_Name/README.md`:

```markdown
# Milestone 0X: <name>

## Goal
What this milestone was supposed to fix/teach.

## What I built
Short description of the final `build/` deliverable.

## What actually clicked
Concepts I understand well now.

## What I struggled with
Be honest — this is what gets carried into the next Gemini/Claude prompt.

## Open questions / revisit later
Anything still fuzzy that isn't blocking progress right now.
```

---

## Rules for This Folder

1. Don't skip the `README.md` per milestone — future-you (and future prompts
   to AI) depend on it being accurate, not optimistic.
2. A milestone isn't "done" until the `build/` script actually runs and does
   what it's supposed to — not until you understand the theory.
3. If a milestone reveals a gap from an earlier one, don't go back and edit
   history — log it under "Open questions" and address it as its own thing.
