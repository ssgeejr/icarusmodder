# Changelog

All notable changes to this repo and the **grok.qualityoflife_P.pak** loadout.

The playable pak is **not** stored in git (see `.gitignore`). Builds live under the game `mods` folder and copies under `backup/`.

---

## [1.16.0] — 2026-08-17

### Loadout — stasis bag no hotbar lock

- Removed `Traits.Equippable.FocusLock` from **10 full stasis bag** items (body-in-bag variants only)
- Allows hotbar **1–0** (e.g. Pete teleporter) while carrying a full stasis bag on **G**
- Animal carcass FocusLock **unchanged**
- LKG refreshed after install

---

## [1.15.0] — 2026-08-16

### Loadout — Super Cooled Ice turbo (sub-second cycle)

- `Super_Cooled_Ice` + `Frozen_Wood` `MiningTimeSeconds`: **1 → 0.1** (~**300×** vs vanilla 30s; ~**600/min** if one unit per cycle)
- Still uses deposit cycle (not drill speed %); Pete-safe full `D_OreDeposit` table
- LKG refreshed after install

---

## [1.14.0] — 2026-08-16

### Loadout — Super Cooled Ice actually faster (real lever)

- **v1.13 failed:** `BaseDeepMiningDrillSpeed_+%` on `Ice_Borer` does **not** change ice yield (still ~2.1/min)
- Real control is `D_OreDeposit` **`MiningTimeSeconds`**:
  - `Super_Cooled_Ice`: **30 → 1** (~30×, ~2/min → ~60/min)
  - `Frozen_Wood`: **30 → 1** (same borer path)
- Full `D_OreDeposit` table added to the pak (only those two rows edited)
- Ice borer still keeps +100 speed stat (harmless); fuel generator unchanged

---

## [1.13.0] — 2026-08-16

### Loadout — ice borer drill-speed attempt (ineffective)

- `Ice_Borer`: `BaseDeepMiningDrillSpeed_+%` **+100** — **did not** raise Super Cooled Ice/min
- Superseded by **v1.14.0** deposit cycle fix

---

## [1.12.0] — 2026-08-15

### Loadout — post-patch schema rebuild

- Game **data.pak** rebuilt after Thursday patch (build `24684690`, ~2026-08-13 evening)
- Full-table QoL tables rebased on post-patch vanilla (not pre-patch live)
- Fixes broken fishing kit icons / missing poles from rod renames:
  - `Item_Carbon_Rod` → **`Item_Carbon_Fishing_Rod`** (with icon)
  - `Item_RadBoss_Rod` → **`Item_RadBoss_Fishing_Rod`**
  - meshes `Mesh_Carbon_Fishing_Rod`, `Mesh_Radboss_Fishing_Rod`
  - recipe + items static **`Carbon_Fishing_Rod`**
- Also picks up other patch rows that stale tables dropped (roast foods, fertility serum, etc.)
- Re-applied: Pete, stacks/weight, craft 50%, gather 2×, dig 2×, drills 2×, energy, voxels, pouches 12, queen bee ×100, armor/food/saddles overlays

---

## [1.11.0] — 2026-08-09

### Loadout — revert action hold time

- Removed `D_CharacterStartingStats.json` (undo **BaseActionHoldTime −50%**)
- That change sped **repair** holds, **not** world pickup
- All other QoL unchanged; LKG refreshed

---

## [1.10.0] — 2026-08-09

### Loadout — faster hold / pickup (reverted in 1.11.0)

- Added `D_CharacterStartingStats.json` with **BaseActionHoldTime_+% = -50**
- Observed: repair holds faster; world pickup unchanged → **rolled back**

---

## [1.9.0] — 2026-08-09

### Loadout — small pouches 2× slots

- `D_InventoryInfo` **`Pouch_Generic`**: `StartingSlots` **6 → 12**
- Applies to **Small Pouch** and **Small Red / Green / Blue** (shared inventory row)
- Itemable descriptions updated to say “12 slot”
- Waterwheel inventory edit preserved; Pete verified; LKG refreshed

---

## [1.8.0] — 2026-08-03

### Full table rebuild from current `data.pak`

- Rebuilt shared full tables from **live game `data.pak`**, then re-applied QoL layers
- **Single Barrel Launcher** present: `Item_Launcher_T2` + `T2_Launcher` recipe (tech tree icons)
- Pete teleport recipe/item/assets preserved
- Re-applied: stacks/weight, craft ~50% cost/speed, compost turbo ×10, tool 2×, dig 2×, drills +100/+166, solar/wind AlwaysActive, batteries 2×, wood fuel, armour 2×, food/saddles overlays, waterwheel, Waste Not + Olympus ores
- LKG refreshed

---

## [1.7.0] — 2026-07-25

### Checkpoint

- Tag current documented loadout line (through compost turbo **v1.6.0** / Olympus ores **v1.5.0** / power **v1.4.0** / drill recovery **v1.3.0**)
- `.gitignore`: ignore `examples/`
- **Known follow-up (done in 1.8.0):** rebuild full shared tables from current `data.pak` for **Single Barrel Launcher**

---

## [1.6.0] — 2026-07-25

### Loadout — composter biofuel turbo

- All **Composter** set biofuel recipes (`Biofuel1`–`10`, `Seed_Biofuel`):
  - **Biofuel output ×10** (`ResourceOutputs.RequiredUnits`)
  - **Input counts ÷4** (minimum 1) — stacks with prior craft-cost reductions
- Affects electric + standard metal composters (same recipe set); wood compost fertilizer recipes untouched
- Pete recipe preserved

---

## [1.5.0] — 2026-07-24

### Loadout — Olympus ores (Li / U / Ruby)

- Merged `olympus_ore_overhaul` into single pak:
  - **`Metal_Dense` → `Uranium_Raw`** (Waste Not exotic secondary kept)
  - Cave weights: **Lithium_Ore_Dense** (Arctic/Desert/Conifer), **Ruby_Ore_Dense** (Arctic only), **Metal_Dense** spawn weight in those caves
- New table path: **`D_VoxelDistributionRegion`**
- Built pak ready under `backup/grok.qualityoflife_P.pak` (install when game unlocked)

### Docs

- README Olympus ore section

---

## [1.4.0] — 2026-07-22

### Loadout (prod pak) — power QoL

- **`D_Energy.json`** added (current vanilla base + edits):
  - **SolarPanel** + **WindTurbine**: `AlwaysActive: true` (Unlimited Energy–style; night/no-wind production intent)
  - **Battery** flow **1500 → 3000**; **Battery_T4** **10000 → 20000** (2× charge/throughput)
- Pete and prior QoL paths unchanged
- LKG refreshed

### Docs

- README power section + feature rows; conflict table includes `D_Energy`

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
