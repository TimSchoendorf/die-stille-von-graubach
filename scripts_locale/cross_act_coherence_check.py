#!/usr/bin/env python3
"""Lightweight cross-act coherence checks for setup -> escalation -> payoff chains."""

from __future__ import annotations

import json
import os
import sys
from typing import Dict, Set

ROOT = os.path.join(os.path.dirname(__file__), "..")


def load_nodes(rel_path: str) -> Dict[str, dict]:
    path = os.path.join(ROOT, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("nodes", {})


def collect_set_flags(nodes: Dict[str, dict]) -> Set[str]:
    flags: Set[str] = set()
    for node in nodes.values():
        t = node.get("type")
        if t == "set_flag" and node.get("flag"):
            flags.add(node["flag"])
        if t == "choice":
            for c in node.get("choices", []):
                flags.update(c.get("set_flags", {}).keys())
                flags.update(c.get("add_flags", {}).keys())
    return flags


def collect_checked_flags(nodes: Dict[str, dict]) -> Set[str]:
    return {
        node.get("flag")
        for node in nodes.values()
        if node.get("type") == "flag_check" and node.get("flag")
    }


def collect_scene_end_targets(nodes: Dict[str, dict]) -> Set[str]:
    out: Set[str] = set()
    for node in nodes.values():
        if node.get("type") == "scene_end":
            target = os.path.basename(node.get("next_file", ""))
            if target:
                out.add(target)
    return out


def reachable_count(nodes: Dict[str, dict], start: str, stop: str) -> int:
    """Count reachable nodes from start until stop (inclusive), following next edges.

    This is intentionally lightweight: it follows common VN edge fields used in this repo.
    """
    stack = [start]
    seen: Set[str] = set()

    while stack:
        key = stack.pop()
        if key in seen or key not in nodes:
            continue
        seen.add(key)
        if key == stop:
            continue

        node = nodes[key]
        node_type = node.get("type")

        nxt = node.get("next")
        if isinstance(nxt, str):
            stack.append(nxt)

        if node_type == "flag_check":
            for edge in ("true_next", "false_next"):
                target = node.get(edge)
                if isinstance(target, str):
                    stack.append(target)

        if node_type == "choice":
            for choice in node.get("choices", []):
                target = choice.get("next")
                if isinstance(target, str):
                    stack.append(target)

    return len(seen)


def main() -> int:
    allies = load_nodes("data/dialogue/act3/allies_choice.json")
    bridge = load_nodes("data/dialogue/act3/ally_fallout_bridge.json")
    descent = load_nodes("data/dialogue/act3/descent.json")
    ritual = load_nodes("data/dialogue/act4/ritual_night.json")

    errors = []

    # Neighboring-act flow checks
    if "ally_fallout_bridge.json" not in collect_scene_end_targets(allies):
        errors.append("allies_choice does not flow into ally_fallout_bridge")
    if "descent.json" not in collect_scene_end_targets(bridge):
        errors.append("ally_fallout_bridge does not flow into descent")

    bridge_sets = collect_set_flags(bridge)
    descent_checks = collect_checked_flags(descent)
    ritual_checks = collect_checked_flags(ritual)

    # Core fallout chain must be consumed in descent and still remembered in ritual
    required_setup = {
        "ally_fallout_payoff_pending",
        "bridge_fallout_seen",
        "georg_hurt_day6",
        "hilde_hurt_day6",
        "voss_hurt_day6",
    }

    missing_setup = required_setup - bridge_sets
    if missing_setup:
        errors.append(f"bridge missing setup flags: {sorted(missing_setup)}")

    required_descent_payoff = {
        "ally_fallout_payoff_pending",
        "georg_hurt_day6",
        "hilde_hurt_day6",
        "voss_hurt_day6",
    }
    if missing := (required_descent_payoff - descent_checks):
        errors.append(f"descent missing payoff checks: {sorted(missing)}")

    if "bridge_fallout_seen" not in ritual_checks:
        errors.append("ritual_night missing memory check for bridge_fallout_seen")

    # Branch-density guardrail: avoid thin alternate routes that undercut Act3 setup.
    sought_konrad_span = reachable_count(allies, "konrad_final", "ally_final_converge")
    avoided_konrad_span = reachable_count(allies, "avoided_konrad", "ally_final_converge")
    if avoided_konrad_span < 6:
        errors.append(
            "allies_choice avoided_konrad branch too thin "
            f"({avoided_konrad_span} nodes < 6 minimum)"
        )
    if avoided_konrad_span * 4 < sought_konrad_span:
        errors.append(
            "allies_choice branch imbalance: avoided_konrad is less than a quarter of sought_konrad "
            f"({avoided_konrad_span} vs {sought_konrad_span})"
        )

    if errors:
        print("CROSS-ACT COHERENCE: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("CROSS-ACT COHERENCE: OK")
    print("  setup: allies_choice -> ally_fallout_bridge")
    print("  escalation: ally fallout + hurt flags in bridge")
    print("  payoff: descent + ritual_night consume fallout memory")
    print(
        "  branch density: avoided_konrad path is substantial vs sought_konrad "
        f"({avoided_konrad_span} vs {sought_konrad_span})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
