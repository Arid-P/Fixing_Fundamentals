# 02 — Phase 1: Foundation Milestones 00–04

**Status legend for atoms:** `[ ]` not started · `[~]` partial · `[x]` verified (own words, no AI writing the answer)
**Frozen structure:** milestone list and order were fixed by the learner. Refinements inside a milestone must be logged in `07`.
**Repo:** one git repo for the `Milestones/` folder; URL goes in `07` §4.

---

## 0. Common structure and rituals

### Folder layout (inside `~/Programing-Workspace/Milestones/`)

```
Milestones/
├── README.md                      # index + progress table
├── .gitignore                     # .venv/, __pycache__/, *.pyc, *.db, *.sqlite, .env
├── 00_Environment_UV/
├── 01_JSON_Environments_Git/      # folder name kept; venv content moved to 00
├── 02_APIs_HTTP/
├── 03_FastAPI_SQLAlchemy_Backend/
└── 04_Frontend_Deployment/
    each has: README.md, data/ (if needed), practice/, build/
```

### The uv ritual (start of every milestone)
```bash
cd ~/Programing-Workspace/Milestones/0X_Name
uv init .                      # pyproject.toml, .python-version (skips existing files)
uv add <packages for this milestone>
uv run python build/<script>.py
```
Never `source .venv/bin/activate`. Commit `pyproject.toml` and `uv.lock`; never commit `.venv`.

### Per-milestone README the learner writes (headings)
Goal · What I built · What actually clicked · What I struggled with · Open questions / revisit later.
Be specific (code lines, error messages, dates). Detail standard is in `06` §4.

### Hours (at 1.5 h/week milestone lane) and target windows
| Milestone | Est. hours | Target window |
|---|---|---|
| M00 | ~8 | DONE (Sep 2026) |
| M01 | ~10 | Oct – early Nov 2026 |
| M02 | ~12 | Nov – Dec 2026 |
| M03 | ~28 | Feb – Jun 2027 (after Class 12 SQL, ideally) |
| M04 | ~28 | Jun – Sep 2027 |

---

## MILESTONE 00 — Environment & Tooling (uv) ✅ DONE

**Goal:** stop fearing environments; understand what uv does and why it beats venv+pip.
**Prerequisites:** none. **Environment:** Ubuntu, uv installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`).

### Atoms (all verified via the learner's own README)
- [x] M00.01 uv replaces pip + venv + pyenv + pip-tools with one tool.
- [x] M00.02 Install uv and check the version.
- [x] M00.03 `uv init` creates `pyproject.toml` and `.python-version`.
- [x] M00.04 `pyproject.toml` anatomy: project name, version, `requires-python`, dependencies.
- [x] M00.05 `uv add` creates `.venv`, resolves the full dependency graph, updates `pyproject.toml` and `uv.lock`.
- [x] M00.06 `uv.lock` stores exact versions and hashes for reproducibility; never edit by hand.
- [x] M00.07 `uv run` needs no activation, auto-syncs `.venv`, leaves shell state untouched.
- [x] M00.08 `uv remove` edits `pyproject.toml` and `uv.lock` and uninstalls.
- [x] M00.09 `uv lock` = resolve only (blueprint); `uv sync` = resolve + install so `.venv` matches (blueprint applied). *Initially confused; resolved (see log).*
- [x] M00.10 `uv lock --upgrade` re-resolves to newest allowed versions.
- [x] M00.11 PEP 723 inline script metadata via `uv add --script file.py pkg`; run with `uv run file.py`.
- [x] M00.12 `uv python list/install/pin`; interpreters live under `~/.local/share/uv/python/`.
- [x] M00.13 Standard-library modules are not installed with `uv add` (`uv add datetime` pulls an unrelated legacy PyPI package, `DateTime`).
- [x] M00.14 Commit `pyproject.toml` + `uv.lock`; ignore `.venv`.

**Build (done):** uv project with `requests` and `rich`, a small script using both, a PEP 723 demo script (`inline_demo.py` with `rich`).
**Notes produced by agy:** `notes.md` (mental models: grocery list/receipt, blueprint/construction, chauffeur, backpack).
**Revisit if:** dependency errors appear in later milestones; re-read atoms M00.06, M00.09.

---

## MILESTONE 01 — JSON + Git Merge Conflicts

**Goal:** remove the "JSON blocker" and finally understand git branching/merging/remotes, including a real conflict.
**Prerequisites:** M00. **Packages:** none required beyond stdlib (`rich` optional for pretty output).
**Real data (download once via browser, save into `data/`):**
- `https://jsonplaceholder.typicode.com/users` → `users.json` (10 users, nested: `address.geo`, `company`)
- `https://jsonplaceholder.typicode.com/todos` → `todos.json` (200 todos, `userId`, `completed`)
- Bonus later: TickTick backup exports as **CSV** (Settings → Backup & Import → Create Backup on the web app), a good CSV→JSON exercise.

