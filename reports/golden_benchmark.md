# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1271.1 ms**
- Average token reduction vs full source context: **3.0%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1533.1 | 788 | 0.0% |  |
| G09 | semantic | PASS | 477.3 | 549 | 0.0% |  |
| G10 | semantic | PASS | 500.1 | 186 | 59.5% |  |
| G14 | mixed | PASS | 1825.6 | 1122 | 0.0% |  |
| G03 | long_term | PASS | 1358.1 | 1419 | 0.0% |  |
| G04 | long_term | PASS | 2417.9 | 1431 | 0.0% |  |
| G07 | episodic | PASS | 259.4 | 481 | 0.0% |  |
| G08 | episodic | PASS | 260.7 | 502 | 0.0% |  |
| G11 | mixed | PASS | 1800.0 | 1278 | 0.0% |  |
| G13 | mixed | PASS | 826.0 | 988 | 0.0% |  |
| G15 | mixed | PASS | 2138.3 | 1891 | 0.0% |  |
| G16 | mixed | PASS | 2083.6 | 1405 | 0.0% |  |
| G17 | mixed | PASS | 2053.5 | 1481 | 0.0% |  |
| G18 | mixed | PASS | 867.8 | 734 | 0.0% |  |
| G19 | mixed | PASS | 1856.2 | 1462 | 0.0% |  |
| G05 | long_term | PASS | 1574.5 | 1411 | 0.0% |  |
| G12 | mixed | PASS | 1794.5 | 1200 | 0.0% |  |
| G20 | mixed | PASS | 1794.2 | 1682 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: LOTUS-88 uses Java for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: LOTUS-88 uses Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z]  <USER_SUMMARY> The user's project is LOTUS-88, prioritizing Java and Spring Boot for b`

### G09 - semantic

`ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3, from internal-api-guideline-v3 updated on 2026-08-10. ENTITY: POST /payments - POST /payments requires that every retryable request must send the same Idempotency-Key. Retries should only occur for HTTP 429 or transient 5xx errors, utilize exponential backoff, and cease after a maximum of three retries, as per PAYMENT-RULE-3. ENTITY: PAYMENT-RULE-3 - PAYMENT-RULE-3 requires that every retryable request to POST /payments must send the same Idempotency-Key. R`

### G10 - semantic

`ENTITY: Agent Memory Privacy Rule - Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store, identified by the marker DELETE-VERIFY-ALL. This rule was last updated on August 12, 2026. ENTITY: short-term context -  ENTITY: semantic context -  ENTITY: Memory Context Budget - This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, and semantic 3 percent context for memory. Lower-priority memory is trimmed first. Marker: BUDGET-10-4-3-3. ENTITY: long-term context -  ENTITY: episodic context -  ENTITY: semantic memory - This lab uses semantic memory at 3 percent. ENTITY: short-term memory - Th`

### G14 - mixed

`<LONG_TERM> FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: LOTUS-88 uses Java for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: LOTUS-88 uses Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z]  <USER_SUMMARY> The user's project is LOTUS-88, prioritizing Java and Sprin`

### G03 - long_term

`FACT: Minh Nguyen prefers Python for personal demo ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-05T08:00:00Z] FACT: Demo ca nhan ORCHID-27 prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen uses Python for personal demo ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Demo ca nhan ORCHID-27 avoids Java. [`

### G04 - long_term

`FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen tried increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen has a to-do item to complete the benchmark report before Friday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen's personal project is ORCHID-27`

### G07 - episodic

`Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan. Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc cua backend cong ty, va cach danh dau request payment de khong trung don. Hom nay toi debug async H`

### G08 - episodic

`Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan. Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay style hay stack cua nguoi khac. Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry paymen`

### G11 - mixed

`<LONG_TERM> FACT: Minh Nguyen tried increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-05T08:00:00Z] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Demo ca nhan ORCHID-27 avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid`

### G13 - mixed

`<EPISODIC> Mai hop mentor, toi nay minh muon don open-loop. Liet ke viec chua dong, deadline, va ma dinh danh task. Can du ba manh de ghi vao note hop. Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan. Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay style hay stack cua nguoi khac. Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem`

### G15 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: The issue with async HTTP still failed after increasing the timeout. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen requested that the topic of async/await be explained using a timeline if encountered in the future. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen tried increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Demo ca nhan ORCHID-27 prioritizes Python. [valid_at=2026-08-01T09:00:2`

### G16 - mixed

`<LONG_TERM> FACT: The benchmark report is an open loop with the identifier LAB-REPORT-1600. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: The Lab Assistant is checking concurrency. [valid_at=2026-08-03T10:01:00Z, invalid_at=None] FACT: Minh Nguyen has a to-do item to complete the benchmark report before Friday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen tried increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: The Lab As`

### G17 - mixed

`<LONG_TERM> FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Coroutine has priority over Task when explaining. [valid_at=2026-08-01T09:02:20Z, invalid_at=None] FACT: Minh Nguyen requested that the topic of async/await be explained using a timeline if encountered in the future. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen believes`

### G18 - mixed

`<EPISODIC> Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. Cong ty yeu cau chinh context window cho agent tren dung backend du an cong ty. Minh can biet stack bat buoc cua BLUEBIRD va ty le budget bon tang nho trong lab de cau hinh cho dung, khong dung so thich project rieng. Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc cua backend cong ty, va cach danh dau request payment de khong trung don. Ten du an ca nhan `

### G19 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen believes that effectively reusing the aiohttp ClientSession is a good strategy. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: The issue with async HTTP still failed after increasing the timeout. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:00Z] FACT: Minh Nguyen requested that the topic of async/await be explained using a timeline if encountered in the future. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen uses Python for personal demo OR`

### G05 - long_term

`FACT: Minh Nguyen requires TypeScript for the backend of project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen requires NestJS for the backend of project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-05T08:00:00Z] FACT: Python is prohibited for the backend of project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen prefers Python for personal demo ORCHID-27. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Demo ca nhan ORCHID-27 prioritizes Python. [valid_at=2026-08-01T09:00:20`

### G12 - mixed

`<LONG_TERM> FACT: Minh Nguyen requires NestJS for the backend of project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Project BLUEBIRD-42 requires TypeScript for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Project BLUEBIRD-42 requires NestJS for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen requires TypeScript for the backend of project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Python is prohibited for the backend of project BLUEBIRD-42. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The da tach scope BLUEBIRD-42 us`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
