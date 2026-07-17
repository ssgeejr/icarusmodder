# icarusmodder

Personal **single-pak** quality-of-life loadout for [Icarus](https://store.steampowered.com/app/1149460/Icarus/).

**One file in the game mods folder:**

`grok.qualityoflife_P.pak`  
→ `Icarus\Content\Paks\mods\`

No Icarus Mod Manager. No multi-pak stack. **Pete’s Beacon Teleport always wins** on shared data.

See **[AGENTS.md](./AGENTS.md)** for build rules, backups, and smoke tests.

---

## What’s in `grok.qualityoflife_P.pak`

Everything below is **folded into that one pak**. Path conflicts between sources were resolved by merging into one table per path (or were never in conflict).

| Feature | Origin | What it does |
|---------|--------|----------------|
| **Pete’s Beacon Teleport** | laanp | Craftable teleport remote + blueprints/UI. Core feature — must never break. |
| **10× stacks / 25% weight** | Deyvid-style itemable | Higher `MaxStack`, lower `Weight` on inventory items (carry more per slot; lighter packs). **Not** harvest yield. |
| **Crafting cost & speed ~50%** | Crafting Cost + Speed pack | Cheaper recipe inputs and faster craft times on processor recipes; Pete’s craft recipe kept. |
| **2× gather tools** | Tool damage table | ×2 mining / felling / reaping / skinning efficiency + ×2 felling damage (trees). **Does not** raise combat `Melee_Damage`. |
| **2× shovel dig (dirt/snow)** | Digging rewards on shovels | ×2 dig yield feel via `BaseDiggingRewards_+%` on shovel rows only. |
| **Waste Not** | CritFail / AgentKush | Mining secondaries become useful (ores/exotics/etc. instead of waste stone where configured). |
| **Armor ~2.5×** | Deyvid | Stronger armor protection values. |
| **Food buffs balanced ~2.5×** | Deyvid | Stronger consumable buffs. |
| **Saddles & backpacks** | Deyvid | Balanced carry capacity on saddles/backpacks. |
| **Wood fuel ×10** | Deyvid | Wood burns much longer as fuel. |
| **No water-wheel junk** | laanp | Water wheels do not accumulate junk (`Waterwheel` inventory slot template). |
| **Deep mining drills (tuned)** | QoL | See below — modest speed + lower biofuel burn on the biofuel deep drill only. |

Optional text/script files from authors may sit inside the pak; the game loads the **data tables + Pete assets**.

### Deep mining (current values)

| Setting | Biofuel deep drill | Electric deep drill | Notes |
|---------|--------------------|---------------------|--------|
| **Speed** `BaseDeepMiningDrillSpeed_+%` | **+75%** (~1.75× bare base) | **+125%** (~2.25× bare base) | Middle band after too-hot (+100/+166) and too-cold (+50/+83). Oil drill unchanged. |
| **Fuel burn** `GenerationRatio` on row `Deep_Mining_Biofuel_Drill` | **0.375** (was 0.75) | N/A (electric) | **−50% biofuel use** while drilling only — **not** base power generators. Empty tanks OK; speed targets ore per run. |

Intent: enough ore per fuel/power cycle to progress without all-day waits or absurd stockpiles.


---

## Conflicts

### Multi-pak (before the single pack)

These **fought** when left as separate paks (whole-file override):

| Shared table | Who fought | Winner if both installed |
|--------------|------------|---------------------------|
| `D_ProcessorRecipes.json` | Crafting Cost vs Pete | Last pak alphabetically |
| `D_Itemable.json` | Stacks/weight vs Pete | Last pak alphabetically |

**Resolution:** one merged `grok.qualityoflife_P.pak` — Pete rows preserved, then QoL applied.

### Current single-pack layout

| Path | Role | Multi-source conflict inside grok? |
|------|------|-------------------------------------|
| Pete blueprints / mesh / UI | Teleport | No (unique) |
| `D_Itemable` | Stacks/weight + Pete items | Merged once |
| `D_ProcessorRecipes` | Craft QoL + Pete recipe | Merged once |
| `D_ItemsStatic` | Pete + shovel dig + deep-drill speed % | Merged once |
| `D_Generator` | Wood fuel ×10 + biofuel deep-drill burn only | Merged once (not power gens except wood trait rows) |
| `D_ToolDamage` | 2× gather tools | Additive unique path |
| `D_InventoryInfo` | Water-wheel junk | **No conflict** — QoL had no inventory table; pure add |
| Armor / food / saddles / voxel | Other QoL | Unique paths |

**laanp-NoWaterWheelJunk** vs existing grok content: **zero path overlap** before merge. Safe additive include.

**Rule:** never install a second `*_P.pak` that ships the same `data/...` path next to grok.

---

## Install

1. Close Icarus.
2. Put **only** `grok.qualityoflife_P.pak` in  
   `...\Icarus\Content\Paks\mods\`
3. Remove old individual mod paks for the same features.
4. Smoke test: **teleport → stacks → craft → gather → dig / water wheel → deep drill**.

Backups: repo `backup/` (gitignored), including `qol_KNOWN_GOOD_latest.zip` after a clean session (production restore pointer).

---

## Repo layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Agent/build defaults (Pete first, `backup/`, single pak) |
| `exmod_to_pak.py` | Helper: EXMOD → pak (offline) |
| `paks/` | Local source paks (gitignored) |
| `backup/` | Zips / built pak copies (gitignored) |
| `_tools/` | UnrealPak / extracts (gitignored) |

Mod binaries (`*.pak`, `*.exmod`, `*.exmodz`, …) are **not** committed.

---

## Version

Tagged releases describe the workflow + docs state of this repo. The playable pak is built locally (or restored from `backup/`) and lives under the game `mods` folder.

**Prod:** only `grok.qualityoflife_P.pak` in `Paks\mods`. After a verified good session, refresh `backup/qol_KNOWN_GOOD_latest.zip` from that live file.
