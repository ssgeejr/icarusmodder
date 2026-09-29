# Deep Ore Scanner range (10×)

**Loadout:** v1.24.0+ (first shipped in v1.23.3)

Patches `BP_ActionableBehaviour_Scanner_DeepOre`:

- `MaxScanningRange`: **30000 → 300000** cm (**300 m → 3000 m**)

Advanced Deep Ore Scanner inherits this base behaviour.

Source approach: AgentKush Extended Deep Ore Scanner Range (researched only; we ship our own copy inside `grok.qualityoflife_P.pak`). Rebuild copies these files from here into the staging pak. Third-party archives stay under `Extracted Mods/` (gitignored).
