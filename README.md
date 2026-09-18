### Pratik Bairoliya

<img alt="99M+ accounts closed nightly · 1.668s max-subarray on CUDA · 600+ LeetCode solved · 4.0 NC State Park Scholar" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/facts-light.svg#gh-light-mode-only" width="620">
<img alt="99M+ accounts closed nightly · 1.668s max-subarray on CUDA · 600+ LeetCode solved · 4.0 NC State Park Scholar" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/facts-dark.svg#gh-dark-mode-only" width="620">

I work at Capital One on the system that closes the bank's books every night. Millions of accounts,
one shot, no do-overs before morning — so most of my time goes into making a very large batch job
fail early and loudly instead of quietly at 4am. That's the job. This page is everything else.

Mostly I like building small things that are annoyingly reliable.

**Stuff I built because I like solving problems and wanted my life easier**

[daily-lookback](https://github.com/pbairoliya/daily-lookback) writes my morning note before I wake
up — calendar, email, texts, one page. It runs entirely on my laptop, because I wasn't about to
ship my iMessage history to somebody's API. The tricky part wasn't the model, it was making it
boring: if it misses a night and runs twice, you get the same note, not two.

[grocery-receipts](https://github.com/pbairoliya/grocery-receipts) started because I kept buying
cumin I already had. Photograph a receipt, it reads it, sorts the groceries, tracks what's about to
expire, and refuses to count the same receipt twice no matter how many times I scan it.

[screenshot-organizer](https://github.com/pbairoliya/screenshot-organizer) cleans a desktop by
actually looking at the screenshots. It asks before it moves anything, which I learned to add the
hard way.

[lc](https://pbairoliya.github.io/projects/lc.html) runs my LeetCode habit out of my notes and
pushes them to a repo every night. There are [600+ solutions](https://github.com/pbairoliya/leetcode-archive)
in there from 2023–24, which says more about my evenings than I'd like.

**Stuff I built to see if I could**

I wrote [a shell with no standard library](https://github.com/pbairoliya/csc246-operating-systems) —
no strlen, no atoi, write your own. Then I solved the same problem five times in a row on purpose:
processes and pipes, threads, semaphores, monitors, and finally CUDA, which did it in 1.668 seconds
on my RTX 2070 and felt like cheating. Same repo has a Scrabble server that holds a thread per
player.

I built [a hash map in C](https://github.com/pbairoliya/csc230-c-software-tools) that stores any
type you want, which C doesn't do, so you fake it with a struct full of function pointers. Nobody
tells you at the time that you're hand-writing a vtable.

I [broke a repeating-key XOR cipher](https://github.com/pbairoliya/csc474-network-security) without
being told the key length — you can get it statistically, which is the closest computer science has
come to magic in my experience. Then I wrote a port scanner, then the 39-line thing that catches
the port scanner.

And [a game AI](https://github.com/pbairoliya/csc484-game-ai) that wanders a room, decides it's
hungry, and A\*s its way to food.

**Where it started**

[first-code](https://github.com/pbairoliya/first-code) is the C++ I wrote in high school, untouched.
The board game Trouble, rebuilt six times because I didn't know about version control yet. An
expression tree attempted four times for the same reason. And this, at the top of one file:

```cpp
#include "E:\myheader.h"
```

A drive letter. On a computer I no longer own. I was very proud of it.

**Off the keyboard**

I ran [InspireNC](https://inspirenc.us) for five years, a student-run nonprofit that gets FIRST
Robotics into NC schools, and captained team 6908 before that. I went to NC State on a Park
Scholarship, came out with degrees in CS and applied math, and still run the Krispy Kreme Challenge
every year, which involves a dozen donuts and questionable judgment.

**What I'm building next**

Publicly, so I actually do it. Each one exists to answer a question I can't yet answer properly
in an interview.

| | The question it answers |
|---|---|
| A log-structured key-value store, in Go | What is a database actually doing when I call `put`? Append-only log, in-memory index, compaction, then a WAL and crash recovery — killing the process mid-write until it stops losing data. |
| Raft — leader election and log replication | I can describe consensus. I want to have implemented it. |
| An idempotent job queue with exactly-once delivery | My day job in miniature, small enough to explain in ten minutes. |
| A CDC pipeline — Postgres WAL to a stream to a sink | The thing every company has and nobody's is clean. |
| A write-up of the nightly close | The most interesting system I work on has no public explanation. That's a gap in this page, not in the system. |

**Where I'm contributing**

Go and Python infrastructure, because that's what I read all day anyway:
[ollama](https://github.com/ollama/ollama) (Go, and I depend on it),
[opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go) and the
[collector](https://github.com/open-telemetry/opentelemetry-collector-contrib),
[temporal](https://github.com/temporalio/sdk-go),
[argo-cd](https://github.com/argoproj/argo-cd). Docs and reproducible bug reports first — the
boring contributions are the ones maintainers actually want.

<img alt="Stack" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/stack-light.svg#gh-light-mode-only" width="430">
<img alt="Stack" src="https://raw.githubusercontent.com/pbairoliya/pbairoliya/main/generated/stack-dark.svg#gh-dark-mode-only" width="430">

**Still here?**

[pratik0520@gmail.com](mailto:pratik0520@gmail.com) ·
[pbairoliya.github.io](https://pbairoliya.github.io) ·
[LinkedIn](https://linkedin.com/in/pbairol) ·
Raleigh / McLean