### Atoms — JSON
- [x] M01.01 JSON syntax rules: double quotes only, no trailing commas, six value types (object, array, string, number, `true/false`, `null`).
- [x] M01.02 JSON is *text*; a Python dict is an in-memory object. Map: `true/false/null` ↔ `True/False/None`; JSON keys are always strings.
- [x] M01.03 `json.load(f)` (file → object) vs `json.loads(s)` (string → object).
- [x] M01.04 `json.dump(obj, f, indent=2)` (object → file) vs `json.dumps(obj)` (object → string).
- [x] M01.05 Always `with open(path, encoding="utf-8")`.
- [x] M01.06 Nested access: `data[0]["address"]["geo"]["lat"]`; mixed list/dict paths.
- [x] M01.07 Safe access: `.get(key, default)`, catching `KeyError`/`TypeError`, checking types.
- [x] M01.08 Filter, sort and group lists of objects: comprehensions, `sorted(key=...)`, `collections.Counter`, `defaultdict`.
- [x] M01.09 Read-modify-write: never `json.dump` across separate runs blindly; write to a temp file then `os.replace`; keep a backup.
- [x] M01.10 Invalid JSON: `json.JSONDecodeError` gives line/column; read the message.
- [x] M01.11 `sort_keys`, `ensure_ascii=False`, `default=str` for non-serializable types (e.g. `datetime`).
- [x] M01.12 Inspect JSON from the terminal: `python -m json.tool`, optionally `jq`.
- [ ] M01.13 CSV ↔ JSON with `csv.DictReader`/`DictWriter` (also a Class 12 CBSE topic).

### Atoms — Git
- [ ] M01.14 Three areas: working directory, staging area, repository; a commit is a snapshot.
- [ ] M01.15 Branches: `git switch -c name`, `git branch`, deleting merged branches.
- [ ] M01.16 Merge types: fast-forward vs three-way merge.
- [ ] M01.17 Conflict markers: `<<<<<<< HEAD`, `=======`, `>>>>>>> branch`; what each side means.
- [ ] M01.18 Resolving: edit file → `git add` → `git commit` (or `git merge --continue`); `git merge --abort` to bail out.
- [ ] M01.19 Remotes: `git remote add origin`, `git push -u origin main`, `git clone`.
- [ ] M01.20 **`fetch` downloads without touching your files; `pull` = `fetch` + merge**; also `pull --rebase` (concept).
- [ ] M01.21 Inspect history: `git log --oneline --graph --all`, `git diff`, `git diff origin/main`.
- [ ] M01.22 `.gitignore` patterns; stop tracking an already-added file (`git rm --cached`).
- [ ] M01.23 Undo tools: `git restore`, `git reset --soft/--mixed/--hard` (concept), `git revert`.
- [ ] M01.24 Commit message hygiene (Conventional Commits, e.g. `feat(m01): ...`).

### Ordered learning sequence
1. Download JSON, `python -m json.tool` it, read it by eye (M01.01–02, 12).
2. Load, print, index into nested values (M01.03, 05–07).
3. Filter/sort/group using both files (M01.08).
4. Modify + save safely (M01.04, 09–11). Break a file on purpose and recover it (M01.10).
5. Git: create GitHub repo, push; then **deliberate conflict recipe** (below).
6. Build the tool. Commit with proper messages.

### Deliberate merge-conflict recipe (real remote required)
1. On `main`, add `build/todo_tool.py` with a `usage()` function; commit and push.
2. `git switch -c feature-a`; change the first line of `usage()`; commit.
3. `git switch main`; change the *same line differently*; commit.
4. `git merge feature-a` → conflict. Resolve by editing, `git add`, `git commit`.
5. Second variation: edit a line on GitHub's web UI, edit the same line locally, then `git pull`. Observe `fetch` first, then merge, then resolve.

### Build spec — `build/todo_tool.py` (CLI with `argparse`)
- `list --user N` shows todos for one user; `stats` prints completed vs incomplete per user; `add --user N --title "..."` appends a todo (new id = max+1) and saves.
- **Acceptance tests (manual):** file stays valid JSON after 10 adds; running `stats` twice gives consistent totals; corrupted JSON gives a friendly error, not a traceback; a backup exists before each write.
- Uses this milestone's uv project. Committed with ≥ 1 resolved conflict visible in `git log --graph`.

