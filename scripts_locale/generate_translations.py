#!/usr/bin/env python3
"""
Generate translation JSON files for Die Stille von Graubach.
Reads all German dialogue JSONs and produces data/translations/{en,fr,es,it}.json
with localized text for every dialogue, narration, choice, and journal node.

Usage: python scripts_locale/generate_translations.py
"""

import json
import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIALOGUE_DIR = os.path.join(BASE_DIR, "data", "dialogue")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "translations")

from translations.common import CHARACTER_NAMES
from translations.prologue import _add_prologue
from translations.act1 import (
    _add_act1_arrival,
    _add_act1_first_night,
    _add_act1_village_exploration,
    _add_act1_smithy_evening,
)
from translations.act2 import (
    _add_act2_investigation_morning,
    _add_act2_church_secrets,
    _add_act2_konrad_encounter,
    _add_act2_hilde_ritual,
    _add_act2_the_book,
)
from translations.act3 import (
    _add_act3_allies_choice,
    _add_act3_reality_breaks,
    _add_act3_descent,
    _add_act3_preparation,
)
from translations.act4 import (
    _add_act4_ritual_night,
    _add_act4_ending_seal,
    _add_act4_ending_escape,
    _add_act4_ending_pact,
    _add_act4_ending_truth,
    _add_act4_ending_sacrifice,
    _add_act4_ending_awakening,
)


def build_translations():
    """Build the complete translation dictionaries for all languages."""
    translations = {"en": {}, "fr": {}, "es": {}, "it": {}}

    # Process each dialogue file
    _add_prologue(translations)
    _add_act1_arrival(translations)
    _add_act1_first_night(translations)
    _add_act1_village_exploration(translations)
    _add_act1_smithy_evening(translations)
    _add_act2_investigation_morning(translations)
    _add_act2_church_secrets(translations)
    _add_act2_konrad_encounter(translations)
    _add_act2_hilde_ritual(translations)
    _add_act2_the_book(translations)
    _add_act3_allies_choice(translations)
    _add_act3_reality_breaks(translations)
    _add_act3_descent(translations)
    _add_act3_preparation(translations)
    _add_act4_ritual_night(translations)
    _add_act4_ending_seal(translations)
    _add_act4_ending_escape(translations)
    _add_act4_ending_pact(translations)
    _add_act4_ending_truth(translations)
    _add_act4_ending_sacrifice(translations)
    _add_act4_ending_awakening(translations)

    return translations


def generate_auto_translations():
    """
    Auto-generate translations for files not yet manually translated.
    Reads each German JSON, extracts text, and creates placeholder entries
    that fall back to German (so no text is lost).
    """
    translations = {"en": {}, "fr": {}, "es": {}, "it": {}}

    json_files = glob.glob(os.path.join(DIALOGUE_DIR, "**", "*.json"), recursive=True)

    for json_path in json_files:
        rel = os.path.relpath(json_path, BASE_DIR).replace("\\", "/")
        file_key = "res://" + rel

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        nodes = data.get("nodes", {})
        for node_id, node in nodes.items():
            ntype = node.get("type", "")
            if ntype in ("dialogue", "narration"):
                text = node.get("text", "")
                if text:
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("text", text)
            elif ntype == "choice":
                choices = node.get("choices", [])
                choice_texts = [c.get("text", "") for c in choices]
                if any(choice_texts):
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("choices", choice_texts)
            elif ntype == "journal":
                title = node.get("title", "")
                content = node.get("content", "")
                if title:
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("title", title)
                if content:
                    for lang in ("en", "fr", "es", "it"):
                        translations[lang].setdefault(file_key, {}).setdefault(node_id, {}).setdefault("content", content)

    return translations


def merge_translations(manual, auto):
    """Merge manual translations over auto-generated ones (manual takes priority)."""
    result = {}
    for lang in ("en", "fr", "es", "it"):
        result[lang] = {}
        # Start with auto
        for file_key, nodes in auto.get(lang, {}).items():
            result[lang][file_key] = {}
            for node_id, fields in nodes.items():
                result[lang][file_key][node_id] = dict(fields)
        # Overlay manual
        for file_key, nodes in manual.get(lang, {}).items():
            if file_key not in result[lang]:
                result[lang][file_key] = {}
            for node_id, fields in nodes.items():
                if node_id not in result[lang][file_key]:
                    result[lang][file_key][node_id] = {}
                result[lang][file_key][node_id].update(fields)
    return result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Building manual translations...")
    manual = build_translations()

    print("Generating auto-translations from German JSONs...")
    auto = generate_auto_translations()

    print("Merging translations...")
    merged = merge_translations(manual, auto)

    for lang in ("en", "fr", "es", "it"):
        # Add character names
        output = {"_characters": CHARACTER_NAMES[lang]}
        output.update(merged[lang])

        out_path = os.path.join(OUTPUT_DIR, f"{lang}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent="\t")

        # Count stats
        total_nodes = sum(len(nodes) for fk, nodes in merged[lang].items())
        manual_nodes = sum(len(nodes) for fk, nodes in manual.get(lang, {}).items())
        print(f"  {lang}.json: {total_nodes} nodes ({manual_nodes} manually translated)")

    print("Done! Translation files written to", OUTPUT_DIR)


if __name__ == "__main__":
    main()
