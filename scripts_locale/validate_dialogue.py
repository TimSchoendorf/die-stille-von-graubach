#!/usr/bin/env python3
"""Validate all dialogue JSON files for structural integrity."""

import json
import os
import sys
from collections import defaultdict

DIALOGUE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "dialogue")
SPRITES_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "sprites", "characters")

# Valid expressions per character (built from sprite files)
VALID_EXPRESSIONS = {}

def build_expression_map():
    """Build map of valid expressions from sprite files on disk."""
    if not os.path.isdir(SPRITES_DIR):
        return
    for char_dir in os.listdir(SPRITES_DIR):
        char_path = os.path.join(SPRITES_DIR, char_dir)
        if not os.path.isdir(char_path):
            continue
        expressions = set()
        for f in os.listdir(char_path):
            if f.endswith(".png") and not f.endswith(".png.import"):
                expressions.add(os.path.splitext(f)[0])
        if expressions:
            VALID_EXPRESSIONS[char_dir] = expressions

def find_all_json_files():
    """Find all dialogue JSON files."""
    files = []
    for root, _, filenames in os.walk(DIALOGUE_DIR):
        for f in filenames:
            if f.endswith(".json"):
                files.append(os.path.join(root, f))
    return sorted(files)

def validate_file(filepath):
    """Validate a single dialogue JSON file. Returns list of errors."""
    errors = []
    rel = os.path.relpath(filepath, DIALOGUE_DIR)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"{rel}: JSON parse error: {e}"]

    nodes = data.get("nodes", {})
    start = data.get("start")

    if not start:
        errors.append(f"{rel}: Missing 'start' field")
    elif start not in nodes:
        errors.append(f"{rel}: Start node '{start}' not found in nodes")

    # Check all references
    for nid, node in nodes.items():
        ntype = node.get("type", "unknown")

        # Check 'next'
        if "next" in node:
            target = node["next"]
            if target not in nodes and ntype != "scene_end":
                errors.append(f"{rel}: Node '{nid}' -> next '{target}' not found")

        # Check flag_check true_next/false_next
        if ntype == "flag_check":
            for field in ("true_next", "false_next"):
                target = node.get(field)
                if target and target not in nodes:
                    errors.append(f"{rel}: Node '{nid}' -> {field} '{target}' not found")

        # Check choice nexts
        if ntype == "choice":
            for i, choice in enumerate(node.get("choices", [])):
                target = choice.get("next")
                if target and target not in nodes:
                    errors.append(f"{rel}: Node '{nid}' choice[{i}] -> next '{target}' not found")

    return errors

def validate_expressions(all_files_data):
    """Validate that all character/dialogue expressions reference existing sprites."""
    errors = []
    if not VALID_EXPRESSIONS:
        return errors

    for filepath, data in all_files_data.items():
        rel = os.path.relpath(filepath, DIALOGUE_DIR)
        nodes = data.get("nodes", {})

        for nid, node in nodes.items():
            ntype = node.get("type", "")

            # Character nodes: check expression
            if ntype == "character":
                char_id = node.get("id", "").lower()
                expr = node.get("expression", "")
                if char_id and expr and char_id in VALID_EXPRESSIONS:
                    if expr not in VALID_EXPRESSIONS[char_id]:
                        valid = sorted(VALID_EXPRESSIONS[char_id])
                        errors.append(f"{rel}: Node '{nid}' character '{char_id}' has invalid expression '{expr}' (valid: {valid})")

            # Dialogue nodes: check expression against speaker
            if ntype == "dialogue":
                speaker = node.get("speaker", "").lower()
                expr = node.get("expression", "")
                if speaker and expr and speaker in VALID_EXPRESSIONS:
                    if expr not in VALID_EXPRESSIONS[speaker]:
                        valid = sorted(VALID_EXPRESSIONS[speaker])
                        errors.append(f"{rel}: Node '{nid}' dialogue speaker '{speaker}' has invalid expression '{expr}' (valid: {valid})")

    return errors

