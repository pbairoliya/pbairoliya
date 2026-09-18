#!/usr/bin/env python3
"""Generate the stat SVGs shown on the profile README.

Self-hosted on purpose: the hosted github-readme-stats instances rate-limit and
return 404s, and a profile that renders broken images is worse than one with none.
Run `python3 scripts/gen_stats.py` (needs `gh` authenticated) or let the daily
workflow do it.
"""
import json
import subprocess
from datetime import datetime

USER = "pbairoliya"
YEARS = range(2021, datetime.now().year + 1)

# Excluded from the language bar: build systems and vendored assets say nothing
# about what I write.
SKIP_LANGS = {"CMake", "Makefile", "Batchfile", "Shell"}

LIGHT = dict(fg="#1f2328", dim="#59636e", line="#d1d9e0", bg="none", accent="#0969da")
DARK = dict(fg="#f0f6fc", dim="#9198a1", line="#3d444d", bg="none", accent="#4493f8")


def gh(query):
    out = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)["data"]


def contributions():
    parts = []
    for y in YEARS:
        parts.append(f'y{y}: contributionsCollection(from: "{y}-01-01T00:00:00Z", '
                     f'to: "{y}-12-31T23:59:59Z") {{ contributionCalendar {{ totalContributions }} }}')
    data = gh(f'{{ user(login: "{USER}") {{ {" ".join(parts)} }} }}')["user"]
    return [(y, data[f"y{y}"]["contributionCalendar"]["totalContributions"]) for y in YEARS]


def languages():
    q = ('{ user(login: "%s") { repositories(first: 100, ownerAffiliations: OWNER, isFork: false) '
         '{ totalCount nodes { languages(first: 10, orderBy: {field: SIZE, direction: DESC}) '
         '{ edges { size node { name color } } } } } } }') % USER
    repos = gh(q)["user"]["repositories"]
    totals = {}
    for repo in repos["nodes"]:
        # Count each language once per repo it appears in. Weighting by bytes lets
        # one vendored library (a 1MB SFML copy) claim 58% of the profile.
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in SKIP_LANGS:
                continue
            entry = totals.setdefault(name, {"size": 0, "color": edge["node"]["color"] or "#888"})
            entry["size"] += 1
    ranked = sorted(totals.items(), key=lambda kv: -kv[1]["size"])[:6]
    total = sum(v["size"] for _, v in ranked) or 1
    return [(n, v["color"], v["size"] / total) for n, v in ranked], repos["totalCount"]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_contributions(rows, theme, path):
    w, h, pad = 480, 132, 16
    peak = max(n for _, n in rows) or 1
    base, top = h - 34, pad + 22
    span = base - top
    slot = (w - pad * 2) / len(rows)
    bw = min(38, slot - 10)
    bars = []
    for i, (year, n) in enumerate(rows):
        # sqrt scale: 617 vs 2 on a linear axis renders five years as invisible
        # slivers. Every bar is labelled with its real count, so the shape is a
        # reading aid and the number is the truth.
        bh = max(3, round(span * ((n / peak) ** 0.5)))
        x = pad + i * slot + (slot - bw) / 2
        y = base - bh
        bars.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh}" rx="3" fill="{theme["accent"]}" '
            f'opacity="{0.45 + 0.55 * ((n / peak) ** 0.5):.2f}"/>'
            f'<text x="{x + bw / 2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-size="10" '
            f'fill="{theme["dim"]}">{n}</text>'
            f'<text x="{x + bw / 2:.1f}" y="{base + 15}" text-anchor="middle" font-size="10" '
            f'fill="{theme["dim"]}">{year}</text>')
    open(path, "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Contributions by year">
<style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>
<text x="{pad}" y="{pad + 8}" font-size="12" font-weight="600" fill="{theme["fg"]}">Contributions by year</text>
<line x1="{pad}" y1="{base + 0.5}" x2="{w - pad}" y2="{base + 0.5}" stroke="{theme["line"]}"/>
{"".join(bars)}
</svg>''')


def svg_languages(langs, repo_count, theme, path):
    w, h, pad = 480, 132, 16
    bar_y, bar_h, bar_w = 44, 10, w - pad * 2
    segs, x = [], float(pad)
    for _, color, frac in langs:
        seg = bar_w * frac
        segs.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{max(seg, 1):.1f}" height="{bar_h}" fill="{color}"/>')
        x += seg
    legend, lx, ly = [], pad, bar_y + 34
    for i, (name, color, frac) in enumerate(langs):
        if i and i % 3 == 0:
            lx, ly = pad, ly + 24
        legend.append(
            f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4.5" fill="{color}"/>'
            f'<text x="{lx + 15}" y="{ly}" font-size="11" fill="{theme["fg"]}">{esc(name)}'
            f'<tspan fill="{theme["dim"]}"> {frac * 100:.0f}%</tspan></text>')
        lx += 152
    open(path, "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Languages by repository count">
<style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>
<text x="{pad}" y="{pad + 8}" font-size="12" font-weight="600" fill="{theme["fg"]}">Languages</text>
<text x="{pad}" y="{pad + 26}" font-size="11" fill="{theme["dim"]}">share of {repo_count} repositories</text>
{"".join(segs)}
{"".join(legend)}
</svg>''')


