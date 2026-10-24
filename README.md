# Starred Skills Catalog

A living index of **AI agent skills** (and skill-related repos) found across the repositories starred by [@kierbica](https://github.com/kierbica).

Generated from your starred repos. Skills typically appear as `SKILL.md` files (YAML frontmatter + instructions) or under `skills/`, `.claude/skills/`, `openclaw/skills/`, etc.

## How to use

1. Browse the **Skill-related starred repos** section below for high-signal sources.
2. Run the scanner script (see `scripts/`) against any of the listed repos to extract `SKILL.md` files.
3. Install interesting skills into your agent (OpenWork, Claude Code, OpenClaw, Cline, etc.).

---

## Skill-related starred repositories

| Repo | Stars | Description |
|------|------:|-------------|
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | 9,527 | Skill + Plugin Registry for OpenClaw |
| [davidondrej/skills](https://github.com/davidondrej/skills) | — | access to david ondrej's personal agent skills |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | — | AAS Core is the local, agent-first control plane for complete catalog discovery |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | — | A hand-picked collection of the finest of resources for Claude Code |
| [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) | 46,229 | Features Agents, MCP, Skills |
| [activeloopai/hivemind](https://github.com/activeloopai/hivemind) | 1,634 | Hivemind turns your traces into reusable skills across agents |
| [ryanfrigo/kalshi-ai-trading-bot](https://github.com/ryanfrigo/kalshi-ai-trading-bot) | 631 | agent-native toolkit (CLI, MCP server, Claude skill) |
| [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | — | packages for Hermes Agent skills, coding harness |
| [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | — | Plugin/Skill/Extension for codebase intelligence |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | — | SuperAgent harness |

> Full table with exact star counts and all 200 repos is in the committed README (regenerated from API).

## All starred repositories

See the full generated list in this repo after the initial push (200 repos sorted by stars).

---

## Scanner

```bash
export GITHUB_TOKEN=ghp_xxx   # optional but recommended for higher rate limits
python scripts/scan_skills.py owner/repo
python scripts/scan_skills.py --from-starred starred_full.json --limit 20
```

The script searches for `filename:SKILL.md` and walks the git tree for skill paths.

## Notes

- Full extraction of every `SKILL.md` from 200+ repos requires rate-limited GitHub API calls; use the scanner.
- Key skill ecosystems in your stars: **OpenClaw / ClawHub**, Claude Code awesome lists, agentic-awesome-skills, OpenWork, REA (morluto/rea), Cline, LibreChat Skills, etc.
- Last updated: 2026-10-24
