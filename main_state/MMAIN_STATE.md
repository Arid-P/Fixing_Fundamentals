# MMAIN_STATE — Rolling Planner State (Phase 1: M00–M05)

**Last updated:** 2026-11-25  
**Planner charter:** `Journey_Docs/PLANNER_CHARTER.md`  
**Docs status:** Restructure edits (`D27`–`D29`, M02 closeout, M03–M05 renumbering) applied to `Journey_Docs/` and `Milestones/` (pending learner diff approval + commit).

---

## 1. Current Pointer

- **Phase 1:**
  - **M00 (`00_Environment_UV`):** Done (14/14 atoms). Actual time ~3.25h (vs ~8h est). `requests` build swapped for learner's `game.py`/`calc.py` + `inline_demo.py`.
  - **M01 (`01_JSON_Environments_Git`):** Done (24/24 atoms; last 4 closed 2026-10-24 via 16/16 check). Hours unlogged. README fixed 2026-11-25 (`json.dump` `.json`, `git switch -c`).
  - **M02 (`02_APIs_HTTP`):** Done (20/21 atoms `[x]`, `M02.21` skipped; M2-8 hardening committed `618b5f2`, S-Gate 7/7 + C-Gate 7/7 passed, token rotated `2026-11-24 18:44`).
    - **Hours:** `~22.0h` logged (`M2-8 ~2.0h`; learner also reported `11.0–11.5h` for whole `gh_report` [M2-7+M2-8] -> `~24.0–24.5h` total vs `~12h` planned).
    - C1 request-count proof waived to pytest; `Used: N/A` and UI typos accepted; six behaviors deferred to M03.
  - **M03 (`03_Testing_Pytest`) — ACTIVE NEXT:** Window Dec 2026–mid Jan 2027 (~2 h/week; est. 12–15 h). Folder initialized (`d62e639`), `gh_report` source copied as capstone (`9884a52`, imports verified under pytest pythonpath). **Next checkpoint: `M3-1` (M03.01–02, practice module A: pure functions). Do not touch `gh_report/` until M3-1..M3-5 practice atoms are done.**
  - **M04 (`04_FastAPI_SQLAlchemy_Backend`):** Planned Feb 2027 (after Class 12 SQL).
  - **M05 (`05_Frontend_Deployment`):** Planned ~Jun–Sep 2027.
- **Phase 2 (CBSE CS):** Class 11 U1 (10/10) + U2 (28/28) done; U3 deferred to last week of Jan 2027 (D22); Class 12 diagnostic (statements 37–66) pending before Jan 2027.
- **Phase 3 (C++/Electronics):** Block 1 part A chats 1–2 done (6.0h); `CPP-04` `[~]` (3 overflow/boundary bugs in `p12`, `p02`, `p09`). Next: chat 3 (`P3-5`).
- **Vision lane (`~/school_project`):** Decision pending (paused until `03_Testing_Pytest` completes).

---

## 2. Phase 1 Atoms Snapshot

- **M00 (`M00.01`–`M00.14`):** 14/14 `[x]`
- **M01 (`M01.01`–`M01.24`):** 24/24 `[x]`
- **M02 (`M02.01`–`M02.21`):** 20/21 `[x]`, `M02.21` `[ ]` (optional, skipped)
- **M03 (`M03.01`–`M03.14`):** 0/14 `[ ]` (`M3-1` next; cold-write tests scheduled at `M3-2` and `M3-5`)
- **M04 (`M04.01`–`M04.25`):** 0/25 `[ ]`
- **M05 (`M05.01`–`M05.27`):** 0/27 `[ ]`

---

## 3. Open Items & Known Backlog

- **M03 Capstone (`gh_report` in `03_Testing_Pytest/src/03_testing_pytest/gh_report/`):**
  - 30+ tests passing with no network in < 5 s; coverage >= 80% on `processing`, `cache`, `utilis`; 3 real bugs reproduced red-then-green; `per_page=100` request count; 90-day boundary (`89`/`90`/`91`); six deferred behaviors (forced timeout, 429/403 stop with reset time, N-aware cache, page-1-only `If-None-Match`, corrupt cache, 5xx backoff wait).
- **Pending commits (waiting for learner approval of diff):**
  - `Milestones/`: `README.md`, `mentor_rules.md`, `01_JSON_Environments_Git/README.md`, `02_APIs_HTTP/README.md`, `02_APIs_HTTP/src/02_apis_http/build/gh_report/DESIGN.md`, `main_state/MMAIN_STATE.md` (note: keep `.gitignore` with `context_harvest/` uncommitted!).
  - Root repo (`~/Programing-Workspace`): `Journey_Docs/PLANNER_CHARTER.md` and `Journey_Docs/{00,01,02,04,06,07}*.md`.
- **Other Phase/Pending Items:** CBSE Class 11 P08/P17/P18 real runs, Class 12 diagnostic, `CPP-04` fixes (`p12`, `p02`, `p09`), confirm Flask folder depth before M04, HTML/CSS/JS diagnostic at M05 start.

---

## 4. Decisions Log

- **Logged in `07_PROGRESS_LOG.md`:** D01–D15, D18–D29 (D16–D17 unused).
  - **D27 (2026-11-25):** Insert `03_Testing_Pytest` (practice first, `gh_report` capstone); FastAPI+SQLAlchemy -> M04, Frontend+Deployment -> M05.
  - **D28 (2026-11-25):** Main-chat architecture (`MMAIN`, `CMAIN`, teacher chats, `PLANNER_CHARTER.md`, rolling state files).
  - **D29 (2026-11-25):** Copy `gh_report` source into `03_Testing_Pytest` as capstone; `02_APIs_HTTP` keeps original.
- **Session / Hardening Decisions:** S4 (source `.env` never wiped), S1 (GitHub token rotated `2026-11-24`), Vision lane paused until M03 completes (`2026-11-25`).

---

## 5. What Each Teacher Chat Knows

| Chat ID | Scope | Harvest File | Status |
|---|---|---|---|
| `00` | M00 (`uv`) | `context_harvest/CONTEXT_M00.md` | Harvested |
| `10` | M01 (JSON + Git) | `context_harvest/CONTEXT_M01.md` | Harvested |
| `20` | M02 (M2-1..M2-4) | `context_harvest/CONTEXT_M02_1.md` | Harvested |
| `21` | M02 (M2-5..M2-6) | `context_harvest/CONTEXT_M02_2.md` | Harvested |
| `22` | M02 (M2-7) | `context_harvest/CONTEXT_M02_3.md` | Harvested |
| `23` | M02 (M2-8) | `context_harvest/CONTEXT_M02_4.md` | Harvested |
| `30` (new) | M03 (`pytest`) | `03_Testing_Pytest/SESSION_STATE.md` | Ready for kickoff |