# Grouped by what the thing does, not by a flat alphabetical list. Order inside
# each row is roughly how central it is to my day job.
STACK = [
    ("Languages", ["Go", "Python", "Java", "TypeScript", "SQL", "C++"]),
    ("Frontend", ["Vue.js", "Angular", "Node.js", "HTML/CSS", "Pinia", "Fastify"]),
    ("Backend", ["Spring Boot", "REST APIs", "MongoDB", "PostgreSQL", "DynamoDB", "Neo4j"]),
    ("Platform", ["Kubernetes", "Temporal", "Docker", "Terraform", "Argo CD", "Helm", "AWS"]),
    ("Data", ["Spark", "Databricks", "Hive", "EMR"]),
    ("Observability", ["OpenTelemetry", "Splunk"]),
]


def svg_stack(theme, path):
    w, pad, row_h = 480, 16, 26
    y = pad + 30
    rows = []
    for label, items in STACK:
        rows.append(f'<text x="{pad}" y="{y + 12}" font-size="10" font-weight="600" '
                    f'letter-spacing="0.4" fill="{theme["dim"]}">{esc(label.upper())}</text>')
        x = pad + 92
        for item in items:
            tw = 7.2 * len(item) + 16
            if x + tw > w - pad:          # wrap rather than run off the card
                y += row_h
                x = pad + 92
            rows.append(
                f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="19" rx="9.5" '
                f'fill="none" stroke="{theme["line"]}"/>'
                f'<text x="{x + tw / 2:.1f}" y="{y + 13.5}" text-anchor="middle" font-size="10.5" '
                f'fill="{theme["fg"]}">{esc(item)}</text>')
            x += tw + 6
        y += row_h + 6
    h = y + 4
    open(path, "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Stack">
<style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>
<text x="{pad}" y="{pad + 8}" font-size="12" font-weight="600" fill="{theme["fg"]}">Stack</text>
{"".join(rows)}
</svg>''')


def main():
    rows = contributions()
    langs, repo_count = languages()
    for theme, suffix in ((LIGHT, "light"), (DARK, "dark")):
        svg_contributions(rows, theme, f"generated/contributions-{suffix}.svg")
        svg_languages(langs, repo_count, theme, f"generated/languages-{suffix}.svg")
        svg_stack(theme, f"generated/stack-{suffix}.svg")
    print("contributions:", ", ".join(f"{y}={n}" for y, n in rows))
    print("languages:", ", ".join(f"{n} {f * 100:.0f}%" for n, _, f in langs))


if __name__ == "__main__":
    main()
