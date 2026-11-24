# Laptop sync — pull then “update to latest changes”

Use this on **Perryville / any non-home box** after `git pull`.

Tell Grok:

> **update to latest changes**

That means: read this file + `README.md` + `CHANGELOG.md` + `AGENTS.md`, match the live pak on **this** PC to the documented loadout, then backup → rebuild/patch → install → LKG → commit/push doc fixes. Game closed for install.

---

## Critical facts

| Fact | Detail |
|------|--------|
| Playable pak | **`grok.qualityoflife_P.pak` is gitignored** — `git pull` does **not** install it |
| Features / numbers | `README.md` + `CHANGELOG.md` |
| Content on a machine | That machine’s live pak (evolve it; never restack old multi-paks) |
| Process | `AGENTS.md` — Pete first, one `_P.pak`, backups under `backup/`, smoke after install |
| Current version | **v2.8.0** (Week **259** schema) |

---

## Paths

| | Home | Laptop (Perryville) |
|--|------|---------------------|
| Repo | `C:\dev\games\icarusmods` | same or clone |
| Game | `D:\SteamLibrary\steamapps\common\Icarus\...` | `C:\Program Files (x86)\Steam\steamapps\common\Icarus\...` |
| Live pak | `...\Icarus\Content\Paks\mods\grok.qualityoflife_P.pak` | same relative under that install |
| Steam manifest | `D:\SteamLibrary\steamapps\appmanifest_1149460.acf` | under that Steam library |
| UnrealPak | `_tools/UnrealPak/.../UnrealPak.exe` (gitignored — recreate if missing) |

---

## Current documented state (v2.8.0) — what the pak must contain

**Game schema:** Week **259** / Steam buildid **26636089** / `data.pak` ~**20 Nov 2026** / game **v3.0.37.160033**

### Must-keep QoL (do not drop on rebuild)

- **Pete’s Beacon Teleport** (recipe + itemable + BP/UI assets) — if teleport fails, rollback
- Stacks **10×** / weight **25%** (`D_Itemable`); portable beacon MaxStack **100** Weight **0**
- Craft cost/speed ~**50%**; compost biofuel **×10** out / inputs **÷4**
- Tool gather **2×** (+ felling damage); shovel dig **2×**; Waste Not voxels
- Armor ~**2.5×**; food buffs ~**2.5×**; wood fuel **×10**; pouches **12** slots
- Solar/wind **AlwaysActive**; wind turbine invulnerable; batteries **2×** flow
- Deep drills: bio/oil **+100**, electric **+166**; ice deposit cycle **0.1s**; fuel burn vanilla
- Pump Jack + Crude Oil Refiner **4000**; Organic Extractor **BLOOM** (gen **5e6**/ratio **100**, fuel **5e6**, UnitsProvided **1e8** fiber/meats/plants)
- Queen/worker bees immortal (UnitsProvided **×10k** + Queen `Max_Durability` **2e9**)
- XP **×2.5**; farm growth **÷6**; Ice Box spoil **-2500**; Fridge **-5000**; Deep Freeze **50** slots
- Cool buildings **400k** HP + BuildingTier **8**; Reinforced Glass = Concrete (**4000** / tier **8**)
- Décor DLC **163** recipes @ Carpentry only; Gustav / textiles / Larkwell O2 / Workshop Repair Kit Grok crafts
- Scanner BP **10×** range (`assets/scanner_range/`); Adv Deep Ore Scanner craft
- Olympus/Elysium cave ores (U/Li/Ruby/Clay); Fireplace stick→**100** charcoal; Windmill queue **10**; wood→sap **×5**
- Stasis bag FocusLock strip; water-wheel no junk

### Vanilla Week 259 rows the rebuild must fold (schema catch-up)

| Row | Table | Notes |
|-----|-------|--------|
| `Armour_Stand_T4` | ItemsStatic + ItemTemplate | Powered armor stand (British spelling) |
| `Armor_Stand_T4` | ProcessorRecipes + Talents | Fabricator/Manufacturer; 120 Al / 4 Elec / 60 Steel Screw / 8 Composites |
| `Item_Armour_Stand_T4` | Itemable | Display/talent link |
| `Advanced_Armor_Stand` | Energy (+ Resource) | AutoActivate repair path (~1 durability / 2s when powered) |
| `Item_Roaster` / `Roaster` | Itemable / Processing / Deployable | **Replaces** `Item_Smoker_T4` / `Smoker_T4` — do not keep smoker names |

