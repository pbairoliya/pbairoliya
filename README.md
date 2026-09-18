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

<p>
  <a href="https://linkedin.com/in/pbairol"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="https://pbairoliya.github.io"><img alt="Website" src="https://img.shields.io/badge/Website-111111?style=flat-square&logo=github&logoColor=white"></a>
  <a href="mailto:pratik0520@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white"></a>
  <img alt="AWS SAA" src="https://img.shields.io/badge/AWS%20Certified-Solutions%20Architect%20Associate-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white">
</p>

<img alt="GitHub stats" height="150" src="https://github-readme-stats.vercel.app/api?username=pbairoliya&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&theme=default#gh-light-mode-only">
<img alt="Top languages" height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=pbairoliya&layout=compact&hide_border=true&langs_count=8&theme=default#gh-light-mode-only">
<img alt="GitHub stats" height="150" src="https://github-readme-stats.vercel.app/api?username=pbairoliya&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&theme=dark&bg_color=0d1117#gh-dark-mode-only">
<img alt="Top languages" height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=pbairoliya&layout=compact&hide_border=true&langs_count=8&theme=dark&bg_color=0d1117#gh-dark-mode-only">


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

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-E76F00?style=flat-square&logo=openjdk&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Temporal](https://img.shields.io/badge/Temporal-000000?style=flat-square&logo=temporal&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo%20CD-EF7B4D?style=flat-square&logo=argo&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white)

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![Hive](https://img.shields.io/badge/Apache%20Hive-FDEE21?style=flat-square&logo=apachehive&logoColor=black)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)

![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)
![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat-square&logo=splunk&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)

AWS Certified Solutions Architect – Associate &nbsp;·&nbsp; B.S. Computer Science + B.S. Applied
Mathematics, NC State (Park Scholar, 4.0)

[pbairoliya.github.io](https://pbairoliya.github.io) &nbsp;·&nbsp;
[LinkedIn](https://linkedin.com/in/pbairol) &nbsp;·&nbsp; pratik0520@gmail.com
