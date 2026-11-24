# Acceptance Run Evidence: `gh_report`

**Date:** 2026-11-24  
**Environment:** Linux (Ubuntu), Python 3.14 via `uv`  
**Milestone:** Milestone 02 Hardening (`M2-8`)

---

## 1. Run With Token (Authenticated)
Command:
```bash
uv run python 02_APIs_HTTP/src/02_apis_http/build/gh_report/src/gh/main.py -i Arid-P -n 4
```

Output:
```text
                                Public Repositres                                
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ S.No. ┃ Name                    ┃ Stars ┃        Last Pushed        ┃ Forked? ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│     1 │ Programing-Workspace    │     1 │ 2026-11-24 11:33:00+00:00 │  False  │
│     2 │ Fixing_Fundamentals     │     1 │ 2026-11-24 11:26:08+00:00 │  False  │
│     3 │ CPP_PATH                │     0 │ 2026-11-19 14:18:08+00:00 │  False  │
│     4 │ FLUX                    │     1 │ 2026-10-14 12:49:49+00:00 │  False  │
│     5 │ The_Flux                │     0 │ 2026-10-11 15:02:08+00:00 │  False  │
│     6 │ Advocate-Diary-System   │     0 │ 2026-09-23 18:20:37+00:00 │  False  │
│     7 │ School_Managemnt_System │     0 │ 2026-09-19 18:56:32+00:00 │  False  │
│     8 │ NumGuessGame-           │     0 │ 2026-04-08 12:59:37+00:00 │  False  │
└───────┴─────────────────────────┴───────┴───────────────────────────┴─────────┘
                   Oeral Stats of Repositres                   
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ S.No. ┃ Name                 ┃ Stars ┃ Language ┃ Untouched ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│     1 │ Programing-Workspace │     1 │  Python  │   False   │
│     2 │ Fixing_Fundamentals  │     1 │  Python  │   False   │
│     3 │ CPP_PATH             │     0 │  Python  │   False   │
│     4 │ FLUX                 │     1 │  Kotlin  │   False   │
└───────┴──────────────────────┴───────┴──────────┴───────────┘
      Language Stats of Repositres       
┏━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ S.No. ┃ Language   ┃ % of Total Bytes ┃
┡━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│     1 │ Python     │            56.38 │
│     2 │ Kotlin     │            40.63 │
│     3 │ Java       │             1.08 │
│     4 │ C++        │             0.80 │
│     5 │ Shell      │             0.63 │
│     6 │ CSS        │             0.39 │
│     7 │ JavaScript │             0.05 │
│     8 │ HTML       │             0.04 │
└───────┴────────────┴──────────────────┘
╭─────────────────────────────────── GitHub Rate Limit Status ────────────────────────────────────╮
│                                                                                                 │
│  Total Rate Limit:        5000                                                                  │
│  Rate Limit Used:         N/A                                                                   │
│  Time Left Till Reset:     59 mins 20 sec                                                       │
│                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
Thankls for using this program.
```

Generated Summary (`data/output/summary_Arid-P.json`):
```json
{
    "user": "Arid-P",
    "generated_at": "2026-11-24 13:11:13.897993+00:00",
    "total_repos": 8,
    "total_stars": 3,
    "untouched_repos_90_days": [],
    "top_languages": {
        "Python": 56.382230455980675,
        "Kotlin": 40.62517416128728,
        "Java": 1.0795597587013381,
        "C++": 0.8013821439758931,
        "Shell": 0.6281337020588026
    },
    "rate_limit_remaining": "Cached used"
}
```
*Note on Correctness C3:* Total stars correctly sums to `3` (Programing-Workspace: 1, Fixing_Fundamentals: 1, FLUX: 1).
*Note on Correctness C4:* Seconds calculation properly displays `20 sec` instead of hardcoded `60 sec`.

---

## 2. Revalidation & Offline Cached Run (ETag / Cache Hit)
Command:
```bash
uv run python 02_APIs_HTTP/src/02_apis_http/build/gh_report/src/gh/main.py -i Arid-P -n 4
```

Output:
```text
[Public Repositories Table Rendered]
[Overall Stats Table Rendered]
[Language Stats Table Rendered]
Using cached data, so no rate limit checked
Thankls for using this program.
```

---

## 3. Unknown User Test (404 Nonexistent User)
Command:
```bash
uv run python src/02_apis_http/build/gh_report/src/gh/main.py -i nonexistent_user_xyz_12345
```

Output:
```text
Error: User 'nonexistent_user_xyz_12345' does not exist on GitHub.
User not found. No user exists with the name: nonexistent_user_xyz_12345
```

Verification:
```bash
ls -l 02_APIs_HTTP/src/02_apis_http/build/gh_report/data/output/summary_nonexistent_user_xyz_12345.json
ls: cannot access '...': No such file or directory
```
*Confirmed: Clean termination without traceback, and NO summary file is written.*

---

## 4. Git Ignore Verification for Secrets
Command:
```bash
git check-ignore -v 02_APIs_HTTP/src/02_apis_http/build/gh_report/data/.env 02_APIs_HTTP/.env
```

Output:
```text
02_APIs_HTTP/.gitignore:1:.env	02_APIs_HTTP/src/02_apis_http/build/gh_report/data/.env
02_APIs_HTTP/.gitignore:1:.env	02_APIs_HTTP/.env
```

---

## 5. History Secrets Leak Audit
Command:
```bash
git log -p --all | grep -E "ghp_|github_pat_"
```

Output:
```text
+    ghp_xxxxxxxxxxxxxxxxxxxx
+    GITHUB_TOKEN=ghp_yourActualSecretTokenHere
```
*Confirmed: Zero active/real secrets in git commit history; only dummy documentation placeholders exist.*

---

## 6. Security & Header Logging Verification
Command:
```bash
grep -c "Bearer" 02_APIs_HTTP/src/02_apis_http/build/gh_report/data/logs/app.log
```

Output:
```text
0
```

File permissions on `.env`:
```bash
ls -l 02_APIs_HTTP/src/02_apis_http/build/gh_report/data/.env
-rw------- 1 hp hp 80 Nov 24 16:07 02_APIs_HTTP/src/02_apis_http/build/gh_report/data/.env
```

---

## 7. Deferred Items (To Pytest with Mocks)
The following behaviors cannot be safely or reliably exercised against live GitHub endpoints without causing network IP rate-limit bans or requiring network tampering, and are formally deferred to unit tests with `pytest` and mocks:
1. Forced Network Timeout (needs socket/network mock).
2. Clean rate-limit exhaustion stop with 429/403 status and `X-RateLimit-Reset` timestamp simulation (needs mock HTTP adapter).
3. N-aware cache invalidation.
4. `If-None-Match` header sent on page 1 only.
5. Corrupt cache recovery.
6. 5xx exponential backoff wait.
