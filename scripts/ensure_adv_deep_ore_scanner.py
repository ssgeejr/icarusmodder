"""
Ensure Grok_Advanced_Deep_Ore_Scanner exists in a staging D_ProcessorRecipes.json.

Usage (from repo root, after extracting live QoL pak to a staging folder):

  python scripts/ensure_adv_deep_ore_scanner.py path/to/staging/data/Crafting/D_ProcessorRecipes.json

Idempotent: inserts or replaces the recipe row from
scripts/recipe_grok_advanced_deep_ore_scanner.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPE_FILE = ROOT / "scripts" / "recipe_grok_advanced_deep_ore_scanner.json"


def ensure(recipes_path: Path) -> None:
    recipe = json.loads(RECIPE_FILE.read_text(encoding="utf-8"))
    data = json.loads(recipes_path.read_text(encoding="utf-8"))
    name = recipe["Name"]
    for i, row in enumerate(data["Rows"]):
        if row.get("Name") == name:
            data["Rows"][i] = recipe
            action = "updated"
            break
    else:
        data["Rows"].append(recipe)
        action = "appended"
    recipes_path.write_text(
        json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    benches = [s["RowName"] for s in recipe["RecipeSets"]]
    print(f"{action} {name} benches={benches} -> {recipes_path}")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"missing: {path}", file=sys.stderr)
        return 1
    ensure(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
