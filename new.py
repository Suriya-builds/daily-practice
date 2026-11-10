"""Scaffold today's practice problem.

Usage:
    py new.py              # fetch today's LeetCode daily problem
    py new.py two-sum      # scaffold a specific LeetCode problem by slug
    py new.py --lang java  # choose solution language (py, java, cpp, js)

Creates problems/YYYY-MM-DD-<slug>/ with README.md (problem + notes) and a
solution file, then adds a row to PROGRESS.md. Uses only the standard library.
"""

import argparse
import datetime as dt
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
PROBLEMS = ROOT / "problems"
PROGRESS = ROOT / "PROGRESS.md"
API = "https://leetcode.com/graphql"

FIELDS = "title titleSlug difficulty content topicTags { name } codeSnippets { langSlug code }"
DAILY_QUERY = "query { activeDailyCodingChallengeQuestion { date question { %s } } }" % FIELDS
SLUG_QUERY = "query q($s: String!) { question(titleSlug: $s) { %s } }" % FIELDS

LANGS = {
    "py": ("python3", "solution.py", "#"),
    "java": ("java", "Solution.java", "//"),
    "cpp": ("cpp", "solution.cpp", "//"),
    "js": ("javascript", "solution.js", "//"),
}


def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        API,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "daily-practice-script",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    if data.get("errors"):
        sys.exit(f"LeetCode API error: {data['errors']}")
    return data["data"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?", help="LeetCode problem slug, e.g. two-sum")
    ap.add_argument("--lang", default="py", choices=LANGS)
    args = ap.parse_args()

    if args.slug:
        q = gql(SLUG_QUERY, {"s": args.slug})["question"]
        if not q:
            sys.exit(f"No problem found with slug '{args.slug}'")
    else:
        q = gql(DAILY_QUERY)["activeDailyCodingChallengeQuestion"]["question"]

    today = dt.date.today().isoformat()
    folder = PROBLEMS / f"{today}-{q['titleSlug']}"
    if folder.exists():
        print(f"Already exists: {folder.relative_to(ROOT)}")
        return
    folder.mkdir(parents=True)

    url = f"https://leetcode.com/problems/{q['titleSlug']}/"
    tags = ", ".join(t["name"] for t in q["topicTags"]) or "-"
    readme = f"""# {q['title']}

**Difficulty:** {q['difficulty']} | **Tags:** {tags} | [Open on LeetCode]({url})

## Problem

{q['content'] or '_Premium problem: see LeetCode._'}

## My approach

<!-- Explain your idea in 2-4 lines, in your own words. -->

## Complexity

- Time: O(?)
- Space: O(?)

## What I learned

-
"""
    (folder / "README.md").write_text(readme, encoding="utf-8")

    lang_slug, filename, comment = LANGS[args.lang]
    snippet = next((s["code"] for s in q["codeSnippets"] or [] if s["langSlug"] == lang_slug), "")
    header = f"{comment} {q['title']} ({q['difficulty']})\n{comment} {url}\n\n"
    if args.lang == "py":
        header += "from typing import List, Optional\n\n"
    (folder / filename).write_text(header + snippet + "\n", encoding="utf-8")

    if not PROGRESS.exists():
        PROGRESS.write_text("# Progress\n\n| Date | Problem | Difficulty |\n|---|---|---|\n", encoding="utf-8")
    rel = folder.relative_to(ROOT).as_posix()
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(f"| {today} | [{q['title']}]({rel}/) | {q['difficulty']} |\n")

    print(f"Created {rel}/")
    print(f"  Problem: {q['title']} ({q['difficulty']})")
    print(f"  Solve it at {url}, then paste your accepted code into {rel}/{filename}")


if __name__ == "__main__":
    main()
