#!/usr/bin/env python3
"""
Convert an Icarus .EXMOD (delta JSON) into a playable *_P.pak without IMM.

Steps:
  1. Read EXMOD deltas
  2. Load matching full JSON tables from the game data.pak (or a pre-extracted folder)
  3. Deep-merge changed fields into those full tables
  4. Pack with UnrealPak using the correct mount point

Usage:
  python exmod_to_pak.py "Extracted Mods/Waste_Not.EXMOD"
  python exmod_to_pak.py "Extracted Mods/Waste_Not.EXMOD" --output Waste_Not_P.pak

Never writes into the game install. Output is only the .pak path you choose.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


# Default locations on this machine (override via CLI flags)
DEFAULT_GAME_ROOT = Path(r"D:\SteamLibrary\steamapps\common\Icarus")
DEFAULT_UNREALPAK = Path(
    r"C:\dev\games\icarusmods\_tools\UnrealPak\UnrealPak\Engine\Binaries\Win64\UnrealPak.exe"
)
DEFAULT_DATA_EXTRACT = Path(r"C:\dev\games\icarusmods\_tools\data_extract")


def deep_merge(base: dict, patch: dict) -> dict:
    """Merge patch into base (dict values recurse; lists/scalars replace)."""
    out = dict(base)
    for key, value in patch.items():
        if key == "Name":
            continue
        if (
            key in out
            and isinstance(out[key], dict)
            and isinstance(value, dict)
        ):
            out[key] = deep_merge(out[key], value)
        else:
            out[key] = value
    return out


def exmod_file_to_path(current_file: str) -> Path:
    """
    EXMOD uses 'Folder-Filename.json' e.g. World-D_VoxelSetupData.json
    Game data uses Folder/Filename.json e.g. World/D_VoxelSetupData.json
    """
    name = current_file
    if name.lower().endswith(".json"):
        name = name[:-5]
    # Split on first '-' only if it looks like Folder-D_Something
    # Known pattern: Category-D_Name
    if "-" in name:
        folder, rest = name.split("-", 1)
        return Path(folder) / f"{rest}.json"
    return Path(f"{name}.json")


def apply_exmod(exmod: dict, data_root: Path) -> dict[Path, dict]:
    """
    Returns map of relative path (under data/) -> full modified JSON object.
    """
    results: dict[Path, dict] = {}
    for file_block in exmod.get("Rows", []):
        current = file_block["CurrentFile"]
        rel = exmod_file_to_path(current)
        src = data_root / rel
        if not src.is_file():
            raise FileNotFoundError(
                f"Base game JSON not found for {current} -> {src}\n"
                f"Extract data.pak first or pass --data-extract."
            )
        base = json.loads(src.read_text(encoding="utf-8"))
        by_name = {row["Name"]: row for row in base.get("Rows", [])}
        for item in file_block.get("File_Items", []):
            name = item["Name"]
            if name not in by_name:
                raise KeyError(f"Row '{name}' not found in {rel}")
            by_name[name] = deep_merge(by_name[name], item)
        # Preserve original row order
        base["Rows"] = [by_name[row["Name"]] for row in base["Rows"]]
        results[rel] = base
    return results


def write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Pretty-print similar to game files (4-space indent)
    path.write_text(
        json.dumps(obj, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def create_pak(
    unrealpak: Path,
    files: dict[Path, Path],
    out_pak: Path,
) -> None:
    """
    files: relative path under data/ -> absolute path to local file
    Mount point style matches working Icarus mods:
      ../../../Icarus/Content/data/<Folder>/<File>
    """
    out_pak.parent.mkdir(parents=True, exist_ok=True)
    if out_pak.exists():
        out_pak.unlink()

    # Response file: "local_path" "mount_path"
    lines = []
    for rel, local in files.items():
        mount = f"../../../Icarus/Content/data/{rel.as_posix()}"
        lines.append(f'"{local}" "{mount}"')

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as rf:
        rf.write("\n".join(lines) + "\n")
        response = Path(rf.name)

    try:
        cmd = [str(unrealpak), str(out_pak), f"-Create={response}", "-compress"]
        print("Running:", " ".join(cmd))
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(unrealpak.parent),
        )
        if proc.returncode != 0:
            print(proc.stdout)
            print(proc.stderr, file=sys.stderr)
            raise RuntimeError(f"UnrealPak failed with code {proc.returncode}")
        # Show summary lines
        for line in (proc.stdout or "").splitlines():
            if "Display:" in line or "Error" in line:
                print(line)
    finally:
        response.unlink(missing_ok=True)


def extract_data_pak(unrealpak: Path, data_pak: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    cmd = [str(unrealpak), str(data_pak), "-Extract", str(dest)]
    print("Extracting data.pak...")
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(unrealpak.parent))
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise RuntimeError("Failed to extract data.pak")


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert Icarus EXMOD to PAK (no IMM)")
    ap.add_argument("exmod", type=Path, help="Path to .EXMOD file")
    ap.add_argument(
        "--game-root",
        type=Path,
        default=DEFAULT_GAME_ROOT,
        help="Icarus install root",
    )
    ap.add_argument(
        "--unrealpak",
        type=Path,
        default=DEFAULT_UNREALPAK,
        help="Path to UnrealPak.exe",
    )
    ap.add_argument(
        "--data-extract",
        type=Path,
        default=DEFAULT_DATA_EXTRACT,
        help="Folder of extracted data.pak JSON tables",
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output .pak path (default: <fileName>_P.pak in the repo root). Never the game mods folder.",
    )
    ap.add_argument(
        "--reextract-data",
        action="store_true",
        help="Force re-extract data.pak before merging",
    )
    args = ap.parse_args()

    exmod_path = args.exmod.resolve()
    if not exmod_path.is_file():
        print(f"EXMOD not found: {exmod_path}", file=sys.stderr)
        return 1

    if not args.unrealpak.is_file():
        print(f"UnrealPak not found: {args.unrealpak}", file=sys.stderr)
        return 1

    data_pak = args.game_root / "Icarus" / "Content" / "Data" / "data.pak"
    if args.reextract_data or not (args.data_extract / "World" / "D_VoxelSetupData.json").is_file():
        if not data_pak.is_file():
            print(f"data.pak not found: {data_pak}", file=sys.stderr)
            return 1
        if args.data_extract.exists():
            shutil.rmtree(args.data_extract)
        extract_data_pak(args.unrealpak, data_pak, args.data_extract)

    exmod = json.loads(exmod_path.read_text(encoding="utf-8"))
    file_name = exmod.get("fileName") or exmod_path.stem
    # Icarus mod paks conventionally end with _P
    pak_name = file_name if file_name.endswith("_P") else f"{file_name}_P"
    if not pak_name.endswith(".pak"):
        pak_name = f"{pak_name}.pak"

    out_pak = args.output or (exmod_path.parent.parent / pak_name)
    out_pak = out_pak.resolve()

    print(f"Mod: {exmod.get('name')} v{exmod.get('version')} by {exmod.get('author')}")
    print(f"Merging EXMOD into base tables from: {args.data_extract}")

    modified = apply_exmod(exmod, args.data_extract)

    work = Path(tempfile.mkdtemp(prefix="exmod2pak_"))
    try:
        local_map: dict[Path, Path] = {}
        for rel, obj in modified.items():
            local = work / rel
            write_json(local, obj)
            local_map[rel] = local
            print(f"  wrote {rel} ({len(obj.get('Rows', []))} rows)")

        create_pak(args.unrealpak, local_map, out_pak)
        print(f"Created: {out_pak} ({out_pak.stat().st_size} bytes)")

        # Verify
        list_proc = subprocess.run(
            [str(args.unrealpak), str(out_pak), "-List"],
            capture_output=True,
            text=True,
            cwd=str(args.unrealpak.parent),
        )
        for line in (list_proc.stdout or "").splitlines():
            if "Mount point" in line or ".json" in line:
                print(line)

        print("Done. Pak was NOT copied into the game mods folder.")
    finally:
        shutil.rmtree(work, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
