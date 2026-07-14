# AGENTS.md — Icarus single-pak QoL mod

## What we are doing

Maintain **one** Icarus mod pak:

**`grok.qualityoflife_P.pak`**

Installed at:

`D:\SteamLibrary\steamapps\common\Icarus\Icarus\Content\Paks\mods\grok.qualityoflife_P.pak`

Personal **quality-of-life** pack: stacks, weight, craft cost/speed, tool harvest yield, Pete teleport, and related QoL — **one `_P.pak` only**. No IMM. No multi-pak stack.

---

## Defaults (always — do not skip)

These are the **default operating rules** for every change. Process theater beyond this is optional; these three are not.

### 1. Backups only in `backup/` + known-good

- **All** backups go under **`backup/`** (gitignored). Never the repo root.
- Before any change that will replace the live pak: write a stamp zip  
  `backup/qol_before_<YYYYMMDD_HHMMSS>.zip` containing the current live pak.
- After a session that plays clean (smoke test pass): refresh known-good:
  - `backup/qol_KNOWN_GOOD_<stamp>.zip`
  - **and** overwrite `backup/qol_KNOWN_GOOD_latest.zip` (stable pointer for rollback)
- No `*.pak` / `*.bak` / backup zips in the project root.

### 2. Smoke test after every install (fixed order)

After installing a new `grok.qualityoflife_P.pak`, verify **in this order**:

1. **Teleport** (Pete) — if this fails, stop and rollback; pack is broken  
2. **Stacks** — one resource shows large max stack  
3. **Craft** — one recipe still cheaper/faster as expected  
4. **Gather** — mine / chop / reap or skin once (yield feel)

Do not call a change “done” until smoke passes (or the user explicitly declines testing).

### 3. Evolve the live single pak only

- **Source of truth for content** = the current live `grok.qualityoflife_P.pak` (game `mods` folder).
- Default build path: **extract that pak → add/edit only the intended table(s) → repack → replace only that one file in `mods`**.
- **Do not** rebuild by re-stacking old individual paks (Crafting Cost, Deyvid_*, laanp alone, Waste Not, etc.) unless the user explicitly orders a full redesign.
- One provider per data path. Pete wins on any shared-table merge: keep Pete rows/assets, then layer QoL.

---

## Non-negotiable: teleporter first

**Pete’s Beacon Teleport (laanp)** is the core of the loadout.

- If teleport breaks, the pack is broken → rollback from `backup/qol_KNOWN_GOOD_latest.zip` (or the latest `qol_before_*`).
- Shared tables (`D_Itemable`, `D_ProcessorRecipes`, Pete blueprints/data): **never drop Pete**.

---

## How we work

### Source of truth

- **Live pack** = game `Paks\mods\grok.qualityoflife_P.pak`
- Staging/extracts under `_tools/` or temp (not committed as product)
- Vanilla tables: game `Content\Data\data.pak`

### Build pattern (no IMM)

1. Backup live pak → **`backup/qol_before_<stamp>.zip`**
2. Extract live pak with UnrealPak → staging
3. Add or merge **only** the intended table(s)
4. Verify Pete + prior QoL still present
5. Pack with mount `../../../Icarus/Content/...`
6. Install **only** when authorized; replace **only** `grok.qualityoflife_P.pak` in `mods`
7. **Smoke test** (defaults §2)
8. If smoke passes and user is happy → update **`backup/qol_KNOWN_GOOD_latest.zip`**

Tools: UnrealPak under `_tools/UnrealPak` when present. Helpers: `exmod_to_pak.py`, scripts under `_tools/`.

### Pak rules

- Prefer `_P` suffix.
- Do not auto-install or delete game mods unless the user explicitly asks.
- Prefer not writing live `mods` while the game is running.

### Merge philosophy

| Concern | Approach |
|---------|----------|
| Shared tables | Pete base → layer QoL by `Name` |
| Unique tables | One full table per path inside the single pak |
| New yield | Minimal surface (e.g. `D_ToolDamage`); not combat unless requested |
| EXMOD / EXMODZ | Merge into full JSON, then pack — never rename to `.pak` |

---

## What the pack is for (intent)

- Teleport (Pete)
- Inventory: higher stacks, lower weight
- Crafting: reduced cost / faster processing where configured
- Gathering: 2× tool efficiencies + felling damage (**not** `Melee_Damage` unless chosen)
- Other folded QoL tables (armor, food, saddles, wood fuel, mining secondaries, etc.)

Format never changes: **one pak, Pete-safe, evolved from live.**

---

## What we are not doing

- IMM as install/merge path
- Multiple competing paks for the same tables
- Letting stacks/craft/yield wipe Pete on shared files
- Treating `MaxStack`/weight as harvest yield
- Silently changing combat damage when the goal is resources
- Rebuilding from the old multi-pak set by default
- Writing backups outside **`backup/`**

---

## Safety checklist (every change)

- [ ] Backup live pak → **`backup/qol_before_<stamp>.zip`**
- [ ] Nothing backup-related outside **`backup/`**
- [ ] Built from **extracted live QoL pak**, not old multi-pak rebuild
- [ ] Diff: only intended paths added/changed
- [ ] Pete recipe + item + blueprints still present
- [ ] Only one pak in `mods` for this loadout (`grok.qualityoflife_P.pak`)
- [ ] User authorized install (if writing to game)
- [ ] **Smoke:** teleport → stacks → craft → gather
- [ ] On success: refresh **`backup/qol_KNOWN_GOOD_latest.zip`**

---

## Rollback

1. Prefer **`backup/qol_KNOWN_GOOD_latest.zip`**
2. Else latest **`backup/qol_before_*.zip`**
3. Extract/copy `grok.qualityoflife_P.pak` into  
   `Icarus\Content\Paks\mods\`  
   (replace the broken one; remove stray competing paks if any)

---

## Agent behavior

- Defaults above are mandatory unless the user overrides.
- Prefer plans when the game is “perfect” and the user has not said execute.
- No destructive/install steps without clear authorization.
- When authorized: one pak, Pete first, minimal surface, backup → change → smoke → known-good.
