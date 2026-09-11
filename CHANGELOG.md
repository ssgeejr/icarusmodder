# Changelog

All notable changes to this repo and the **grok.qualityoflife_P.pak** loadout.

The playable pak is **not** stored in git (see `.gitignore`). Builds live under the game `mods` folder and copies under `backup/`.

---

## [1.22.0] — 2026-09-11

### Loadout — Week 249 schema rebuild (Inaris Powerbank)

- Rebased on game `data.pak` **Sep 10 ~17:15** (Week **249** / Steam buildid **25226979**)
- Closes shared-table gaps: `Meta_Powerbank`, `Item_Crab_Head`, Ground Dragon XP/meshes, tame Conifer Wolf carcass, alloy/ore meshes, etc.
- Re-applied full QoL stack (Pete, stacks/weight, craft 50%, XP 2.5×, Ice Box/Fridge, ruby=uranium, Adv scanner 3 benches, bees, drills, …)
- LKG refreshed

---

## [1.21.9] — 2026-09-10

### Loadout — Adv scanner on Fab/Manufacturer + laptop sync docs

- `Grok_Advanced_Deep_Ore_Scanner` RecipeSets: **Machining_Bench + Fabricator + Manufacturer**
- Tracked: `docs/ADVANCED_DEEP_ORE_SCANNER.md`, `docs/LAPTOP_SYNC.md`, `scripts/recipe_*.json`, `scripts/ensure_adv_deep_ore_scanner.py`
- After `git pull` on laptop, tell Grok: **update to latest changes** (see `docs/LAPTOP_SYNC.md`)
- LKG refreshed

---

## [1.21.8] — 2026-09-10

### Loadout — Advanced Deep Ore Scanner at Machining Bench

- New recipe `Grok_Advanced_Deep_Ore_Scanner` → outputs workshop **`Meta_Scanner_DeepOre`** (Advanced Deep Mining Ore Scanner)
- Bench: **Machining Bench** only (extended to Fab/Manufacturer in 1.21.9); no talent/Ren gate
- Cost (QoL 50% already applied): Aluminium 4, Electronics 4, Gold Wire 10, Steel Screw 10, Copper Wire 20, Glass 2; 5000 mJ
- Same item/BP as orbital Advanced scanner (ore-type toggle)
- LKG refreshed

---

## [1.21.7] — 2026-09-10

### Loadout — electric fridge spoil buff

- `Refrigerator_Spoil_Rate` `BaseInventorySpoilRate_+%` **-1000 → -5000** (**5×** QoL Ice Box at -2500)
- Ice Box values unchanged (rate 0.1 / spoil -2500)
- LKG refreshed

---

## [1.21.6] — 2026-09-10

### Loadout — Ice Box efficiency

- `Ice_Box` generator `GenerationRate` **1 → 0.1** (~**10×** ice fuel duration; Ice Box only)
- `IceBox_Spoil_Rate` `BaseInventorySpoilRate_+%` **-500 → -2500** (~**5×** longer food preserve vs prior icebox; approximate)
- Added full `D_ModifierStates` to the pak for the spoil modifier
- LKG refreshed

---

## [1.21.5] — 2026-09-09

### Loadout — +150% experience (2.5×)

- `D_ExperienceEvents`: all nonzero `ExperienceGranted` values ×**2.5** (+150% XP)
- `D_Experience` trait overrides: nonzero `GainedExperience` ×**2.5**
- Intent: 5th character start-over — cut re-grind, keep early helplessness
- Examples: ChopTree 100→250, MineStone 30→75, Easy_Mission 5000→12500
- LKG refreshed

---

## [1.21.4] — 2026-09-08

### Loadout — revert oil barrel backpack experiment

- Restored `Mesh_Oil_Barrel` to **vanilla** (`EquipBackMesh` + `EquipBackActor` / dedicated back slot)
- 1.21.3 backpack attempt failed in-game; rolled back
- LKG refreshed

---

## [1.21.3] — 2026-09-08

### Loadout — oil barrel in backpack (reverted in 1.21.4)

- Attempted: remove `EquipBackMesh` / `EquipBackActor` so Oil Barrel uses backpack inventory
- **Failed in play** — do not reapply without a different approach

---

## [1.21.2] — 2026-09-07

### Loadout — portable beacons stack again

- `Item_Portable_Beacon`: `MaxStack` **100**, `Weight` **0** (laanp Pete w248 parity; laptop behavior)
- Home Week 248 rebuild had left vanilla non-stacking beacons; fixed and locked into `rebuild.py`
- Pete teleport remote unchanged
- LKG refreshed: `backup/qol_KNOWN_GOOD_latest.zip`

