# Changelog

All notable changes to this repo and the **grok.qualityoflife_P.pak** loadout.

The playable pak is **not** stored in git (see `.gitignore`). Builds live under the game `mods` folder and copies under `backup/`.

---

## [1.2.0] — 2026-07-17

### Loadout (prod pak)

- Deep mining **middle band**: biofuel **+75%** / electric **+125%** `BaseDeepMiningDrillSpeed_+%`
- Biofuel deep drill fuel burn **−50%** (`GenerationRatio` 0.75 → 0.375); power generators unchanged
- Prior extremes documented in README (too-hot +100/+166, too-cold +50/+83)

### Docs / process

- README: full feature table + deep-mining values + smoke includes deep drill
- AGENTS: intent list points at README for numbers; smoke/checklist includes dig/wheel/drill
- LKG: `backup/qol_KNOWN_GOOD_latest.zip` tracks verified prod

---

## [1.1.0] — 2026-07-15

### Loadout

- Folded **laanp NoWaterWheelJunk** (`D_InventoryInfo` — water wheels no junk)
- Documented single-pak merge of Pete + stacks/weight + craft QoL + tools 2× + dig 2× + Waste Not + Deyvid QoL

### Docs / repo

- README loadout + conflict history
- Ignore `paks/`, mod binaries, `backup/`, `_tools/`

---

## [1.0.0] — 2026-07-14

### Repo

- Initial **AGENTS.md** defaults: single pak, Pete first, backups only in `backup/`, smoke test order
- `exmod_to_pak.py` helper
- `.gitignore` for mod packages and local tooling

### Loadout (established by this point)

- Single `grok.qualityoflife_P.pak` replacing multi-pak stack
- Pete teleport preserved on shared tables
- 2× gather tools, shovel dig rewards, stacks/weight, craft cost/speed, armor/food/saddles/wood fuel, Waste Not
