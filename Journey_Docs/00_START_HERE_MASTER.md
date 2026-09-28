# 00 — START HERE: Master Handoff & Control Document

**Document set version:** 1.0 · **Created:** 2026-09-28 · **Last updated:** 2026-09-28
**Maintained by:** the learner (in a git repo), with a PLANNER AI proposing every edit.

---

## 1. What this document set is

A complete, self-contained specification of one learner's multi-year self-study journey:
from "can solve easy LeetCode and has never written a real program alone" to
"ready to start an Electrical Engineering degree in mid-2028 with a strong software,
math and systems foundation."

It has two jobs:

1. **Completeness.** Every phase is broken into *atoms* (the smallest testable units of
   knowledge, like letters of an alphabet). Nothing should need to be re-planned; if a
   milestone must be revisited, the atoms tell you exactly what it contained.
2. **Continuity.** If the original chat is lost, any AI can be given these files and
   continue the process without re-asking the learner what they know.

### File map (read in this order)

| File | Purpose |
|---|---|
| `00_START_HERE_MASTER.md` | This file. Rules for the AI, dashboard, timeline, pending items. |
| `01_LEARNER_PROFILE.md` | Verified skills, gaps, environment, constraints, learning quirks, AI pipeline, communication style. |
| `02_PHASE1_FOUNDATION_MILESTONES.md` | Milestones 00–04 (uv, JSON+Git, APIs, FastAPI+SQLAlchemy, Frontend+Deployment). Atoms, builds, checks. |
| `03_PHASE2_CBSE_CS_11_12.md` | CBSE Computer Science Class 11 and 12 (2026-27 syllabus) as atoms, schedule, practical lists. |
| `04_PHASE3_CPP_ELECTRONICS_SYSTEMS.md` | C++, electronics, digital logic, embedded (simulated), Blocks 1–5. |
| `05_MATH_TRACK.md` | Just-in-time math protocol and atom map. |
| `06_CROSS_CUTTING_AND_TEMPLATES.md` | System design thread, DSA upkeep, UI/UX method, git/repo conventions, verification method, prompt and report templates, update protocol. |
| `07_PROGRESS_LOG.md` | Append-only log, decision log, evidence, repo links. |

---

## 2. Instructions for any AI receiving this document set

You are taking over as the **PLANNER** (auditor and architect). Follow these rules.

1. **Read every file, 00 through 07, before replying.** Do not restart planning. Continue
   from the *Current Pointer* (section 4).
2. **You cannot edit the learner's files.** When something must change, output the exact
   replacement block (section heading + new text) and say which file and section it goes in.
