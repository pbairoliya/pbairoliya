<h3 align="center">Pratik Bairoliya</h3>
<p align="center">
  <b>Every night, a bank has to close its books. I own that job.</b><br>
  <sub>Full-stack software engineer · Capital One · Go, Temporal, Kubernetes, Spark</sub>
</p>

---

At **Capital One** I own the nightly **end-of-day close** — posting, settlement and ledger cutoff
for Card, Bank and Financial Service accounts, on the platform replacing the third-party cores the
bank ran on for decades.

It runs on **Temporal**. It publishes **99M+ Card accounts** downstream before morning. It gets
**one shot** — there is no re-running the day. Most of my job is making a very large batch fail
loudly and early instead of quietly at 4am.

**Shipped, mine end to end:**

- 🏗️ The ledger's **batch write path in Go** — empty repo to production. Every nightly cycle runs through it.
- 🔑 A **block-allocation ID service**: one call reserves a range, taking per-ID contention off bulk account opens.
- 🔍 The **PySpark reconciliation** that diffs day-over-day aggregates and alerts *before* a bad cycle ships.
- 📉 Cut data egress on the 99M-account publish by performance-tuning **Hive sort** on **AWS EMR**.
- 🔐 Rolled **proof-of-possession tokens** across Card and Bank endpoints — a stolen token is useless without the key that minted it.
- 📡 **OpenTelemetry + Splunk** tracing, so a stalled stage pages on-call mid-run instead of at cutoff.

Promoted **SWE I → SWE II in a year**.

<img alt="Contributions by year" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/contributions-light.svg#gh-light-mode-only" width="420"><img alt="Languages" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/languages-light.svg#gh-light-mode-only" width="420">
<img alt="Contributions by year" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/contributions-dark.svg#gh-dark-mode-only" width="420"><img alt="Languages" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/languages-dark.svg#gh-dark-mode-only" width="420">

## 🧠 The idea I keep building around

> **The model proposes, deterministic code decides.**

Categories an LLM suggests get thrown away and reassigned by fixed rules, so a scheduled job
produces the same thing today as yesterday. Decisions live in append-only stores outside the
generated text, so a rerun is **idempotent** instead of destructive. An index is the source of
truth, never the files. Everything runs end-to-end in CI with the network, the model and the
credentials stubbed out.

Same instinct as the day job: make the nondeterministic part small, and make everything around it
provable.

## ⚡ Things I've built

**Local-first LLM tools** — [read how they fit together →](https://pbairoliya.github.io/projects/on-device-tools.html)

| | |
|---|---|
| [**daily-lookback**](https://github.com/pbairoliya/daily-lookback) | Calendar + Gmail + iMessage → one generated morning note. 100% on-device. A missed night rebuilds the same note instead of duplicating it. |
| [**grocery-receipts**](https://github.com/pbairoliya/grocery-receipts) | Photograph a receipt → structured expenses and pantry stock. Fingerprinted ingest, so a rescan can't double-count. |
| [**screenshot-organizer**](https://github.com/pbairoliya/screenshot-organizer) | Sorts a messy Desktop by reading what's *in* the images, human-in-the-loop before anything moves. |

**Systems, the hard way**

| | |
|---|---|
| [**csc246**](https://github.com/pbairoliya/csc246-operating-systems) | A shell written without libc. Max-subarray solved five ways — fork/pipe, threads, semaphores, monitors, **CUDA** (1.668s on an RTX 2070). A 586-line multithreaded Scrabble server with RSA auth. |
| [**csc230**](https://github.com/pbairoliya/csc230-c-software-tools) | A generic hash map in C — function-pointer **vtables written by hand**, because C has no generics. Base64 from the bits up. |
| [**csc474**](https://github.com/pbairoliya/csc474-network-security) | A repeating-key XOR breaker that recovers the key length by **index of coincidence**. Plus a port scanner and the 39-line sliding-window detector that catches it. |
| [**csc484**](https://github.com/pbairoliya/csc484-game-ai) | Steering behaviours that compose by summing accelerations, A\* with swappable heuristics, and a decision tree driving both. |
| [**customBash**](https://github.com/pbairoliya/customBash) · [**leetcode-archive**](https://github.com/pbairoliya/leetcode-archive) | A Unix shell in C++. 600+ solutions from 2023–24. |

<img alt="Stack" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/stack-light.svg#gh-light-mode-only" width="420">
<img alt="Stack" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/stack-dark.svg#gh-dark-mode-only" width="420">

## 📜 Receipts

**AWS Certified Solutions Architect – Associate** · **B.S. Computer Science + B.S. Applied
Mathematics**, NC State — **4.0**, **Park Scholar** (full ride, top 1% of applicants) · Chairman of
[InspireNC](https://inspirenc.us), teaching FIRST Robotics in NC schools

---

<p align="center">
  <b>I'd rather talk than be screened.</b><br>
  Backend and full-stack work where correctness is the hard part — ledgers, payments,<br>
  anything that has to be right the first time.<br><br>
  <a href="mailto:pratik0520@gmail.com">pratik0520@gmail.com</a> ·
  <a href="https://pbairoliya.github.io">pbairoliya.github.io</a> ·
  <a href="https://linkedin.com/in/pbairol">LinkedIn</a>
</p>
