# Resources — travel / rebuild downloads

Links used to rebuild `grok.qualityoflife_P.pak` on a machine that does **not** have the home live pack or `_tools`. This is a download map, not loadout truth. Numbers and features stay in [README.md](./README.md).

The playable product is still **one file**: `grok.qualityoflife_P.pak`. Do not drop these sources into the game `mods` folder as a stack.

`_tools/`, `paks/`, and `backup/` are gitignored. Binaries stay local.

---

## Game

| What | Why | Where |
|------|-----|--------|
| **Icarus** (current week) | Vanilla `data.pak` is the table base. This laptop: `C:\Program Files (x86)\Steam\steamapps\common\Icarus`. Home docs use `D:\SteamLibrary\...`. | Steam app **1149460** |
| Live install path | Only this file goes in game mods after a merge. | `...\Icarus\Content\Paks\mods\grok.qualityoflife_P.pak` |

---

## Packer

| What | Why | Download |
|------|-----|----------|
| **UnrealPak** (zip, includes Oodle) | Extract `data.pak` / source paks; pack the merged QoL file. | https://github.com/Jimk72/Icarus_Software/raw/main/UnrealPak.zip |
| Extract to | Local only. | `\_tools\UnrealPak\` so `UnrealPak.exe` is under `UnrealPak\UnrealPak\Engine\Binaries\Win64\` |

Same zip is also in Jimk72’s repo: https://github.com/Jimk72/Icarus_Software/blob/main/UnrealPak.zip

---

## Source mods (put downloads in `paks/`)

Get the **current week** build (e.g. `w248`). Old week paks (w195–w202) are not usable.

| File / variant | Purpose in the merge | Download |
|----------------|----------------------|----------|
| **laanp-PetesBeaconTeleport** `*_P.pak` | Teleport remote + blueprints. **Must survive the merge.** | https://github.com/laanp/Icarus_Mods_Separated/releases/latest |
| **laanp-NoWaterWheelJunk** `*_P.pak` | Water wheels: no junk (`SlotTemplate` Any_Water). | Same release |
| **Bigger Resource Stacks + Reduced Weight — 10x Stacks 25% Weight** | `D_Itemable` MaxStack / Weight. **10× + 25% only.** | https://www.nexusmods.com/icarus/mods/103 |
| **Crafting Cost And Speed Reduction — 50%** | Cheaper / faster recipes. **50% remaining, not 25%.** | https://www.nexusmods.com/icarus/mods/106 |
| **Tool Yield Multiplier — 2x** | Mining / felling / reaping / skinning efficiency + felling damage. **2×, not 10×. Not melee.** | https://www.nexusmods.com/icarus/mods/96 |
| **Unlimited Energy** | `AlwaysActive` on solar + wind (`D_Energy`). Prefer current EXMODZ; old 2025 PAK is stale. | https://www.nexusmods.com/icarus/mods/66 |
| **Waste Not** `.EXMOD` / `.EXMODZ` | Mining secondaries (ores/exotics instead of waste stone). | [Project Daedalus](https://www.projectdaedalus.app/) → author **CritFail (Updated by AgentKush)** → Waste Not |
| **Deyvid Mods All-in-One** | Armor, food buffs, saddle/backpack slots. Prefer a **25% weight / ~2.5× armor** variant, **not Zero Weight**. | Nexus, author **DeyvidMods** — search [Icarus mods](https://www.nexusmods.com/icarus) |

laanp paks are also listed on [Project Daedalus](https://www.projectdaedalus.app/) (author **laanp**).

Hubs (browse, not required to pack):

- https://www.projectdaedalus.app/
- https://github.com/Jimk72/Icarus_Software (IMM — we do **not** use IMM as the install/merge path)

---

## Local tools (already on this laptop)

| What | Why |
|------|-----|
| Python 3 | `_tools/build_qol.py` merge + pack |
| 7-Zip | Extract Nexus `.rar` / `.zip` / `.EXMODZ` |

---

## Merge reminder

Pete first on shared tables (`D_Itemable`, `D_ProcessorRecipes`, Pete assets). Then layer stacks / craft / yield / energy / Waste Not / Deyvid unique stats. Output **only** `grok.qualityoflife_P.pak`.
