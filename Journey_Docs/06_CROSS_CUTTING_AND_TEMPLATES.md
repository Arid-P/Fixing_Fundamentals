# 06 — Cross-Cutting Threads, Conventions, Templates and Update Protocol

---

## 1. Purpose
Everything that spans phases: system design, repo conventions, documentation standards, DSA upkeep, verification method, prompt/report templates, AI usage rules, UI/UX method, and the procedure for updating these documents.

---

## 2. System design thread (runs through Phase 3, appears earlier in small form)

**Goal:** by mid-2028 he designs before he codes, and can justify tradeoffs on paper.

| Atom | Where introduced | What he can do |
|---|---|---|
| SD-01 | Block 1 (and M01 onward) | Write a one-page design: purpose, inputs, outputs, states, block diagram |
| SD-02 | Block 2 | Draw and implement a finite state machine (states, events, transitions) |
| SD-03 | Block 3 | Design data flow between modules (producer/consumer, ring buffers), define interfaces |
| SD-04 | Block 4 | Compute a timing/latency budget; separate ISR work from main-loop work |
| SD-05 | Block 5 (reuses M03/M04) | Sketch client/server + API + DB schema; identify failure points |
| SD-06 | Block 5 | Write a design doc with requirements, options, tradeoffs, failure modes |

### One-page design template (copy into each build's `README.md` or `DESIGN.md`)
```
# Design: <name>
## Purpose (2 sentences)
## Inputs / Outputs
## States and transitions (diagram or table)
## Modules and interfaces (who calls whom, with what data)
## Constraints (time, memory, hardware, cost)
## Failure modes and handling
## Tradeoffs considered (option A vs B, why chosen)
## Test plan (how I will know it works)
```
For diagrams: hand-drawn photo, ASCII, or Mermaid text is enough. Clarity beats polish.

---

## 3. Git, repo and workspace conventions

### Repos (one per phase; add URLs to `07` §4 when created)
| Repo (suggested name) | Contents |
|---|---|
| `journey-docs` | This document set (updated by the update protocol) |
| `milestones` | Phase 1: `Milestones/` folder (M00–M04) |
| `cbse-cs-11-12` | Phase 2: notes, record-file programs, projects, diagnostic results |
| `cpp-electronics-path` | Phase 3: C++ exercises, block builds, simulator links/screenshots, math notes |

### Workspace layout (extend the existing `~/Programing-Workspace`)
```
Programing-Workspace/
├── Milestones/        # existing, own git repo
├── CBSE_CS/           # Class11/, Class12/ (programs/, project/, notes/)
├── CPP_Path/          # block1_bits/, block2_memory/, ... each with README + design page
├── Electronics_Sim/   # README with links to Wokwi/Tinkercad/CircuitVerse/Falstad projects + screenshots
├── Math_Notes/        # debt list, problem sets
├── Journey_Docs/      # this set
└── (existing: Leetcode/, Python/, Python +SQL/, SQL/, Projects/, Miscellanious/, random/)
```
Online simulators keep projects on their sites: store the **share link, screenshots and an exported file** in the README. Do not rely on the site alone.

### Commit and branch style
- **Conventional Commits:** `feat(m02): fetch weather with timeout`, `fix(m03): break circular import in models`, `docs(c11): add unit 1 notes`, `test(...)`, `chore(...)`.
- Commit after each atom cluster or topic (the learner already does this).
- Branches for experiments: `feature/<topic>`; merge to `main` when the build passes.
- `.gitignore` in every repo (`.venv/`, `__pycache__/`, `*.pyc`, `*.db`, `*.sqlite`, `.env`, build outputs).
- **Never commit secrets.** If one is committed by mistake, rotate the key first, then clean history.

---

## 4. Documentation and practice standards

### 4.1 README standard for every milestone/block
Headings: **Goal · What I built · What actually clicked · What I struggled with · Open questions / revisit later** (Phase 1 also has a "Cross-links" line if useful).

Quality bar: specific enough that a stranger learns exactly what he knows and does not know.
- Bullets, not essays. Include the *exact* confusing lines of code or error messages.
- Record dates when something clicked (or did not).
- Never delete earlier confusion; append "resolved on <date> because ...".
- List atom IDs achieved, partial, and pushed to the debt/revisit list.
- Own words only. AI-generated `notes.md` is a separate file and not a substitute.

### 4.2 DSA upkeep (light, runs alongside everything)
- **Budget:** ≤ 30–45 minutes per week; never eat into build time.
- **Now to Block 3:** keep arrays, hashmaps, two pointers, stacks, queues warm on LeetCode/HackerRank; store attempts as `v1.py`, `v2.py`, ... (his existing style) with a note on the pattern and what was missed.
- **Block 3:** formal learning of DS-01..07 in C++ (sorting, binary search, recursion, trees, graphs, DP, ring buffer). Then resume problems by pattern.
- **Tracking table** (append in the CPP_Path README):

| Problem | Pattern | First try (min) | Needed hint? | Revisit date |
|---|---|---|---|---|

- Rule: after a hint, re-solve from scratch after 3 days.

---

## 5. Verification method (how atoms become `[x]`)

The learner explicitly wants **fact-checks through highly specific true/false statements** and is happy to answer 20–80 at a time.

Rules for the PLANNER when writing statements:
1. One claim per statement. No compound claims.
2. Mix true and false; make false ones subtly wrong (reversed definitions, off-by-one, common misconceptions).
3. Cover *every* atom in scope; include at least one applied statement per unit.
4. Number statements. The learner answers `1. True`, `2. False`, `3. Partial — note`.
5. Keep the answer key in a separate section/message until he answers.
6. Score by atom, not by total. Wrong or partial → the atom stays `[ ]` or `[~]`.
7. For atoms where "True/False" is weak (writing code), use a **cold-write test**: write from a blank file in ≤ 10 minutes, no AI, no notes.
8. Spot-check the *why*: for two random correct answers, ask him to explain in one sentence.

