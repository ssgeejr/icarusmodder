# Perryville laptop session — 2026-09-05

Travel machine (Dynabook PORTEGE X40-J). Not the home gaming box. Home live pack, `_tools`, and `backup/qol_KNOWN_GOOD_latest.zip` were not on this laptop. Work was rebuilt from **README / CHANGELOG (v1.20.0)** plus current-week community sources, then installed as **one** `grok.qualityoflife_P.pak`.

Game install here:

`C:\Program Files (x86)\Steam\steamapps\common\Icarus`

(not `D:\SteamLibrary\...`). Steam build **25030066**, `data.pak` dated **4 Sep 2026** (week **248**). Documented home loadout was Week **247**.

No IMM. Pete first on shared tables.

---

## What was done

1. **Cleared the game `mods` folder.** It had a 2025 multi-pak stack (Pete w201, aux slots, item finder, mission rewards ×10, bag-first sort, Unlimited Energy). Those files were stale vs week 248. Keepers moved to repo `mods/` then the live folder was emptied.

2. **Downloaded current sources into `paks/`** (gitignored). UnrealPak zip into `_tools/` (gitignored).

3. **Built a single pak** from vanilla week-248 `data.pak` + sources, Pete rows/assets first, then QoL. Output:

   `backup/grok.qualityoflife_P.pak`

   Installed to:

   `...\Icarus\Content\Paks\mods\grok.qualityoflife_P.pak`

   Only that file in `mods`. Before-stamps: `backup/qol_before_*.zip`. **LKG was not written** (no `qol_KNOWN_GOOD_latest.zip` on this machine).

4. **Ruby on Olympus caves.** After the first install, `Ruby_Ore_Dense` weight **3** was added to **Desert** and **Conifer** caves as well as Arctic (it had been Arctic-only). Uranium (dense-metal remap) and lithium **20** were already on all three. Pak rebuilt and reinstalled. Existing mined caves do not reroll voxels.

5. **`resources.md`** added and pushed earlier (download map). This file is the session log.

6. **Did not** restack old paks into the game folder. Did not change combat `Melee_Damage`. Did not write live mods while Icarus was running.

---

## Loadout applied (match to home docs)

Applied from README numbers, not by copying the home binary (home pak was not here).

| Item | This pak |
|------|----------|
| Pete Beacon Teleport | laanp **w248** recipe + item + blueprints |
| Stacks / weight | 10× / 25% (`D_Itemable`), Pete rows protected |
| Craft cost | ~50% inputs (50% file, not the 25% download) |
| Tools | **2×** yield (not the 10× download); melee untouched |
| Waste Not | EXMOD merged into `D_VoxelSetupData` |
| Water-wheel no junk | laanp w248 `SlotTemplate` |
| Solar / wind AlwaysActive; batteries 2×; wind invulnerable | yes |
| Composter biofuel | ×10 output, inputs ÷4 |
| Biofuel deep drill | `BaseDeepMiningDrillSpeed_+%` **+100** (~2× ore). Fuel **vanilla 0.75** (`D_Generator` not in pak) |
| Electric deep drill | **+166%** |
| Ice | deposit cycle 0.1s |
| Bees | `UnitsProvided` queen **3.6B**, workers **1.8B** |
| Pouches | `Pouch_Generic` 12 slots |
| Wood fuel | `Wood` `UnitsProvided` ×10 on `D_Transmutable` (home docs also mention `D_Generator`; that table is **not** in this pak) |
| Olympus Li / U / Ruby | as above |

Wrong downloads were **not** used as-is: craft 25%, tool 10×, Deyvid **Zero Weight** all-in-one (armor/food/inventory slots still overlaid from that AIO). Stasis FocusLock strip was a no-op (tag not on week-248 item rows).

---

## Why portable beacons stack here (and may not at home)

Verified on this build:

| | `Item_Portable_Beacon` Weight | MaxStack |
|--|-------------------------------|----------|
| Vanilla week 248 | 10000 | none (does not stack) |
| laanp Pete **w248** source | **0** | **100** |
| This QoL pak | **0** | **100** |

The **w248 Pete Beacon Teleport pak itself** sets portable beacons to `MaxStack: 100`. Merge rule was Pete-wins on `Item_Portable_Beacon` and `Item_Petes_BeaconTeleportRemote`, so the **stacks overlay never touched beacons**. They stack because we kept laanp’s row, not because of the 10× stacks pack.

Home “they do not stack any more” is consistent with a later home merge that:

- started from **vanilla** itemable (no MaxStack) and only *added* Pete’s remote, or
- applied stacks/QoL to beacons in a way that dropped Pete’s `MaxStack: 100`, or
- used an older Pete that did not stack beacons.

This laptop used **current laanp w248**, which **does** stack them.

### Agent: what to do about beacon stacks

Do **not** “fix” stacking from a travel rebuild unless the user chooses.

- **Keep travel behavior (stack 100):** leave Pete’s `Item_Portable_Beacon` row as-is (`MaxStack: 100`, `Weight: 0`). Never let the 10× stacks overlay write that name.
- **Match home (do not stack):** after Pete extras are merged, set `Item_Portable_Beacon` back to **vanilla**: omit `MaxStack` (or null), `Weight: 10000`. Do **not** strip `Item_Petes_BeaconTeleportRemote` or the teleport recipe/assets.
- Confirm with the user before changing this. Home truth: *portable beacons no longer stack*.

Pete **teleport remote** is a separate item (`Item_Petes_BeaconTeleportRemote`). Collision check: Pete recipe/item/static/mesh/BP identical to w248 source; 44 unique pak paths; no duplicates.

---

## Not done / not on this machine

- Hash compare to `D:\SteamLibrary\...` live pak  
- `qol_KNOWN_GOOD_latest.zip`  
- Version bump / CHANGELOG / tag (README ruby line may be the only other md drift)  
- Raising ruby weight (left at **3**, rare on purpose)

`_tools/`, `paks/`, `backup/`, `*.pak` remain gitignored.
