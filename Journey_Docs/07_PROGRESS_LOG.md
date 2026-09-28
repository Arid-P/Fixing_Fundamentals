# 07 — Progress Log (append-only)

Rules: never rewrite old entries; add corrections as new lines ("Correction <date>: ...").
Update procedure: `06` §9.

---

## 1. Log entries (newest at the bottom)

### 2026-09 (before 28th) — Profile audit (68-statement true/false check)
- Purpose: replace an over-optimistic AI audit with the learner's own facts.
- Outcome summary is in §2 below and in `01_LEARNER_PROFILE.md` §4.
- Key discoveries: the four "big projects" were AI-written; Flask and APIs were unknown; JSON was a blocker; DSA and Python core were solid.

### 2026-09 (before 28th) — Milestone 00 (uv) completed
- **Atoms achieved:** M00.01–M00.14 (all).
- **Built:** uv project with `requests` and `rich`; a PEP 723 inline script (`inline_demo.py`, depends on `rich`); project files `pyproject.toml`, `.python-version`, `.venv`, `uv.lock`.
- **Tooling reported by the teacher AI:** uv v0.12.17 and CPython 3.14 on Ubuntu (not independently checked by the planner).
- **Evidence provided:** learner-written README (own words, accurate), AI-written `notes.md` (mental models: grocery list vs receipt, blueprint vs construction, chauffeur, backpack), teacher-AI "final report".
- **What clicked (learner):** `uv init` outputs; `uv add` auto-creates `.venv` and lockfile; `uv.lock` pins exact versions so `uv sync` elsewhere gives the same environment; `uv run` needs no activation and auto-syncs; `uv remove`; `uv sync`; PEP 723 scripts; `uv python list/install/pin`.
- **Struggled:** `uv lock` (why it exists). **Resolved 2026-09-28:** learner stated "`uv lock` creates the blueprint; `uv sync` creates and applies it" (correct: lock resolves without installing; sync installs so `.venv` matches). Original README line "didn't understand" was left in place; add "resolved 2026-09-28" to it.
- **Technical fact-checks by planner:** grocery-list/receipt, blueprint/construction, `uv run`, PEP 723 all accurate. The pitfall "`uv add datetime` installs an unrelated legacy package" was verified (a real PyPI package named `DateTime` exists; PyPI names are case-insensitive).
- **Discrepancy:** the teacher report claimed "Conventional Commits" history not visible in the learner's notes. Learner says he committed after every topic and told the AI to write per-milestone commit messages, so the AI was confused. **Open:** confirm with `git log --oneline`.
- **Hours:** not recorded. (Start recording from M01: see §5.)

### 2026-09-28 — Planning session outputs
- Frozen milestone list 00–04 (learner request).
- Chose C++ over C; dropped Flutter/FLUX; simulators only; math just-in-time.
- Inserted CBSE Class 11 (by 31 Dec 2026) and Class 12 (by 31 Mar 2027).
- Produced this 8-file document set (v1.0).
- **Pending:** Class 11/12 diagnostic; `git log` check; repo creation and links.

*(Add new entries below this line using the format at the bottom of this file.)*

---

## 2. Audit and diagnostic records

### 2.1 The 68-statement audit (statement numbers by topic)
Topics: 1–9 Python core · 10–13 classes · 14–18 files/JSON · 19–26 APIs/HTTP · 27–32 FastAPI · 33–35 Flask · 36–41 databases/SQL · 42–45 NumPy/Matplotlib · 46–49 Git · 50–57 DSA · 58–61 web basics · 62–65 general dev practice · 66–68 environment.

**True:** 1–6, 10, 12, 13, 14, 27, 29, 31, 36–39, 41, 42, 43, 45, 46, 47, 50–57 (52–54 as stated; 55–57 confirm *zero* practical understanding of trees, graphs, DP), 59, 60, 61, 62, 63, 65.
**False:** 8 (venv understanding; since addressed by M00), 15–18 (JSON write/read/use/persist), 19–26 (all APIs/HTTP), 30 (uvicorn), 32 (`async def`), 33–35 (Flask), 44 (write Matplotlib plot from memory), 48 (resolved merge conflict), 58 (i.e., he *has* written some HTML), 64 (never deployed anything).
**Partial:** 7 (multi-file imports; circular imports with SQLAlchemy models), 9 (pip works, mechanics unclear), 11 (inheritance understood, not used well), 28 (path/query parameters: theory yes, practice needs effort), 40 (relationships mostly conceptual), 49 (pull vs fetch; corrected: pull = fetch + merge).
**Ambiguity:** the learner wrote "28" as partial twice; the second may have referred to another FastAPI item (29 or 31), which he also listed as True. Recheck during M03.
**Environment (66–68):** now Ubuntu + VS Code on a laptop (item 66 "primarily Termux" no longer true); laptop available (67 true); understands Termux vs Linux differences "somewhat" (68).

