#!/usr/bin/env python3
"""Flag low-impact fallback phrasing in Act 2/3/4 dialogue for rewrite passes."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIALOGUE_ROOT = ROOT / "data" / "dialogue"
TARGET_ACTS = ["act2", "act3", "act4"]

# phrase -> rewrite hint
PHRASE_HINTS = {
    "Ich weiß": "Präzisieren, woher das Wissen kommt (Beobachtung, Erinnerung, Beweis).",
    "So oder so": "Konkrete Konsequenz für beide Wege benennen.",
    "irgendwie": "Vages Wort ersetzen durch sinnliche Wahrnehmung oder klare Ursache.",
    "Das muss": "Behauptung mit Risiko oder Einsatz aufladen.",
    "Egal was": "Absolutismus vermeiden; stattdessen moralischen Preis benennen.",
}


def iter_dialogue_files():
    for act in TARGET_ACTS:
        act_dir = DIALOGUE_ROOT / act
        if not act_dir.exists():
            continue
        for path in sorted(act_dir.glob("*.json")):
            yield path


def main() -> int:
    findings = []

    for path in iter_dialogue_files():
        data = json.loads(path.read_text(encoding="utf-8"))
        for node_id, node in data.get("nodes", {}).items():
            text = node.get("text", "")
            if not text:
                continue
            for phrase, hint in PHRASE_HINTS.items():
                if phrase in text:
                    findings.append((path.relative_to(ROOT), node_id, phrase, hint, text))

    if not findings:
        print("dialogue-impact-lint: OK (no flagged fallback phrases in act2/3/4)")
        return 0

    print(f"dialogue-impact-lint: {len(findings)} findings")
    for rel, node_id, phrase, hint, text in findings:
        print(f"- {rel}:{node_id} | phrase='{phrase}'")
        print(f"  hint: {hint}")
        print(f"  text: {text}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
