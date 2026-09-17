### Pratik Bairoliya

Software engineer at **Capital One**, on the team replacing the legacy third-party cores with
Prometheus FINCORE. I own nightly **End-of-Day settlement** for Card, Bank and Financial Service
accounts — millions of accounts, every night, and it has to be right by morning.

Outside work I build **local-first tools**: small systems that use a language model but run
entirely on your machine, so nothing personal leaves it. The part I find interesting isn't the
prompting — it's making nondeterministic output behave like software.

**The model proposes, deterministic code decides.** Categories the model suggests get thrown
away and reassigned by fixed rules, so a scheduled job produces the same thing today as
yesterday. Decisions live in append-only stores outside the generated text, so a rerun is
idempotent instead of destructive. An index is the source of truth, never the files. Everything
runs end-to-end in CI with the network, the model and the credentials stubbed out.

---

**[On-device tools](https://pb0224.github.io/projects/on-device-tools.html)** — three programs
sharing one OCR + local-LLM core
&nbsp;&nbsp;·&nbsp; [daily-lookback](https://github.com/pb0224/daily-lookback) — Calendar, Gmail
and iMessage into one generated daily note
&nbsp;&nbsp;·&nbsp; [grocery-receipts](https://github.com/pb0224/grocery-receipts) — scan any
receipt, get structured expenses and pantry stock
&nbsp;&nbsp;·&nbsp; [screenshot-organizer](https://github.com/pb0224/screenshot-organizer) — sort
a messy Desktop by reading what's in the images

**[lc](https://pb0224.github.io/projects/lc.html)** — a LeetCode workflow where an Obsidian note
is the source of truth, reconciled with a Git repo, with spaced-repetition reviews

---

`Go` `Python` `Java` `TypeScript` &nbsp;·&nbsp; `Kubernetes` `Temporal` `Docker` `Terraform`
`Argo` `Helm` &nbsp;·&nbsp; `AWS (EMR, S3, DynamoDB)` `Hive` `Postgres` `Neo4j`

AWS Certified Solutions Architect – Associate &nbsp;·&nbsp; B.S. Computer Science + B.S. Applied
Mathematics, NC State (Park Scholar, 4.0)

[pb0224.github.io](https://pb0224.github.io) &nbsp;·&nbsp;
[LinkedIn](https://linkedin.com/in/pbairol) &nbsp;·&nbsp; pratik0520@gmail.com
