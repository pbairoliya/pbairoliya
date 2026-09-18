### Pratik Bairoliya

Software engineer at **Capital One**, on the team replacing the legacy third-party cores with
Prometheus FINCORE. I own the nightly **end-of-day close** — posting, settlement and ledger
cutoff for Card, Bank and Financial Service accounts. It runs on **Temporal**, it publishes
**99M+ Card accounts** downstream before morning, and it has to be right the first time.

Things I've built there: the ledger's batch write path in **Go**, from an empty repo to every
nightly cycle running through it. A **block-allocation ID service** so bulk account opens stop
contending for a shared sequence. The **PySpark/Databricks** reconciliation that compares
day-over-day aggregates and alerts before a bad cycle ships.

Outside work I build **local-first tools**: small systems that use a language model but run
entirely on your machine, so nothing personal leaves it. The part I find interesting isn't the
prompting — it's making nondeterministic output behave like software.

**The model proposes, deterministic code decides.** Categories the model suggests get thrown
away and reassigned by fixed rules, so a scheduled job produces the same thing today as
yesterday. Decisions live in append-only stores outside the generated text, so a rerun is
idempotent instead of destructive. An index is the source of truth, never the files. Everything
runs end-to-end in CI with the network, the model and the credentials stubbed out.

---

**[On-device tools](https://pbairoliya.github.io/projects/on-device-tools.html)** — three programs
sharing one OCR + local-LLM core
&nbsp;&nbsp;·&nbsp; [daily-lookback](https://github.com/pbairoliya/daily-lookback) — Calendar, Gmail
and iMessage into one generated daily note
&nbsp;&nbsp;·&nbsp; [grocery-receipts](https://github.com/pbairoliya/grocery-receipts) — scan any
receipt, get structured expenses and pantry stock
&nbsp;&nbsp;·&nbsp; [screenshot-organizer](https://github.com/pbairoliya/screenshot-organizer) — sort
a messy Desktop by reading what's in the images

**[lc](https://pbairoliya.github.io/projects/lc.html)** — a LeetCode workflow where an Obsidian note
is the source of truth, reconciled with a Git repo, with spaced-repetition reviews

**Systems and algorithms**
&nbsp;&nbsp;·&nbsp; [customBash](https://github.com/pbairoliya/customBash) — a Unix shell in C++:
process control, piping, redirection
&nbsp;&nbsp;·&nbsp; [ai-cops-and-robbers](https://github.com/pbairoliya/ai-cops-and-robbers) —
pursuit-evasion in C++/SFML, two agents running different search algorithms
&nbsp;&nbsp;·&nbsp; [ai-arcade-games](https://github.com/pbairoliya/ai-arcade-games) — a Deep
Q-Network agent that learns Snake
&nbsp;&nbsp;·&nbsp; [leetcode-archive](https://github.com/pbairoliya/leetcode-archive) — 600+
solutions, 2023–2024

---

`Go` `Python` `Java` `TypeScript` &nbsp;·&nbsp; `Kubernetes` `Temporal` `Docker` `Terraform`
`Argo CD` `Helm` &nbsp;·&nbsp; `AWS (EMR, S3, DynamoDB)` `Hive` `Databricks` `Spark` `Neo4j`
&nbsp;·&nbsp; `OpenTelemetry` `Splunk`

AWS Certified Solutions Architect – Associate &nbsp;·&nbsp; B.S. Computer Science + B.S. Applied
Mathematics, NC State (Park Scholar, 4.0)

[pbairoliya.github.io](https://pbairoliya.github.io) &nbsp;·&nbsp;
[LinkedIn](https://linkedin.com/in/pbairol) &nbsp;·&nbsp; pratik0520@gmail.com