### Definition of Done
Atoms checked · build passes acceptance tests · README written by the learner · repo pushed · conflict resolved once on purpose.

### Verification statements (examples; answer True/False from memory)
1. `json.dumps` writes to a file. (False)
2. JSON allows single-quoted strings. (False)
3. `null` becomes `None` when loaded. (True)
4. `git pull` only downloads and never changes your working files. (False)
5. After fixing a conflicted file you must `git add` it before committing. (True)
6. Keys in a JSON object can be integers. (False; they are strings)

### Pitfalls
`json.dump` overwriting the whole file; forgetting `.gitignore` (committing `.venv`); resolving a conflict but leaving markers in the file; mixing up `dump/dumps` and `load/loads`.

### Teacher-AI prompt seed
Use the template in `06` §6. Insert: profile summary from `01` §4; "I already know uv (M00 done), do not re-teach"; the atom list above; the build spec; the evidence rules.

---

## MILESTONE 02 — APIs & HTTP (for real)

**Goal:** replace "an API is a link" with a working mental and practical model of HTTP requests.
**Prerequisites:** M00, M01 (JSON). **Packages:** `uv add requests python-dotenv rich`.
**Real data sources (verify availability before use):** JSONPlaceholder (fake but practice for POST/PUT/DELETE), Open-Meteo (free weather, no key), PokeAPI (free, no key). For key-based auth practice pick one free-key API (e.g. NASA Open APIs). 

### Atoms
- [ ] M02.01 Client–server model; one request → one response.
- [ ] M02.02 URL anatomy: scheme, host, port, path, query string, fragment.
- [ ] M02.03 Request anatomy: method, path, headers, optional body.
- [ ] M02.04 Response anatomy: status line, headers, body.
- [ ] M02.05 Methods: GET, POST, PUT, PATCH, DELETE; safe vs idempotent.
- [ ] M02.06 Status families 1xx–5xx and must-know codes: 200, 201, 204, 301/302, 400, 401, 403, 404, 405, 409, 422, 429, 500, 502, 503.
- [ ] M02.07 Headers: `Content-Type`, `Accept`, `Authorization`, `User-Agent`, `Retry-After`, rate-limit headers.
- [ ] M02.08 Path params vs query params vs body; `params=` in `requests`.
- [ ] M02.09 JSON bodies: `json=` vs `data=`.
- [ ] M02.10 `requests.get/post`, `.status_code`, `.json()`, `.text`, `.headers`, `.raise_for_status()`.
- [ ] M02.11 **Always set timeouts**; `requests.Session`; retry with backoff.
- [ ] M02.12 Error classes: `ConnectionError`, `Timeout`, `HTTPError`, JSON decode errors.
- [ ] M02.13 Auth types: API key (header/query), Bearer token, Basic auth; OAuth 2.0 *concept* (authorization code flow, access/refresh tokens).
- [ ] M02.14 Secrets hygiene: environment variables, `.env` + `python-dotenv`, `.gitignore`, rotating a leaked key.
- [ ] M02.15 Rate limits and 429 handling.
- [ ] M02.16 Pagination patterns: page/limit, cursor.
- [ ] M02.17 Read API docs: endpoints, params, response schema, examples; what OpenAPI/Swagger is.
- [ ] M02.18 Hand-test APIs: browser, `curl`, DevTools Network tab.
- [ ] M02.19 Cache responses to JSON on disk to avoid repeated calls.
- [ ] M02.20 What happens when you request a URL: DNS → TCP → TLS → HTTP (ties to CBSE Class 12 networks).
- [ ] M02.21 (optional) `httpx`/async preview.

### Ordered sequence
Browser + DevTools + `curl -i` first (see raw request/response) → `requests.get` on JSONPlaceholder → params and headers → POST/PUT/DELETE on JSONPlaceholder → error and timeout handling → Open-Meteo (real data) → key-based API with `.env` → caching → build.

### Build spec — `build/data_fetcher.py`
- Fetches real data (e.g. multi-day weather for 3+ cities via Open-Meteo, or PokeAPI records), validates responses, handles timeouts/HTTP errors/rate limits, caches to `data/cache/*.json`, writes a tidy summary JSON and prints a table with `rich`.
- Second script `build/auth_demo.py` calls a key-protected API with the key read from `.env`.
- **Acceptance tests:** works offline from cache; wrong URL and forced timeout each produce friendly messages; no secret appears in `git log -p`; `.env` is ignored.

