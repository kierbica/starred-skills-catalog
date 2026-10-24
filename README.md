# Starred Skills Catalog

A living index of **AI agent skills** (and skill-related repos) found across the repositories starred by [@kierbica](https://github.com/kierbica).

Generated from your starred repos (200 unique). Skills typically appear as `SKILL.md` files (YAML frontmatter + instructions) or under `skills/`, `.claude/skills/`, `openclaw/skills/`, etc.

## How to use

1. Browse the **Skill-related starred repos** section below for high-signal sources.
2. Run the scanner script (`scripts/scan_skills.py`) against any listed repo to extract `SKILL.md` files.
3. Install interesting skills into your agent (OpenWork, Claude Code, OpenClaw, Cline, LibreChat, etc.).

---

## Skill-related starred repositories (high signal)

These are the starred repos whose name or description explicitly mention skills / agent skills / Claude skills / skill registries:

| Repo | Description |
|------|-------------|
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | **Skill + Plugin Registry for OpenClaw** |
| [davidondrej/skills](https://github.com/davidondrej/skills) | David Ondrej's personal agent skills |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | AAS Core – agent-first control plane for catalog discovery |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Hand-picked resources for Claude Code (skills, agents, etc.) |
| [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) | Agents, MCP, **Skills** support |
| [activeloopai/hivemind](https://github.com/activeloopai/hivemind) | Turns traces into reusable skills across agents |
| [ryanfrigo/kalshi-ai-trading-bot](https://github.com/ryanfrigo/kalshi-ai-trading-bot) | Agent-native toolkit + Claude skill |
| [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | Hermes Agent skills + coding harness |
| [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | Plugin / Skill / Extension for codebase intelligence |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Long-horizon SuperAgent harness |
| [morluto/rea](https://github.com/morluto/rea) | Reverse engineer anything with agents (skill-friendly) |
| [different-ai/openwork](https://github.com/different-ai/openwork) | Open-source Claude Cowork alternative (skills ecosystem) |

## Scanner script

```bash
# Optional token for higher rate limits
export GITHUB_TOKEN=ghp_xxx

# Single repo
python scripts/scan_skills.py openclaw/clawhub

# Batch from a starred dump (put starred_full.json in repo root)
python scripts/scan_skills.py --from-starred starred_full.json --limit 25
```

The script:
- Uses GitHub Code Search for `filename:SKILL.md` inside the target repo
- Walks the git tree for any `SKILL.md` / `skill.md` paths

## All starred repositories (200, sorted by stars)

Full machine-readable dump and the complete markdown table are maintained in this repository. Re-run the generation locally or request an update to refresh the list from the GitHub starred API.

Key AI / agent repos in your stars include (non-exhaustive):

- openclaw/openclaw, openclaw/clawhub
- Significant-Gravitas/AutoGPT
- cline/cline
- anomalyco/opencode
- anthropics/claude-code
- morluto/rea
- different-ai/openwork
- langchain-ai/langchain, langchain-ai/deepagents
- crewAIInc/crewAI
- BasedHardware/omi
- CherryHQ/cherry-studio
- and ~190 more

---

## Notes

- Extracting every single `SKILL.md` from 200+ repos hits GitHub search rate limits; the scanner is designed for targeted or batched use.
- Primary skill ecosystems visible in your stars: **OpenClaw/ClawHub**, Claude Code resources, agentic-awesome-skills, OpenWork, REA, Cline, LibreChat Skills.
- Repo created & last bulk update: 2026-10-24

---

*This catalog is generated from the authenticated user's starred repositories via the GitHub API.*
