## Pratik Bairoliya

Software engineer at **Capital One**, on the team replacing the legacy third-party cores with
Prometheus FINCORE. I own the nightly **end-of-day close** — posting, settlement and ledger
cutoff for Card, Bank and Financial Service accounts. It runs on Temporal, it publishes 99M+
Card accounts downstream before morning, and it gets one shot to be right.

Most of that job is making a very large batch fail loudly and early instead of quietly at the
last minute. The ledger's batch write path is mine, in Go, from an empty repo to every nightly
cycle running through it. So is the block-allocation ID service that stopped bulk account opens
contending for a shared sequence, and the PySpark reconciliation that compares day-over-day
aggregates and alerts before a bad cycle ships.

Off the clock I build **local-first tools** — small systems that use a language model but run
entirely on your own machine. The interesting part isn't the prompting, it's making something
that guesses behave like something that doesn't.

> **The model proposes, deterministic code decides.** Categories it suggests get thrown away and
> reassigned by fixed rules, so a scheduled job produces the same thing today as yesterday.
> Decisions live in append-only stores outside the generated text, so a rerun is idempotent
> instead of destructive. An index is the source of truth, never the files. Everything runs
> end-to-end in CI with the network, the model and the credentials stubbed out.

<img alt="Contributions by year" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/contributions-light.svg#gh-light-mode-only" width="420"><img alt="Languages" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/languages-light.svg#gh-light-mode-only" width="420">
<img alt="Contributions by year" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/contributions-dark.svg#gh-dark-mode-only" width="420"><img alt="Languages" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/languages-dark.svg#gh-dark-mode-only" width="420">

<img alt="Stack" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/stack-light.svg#gh-light-mode-only" width="420">
<img alt="Stack" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/stack-dark.svg#gh-dark-mode-only" width="420">

### On-device tools

Three programs sharing one core — Apple Vision OCR, a local LLM, and a deterministic rules layer
on top. [Read how they fit together →](https://pbairoliya.github.io/projects/on-device-tools.html)

| | |
|---|---|
| **[daily-lookback](https://github.com/pbairoliya/daily-lookback)** | Calendar, Gmail and iMessage collapsed into one generated morning note. A missed night rebuilds the same note rather than duplicating it. |
| **[grocery-receipts](https://github.com/pbairoliya/grocery-receipts)** | Photograph a receipt, get structured expenses and pantry stock. Fingerprinted ingest, so a rescan can't double-count. |
| **[screenshot-organizer](https://github.com/pbairoliya/screenshot-organizer)** | Sorts a messy Desktop by reading what's actually in the images, with a human-in-the-loop review step. |

### Practice and earlier work

| | |
|---|---|
| **[lc](https://pbairoliya.github.io/projects/lc.html)** | A LeetCode workflow where an Obsidian note is the source of truth, reconciled with a Git repo, with spaced-repetition reviews. |
| **[customBash](https://github.com/pbairoliya/customBash)** | A Unix shell in C++ — process control, piping, redirection. |
| **[ai-cops-and-robbers](https://github.com/pbairoliya/ai-cops-and-robbers)** | Pursuit-evasion in C++/SFML, two agents running different search algorithms against each other. |
| **[ai-arcade-games](https://github.com/pbairoliya/ai-arcade-games)** | Snake as an RL environment, plus an unfinished Deep Q-Network. Kept honest about where it stops. |
| **[leetcode-archive](https://github.com/pbairoliya/leetcode-archive)** | 200 problems, 2023–24, unedited first drafts. |

---

AWS Certified Solutions Architect – Associate &nbsp;·&nbsp; B.S. Computer Science + B.S. Applied
Mathematics, NC State — Park Scholar, 4.0

[pbairoliya.github.io](https://pbairoliya.github.io) &nbsp;·&nbsp;
[LinkedIn](https://linkedin.com/in/pbairol) &nbsp;·&nbsp;
[pratik0520@gmail.com](mailto:pratik0520@gmail.com)