---

## [1.21.1] — 2026-09-04

### Loadout — ruby parity with uranium

- `Ruby_Ore_Dense` weight now **equals `Metal_Dense`** in every distribution region that spawns uranium dense nodes (11 regions): Olympus Arctic/Desert/Conifer **20**, plus Prometheus cave clusters and Elysium Tundra Gorge
- Olympus Arctic ruby **3 → 20**; Desert/Conifer gained ruby **20** (were missing)
- Intent: stop buying rubies from orbit — same rarity footprint as uranium nodes
- Existing worlds may need Deep Cycler / new cave voxels to see new ruby pockets

---

## [1.21.0] — 2026-09-04

### Loadout — post Week 248 schema rebuild

- Rebased on game `data.pak` **Sep 3** (Week **248** / Scoria deep veins + new creatures era; Steam buildid **25030066**)
- Closes gaps from Week 248 shared tables:
  - `Item_Carcass_Axolotl`, `Item_Carcass_Crawler`, `Item_Carcass_Giant_Beetle`, `Item_Carcass_Plant_Minion_Elite`, `Item_Giant_Beetle_Head`
  - `Mesh_Carcass_Axolotl`, `Mesh_Carcass_Crawler`, `Mesh_Carcass_Giant_Beetle`, `Mesh_Carcass_Plant_Minion_Elite`
- Vanilla also dropped `Tropical_Bird` AI row; QoL no longer needs those carcass extras from Week 247
- Re-applied full QoL stack (Pete, stacks/weight, craft 50%, drills, ice 0.1s, wind AlwaysActive+invuln, stasis unlock, bees ×10,000, pouches, voxels, compost, etc.)
- Scoria deep-vein deposits remain vanilla cycle (**40s** `MiningTimeSeconds`) — no Ice_Borer-style override
- Zero missing rows on shared full tables after rebuild; LKG pending in-game smoke

---

## [1.20.0] — 2026-08-31

### Loadout — immortal queens and workers

- `D_Transmutable` **Queen_Bee**: `UnitsProvided` **3,600,000,000** (×10,000 vanilla / ×100 prior QoL)
- `D_Transmutable` **Bee** (workers): `UnitsProvided` **1,800,000,000** (×10,000 vanilla)
- Practical immortality for hive fuel/breeding life; breed *rate* unchanged (still BP 0.05/min)
- LKG refreshed

---

## [1.19.0] — 2026-08-30

### Loadout — post Week 247 schema rebuild (Slinker)

- Rebased on game build **24941209** / `data.pak` **Aug 30** (Week **247** Slinker saddles era)
- Closes gaps from Week 247: `Item_Carcass_Tropical_Bird`, `Item_Tropical_Bird_Head`, `Mesh_Carcass_Tropical_Bird`
- Re-applied full QoL stack (Pete, stacks/weight, craft, drills, ice 0.1s, wind AlwaysActive+invuln, stasis unlock, queen ×100, pouches, voxels, compost, etc.)
- AgentKush EXMOD candidates reviewed and **rejected** (NVG / Survival Attachments / Solar Workshop) under no-risk policy — not merged
- Zero missing rows on shared full tables after rebuild; LKG refreshed

---

## [1.18.0] — 2026-08-30

### Loadout — post Week 246 schema rebuild

- Game `data.pak` refreshed (**Aug 21** / Week **246** Metal Weapon Rack era; build beyond our Aug 15 extract)
- Full-table QoL rebased on latest vanilla so shared overrides no longer hide new rows
- Newly present (examples): **`Weapon_Rack_T3` / `T3_Weapon_Rack_Single`**, `AnimalCarcass_Orka_Mount`, jungle/centipede/slinker carcass itemables+meshes, Kiwi bait/itemable rows
- Re-applied: Pete, stacks/weight, craft 50%, gather 2×, dig 2×, drills, ice 0.1s, wind AlwaysActive+invuln, stasis FocusLock strip, queen ×100, pouches 12, voxels, compost, armor/food/saddles overlays
- Zero missing-from-mod rows on recipes / ItemsStatic / ItemTemplate / Itemable / Meshable after rebuild
- LKG refreshed

---

## [1.17.0] — 2026-08-18

### Loadout — uninterrupted wind power

- `Wind_Turbine`: `IsInvulnerable_? = 1` (no storm/overproduction durability loss)
- Keeps existing `WindTurbine` `AlwaysActive` (already in pack)
- Together: continuous wind power without babysitting repairs
- LKG refreshed after install

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
