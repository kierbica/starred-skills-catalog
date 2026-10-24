#!/usr/bin/env python3
"""
Scan a GitHub repository (or list of starred repos) for SKILL.md files
and skills/ directories. Uses the GitHub API (needs GITHUB_TOKEN).

Usage:
  export GITHUB_TOKEN=ghp_...
  python scripts/scan_skills.py owner/repo
  python scripts/scan_skills.py --from-starred starred_full.json
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.parse

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "starred-skills-catalog",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)

def find_skills(owner, repo):
    found = []
    try:
        q = f"filename:SKILL.md repo:{owner}/{repo}"
        data = api(f"/search/code?q={urllib.parse.quote(q)}&per_page=50")
        for item in data.get("items", []):
            found.append({
                "path": item["path"],
                "html_url": item.get("html_url"),
                "name": item["name"],
            })
    except Exception as e:
        print(f"  search error: {e}", file=sys.stderr)
    try:
        tree = api(f"/repos/{owner}/{repo}/git/trees/HEAD?recursive=1")
        for t in tree.get("tree", []):
            p = t["path"]
            if p.endswith("SKILL.md") or p.endswith("skill.md"):
                if not any(f["path"] == p for f in found):
                    found.append({"path": p, "html_url": f"https://github.com/{owner}/{repo}/blob/HEAD/{p}"})
    except Exception as e:
        print(f"  tree error: {e}", file=sys.stderr)
    return found

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", nargs="?", help="owner/repo")
    ap.add_argument("--from-starred", help="JSON file of starred repos")
    ap.add_argument("--limit", type=int, default=15, help="max repos to scan from starred")
    args = ap.parse_args()
    if args.from_starred:
        with open(args.from_starred) as f:
            repos = json.load(f)
        repos = sorted(repos, key=lambda r: ("skill" in (r.get("description") or "").lower() or "skill" in r["full_name"].lower()), reverse=True)
        for r in repos[:args.limit]:
            owner, name = r["full_name"].split("/")
            print(f"\n=== {r['full_name']} ===")
            skills = find_skills(owner, name)
            if skills:
                for s in skills:
                    print(f"  - {s['path']}  {s.get('html_url','')}")
            else:
                print("  (no SKILL.md found)")
    elif args.repo:
        owner, name = args.repo.split("/")
        skills = find_skills(owner, name)
        print(json.dumps(skills, indent=2))
    else:
        ap.print_help()

if __name__ == "__main__":
    main()