### Verification statements (examples)
1. `POST` is idempotent by definition. (False)
2. A `404` means the server crashed. (False)
3. `requests.get(url)` waits forever by default. (True)
4. Putting an API key in the URL of a public repo's code is safe if the repo is small. (False)
5. `json=` sets `Content-Type: application/json` automatically. (True)

### Pitfalls
No timeout; committing `.env`; assuming 200 means valid data; treating `.json()` as always safe; hammering a free API.

---

## MILESTONE 03 — FastAPI + SQLAlchemy Backend (fix circular imports)

**Goal:** understand and control a real backend: routes, validation, DB layer, tests, import structure.
**Prerequisites:** M01, M02. Strongly helped by CBSE Class 12 SQL (Feb–Mar 2027).
**Packages (uv):** `fastapi`, `uvicorn` (or `fastapi[standard]`), `sqlalchemy`, `pydantic`, `pytest`, `httpx`, `alembic` (later). Confirm current CLI (`fastapi dev`) in docs.

### Atoms — Web layer
- [ ] M03.01 Server concepts: WSGI vs ASGI; what `uvicorn` does (listen on a port, speak HTTP, call the app). Run: `uv run uvicorn app.main:app --reload`.
- [ ] M03.02 App object, route decorators, HTTP-method decorators.
- [ ] M03.03 Path params with types; query params with defaults/optional; automatic 422 on bad input.
- [ ] M03.04 Request bodies with Pydantic models; `Field` constraints.
- [ ] M03.05 `response_model`, `status_code`, `HTTPException`.
- [ ] M03.06 `def` vs `async def`: event loop, I/O-bound benefit, never block inside `async def`; sync routes run in a threadpool.
- [ ] M03.07 Dependency injection with `Depends` (DB session, auth).
- [ ] M03.08 `APIRouter` and project layout.
- [ ] M03.09 Settings via environment (e.g. `pydantic-settings`).
- [ ] M03.10 CORS middleware (needed for M04).
- [ ] M03.11 Auto docs at `/docs` and `/redoc`.
- [ ] M03.12 Auth basics: never store plaintext passwords; hashing; token concept. (Implementation optional, late.)

### Atoms — Database layer
- [ ] M03.13 Map SQL knowledge to ORM: table ↔ class, row ↔ instance, column ↔ attribute.
- [ ] M03.14 SQLAlchemy 2.x style: `engine`, `Session`, `DeclarativeBase`, `Mapped[...]`, `mapped_column`.
- [ ] M03.15 `metadata.create_all` vs migrations (Alembic concept + one migration).
- [ ] M03.16 CRUD via session: add, get, `select()`, update, delete, commit, rollback.
- [ ] M03.17 Relationships: `ForeignKey`, `relationship`, `back_populates`; one-to-many; many-to-many with an association table; cascades.
- [ ] M03.18 Queries: filters, joins, `order_by`, `limit/offset`; lazy vs eager loading; the N+1 problem.
- [ ] M03.19 One session per request via a yielding dependency; closing it.
- [ ] M03.20 SQLite specifics: enable `PRAGMA foreign_keys=ON`; `check_same_thread` for FastAPI.

### Atoms — Circular imports (the learner's chronic pain)
- [ ] M03.21 Why they occur: import statements execute code; A imports B while B imports A; `sys.modules` holds a partially initialized module.
- [ ] M03.22 Fix toolbox in preference order: restructure (separate `db/base.py` from models; models never import services/routers); string names in `relationship("Model")`; `if TYPE_CHECKING:` for type-only imports; function-level imports as last resort.
- [ ] M03.23 Reproduce a circular import on a toy pair of files, read the traceback, fix it, then repeat in a model package.

### Atoms — Testing
- [ ] M03.24 `pytest` basics, fixtures, `TestClient`, dependency overrides with in-memory SQLite.
- [ ] M03.25 Test both happy paths and failure paths (404, 422, duplicates).

### Build spec — "Study Tracker API" (not FLUX, not the diary system)
- Tables: `topics` (1) → `sessions` (many) plus `tags` (many-to-many with topics).
- Endpoints: CRUD for all three; filters (by tag, date range); a stats endpoint (minutes per topic per week).
- **Acceptance:** ≥ 12 passing tests; app starts with `uv run`; `/docs` works; data persists across restarts; a documented circular-import incident (what, why, fix) in the README; one Alembic migration.
- **Optional read-along:** explain each file of the AI-written `AdvocateDiarySystem` layout back in his own words. Not a build target.

