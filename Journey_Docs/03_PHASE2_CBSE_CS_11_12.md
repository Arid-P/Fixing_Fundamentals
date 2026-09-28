# 03 — Phase 2: CBSE Computer Science, Class 11 and Class 12

**Why this phase exists:** the learner teaches his younger brother (school, CBSE) and wants to learn the
syllabus properly first. It also fills real gaps (number systems, Boolean logic, networking, SQL, file handling).
**Deadlines (learner's):** Class 11 fully learned by **31 Dec 2026**; Class 12 by **31 Mar 2027**.
**Source of truth:** official CBSE syllabus, Computer Science (083), 2026-27:
`https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Computer_Science_SecP2_2026-27.pdf`
(fetched 2026-09-28). **Re-check it each academic year;** syllabi change.
**Textbooks:** NCERT Computer Science textbooks for Class XI and XII (free PDFs on ncert.nic.in), plus CBSE support material and sample papers on the CBSE academic site. Verify current links yourself.

Atom legend: `[ ]` not started · `[~]` partial · `[x]` verified. Since he already writes Python, mark Python atoms only after the diagnostic (§7) or a cold-write test.

---

## 1. Marks structure (official)

| Class | Theory (70) | Practical (30) |
|---|---|---|
| **XI** | Unit 1 Computer Systems & Organisation 10 · Unit 2 Computational Thinking & Programming-I 45 · Unit 3 Society, Law & Ethics 15 | Lab test 12 (60% logic, 20% documentation, 20% code quality) · Report file (min. 20 Python programs) 7 + viva 3 · Project 8 |
| **XII** | Unit 1 Computational Thinking & Programming-2: 40 · Unit 2 Computer Networks 10 · Unit 3 Database Management 20 | Lab test: Python 8 + SQL (4 queries on 1–2 tables) 4 · Report file: min. 15 Python programs, 5 SQL sets, 4 Python-SQL programs: 7 · Project 8 · Viva 3 |

---

## 2. CLASS 11 ATOMS

### Unit 1 — Computer Systems and Organisation (10 marks)
- [ ] C11-U1-01 Basic organisation: hardware vs software; input device, output device, CPU.
- [ ] C11-U1-02 Memory types: primary, cache, secondary; speed/size/cost ordering.
- [ ] C11-U1-03 Units of memory: bit, byte, KB, MB, GB, TB, PB (1 KB = 1024 B).
- [ ] C11-U1-04 Types of software: system software (OS, utilities, device drivers), programming tools, application software.
- [ ] C11-U1-05 Language translators: assembler, compiler, interpreter (differences).
- [ ] C11-U1-06 Operating system functions and user interfaces (CLI/GUI).
- [ ] C11-U1-07 Boolean logic: NOT, AND, OR, NAND, NOR, XOR; truth tables.
- [ ] C11-U1-08 De Morgan's laws; simplify small expressions; draw logic circuits.
- [ ] C11-U1-09 Number systems: binary, octal, decimal, hexadecimal and conversions in all directions (including fractions if the textbook includes them).
- [ ] C11-U1-10 Encoding schemes: ASCII, ISCII, Unicode (UTF-8, UTF-32).

### Unit 2 — Computational Thinking and Programming-I (45 marks)
Problem solving
- [ ] C11-U2-01 Steps of problem solving: analyse, algorithm, code, test, debug.
- [ ] C11-U2-02 Flowchart symbols and drawing; pseudocode; decomposition.
Python basics
- [ ] C11-U2-03 Features of Python; interactive vs script mode; "hello world".
- [ ] C11-U2-04 Character set and tokens: keyword, identifier, literal, operator, punctuator.
- [ ] C11-U2-05 Variables, l-value vs r-value, comments.
- [ ] C11-U2-06 Data types: int, float, complex, bool, str, list, tuple, dict, `None`.
- [ ] C11-U2-07 Mutable vs immutable types.
- [ ] C11-U2-08 Operators: arithmetic, relational, logical, assignment, augmented assignment, identity (`is`, `is not`), membership (`in`, `not in`).
- [ ] C11-U2-09 Precedence, expression evaluation, implicit and explicit type conversion.
- [ ] C11-U2-10 Console input/output.
- [ ] C11-U2-11 Errors: syntax, logical, run-time.
Control flow
- [ ] C11-U2-12 Indentation; sequential, conditional, iterative flow.
- [ ] C11-U2-13 `if`, `if-else`, `if-elif-else` with flowcharts (absolute value, sort 3 numbers, divisibility).
- [ ] C11-U2-14 `for`, `range()`, `while`, `break`, `continue`, nested loops; patterns, series sums, factorial.
Strings
- [ ] C11-U2-15 String operations: concatenation, repetition, membership, slicing; traversal with loops.
- [ ] C11-U2-16 String methods (must recall exact behavior): `len, capitalize, title, lower, upper, count, find, index, endswith, startswith, isalnum, isalpha, isdigit, islower, isupper, isspace, lstrip, rstrip, strip, replace, join, partition, split`.
Lists
- [ ] C11-U2-17 Lists: indexing, operations, traversal, nested lists.
- [ ] C11-U2-18 List functions/methods: `len, list, append, extend, insert, count, index, remove, pop, reverse, sort, sorted, min, max, sum`.
- [ ] C11-U2-19 List programs: max/min/mean, linear search, frequency counting.
Tuples
- [ ] C11-U2-20 Tuples: indexing, operations, tuple assignment, nested tuples; `len, tuple, count, index, sorted, min, max, sum`.
- [ ] C11-U2-21 Tuple programs (min/max/mean, linear search, frequency).
Dictionaries
- [ ] C11-U2-22 Dictionaries: keys access, mutability, traversal.
- [ ] C11-U2-23 Dict functions/methods: `len, dict, keys, values, items, get, update, del, clear, fromkeys, copy, pop, popitem, setdefault, max, min, sorted`.
- [ ] C11-U2-24 Dict programs (character counting, employee/salary dictionary).
Modules
- [ ] C11-U2-25 `import module` vs `from module import name`.
- [ ] C11-U2-26 `math`: `pi, e, sqrt, ceil, floor, pow, fabs, sin, cos, tan`.
- [ ] C11-U2-27 `random`: `random, randint, randrange` (know endpoints included/excluded).
- [ ] C11-U2-28 `statistics`: `mean, median, mode`.

### Unit 3 — Society, Law and Ethics (15 marks)
- [ ] C11-U3-01 Digital footprints (active vs passive).
- [ ] C11-U3-02 Netizen and etiquette: net, communication, social media.
- [ ] C11-U3-03 Intellectual property: copyright, patent, trademark; violations (plagiarism, infringement).
- [ ] C11-U3-04 Open source and licences: Creative Commons, GPL (copyleft), Apache (permissive).
- [ ] C11-U3-05 Cyber crime types: hacking, eavesdropping, phishing/fraud emails, ransomware, trolling, bullying.
- [ ] C11-U3-06 Cyber safety: safe browsing, identity protection, confidentiality.
- [ ] C11-U3-07 Malware: viruses, trojans, adware.
- [ ] C11-U3-08 E-waste management.
- [ ] C11-U3-09 Information Technology Act (IT Act).
- [ ] C11-U3-10 Technology and society: gender and disability issues in teaching/using computers.

### Class 11 practicals (official suggested list; record file needs ≥ 20 programs, write them all himself)
Welcome message input/display · larger/smaller of two numbers · largest/smallest of three · three star/number/letter patterns with nested loops · four series sums (in `x` and `n`, alternating signs, `x^k/k`, `x^k/k!`) · perfect/Armstrong/palindrome numbers · prime vs composite · Fibonacci terms · GCD and LCM · count vowels/consonants/upper/lower in a string · palindrome string and case conversion · largest/smallest in a list/tuple · swap even/odd positioned list elements · search in list/tuple · dictionary of roll/name/marks and students above 75.
To reach 20, add his own variants (each with documentation and clean code, since the lab test scores logic/documentation/code quality 60/20/20).
**Class 11 project (8 marks):** something tangible using most concepts learned.

---

## 3. CLASS 12 ATOMS

### Unit 1 — Computational Thinking and Programming-2 (40 marks)
- [ ] C12-U1-01 Revision of all Class 11 Python (retest via diagnostic §7).
- [ ] C12-U1-02 Function types: built-in, module functions, user-defined.
- [ ] C12-U1-03 Defining functions; arguments vs parameters; default and positional parameters; returning one or many values.
- [ ] C12-U1-04 Flow of execution; scope: local vs global (`global` keyword).
- [ ] C12-U1-05 Exception handling: `try/except/finally`; multiple except blocks.
- [ ] C12-U1-06 Files: text, binary, CSV; relative vs absolute paths.
- [ ] C12-U1-07 Text files: open modes `r, r+, w, w+, a, a+`; behavior of each (truncate/create/append).
- [ ] C12-U1-08 Text files: `close`, `with`, `write`, `writelines`, `read`, `readline`, `readlines`, `seek`, `tell`; data manipulation (count, replace, filter lines).
- [ ] C12-U1-09 Binary files: modes `rb, rb+, wb, wb+, ab, ab+`; `import pickle`; `dump`/`load`; create, read, search, append, update records; `EOFError` handling.
- [ ] C12-U1-10 CSV: `import csv`; `writer`, `writerow`, `writerows`; `reader`; search a row.
- [ ] C12-U1-11 Stack: LIFO, push/pop, implementation using a list; overflow/underflow reasoning.

### Unit 2 — Computer Networks (10 marks)
- [ ] C12-U2-01 Evolution: ARPANET, NSFNET, Internet.
- [ ] C12-U2-02 Data communication: sender, receiver, message, medium, protocols.
- [ ] C12-U2-03 Capacity: bandwidth, data transfer rate; IP address.
- [ ] C12-U2-04 Switching: circuit vs packet.
- [ ] C12-U2-05 Transmission media: twisted pair, coaxial, fibre-optic; radio, micro, infrared waves.
- [ ] C12-U2-06 Devices: modem, Ethernet card, RJ45, repeater, hub, switch, router, gateway, WiFi card.
- [ ] C12-U2-07 Network types: PAN, LAN, MAN, WAN; topologies: bus, star, tree.
- [ ] C12-U2-08 Protocols: HTTP, HTTPS, FTP, PPP, SMTP, POP3, TCP/IP, TELNET, VoIP (which sends, which receives).
- [ ] C12-U2-09 Web: WWW, HTML, XML, domain names, URL, website, browser, web server, hosting.

### Unit 3 — Database Management (20 marks)
- [ ] C12-U3-01 Need for databases; DBMS advantages.
- [ ] C12-U3-02 Relational model: relation, attribute, tuple, domain, **degree (columns)**, **cardinality (rows)**.
- [ ] C12-U3-03 Keys: candidate, primary, alternate, foreign.
- [ ] C12-U3-04 Data types: `char(n)`, `varchar(n)`, `int`, `float`, `date`; constraints: `not null`, `unique`, `primary key`.
- [ ] C12-U3-05 DDL: `create database`, `use`, `show databases`, `drop database`, `show tables`, `create table`, `describe`, `alter table` (add/remove attribute, add/remove primary key), `drop table`.
- [ ] C12-U3-06 DML: `insert`, `select`, `update`, `delete`.
- [ ] C12-U3-07 `select` details: operators (math, relational, logical), aliasing, `distinct`, `where`, `in`, `between`, `order by`, `like` (`%`, `_`), meaning of NULL, `is null`, `is not null`.
- [ ] C12-U3-08 Aggregates: `max, min, avg, sum, count` (`count(*)` vs `count(col)` and NULLs).
- [ ] C12-U3-09 `group by`, `having` (WHERE vs HAVING).
- [ ] C12-U3-10 Joins: Cartesian product (rows multiply), equi-join, natural join.
- [ ] C12-U3-11 Python-SQL connectivity: `connect()`, `cursor()`, `execute()`, `commit()`, `fetchone()`, `fetchall()`, `rowcount`; insert/update/delete/select from Python; `%s` placeholders or `format()`.
- [ ] C12-U3-12 Build a small connectivity application (menu-driven, database-backed).

### Class 12 practicals (official suggested list)
Python: read a text file line by line and print words separated by `#` · count vowels/consonants/upper/lower in a file · remove lines containing `a` and write to another file · binary file of name+roll: search by roll · binary file of roll+name+marks: update marks by roll · dice simulator with random numbers 1–6 · stack using a list · CSV of user-id/password with password search.
SQL: create a `student` table and insert data; then `ALTER` (add/modify/drop attribute), `UPDATE`, `ORDER BY` asc/desc, `DELETE`, `GROUP BY` with min/max/sum/count/avg; repeat similar exercises for other tables. Connect SQL with Python.
Report file minimums: 15 Python programs, 5 SQL query sets (1–2 tables), 4 Python-SQL connectivity programs.
**Class 12 project (8 marks):** useful, real-world, built on file handling or Python-SQL connectivity (the official note says groups of 2–3 and start ≥ 6 months before submission; for the learner, start choosing the idea in Jan 2027).

---

## 4. Environment note: CBSE uses MySQL, not SQLite

The learner's past SQL was sqlite3/SQLAlchemy. Differences that matter for exams and practicals:

| Topic | MySQL (CBSE) | SQLite |
|---|---|---|
| Admin commands | `SHOW DATABASES`, `SHOW TABLES`, `USE db`, `DESCRIBE t` | none of these (uses `.tables`, `.schema` shell commands) |
| Add primary key later | `ALTER TABLE t ADD PRIMARY KEY(col)` | not supported like this |
| Auto ID | `AUTO_INCREMENT` | `AUTOINCREMENT` / rowid |
| Python placeholders | `%s` (mysql-connector) | `?` (sqlite3) |
| Typing | strict types | flexible typing |

**Setup on Ubuntu (verify commands against current docs):**
```bash
sudo apt update && sudo apt install mysql-server      # MariaDB (mariadb-server) also matches syllabus syntax
sudo systemctl status mysql
sudo mysql                                             # root shell via auth_socket
# inside: CREATE DATABASE school; CREATE USER 'learner'@'localhost' IDENTIFIED BY '...'; GRANT ALL ON school.* TO 'learner'@'localhost';
uv add mysql-connector-python                          # in the practice project
```
Never put real passwords in git; use `.env` (see M02.14).
Security aside: the syllabus allows `%s` or `format()`. Always prefer `%s` parameters (safe from SQL injection); string-formatting user input into SQL is unsafe.

---

## 5. Schedule (week 1 = week of 28 Sep 2026)

**Class 11 (13 weeks × 2 h = ~26 h).** Write the record-file programs *as topics are covered*, not at the end.

| Week | Content (atoms) |
|---|---|
| 1 | U1-01..06 (organisation, memory, software, translators, OS) |
| 2 | U1-09 number systems and conversions (heavy; do drills) |
| 3 | U1-07..08, U1-10 Boolean logic, De Morgan, circuits (CircuitVerse), encoding |
| 4 | U2-01..07 problem solving, flowcharts, Python basics, tokens, types, mutability |
| 5 | U2-08..13 operators, conversion, I/O, errors, conditionals |
| 6 | U2-14 loops, patterns, series programs |
| 7 | U2-15..16 strings and method drills |
| 8 | U2-17..21 lists and tuples |
| 9 | U2-22..28 dictionaries and modules |
| 10 | Finish 20-program record file; cold-write test of every method list |
| 11 | U3 all (read NCERT chapter; write your own 1-page summary per topic) |
| 12 | Class 11 project + viva questions |
| 13 | Two full sample papers; repair gaps; retest weak atoms |

**Class 12 (13 weeks × 3 h = ~39 h), Jan–Mar 2027.**

| Week | Content |
|---|---|
| 1 | U1-01..04 revision, functions, scope |
| 2 | U1-05..06 exceptions, file types, paths |
| 3 | U1-07..08 text files |
| 4 | U1-09 binary files, pickle |
| 5 | U1-10..11 CSV, stack |
| 6 | U2-01..06 networks part 1 |
| 7 | U2-07..09 networks part 2 |
| 8 | U3-01..05 database concepts, keys, MySQL install, DDL |
| 9 | U3-06..07 DML, `select` details |
| 10 | U3-08..10 aggregates, group by/having, joins |
| 11 | U3-11..12 Python-SQL connectivity, 4+ programs |
| 12 | Complete report-file minimums; project |
| 13 | Sample papers; repair gaps; retest |

**Teach-back protocol (with brother, from Class 11 on):** after each unit, explain it aloud using no notes; note every question the brother gets wrong or you hesitate on; log the "fumbles" in the phase README. Teaching is a verification step, not an extra.

---

## 6. Overlaps with other phases (do once, use twice)
- Number systems + Boolean logic ↔ Phase 3 Block 1 (binary, gates, CircuitVerse, C++ binary adder).
- File handling, CSV, JSON ↔ Milestone 01.
- Networks (IP, HTTP, URL, TCP/IP) ↔ Milestone 02.
- Stack ↔ DSA (stack) ↔ C++ Block 3.
- SQL + Python connectivity ↔ Milestone 03 (SQLAlchemy).

---

## 7. Diagnostic (run before starting; answer True/False from memory)

Ask the learner to answer each numbered statement. The PLANNER then marks atoms `[x]` only where he was correct *and* could state why. **Answer key is at the very end, for the PLANNER only.**

### Class 11 statements
1. `type(3+4j)` is `complex`.
2. `5 / 2` evaluates to `2`.
3. `-5 // 2` evaluates to `-3`.
4. `==` compares identity and `is` compares values.
5. Strings in Python are mutable.
6. `my_list.sort()` returns a new sorted list and leaves `my_list` unchanged.
7. `sorted((3,1,2))` returns a tuple.
8. `d.get("k")` raises `KeyError` if `"k"` is missing.
9. `d.setdefault("k", 5)` inserts `"k": 5` if `"k"` is missing and returns the value for `"k"`.
10. `"abc".partition("b")` returns `('a', 'b', 'c')`.
11. `"hello".find("z")` returns `-1`, while `"hello".index("z")` raises `ValueError`.
12. `"a b  c".split()` returns `['a', 'b', 'c']`.
13. `list(range(2, 10, 3))` is `[2, 5, 8]`.
14. `break` skips only the current iteration and continues the loop.
15. After `a = b = []`, `a` and `b` are two independent lists.
16. `(5)` is a tuple with one element.
17. `x.extend([1,2])` and `x.append([1,2])` produce the same list.
18. `del d["k"]` removes the key `"k"` from dictionary `d`.
19. `random.randint(1, 6)` can return `6`, and `random.randrange(1, 6)` can also return `6`.
20. `statistics.mode([1,2,2,3])` returns `2`.
21. `math.ceil(-2.5)` is `-2`.
22. A syntax error is detected before the program starts running.
23. `'a' + 1` raises `TypeError`.
24. `int("3.5")` returns `3`.
25. `bool("False")` is `True`.
26. Python identifiers are case-sensitive.
27. Binary `1011` equals decimal `11`.
28. Hex `1F` equals decimal `31`.
29. Standard ASCII represents 128 characters using 7 bits.
30. UTF-8 always uses exactly 4 bytes per character.
31. De Morgan: NOT(A AND B) equals (NOT A) OR (NOT B).
32. XOR outputs 1 when its two inputs are different.
33. A compiler translates the whole program before execution; an interpreter translates and runs statement by statement.
34. Cache memory is faster and smaller than main memory.
35. Copyright protects ideas themselves, not just how they are expressed.
36. The GPL requires derivative works to be shared under the same licence terms (copyleft).

### Class 12 statements
37. In a function definition, parameters with default values must come after those without.
38. A variable assigned inside a function is global by default.
39. `finally` runs only when an exception occurs.
40. `open(f, "w")` appends if the file already exists.
41. Mode `"a+"` opens for appending and reading.
42. Mode `"r+"` creates the file if it does not exist.
43. `readlines()` returns a list of strings that include newline characters.
44. `seek(0)` moves the file position to the start.
45. `pickle.load(f)` raises `EOFError` when there are no more objects.
46. `writerows` in `csv.writer` takes a list of rows.
47. A stack follows FIFO order.
48. `list.pop()` with no argument removes the last element.
49. A relative path depends on the current working directory.
50. ARPANET came before the Internet.
51. A hub forwards data only to the intended device; a switch sends to all devices.
52. A router forwards packets between networks using IP addresses.
53. SMTP is used to receive emails.
54. Packet switching breaks data into packets that may take different routes.
55. A primary key column can contain `NULL`.
56. A foreign key refers to the primary key of another table.
57. Degree is the number of rows and cardinality is the number of columns.
58. `DELETE FROM t;` without `WHERE` removes all rows.
59. `WHERE` filters rows before grouping and `HAVING` filters groups after aggregation.
60. `COUNT(*)` counts rows with NULLs, but `COUNT(col)` ignores NULLs in `col`.
61. `LIKE '_a%'` matches strings whose second character is `a`.
62. In SQL, `NULL = NULL` evaluates to true.
63. The Cartesian product of tables with 4 and 5 rows has 9 rows.
64. A natural join joins on all columns having the same name in both tables.
65. `INSERT`, `UPDATE`, `DELETE` from Python need `commit()` to be saved.
66. Building SQL by string-formatting user input is safe from SQL injection.

---

### PLANNER-ONLY answer key (do not show before the learner answers)
1 T · 2 F (2.5) · 3 T · 4 F (reversed) · 5 F · 6 F (returns None, sorts in place) · 7 F (returns list) · 8 F (returns None) · 9 T · 10 T · 11 T · 12 T · 13 T · 14 F (that is `continue`) · 15 F (same object) · 16 F (needs comma) · 17 F · 18 T · 19 F (`randrange` excludes end) · 20 T · 21 T · 22 T · 23 T · 24 F (`ValueError`) · 25 T · 26 T · 27 T · 28 T · 29 T · 30 F (variable 1–4 bytes; UTF-32 is fixed 4) · 31 T · 32 T · 33 T · 34 T · 35 F (expression, not ideas) · 36 T · 37 T · 38 F (local) · 39 F (always runs) · 40 F (truncates) · 41 T · 42 F · 43 T · 44 T · 45 T · 46 T · 47 F (LIFO) · 48 T · 49 T · 50 T · 51 F (reversed) · 52 T · 53 F (SMTP sends; POP3 receives) · 54 T · 55 F · 56 T · 57 F (reversed) · 58 T · 59 T · 60 T · 61 T · 62 F (use `IS NULL`) · 63 F (20) · 64 T · 65 T · 66 F.