def track_flags(all_files_data):
    """Track which flags are set and which are checked across all files."""
    set_flags = defaultdict(list)  # flag -> [(file, node_id)]
    checked_flags = defaultdict(list)  # flag -> [(file, node_id)]

    for filepath, data in all_files_data.items():
        rel = os.path.relpath(filepath, DIALOGUE_DIR)
        nodes = data.get("nodes", {})

        for nid, node in nodes.items():
            ntype = node.get("type", "")

            # Flags set via set_flag node
            if ntype == "set_flag":
                flag = node.get("flag", "")
                if flag:
                    set_flags[flag].append((rel, nid))

            # Flags set via add_flag node
            if ntype == "add_flag":
                flag = node.get("flag", "")
                if flag:
                    set_flags[flag].append((rel, nid))

            # Flags checked via flag_check
            if ntype == "flag_check":
                flag = node.get("flag", "")
                if flag:
                    checked_flags[flag].append((rel, nid))

            # Flags set via choice set_flags
            if ntype == "choice":
                for choice in node.get("choices", []):
                    for flag in choice.get("set_flags", {}):
                        set_flags[flag].append((rel, nid))
                    for flag in choice.get("add_flags", {}):
                        set_flags[flag].append((rel, nid))
                    for flag in choice.get("require_flags", {}):
                        if not flag.startswith("_"):
                            checked_flags[flag].append((rel, nid))

    return set_flags, checked_flags

def check_reachability(all_files_data):
    """Check which ending files are reachable via scene_end chains."""
    endings = {
        "ending_seal.json", "ending_truth.json", "ending_pact.json",
        "ending_escape.json", "ending_sacrifice.json", "ending_awakening.json"
    }

    reachable_files = set()
    for filepath, data in all_files_data.items():
        nodes = data.get("nodes", {})
        for nid, node in nodes.items():
            if node.get("type") == "scene_end":
                next_file = node.get("next_file", "")
                # Extract just filename
                fname = os.path.basename(next_file)
                reachable_files.add(fname)

    unreachable = endings - reachable_files
    return unreachable

def main():
    build_expression_map()
    files = find_all_json_files()
    print(f"Found {len(files)} dialogue files")
    if VALID_EXPRESSIONS:
        print(f"Loaded expressions for {len(VALID_EXPRESSIONS)} characters")
    print()

    all_errors = []
    all_data = {}

    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                all_data[fp] = json.load(f)
        except json.JSONDecodeError:
            pass

        errs = validate_file(fp)
        all_errors.extend(errs)

    # Print structural errors
    if all_errors:
        print(f"=== STRUCTURAL ERRORS ({len(all_errors)}) ===")
        for e in all_errors:
            print(f"  ERROR: {e}")
    else:
        print("=== STRUCTURAL VALIDATION: ALL OK ===")

    # Expression validation
    expr_errors = validate_expressions(all_data)
    print()
    if expr_errors:
        print(f"=== EXPRESSION ERRORS ({len(expr_errors)}) ===")
        for e in expr_errors:
            print(f"  ERROR: {e}")
        all_errors.extend(expr_errors)
    else:
        print("=== EXPRESSION VALIDATION: ALL OK ===")

    # Flag tracking
    print()
    set_flags, checked_flags = track_flags(all_data)

    dead_set = set(set_flags.keys()) - set(checked_flags.keys())
    dead_check = set(checked_flags.keys()) - set(set_flags.keys())

    # Filter out known special flags
    special = {"act3_complete", "read_final_entries"}
    dead_set -= special

    print(f"=== FLAG ANALYSIS ===")
    print(f"  Flags set: {len(set_flags)}")
    print(f"  Flags checked: {len(checked_flags)}")
    print(f"  Dead flags (set but never checked): {len(dead_set)}")
    if dead_set:
        for flag in sorted(dead_set):
            locs = set_flags[flag]
            loc_str = ", ".join(f"{r}:{n}" for r, n in locs[:3])
            print(f"    - {flag} (set in: {loc_str})")

    print(f"  Missing flags (checked but never set): {len(dead_check)}")
    if dead_check:
        for flag in sorted(dead_check):
            locs = checked_flags[flag]
            loc_str = ", ".join(f"{r}:{n}" for r, n in locs[:3])
            print(f"    - {flag} (checked in: {loc_str})")

    # Reachability
    print()
    unreachable = check_reachability(all_data)
    if unreachable:
        print(f"=== UNREACHABLE ENDINGS ({len(unreachable)}) ===")
        for e in sorted(unreachable):
            print(f"  WARNING: {e} is never referenced as next_file")
    else:
        print("=== ALL 6 ENDINGS REACHABLE ===")

    # Node counts
    print()
    total = sum(len(d.get("nodes", {})) for d in all_data.values())
    print(f"=== TOTAL NODES: {total} ===")

    return 1 if all_errors else 0

if __name__ == "__main__":
    sys.exit(main())