### Verification statements (examples)
1. `uvicorn` is the code that defines my routes. (False)
2. Putting `time.sleep(5)` inside an `async def` route blocks other requests. (True)
3. Circular imports are fixed by adding more imports. (False)
4. `relationship("Topic")` lets me reference a class before it is imported. (True)
5. SQLite enforces foreign keys by default. (False)

---

## MILESTONE 04 — Frontend Basics + Deployment (first full loop)

**Goal:** frontend → API → DB → **live URL**. Learn just enough HTML/CSS/JS to call his own API, then deploy.
**Prerequisites:** M03. **Constraint:** design method is "study examples, then vary"; never blank-canvas design (`06` §8).

### Atoms — HTML
- [ ] M04.01 Document skeleton, semantic tags (`header`, `nav`, `main`, `section`, `article`, `footer`).
- [ ] M04.02 Forms, inputs, labels, buttons, built-in validation attributes.
- [ ] M04.03 Lists, tables, links, images, accessibility basics (`alt`, labels).

### Atoms — CSS
- [ ] M04.04 Selectors, cascade, specificity, inheritance.
- [ ] M04.05 Box model, `display`, `position`.
- [ ] M04.06 Flexbox and Grid layouts.
- [ ] M04.07 Responsive design: viewport meta, relative units, media queries.
- [ ] M04.08 CSS variables; light/dark via `prefers-color-scheme`.
- [ ] M04.09 Spacing/typography/color decisions as tokens, copied from reference apps.

### Atoms — JavaScript
- [ ] M04.10 `let/const`, types, functions/arrow functions, arrays/objects, template strings.
- [ ] M04.11 DOM: `querySelector`, creating/updating elements, events, event delegation.
- [ ] M04.12 `fetch` GET/POST with JSON, `response.ok`, error handling.
- [ ] M04.13 Promises, `async/await`, `try/catch`.
- [ ] M04.14 State → render pattern (one state object, one render function).
- [ ] M04.15 DevTools: Elements, Console, Network, Application.
- [ ] M04.16 ES modules (`type="module"`), split into `api.js`, `state.js`, `ui.js`.
- [ ] M04.17 `localStorage` for small per-user conveniences.

### Atoms — Integration and deployment
- [ ] M04.18 CORS: what it is, why browsers enforce it, fix in FastAPI; alternative is serving the frontend from FastAPI via `StaticFiles`.
- [ ] M04.19 API base URL per environment.
- [ ] M04.20 What deployment means: a machine, a process, a port, a URL, HTTPS.
- [ ] M04.21 Production server: no `--reload`; workers; reverse proxy concept.
- [ ] M04.22 Config through environment variables; secrets in the platform dashboard.
- [ ] M04.23 Reproducible install on the server (`uv sync --frozen` or platform equivalent), pinned Python version.
- [ ] M04.24 Persistent data: ephemeral disks and SQLite risk; managed Postgres or a persistent volume; change SQLAlchemy URL/driver.
- [ ] M04.25 Logs and a health-check endpoint.
- [ ] M04.26 Choose a host with *currently* free terms (verify at the time; candidates: Render, Fly.io, PythonAnywhere for Python; GitHub Pages/Cloudflare Pages/Netlify for static). Note cold-start behavior.
- [ ] M04.27 (optional) GitHub Actions to run tests on every push.

### Build spec — deployed full-stack app
- New small app or an extension of the M03 Study Tracker: list/add/edit/delete with a filter and a stats view.
- Frontend pure HTML/CSS/JS (no framework). Built from ≥ 3 reference apps he screenshotted and annotated.
- **Acceptance:** live URL opened by someone else who completes a task; tests pass locally and (optionally) in CI; README includes an architecture diagram (boxes and arrows: browser → server → DB); secrets not in repo; documented free-tier limits.

### Verification statements (examples)
1. CORS is a server-side security feature that stops curl from working. (False; it is enforced by browsers)
2. `fetch()` rejects on HTTP 404 by default. (False; check `response.ok`)
3. SQLite on an ephemeral disk keeps my data forever. (False)
4. Flexbox is for two-dimensional layouts; Grid is for one-dimensional. (False; reversed)
5. `--reload` should be on in production. (False)

---

## Cross-links
- M01 ↔ CBSE 12 (file handling, CSV) · M02 ↔ CBSE 12 (networks: IP, HTTP, TCP/IP, URL) · M03 ↔ CBSE 12 (SQL, Python-SQL connectivity) and Phase 3 (system design).
- M04 web work is deliberately separate from Flutter (dropped).