Other verification tools: explain-back (teach the brother), debugging a planted bug, predicting output before running.

---

## 6. Templates

### 6.1 Evidence bundle (required with every completion report)
1. `tree -L 3` (or similar) of the milestone/block folder.
2. `git log --oneline --graph -n 20` output.
3. Test/acceptance output (`uv run pytest`, or paste terminal runs).
4. The learner's own README (unedited by AI).
5. A list of atoms he claims, each with one line of proof (file/line or output).
6. A list of things he could **not** do without help.

The PLANNER rejects "Mastered/Completed" claims that lack items 1–4.

### 6.2 Teacher-AI (agy) prompt template (fill the brackets)
```
[ROLE] You are my hands-on tutor. Teach; do not write my solutions for me.

[MY VERIFIED LEVEL] <paste 01_LEARNER_PROFILE.md §4>

[ALREADY DONE, DO NOT RE-TEACH] <milestones/blocks completed>

[THIS SESSION] <milestone/block name>; atoms: <paste atom list>
Real data / tools: <files, links>

[TEACHING RULES]
1. For each atom: 2–3 sentence explanation → tiny runnable example using MY data →
   I type it myself → you give me a bug to find → you ask me to explain it back.
2. Never move on until I pass the atom's "can-do" test.
3. If I say EXPLAIN SIMPLER, re-explain with a different analogy. Do not repeat yourself.
4. Point out 2–3 common beginner mistakes per atom.
5. Do not write the build for me. Give me acceptance tests and review my code.
6. Do not claim I have mastered anything. Only list what I demonstrated.

[BUILD] <build spec + acceptance tests>

[END OF SESSION] Produce: (a) notes.md (mental models, steps, code, pitfalls),
(b) an evidence bundle (see 06 §6.1), (c) a "could not do alone" list.
```

### 6.3 Extraction prompt for the ADAPTER (Gemini) when re-auditing the learner
```
Summarize, from our conversation history only, what I have actually practiced in code.
For each topic give: name; what I built myself vs what an AI wrote; whether I typed it or pasted it;
how recently; and any misconception you corrected. Mark anything you inferred from files
(rather than from my own work) as INFERRED. Do not say I know something because a project
in my folder uses it. Be blunt.
```

### 6.4 Resume prompt (paste with the whole document set into a new AI)
```
I am continuing a long self-study plan. Read all 8 files in this set (00–07) fully.
Act as PLANNER per 00_START_HERE_MASTER.md §2. Tell me: (1) current pointer, (2) which
atoms are open in the current milestone/block, (3) what evidence you need from me, and
(4) the next single action. Do not re-plan phases. Do not ask me more than 3 questions.
```

---

## 7. AI usage rules (learner's own conclusion after earlier experience)

1. AI **explains, quizzes, reviews and debugs with him**; it does not write the code he is learning.
2. AI may generate practice data, test cases, diagrams, and note formatting.
3. AI-written projects (FluxDone, PDF merger, Spotify migrator, orbital visualizer) are *not* skill evidence.
4. If an AI output contains a fact that can be checked (`git log`, `tree`, running the code), **check it**.
5. Token-limited? Ask for short, atom-sized explanations rather than full lessons.
6. Long "reports" are secondary; his README wins conflicts.

---

## 8. UI/UX by example (the learner cannot design from a blank page)

1. Pick **3 reference apps/sites** he likes and would actually use.
2. Take screenshots and annotate: layout grid, spacing scale, font sizes, color palette (hex), components (cards, buttons, forms), states (hover, empty, error).
3. Extract **design tokens** into CSS variables: colors, spacing (4/8/16/24), radii, font sizes.
4. Rebuild one screen to look *close* to one reference (structure and tokens, never copy code or assets).
5. Then change three things on purpose (layout, color, density) and note why they look better or worse.
6. Keep a `references/` folder with screenshots and notes in each frontend project.

---

## 9. Update protocol (run after every milestone/block/phase completes)

1. **Collect evidence** (§6.1). Reject if incomplete.
2. **Verify atoms** with a statement list (§5). Update atom boxes in the phase file: `[x]` / `[~]` / `[ ]`.
3. **Update `07_PROGRESS_LOG.md`:** add an entry (date, what was done, what struggled, what remains, hours spent), update the repo-link table (§4), add any decisions to the decision log.
4. **Update `00_START_HERE_MASTER.md`:** the Current Pointer, Pending verifications, and any timeline shifts.
5. **Update `01_LEARNER_PROFILE.md`:** move verified skills from GAP/PARTIAL to SOLID; add newly discovered quirks; refresh "Known reliability problems" if the AI erred.
6. **Refine future plans:** adjust hours per atom based on real pace; re-plan the next phase only if pace differs by > 25%. Log the re-plan.
7. **Bump the document version** in `00` and note the change in the log.
8. Commit to the `journey-docs` repo with `docs(journey): <what changed>` and push.
9. When a **phase** completes, add its GitHub repo link in `07` §4 and in `00` §4.

The PLANNER produces the exact replacement text; the learner pastes and commits.

---

## 10. Housekeeping backlog (do when convenient; not part of milestones)

- Add `.gitignore` to `Projects/` and remove committed `__pycache__` folders.
- Decide which `AdvocateDiarySystem` copy is canonical; archive the other.
- Confirm `Milestones/` has **two separate files** (`README.md` and `.gitignore`); an earlier typo once created one file named `README.md,.gitignore`.
- Confirm all milestone folders are inside the repo and `git status` is clean before starting each new one.
