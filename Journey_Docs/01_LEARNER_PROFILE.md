# 01 — Learner Profile (verified, non-personal)

**Last verified:** 2026-09-28. Everything marked VERIFIED comes from the learner's own answers to a
68-statement true/false audit, or from his own written README. Everything else is labelled.

---

## 1. Who the learner is (relevant facts only)

- Student currently in a **diploma unrelated to engineering**.
- Will start an **Electrical Engineering degree** when admissions open (mid-2028, learner's statement). India-based; the CBSE school system is the reference context.
- **Teaches a younger sibling** in school (PCM, Computer Science, English). Can teach PCM comfortably; needs to learn CBSE CS Class 11 and 12 himself first.
- Appears to prepare for math olympiads (IOQM notes in workspace; an earlier AI audit called his math "elite"). **Level unverified.** Olympiad skills (number theory, combinatorics, algebra) are not the same as the calculus/linear algebra/ODE skills EE needs.

## 2. Goals in his own framing

1. Learn "the way a CS student learns," with structure, ordering and prerequisites made explicit.
2. Learn *to build*: real, usable things, not tutorial toys.
3. Get a **foundation before the degree**, not finish everything before it ("then why the degree").
4. Software skills that help an EE degree: C++, embedded-style thinking, math, system design.
5. Build the habit of verifying knowledge instead of trusting AI summaries.

Out of scope by his decision: **FLUX** (a parked Flutter app spec), Flutter/Dart, desktop GUI frameworks.

## 3. Constraints

- **Time:** 4 to 5 hours per week for the whole journey (all lanes combined).
- **Money:** none for hardware. Simulators and free tools only.
- **Hardware/OS:** Ubuntu Linux laptop + VS Code (recently switched; earlier he coded on Android via Termux/Acode/Pydroid).
- **Tools in use:** uv (Astral), git + GitHub, TickTick (tasks), Notewise/NotebookLM (notes), Gemini, agy, Claude.
- **Python:** CPython 3.14 (via uv), earlier 3.11/3.12 appear in the workspace.

## 4. Verified skill inventory

Legend: **SOLID** (can do without help), **PARTIAL** (works but shaky), **GAP** (does not know/never did).

### SOLID
- Python core: `for`/`while` loops, list comprehensions, list vs tuple, try/except used deliberately, functions with default params and `*args/**kwargs`, `import` of modules.
- Classes: writes `__init__`, explains `self`, has written a multi-method useful class.
- Text files: open/read/close (his answer covered plain-text reading only).
- FastAPI: has written basic routes himself; used a Pydantic model for a request body; tested endpoints via `/docs`.
- SQL: writes basic queries from memory; primary/foreign keys; created tables himself; understands what an ORM does; has queried a DB from Python.
- NumPy: array creation/operations/slicing (retention weaker than he fears).
- Git: init/add/commit/push, has created branches.
- DSA (LeetCode-level): arrays, hashmaps, two pointers, stacks, queues; binary search; recursion; Big-O estimation; conceptual linked lists. Solved a handful of easy/medium problems (Two Sum, Add Two Numbers, Longest Substring Without Repeating Characters, Best Time to Buy/Sell Stock, Remove Duplicates from Sorted Array, HackerRank array set).
- Debugging own code with prints/debugger; knows what a dependency and an environment variable are; understands frontend vs backend conceptually.
- **Milestone 00 (uv):** completed and explained in his own README (see `07` log).

### PARTIAL
- Multi-file imports: writes modules but repeatedly hits **circular imports** in SQLAlchemy model files.
- `pip install`: works, does not understand the mechanics (partly addressed by M00).
- Inheritance: understands, has not used it properly.
- FastAPI path vs query parameters: understands theory, needs conscious effort in practice.
- One-to-many / many-to-many relationships: mostly conceptual.
- `git pull` vs `git fetch`: his statement was imprecise ("pull overrides your files"). Correct model: `pull` = `fetch` + merge into the current branch.

### GAP (never done / cannot do)
- **JSON:** cannot write, read, or use it reliably (`json.dump/load` never used successfully).
- **APIs/HTTP:** has never made a real `requests.get()`; does not know status codes, HTTP methods as concepts, headers, or authentication in practice. (Oddity: he can write `@app.get` routes without formally knowing HTTP methods.)
- `uvicorn` and `async def` (what they do).
- **Flask:** never wrote a route, does not know `render_template`. (See §9: an AI summary falsely claimed this.)
- Merge conflicts (never resolved manually).
- Plotting from memory (Matplotlib).
- Deployment: never deployed anything.
- Trees, graphs (BFS/DFS), dynamic programming: zero practical understanding.
- CSS and JavaScript: never written. HTML: has written *some* (self-check statement "never written HTML" was false).
- CBSE-style Python details (method lists, output prediction) and CBSE Units on Boolean logic/number systems/networks/society-law-ethics: not yet assessed.

## 5. Projects: who really wrote what

| Item | Author | Notes |
|---|---|---|
| FluxDone / AdvocateDiarySystem (FastAPI+SQLAlchemy+SQLite), PDF merger, Spotify→YTMusic migrator, quantum orbital visualizer | **AI, entirely** (learner's statement) | Do **not** treat as evidence of skill. |
| `Python/` course folders (basics, strings, lambda, collections, OOP, modules, iterators/generators, decorators, GUI Tkinter, Numpy/Pandas/Regex, Flet, a small Flask example) | Followed a structured Python course (workspace evidence) | Depth **unverified** for decorators, generators, Pandas, Regex, Tkinter, Flet, Flask. |
| `Python/5 Projects` (guessing game, password generator, number-system converter, calculators, file organizer, budget tracker, to-do, expense tracker) | Mostly himself, some GPT-assisted (filenames like "I and GPT improved") | CLI-level projects. |
| `Leetcode/`, `Python +SQL/` (sqlite3 CRUD, SQLAlchemy ORM basics) | Himself | Multiple `v1..v4` solution versions; stress-test files exist. |

Workspace root (`~/Programing-Workspace`): `Leetcode/`, `Miscellanious/`, `Projects/`, `Python/`, `Python +SQL/`, `random/`, `SQL/`, `Milestones/` (new, own git repo). Housekeeping issues: `__pycache__` folders committed under `Projects/`, and two AdvocateDiarySystem copies (original and "(Copy)").

## 6. Learning style and quirks (the "weirdness")

1. **Retention requires building.** Concepts studied but not used are forgotten (NumPy is the standard example).
2. **Real data beats toy examples.** He wants files he can "fiddle with."
3. **Hates vague roadmaps.** "Learn X" without the minimum list of atoms is unusable to him. Wants explicit prerequisites.
4. **Chose AI-assisted learning, then noticed AI leaves invisible holes.** He has seen missing topics surface later 3–4 times. Atoms + verification statements exist for this reason.
5. **Strong logic, weak boilerplate.** Grasps algorithms and formulas quickly; gets stuck on environment setup, config, framework ceremony, import structure.
6. **UI/UX from scratch is hard.** Needs many concrete examples first, then creates variations. Method in `06` §8.
7. **Uses AI as tutor at scale.** Token budgets are a real constraint; long AI generations that "don't build exactly what I want" frustrate him.
8. **Emotional context:** he has felt stuck and that "AI made building obsolete." The plan's answer: understanding is what lets you steer, debug and judge AI output, and EE/embedded work needs it.
9. **Structured note habit:** writes his own README per milestone; AI produces `notes.md` (mental models, steps, code, pitfalls) formatted for NotebookLM/Notewise.
10. **Commits after each topic**; keeps one repo per phase (see `06` §3).
11. Writes quickly with typos; do not "correct" this, read for meaning.

## 7. AI pipeline (as he uses it)

`PLANNER` (currently Claude; audits, designs, fact-checks) → `ADAPTER` (Gemini; tailors the planner's prompts and holds his chat history) → `TEACHER` (agy; hands-on tutor that runs inside his workspace and writes notes/reports).

- His learning reports come back from the TEACHER and are pasted to the PLANNER for fact-checking.
- His own README (in his words) is treated as the primary truth; TEACHER reports are secondary.
- Any AI taking a role should follow the templates in `06`.

## 8. How to communicate with him

- Casual, direct, occasional profanity; he prefers bluntness to politeness.
- Give complete maps and exact commands. State assumptions explicitly.
- Correct his misconceptions plainly (he welcomes it: e.g., the `pull` vs `fetch` correction was accepted).
- Do not use long "motivational" text. Acknowledge frustration in one or two lines, then get practical.
- Prefer numbered lists for diagnostics; prefer copy-pasteable prompts for Gemini/agy.

## 9. Known reliability problems in earlier AI output (do not repeat)

1. **Gemini's audit** claimed "Flask + SQLAlchemy backend" as learned skills, "deployment-ready" projects, and inferred personality traits (custom notation habits, colour-coded models). Most of this was inference from files that the AI itself wrote. The learner's true/false audit contradicted it: no Flask, no deployment, no API knowledge.
2. **"Understood API"** was recorded because he could describe an API as "a link"; the audit showed the whole HTTP/API category was false.
3. **agy's M00 final report** mentioned "Conventional Commits" history that the learner's notes did not show. He later explained he *did* commit after each topic and that the AI was confused by his commit-message instructions. Check with `git log --oneline` anyway.
4. Language like "Concepts Mastered" and "Final Report" tends to inflate. Use the evidence bundle (`06` §6).

## 10. Decisions already made by the learner

See the decision log in `07` §3. Key ones: uv over pip; milestone list 00–04 frozen; FLUX ignored; C++ chosen over C; math learned just-in-time or in college; simulators only; CBSE 11/12 syllabus inserted with deadlines (31 Dec 2026, 31 Mar 2027).
