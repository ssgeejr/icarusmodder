# Advanced Deep Mining Ore Scanner (planet craft)

**Loadout version:** v1.21.9+  
**Recipe name:** `Grok_Advanced_Deep_Ore_Scanner`  
**Output item:** `Meta_Scanner_DeepOre` (vanilla **Advanced Deep Mining Ore Scanner** — same as Orbital Workshop)

## What this is

The Workshop Advanced scanner (ore-type toggle, T4 meta handheld mesh / advanced BP) was Workshop-Ren only. We did **not** invent a new item. We added a ProcessorRecipes row that crafts the **existing** `Meta_Scanner_DeepOre`.

Basic Fabricator `Deep_Ore_Scanner` is unchanged (no ore-type picker).

## Benches

- Machining Bench  
- Fabricator  
- Manufacturer  

## Cost (already QoL craft-50% counts)

| Mat | Count |
|-----|------:|
| Aluminium | 4 |
| Electronics | 4 |
| Gold Wire | 10 |
| Steel Screw | 10 |
| Copper Wire | 20 |
| Glass | 2 |
| Energy | 5000 mJ |

## Files involved

| Path | Tracked in git? | Role |
|------|-----------------|------|
| `scripts/recipe_grok_advanced_deep_ore_scanner.json` | **Yes** | Recipe source of truth |
| `scripts/ensure_adv_deep_ore_scanner.py` | **Yes** | Idempotent apply into extracted `D_ProcessorRecipes.json` |
| Live pak `data/Crafting/D_ProcessorRecipes.json` | No (inside `.pak`) | Where the game reads it |
| `_tools/qol_rebuild/rebuild.py` | **No** (`_tools/` gitignored) | Home rebuild also merges this recipe from live / embeds fallback |
| `_tools/qol_adv_scanner*/` | No | One-off home staging (safe to delete) |

## Software used (home)

- **UnrealPak** under `_tools/UnrealPak/` (gitignored) — extract / create `_P.pak`
- **Python 3** — JSON edit + pack helper scripts
- No IMM. No new Blueprints (game already has Advanced scanner BP/mesh/icon)

## Apply on any machine

1. Game **closed**. Backup live pak → `backup/qol_before_<stamp>.zip`.
2. Extract live `grok.qualityoflife_P.pak` with UnrealPak → staging.
3. `python scripts/ensure_adv_deep_ore_scanner.py <staging>/data/Crafting/D_ProcessorRecipes.json`
4. Repack with mount `../../../Icarus/Content/...`, install **only** that pak into `mods/`.
5. Smoke: Machining / Fabricator / Manufacturer → craft → equip → ore-type UI.
6. LKG + update CHANGELOG/README if version bumped → **commit/push**.

## Smoke (done on home)

Screenshot confirmed Advanced UI (Gold Ore selected, % signal). Initially Machining-only; v1.21.9 adds Fabricator + Manufacturer.
