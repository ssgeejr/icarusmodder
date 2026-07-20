# Changelog

All notable changes to this repo and the **grok.qualityoflife_P.pak** loadout.

The playable pak is **not** stored in git (see `.gitignore`). Builds live under the game `mods` folder and copies under `backup/`.

---

## [1.3.0] — 2026-07-20

### Loadout (prod pak) — deep mining recovery

- Reset deep drill **speed from vanilla originals** only:
  - Biofuel: **+100%** (2× bare production)
  - Electric: **+166%** (2× original effective vs +33%)
- Biofuel deep drill **`GenerationRatio` restored to vanilla 0.75** (undid 0.375 fuel cut that correlated with empty tanks / no ore)
- Oil drill, power generators, wood-fuel rows, Pete: unchanged
- LKG refreshed from this prod build

### Docs

- README deep-mining table matches recovery values
- Note: fuel-efficiency experiments deferred until 2× ore is verified in-game

---

## [1.2.0] — 2026-07-17

### Loadout (prod pak)

- Deep mining experiments (middle band / fuel cuts) — **superseded by 1.3.0**
- Docs process: README loadout, AGENTS → README for numbers, LKG pointer

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
