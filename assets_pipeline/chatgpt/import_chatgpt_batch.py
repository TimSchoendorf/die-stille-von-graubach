#!/usr/bin/env python3
"""Deterministic importer for ChatGPT image batches.

Maps newest downloaded ChatGPT Image*.png files from inbox/raw_sync onto the
next missing asset IDs, then copies each source image to the manifest target.

Default mapping behavior:
- Select N newest source files (N = missing entries count, capped by available files)
- Map them to missing IDs in listed order
- Within selected files, map oldest->newest to preserve prompt order

Use --map-order newest to map newest->oldest instead.
"""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class SourceImage:
    path: Path
    mtime: float


def utc_now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_missing_ids(missing_file: Path) -> List[str]:
    ids: List[str] = []
    for raw in missing_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        stem = line[:-4] if line.lower().endswith(".png") else line
        ids.append(stem)
    return ids


def load_manifest_targets(manifest_file: Path) -> Dict[str, str]:
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    mapping: Dict[str, str] = {}
    for entry in entries:
        asset_id = entry.get("id")
        target = entry.get("target")
        if asset_id and target:
            mapping[asset_id] = target
    return mapping


def collect_raw_sync_images(raw_sync_dir: Path) -> List[SourceImage]:
    images: List[SourceImage] = []
    for p in raw_sync_dir.glob("ChatGPT Image*.png"):
        if p.is_file():
            images.append(SourceImage(path=p, mtime=p.stat().st_mtime))
    # Deterministic: newest first, ties by lexical name
    images.sort(key=lambda i: (-i.mtime, i.path.name))
    return images


def map_sources_to_missing(
    missing_ids: List[str],
    sources_newest_first: List[SourceImage],
    manifest_targets: Dict[str, str],
    map_order: str,
) -> Tuple[List[dict], List[str], List[str], int]:
    selected_count = min(len(missing_ids), len(sources_newest_first))
    selected = sources_newest_first[:selected_count]

    if map_order == "oldest":
        selected = sorted(selected, key=lambda i: (i.mtime, i.path.name))

    missing_manifest = [asset_id for asset_id in missing_ids[:selected_count] if asset_id not in manifest_targets]

    mappings: List[dict] = []
    for asset_id, src in zip(missing_ids[:selected_count], selected):
        target_rel = manifest_targets.get(asset_id)
        if not target_rel:
            continue
        mappings.append(
            {
                "asset_id": asset_id,
                "source": str(src.path),
                "source_name": src.path.name,
                "source_mtime": datetime.fromtimestamp(src.mtime, timezone.utc).isoformat(),
                "target_rel": target_rel,
            }
        )

    unmatched_missing = missing_ids[selected_count:] + missing_manifest
    unused_sources = [str(s.path) for s in sources_newest_first[selected_count:]]
    return mappings, unmatched_missing, unused_sources, selected_count


def render_text_report(report: dict) -> str:
    lines: List[str] = []
    lines.append("ChatGPT batch import report")
    lines.append(f"generated_at: {report['generated_at']}")
    lines.append(f"repo_root: {report['repo_root']}")
    lines.append(f"raw_sync_dir: {report['raw_sync_dir']}")
    lines.append(f"missing_file: {report['missing_file']}")
    lines.append(f"manifest_file: {report['manifest_file']}")
    lines.append(f"dry_run: {report['dry_run']}")
    lines.append(f"map_order: {report['map_order']}")
    lines.append("")
    lines.append("Counts")
    lines.append(f"- missing_total: {report['counts']['missing_total']}")
    lines.append(f"- source_candidates_total: {report['counts']['source_candidates_total']}")
    lines.append(f"- mapped_total: {report['counts']['mapped_total']}")
    lines.append(f"- copied_total: {report['counts']['copied_total']}")
    lines.append("")
    lines.append("Mappings")
    for row in report["mappings"]:
        lines.append(f"- {row['asset_id']}")
        lines.append(f"  source: {row['source']}")
        lines.append(f"  target: {row['target_abs']}")
        lines.append(f"  copied: {row['copied']}")

    if report["unmatched_missing"]:
        lines.append("")
        lines.append("Unmatched missing asset IDs")
        for item in report["unmatched_missing"]:
            lines.append(f"- {item}")

    if report["unused_sources"]:
        lines.append("")
        lines.append("Unused source images")
        for item in report["unused_sources"]:
            lines.append(f"- {item}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic ChatGPT batch image importer")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--manifest", type=Path, default=Path("assets_pipeline/manifest.json"))
    parser.add_argument("--missing", type=Path, default=Path("assets_pipeline/chatgpt/missing_now.txt"))
    parser.add_argument("--raw-sync", type=Path, default=Path("assets_pipeline/inbox/raw_sync"))
    parser.add_argument("--reports-dir", type=Path, default=Path("assets_pipeline/reports"))
    parser.add_argument("--map-order", choices=["oldest", "newest"], default="oldest")
    parser.add_argument("--dry-run", action="store_true", help="Compute and report mapping without copying files")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    manifest_file = (repo_root / args.manifest).resolve()
    missing_file = (repo_root / args.missing).resolve()
    raw_sync_dir = (repo_root / args.raw_sync).resolve()
    reports_dir = (repo_root / args.reports_dir).resolve()

    manifest_targets = load_manifest_targets(manifest_file)
    missing_ids = parse_missing_ids(missing_file)
    source_images_newest_first = collect_raw_sync_images(raw_sync_dir)

    mappings, unmatched_missing, unused_sources, selected_count = map_sources_to_missing(
        missing_ids, source_images_newest_first, manifest_targets, args.map_order
    )

    copied_total = 0
    for row in mappings:
        target_abs = (repo_root / row["target_rel"]).resolve()
        row["target_abs"] = str(target_abs)
        if not args.dry_run:
            target_abs.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(row["source"], target_abs)
            row["copied"] = True
            copied_total += 1
        else:
            row["copied"] = False

    ts = utc_now_compact()
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_json_path = reports_dir / f"chatgpt_import_report_{ts}.json"
    report_txt_path = reports_dir / f"chatgpt_import_report_{ts}.txt"

    report = {
        "generated_at": utc_now_iso(),
        "repo_root": str(repo_root),
        "manifest_file": str(manifest_file),
        "missing_file": str(missing_file),
        "raw_sync_dir": str(raw_sync_dir),
        "dry_run": args.dry_run,
        "map_order": args.map_order,
        "counts": {
            "missing_total": len(missing_ids),
            "source_candidates_total": len(source_images_newest_first),
            "selected_sources_total": selected_count,
            "mapped_total": len(mappings),
            "copied_total": copied_total,
        },
        "mappings": mappings,
        "unmatched_missing": unmatched_missing,
        "unused_sources": unused_sources,
    }

    report_json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report_txt_path.write_text(render_text_report(report), encoding="utf-8")

    print(f"Wrote report JSON: {report_json_path}")
    print(f"Wrote report TXT:  {report_txt_path}")
    print(f"Mapped: {len(mappings)} | Copied: {copied_total} | Missing IDs total: {len(missing_ids)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