3. **Never trust a completion claim without evidence.** Earlier AI outputs over-claimed
   several times (see `01_LEARNER_PROFILE.md` §9). Ask for the evidence bundle defined in
   `06_CROSS_CUTTING_AND_TEMPLATES.md` §6 (file tree, `git log --oneline`, test output,
   the learner's own README in his own words).
4. **Verify understanding with atomic true/false statements**, not "do you understand?".
   The learner explicitly asked for this and is happy to answer 20–80 statements.
   Format is in `06` §5.
5. **Milestones 00–04 are frozen.** The learner asked for no changes to their structure.
   You may refine *inside* a milestone (add an atom, fix an inaccuracy) but log it.
6. **Do not reintroduce FLUX** (a parked Flutter app project). It is out of scope for this journey.
7. **Do not let AI write the code the learner is supposed to learn.** AI explains, reviews,
   debugs *with* him, and generates practice data/prompts. See `06` §7.
8. **Be direct and specific.** No vague advice like "learn X"; always list the minimum atoms.
   Casual tone and blunt honesty are welcome. Skip flattery.
9. **Ask few questions.** Prefer a numbered statement list over open-ended questions.
10. **Check anything time-sensitive** (free-tier limits, tool availability, syllabus changes,
    package versions) instead of relying on memory. The CBSE syllabus in `03` was taken from
    the official PDF on 2026-09-28; re-check it before each academic year.
11. **When a phase or milestone finishes**, run the update protocol (`06` §9).

---

## 3. Journey overview

**End state (mid-2028):** starts an Electrical Engineering degree (admissions open mid-2028,
per the learner) with:

- working ability to write and debug C++ (pointers, classes, STL) without AI writing it;
- Python + tooling fluency (uv, JSON, APIs, FastAPI, SQL, one deployed full-stack app);
- the CBSE Class 11 and 12 Computer Science syllabus fully mastered (needed to teach his
  younger brother, who is in school);
- hands-on simulated experience of circuits, digital logic, microcontrollers, control loops;
- just-in-time math exposure (calculus, linear algebra, complex numbers, basic differential
  equations) at a "seen and used once" level; the degree teaches the rest;
- system-design habits (block diagrams, state machines, interfaces, tradeoffs);
- a portfolio of ~10 builds, each with an honest README and a GitHub repo.

**Non-goal:** finishing a CS degree before the EE degree. The purpose is a *foundation*.

### Phases run as parallel lanes (learner prefers a mix, not one topic at a time)

| Phase | Name | Doc |
|---|---|---|
| 1 | Foundation Milestones 00–04 | `02` |
| 2 | CBSE CS Class 11 & 12 | `03` |
| 3 | C++ / Electronics / Digital / Embedded / Systems | `04` |
| T | Math (just-in-time) | `05` |
| X | Cross-cutting (system design, DSA upkeep, UI/UX method) | `06` |

### Weekly hours (learner's stated cap: 4 to 5 hours/week; plan uses 4.5)

| Period | CBSE (Phase 2) | Milestones (Phase 1) | C++/Electronics (Phase 3) | Notes |
|---|---|---|---|---|
| Oct–Dec 2026 | 2.0 | 1.5 | 1.0 | Class 11 target: done by 31 Dec 2026 |
| Jan–Mar 2027 | 3.0 | 1.5 | 0 (paused) | Class 12 target: done by 31 Mar 2027 |
| Apr–Sep 2027 | 0.5 (teach-back) | 1.5 | 2.5 | M03 finishes, M04 done ~Sep 2027 |
| Oct 2027–Jun 2028 | 0.5 (teach-back) | 0 | 4.0 | Phase 3 gets nearly all the time |

Assumptions (unverified, confirm with the learner):
- His brother starts Class 12 in April 2027, so Class 12 must be ready by 31 Mar 2027.
- His brother is in Class 11 now (2026-27).
- Hours above are a *ceiling*; missed weeks push dates, they do not shrink scope.

### Tentative Phase 3 block windows (re-plan in March 2027 using real pace)

| Block | Theme | Window |
|---|---|---|
| 1 | Bits & Basics | Oct 2026–Dec 2026 (light) + Apr–Jun 2027 |
| 2 | Memory & Circuits | Jul–Oct 2027 |
| 3 | Data & Sensors | Nov 2027–Jan 2028 |
| 4 | Time & Interrupts | Feb–Apr 2028 |
| 5 | Signals & Systems Thinking | May–Jun 2028 (as far as time allows) |
| Optional | HDL/FPGA sim, nand2tetris, syllabus preview | Only if buffer exists |

---

## 4. Current Pointer (update this after every session)

- **Date of pointer:** 2026-09-28
- **Phase 1:** Milestone 00 ✅ done. Next: **Milestone 01** (JSON + Git merge conflicts). Prompt seed is in `02` under M01.
- **Phase 2:** Not started. Next: run the Class 11 / 12 true/false diagnostic (`03` §7), then start Class 11 Unit 1 in Oct 2026.
- **Phase 3:** Not started. Next: install g++, follow the first learncpp topics, build gates in CircuitVerse.
- **Math:** dormant until a build needs it (`05`).

### Pending verifications and open questions

1. Run `git log --oneline` in the Milestones repo to confirm M00 commits exist (an AI report claimed a commit style not seen in the learner's own notes; the learner says he committed after each topic).
2. Confirm which "half of Class 12 Python" the learner has actually done (diagnostic in `03`).
3. Workspace has a folder `Python/3 Advance Topics 2/4 Libraries/Flask`, but the learner reports never having written Flask. Confirm authorship/depth before M03.
4. Learner reported having written *some* HTML (self-check item 58 was false) but no CSS or JavaScript. Confirm scope during M04 diagnostic.
5. Brother's school pacing is unknown; Class 11/12 dates above are the learner's, not the school's.
6. Real GitHub repo URLs are not created yet; placeholders live in `07_PROGRESS_LOG.md` §4.

---

## 5. Global rules (apply everywhere)

1. **Build to retain.** The learner forgets anything he does not build with. Every block ends with a real build, never a calculator-style toy.
2. **Use real data**, not made-up examples, wherever possible.
3. **Atoms are the unit of progress.** An atom is `[x]` only if the learner can pass its "can-do" test *without notes and without AI writing the answer*.
4. **Definition of Done (milestone/block):** the build runs, acceptance tests pass, the learner's own README is filled in with specifics (including struggles), atoms are checked, and it is committed and pushed.
5. **Honest READMEs.** Struggles are data. Never delete earlier confusion; annotate it.
6. **Math rule:** learn a missing concept first (capped at ~1 hour per session), then return to the concept that needed it. Overflow goes to the "math debt" list (`05`).
7. **Costs:** zero-budget. Simulators only (Tinkercad, Wokwi, Falstad, CircuitVerse, EDA Playground, ngspice). No hardware purchases assumed.
8. **Environment:** Ubuntu Linux laptop, VS Code, uv-managed Python projects (one project + one `.venv` per milestone).

---

## 6. Weekly session template (4.5 hours)

| Slot | Time | Content |
|---|---|---|
| A | 1.5 h | Main learning (Phase depends on period; see table above) |
| B | 1.0 h | Math concept or CBSE theory for what is being built |
| C | 1.5 h | Build / practice / simulator |
| D | 0.5 h | README notes, atom checkboxes, commit, log entry |

Adjust proportions to the period table; the total stays ≤ 4.5 h.