Also keep prior catch-up rows: `Workshop_Lantern`, `Item_Captured_Juvenile_Bear`, `Item_NPC_Rancher`, `Item_Fertility_Serum_Mammoth_Arctic`, W255 turret/curry, W256 Alteration Durable **750/1500**, etc.

**QoL balance was not changed in v2.8.0** — schema rebase only.

---

## After `git pull` checklist for Grok

1. `git status` / `git log -5` — confirm **v2.8.0** (or newer) in CHANGELOG.
2. Check this PC’s Steam `buildid` + `data.pak` date vs README Week/buildid.
3. Locate live `grok.qualityoflife_P.pak`; confirm Icarus is **not** running.
4. Backup → `backup/qol_before_<stamp>.zip`.
5. If game week > documented week **or** live missing vanilla rows:
   - Extract `data.pak` → `_tools/data_extract_wNNN`
   - Promote → `_tools/data_extract_latest`
   - Refresh `_tools/qol_rebuild/live` from **this** live pak
   - Update `rebuild.py` asserts for new rows; run `python _tools/qol_rebuild/rebuild.py` (installs prod)
   - Post-diff shared tables **CLEAN**; spot Pete + Deep Freeze 50 + Pump Jack 4000 + OE 5e6
6. If only docs ahead of live pak: surgical patch or full rebuild until README features match.
7. Smoke: **teleport → stacks → craft → gather**.
8. Refresh `backup/qol_KNOWN_GOOD_latest.zip`; update README/CHANGELOG if needed; **commit + push**.

### UnrealPak

```
UnrealPak.exe <pak> -Extract <outdir>
# pack to temp then copy to mods — never -Extract= (can wipe pak)
```

`_tools/` is gitignored. If missing on laptop: restore UnrealPak zip, recreate `qol_rebuild/rebuild.py` from home/memory, or copy tooling from home.

---

## Ranked backlog (what to build / improve next)

Prefer first-30-minutes session friction. Avoid BP-locked bee breed times, combat damage buffs, or another 10× on already-10× systems.

1. **Hydrazine dehumidifier** (Week 260 preview) — fold into schema when it ships; optional QoL only if vanilla is gated awkwardly.
2. **Plain Glass → concrete-class toughness** (Reinforced Glass already done).
3. **Bigger logistics storage** / chest tetris relief.
4. **Benches / storage / drills / refiners / troughs** as tough as cool buildings.
5. **Tool / weapon wear** reduction.
6. **Pet Companions unlock @ Carpentry only** (no mission recipes) — FeatureLevel `PenPals` / bear track is in vanilla now; don’t fight it.
7. Processor craft speed polish (honorable mention).

Do **not** chase: bee breed interval (BP_Beehive), sprinkler radius (BP-locked), restacking old multi-paks, IMM.

---

## Tracked in git (pull these)

- `README.md`, `CHANGELOG.md`, `AGENTS.md`
- `docs/` (this file, `ADVANCED_DEEP_ORE_SCANNER.md`, …)
- `scripts/` (portable recipe helpers)
- `assets/scanner_range/` (scanner BP sources)
- `exmod_to_pak.py`, `continue*.cmd`, `perryville.changes.md`, `resources.md`

## Not in git (local / recreate)

- `_tools/` (UnrealPak, extracts, `qol_rebuild/rebuild.py` working copy)
- `backup/`, `paks/`, `*.pak`
- Live game `mods\` pak

---

## Recent feature pointers

| Feature | Doc / script |
|---------|----------------|
| Advanced Deep Ore Scanner | `docs/ADVANCED_DEEP_ORE_SCANNER.md`, `scripts/ensure_adv_deep_ore_scanner.py` |
| Full loadout numbers | `README.md` |
| Version history | `CHANGELOG.md` |
| Process / Pete-first | `AGENTS.md` |
| Older laptop session log | `perryville.changes.md` (historical; this file wins for current sync) |
