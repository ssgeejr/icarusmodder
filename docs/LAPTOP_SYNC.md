# Laptop sync — pull then “update to latest changes”

Use this on **Perryville / any non-home box** after `git pull`.

## Critical fact

The playable **`grok.qualityoflife_P.pak` is gitignored**.  
`git pull` updates **docs + scripts + process**, not the binary in `Icarus\Content\Paks\mods\`.

**Source of truth for features/numbers:** `README.md` + `CHANGELOG.md` (current version in README header).  
**Source of truth for content on a machine:** that machine’s live pak (evolve it; don’t restack old multi-paks).

## What to tell Grok after pull

> **update to latest changes**

That means: read `README.md` / `CHANGELOG.md` / this file / `AGENTS.md`, diff vs the live pak on **this** PC, then backup → patch → install → LKG → commit/push any doc fixes. Game closed for install.

## Paths

| | Home | Laptop (Perryville) |
|--|------|---------------------|
| Repo | `C:\dev\games\icarusmods` | same or clone |
| Game | `D:\SteamLibrary\steamapps\common\Icarus\...` | `C:\Program Files (x86)\Steam\steamapps\common\Icarus\...` |
| Live pak | `...\Icarus\Content\Paks\mods\grok.qualityoflife_P.pak` | same relative under that install |

## Tracked in git (pull these)

- `README.md`, `CHANGELOG.md`, `AGENTS.md`
- `docs/` (this file, scanner notes, …)
- `scripts/` (portable recipe helpers)
- `exmod_to_pak.py`, `continue*.cmd`, `perryville.changes.md`, `resources.md`

## Not in git (local / recreate)

- `_tools/` (UnrealPak, extracts, `qol_rebuild/rebuild.py` working copy)
- `backup/`, `paks/`, `*.pak`
- Live game `mods\` pak

## After pull checklist for Grok

1. `git status` / `git log -5` — confirm latest CHANGELOG version.  
2. Locate live pak on this machine; extract with UnrealPak.  
3. Compare key features from README to extracted JSON (XP 2.5×, Ice Box, Fridge -5000, ruby=uranium, beacon MaxStack 100, Adv scanner recipe benches, Pete, …).  
4. Apply missing pieces (use `scripts/ensure_adv_deep_ore_scanner.py` for scanner; rebuild or surgical patch for the rest).  
5. Install sole `grok.qualityoflife_P.pak`; smoke Pete first.  
6. Refresh `backup/qol_KNOWN_GOOD_latest.zip`; commit/push if docs changed.

## Recent feature pointers

| Feature | Doc / script |
|---------|----------------|
| Advanced Deep Ore Scanner | `docs/ADVANCED_DEEP_ORE_SCANNER.md`, `scripts/ensure_adv_deep_ore_scanner.py` |
| Full loadout numbers | `README.md` |
| Version history | `CHANGELOG.md` |
| Process / Pete-first | `AGENTS.md` |