### 2.2 Diagnostics scheduled
| Diagnostic | Where | When | Status |
|---|---|---|---|
| CBSE Class 11 + 12 (66 statements) | `03` §7 | Before Oct 2026 study | Pending |
| M01 verification statements | `02` M01 | End of M01 | Pending |
| Math diagnostic (20–30 statements) | `05` §2 | ~Jul 2027 | Pending |
| Web basics diagnostic | M04 start | ~Jun 2027 | Pending |

---

## 3. Decision log

| ID | Date | Decision | Reason |
|---|---|---|---|
| D01 | 2026-09 | Use **uv** instead of pip/venv | Modern, faster, matches how his projects are already set up; taught in M00 |
| D02 | 2026-09 | Add **Milestone 00** (environment) before topic milestones | Tooling underpins everything; learn once, reuse per milestone |
| D03 | 2026-09 | One uv project + one `.venv` **per milestone**, not one shared venv | Isolation habit; uv makes it nearly free |
| D04 | 2026-09 | Remove the venv section from M01; keep folder name `01_JSON_Environments_Git` | Content moved to M00; renaming optional |
| D05 | 2026-09 | Ignore **FLUX** (Flutter apps) for the whole journey | Learner wants a CS-student-style foundation instead |
| D06 | 2026-09 | Study like a CS student (systems, DSA, math), tailored to EE | Degree is Electrical Engineering, admissions mid-2028 |
| D07 | 2026-09 | **C++** instead of C as the systems language | Learner's choice; Arduino is C++; C still read later |
| D08 | 2026-09 | No purchases; **simulators only** | No budget for components |
| D09 | 2026-09 | Math learned **just-in-time** or in college | Learner's choice; avoids a standalone math phase |
| D10 | 2026-09 | Phases run **in parallel lanes**, not one topic at a time | Learner prefers a mix to connect ideas |
| D11 | 2026-09-28 | Insert **CBSE CS Class 11 (by 31 Dec 2026) and Class 12 (by 31 Mar 2027)** | To teach his brother and to fill gaps (networks, SQL, file handling) |
| D12 | 2026-09-28 | Milestones 00–04 **frozen** (no structural changes) | Learner request |
| D13 | 2026-09-28 | C++ paused Jan–Mar 2027; Phase 3 compressed to 5 blocks | Time budget (4.5 h/week) |
| D14 | 2026-09-28 | Use MySQL/MariaDB (not SQLite) for CBSE SQL practice | Board syllabus is MySQL-style |
| D15 | 2026-09-28 | TEACHER reports need an evidence bundle | Prior AI over-claims (see `01` §9) |

---

## 4. Repositories (fill in as created)

| Phase | Repo | URL | Created | Last push | Notes |
|---|---|---|---|---|---|
| Docs | `journey-docs` | <TBD> | | | This document set |
| 1 | `milestones` | <TBD> | | | Needs a real remote for M01's merge-conflict work |
| 2 | `cbse-cs-11-12` | <TBD> | | | |
| 3 | `cpp-electronics-path` | <TBD> | | | |

Phase completion links (add when each phase finishes): _none yet_.

---

## 5. Hours and pace tracker (start from M01)

| Week of | Lane | Hours | Atoms cleared | Notes |
|---|---|---|---|---|
| — | — | — | — | (empty) |

**Pace rule:** after 4 weeks of data, compute hours per atom for each lane and compare with the plan (`00` §3 and `04` blocks). If the actual pace differs by more than 25%, re-plan dates only (not scope) and log a decision (D-number).

---

## 6. Entry format (copy for new entries)

```
### <YYYY-MM-DD> — <Milestone/Block/Topic> — <status: started/in progress/completed>
- Atoms achieved: <IDs>
- Atoms partial: <IDs>
- Built: <what, with paths>
- Evidence provided: <tree, git log, tests, README>
- What clicked (learner's words): ...
- Struggled: ...
- Correction / resolved: ...
- Discrepancies between AI report and learner evidence: ...
- Hours: <n>
- Next action: ...
```
