"""
Insert sound nodes into all dialogue JSON files.
Based on the audio map from the integration plan.

Each insertion is defined as:
  (file_path, after_node_id, sound_node_id, sound_type, path_or_empty)

The script:
1. Loads the JSON
2. For each insertion, creates a new sound node
3. Rewires: after_node.next -> sound_node_id, sound_node.next -> original_next
4. Saves the JSON
"""

import json
import os
import sys

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "dialogue")

# Insertion definitions: (json_file, after_node, new_node_id, sound_type, audio_file)
# sound_type: "music", "sfx", "ambience", "stop_music", "stop_ambience"
# For stop types, audio_file is empty string

INSERTIONS = [
    # ============================================================
    # PROLOGUE (prologue.json) - 8 nodes
    # ============================================================
    ("prologue.json", "bg_berlin", "snd_rain", "ambience", "rain.wav"),
    ("prologue.json", "snd_rain", "snd_main_theme", "music", "main_theme.wav"),
    ("prologue.json", "transition_train_in", "snd_stop_rain", "stop_ambience", ""),
    ("prologue.json", "snd_stop_rain", "snd_train_music", "music", "village_day.wav"),
    ("prologue.json", "narration_train_3", "snd_whispers", "sfx", "whispers.wav"),
    ("prologue.json", "transition_village_in", "snd_village_amb", "ambience", "village_ambience.wav"),
    ("prologue.json", "narration_arrival_5", "snd_footsteps", "sfx", "footsteps_wood.wav"),
    ("prologue.json", "effect_shake_door", "snd_door", "sfx", "door_creak.wav"),

    # ============================================================
    # ACT 1: ARRIVAL (act1/arrival.json) - 3 nodes
    # ============================================================
    ("act1/arrival.json", "bg_house", "snd_tension", "music", "tension.wav"),
    ("act1/arrival.json", "snd_tension", "snd_clock", "sfx", "clock_ticking.wav"),
    ("act1/arrival.json", "effect_evening_desat", "snd_bells", "sfx", "church_bell.wav"),

    # ============================================================
    # ACT 1: FIRST NIGHT (act1/first_night.json) - 6 nodes
    # ============================================================
    ("act1/first_night.json", "bg_house_night", "snd_night", "music", "village_night.wav"),
    ("act1/first_night.json", "narration_dream_1", "snd_whispers", "sfx", "whispers.wav"),
    ("act1/first_night.json", "narration_wake_2", "snd_underground", "ambience", "underground.wav"),
    ("act1/first_night.json", "narration_singing_2", "snd_glass", "sfx", "glass_break.wav"),
    ("act1/first_night.json", "narration_singing_3", "snd_heartbeat", "sfx", "heartbeat.wav"),
    ("act1/first_night.json", "converge_night_2", "snd_stop_underground", "stop_ambience", ""),

    # ============================================================
    # ACT 1: VILLAGE EXPLORATION (act1/village_exploration.json) - 4 nodes
    # ============================================================
    ("act1/village_exploration.json", "bg_village_day", "snd_village_music", "music", "village_day.wav"),
    ("act1/village_exploration.json", "snd_village_music", "snd_village_amb", "ambience", "village_ambience.wav"),
    ("act1/village_exploration.json", "church_path", "snd_church", "music", "church.wav"),
    ("act1/village_exploration.json", "explore_converge", "snd_village_ret", "music", "village_day.wav"),

    # ============================================================
    # ACT 1: SMITHY EVENING (act1/smithy_evening.json) - 4 nodes
    # ============================================================
    ("act1/smithy_evening.json", "bg_smithy", "snd_fire", "ambience", "fire_crackling.wav"),
    ("act1/smithy_evening.json", "snd_fire", "snd_invest", "music", "investigation.wav"),
    ("act1/smithy_evening.json", "georg_converge", "snd_tension", "music", "tension.wav"),
    ("act1/smithy_evening.json", "act1_end", "snd_underground", "ambience", "underground.wav"),

    # ============================================================
    # ACT 2: INVESTIGATION MORNING (act2/investigation_morning.json) - 2 nodes
    # ============================================================
    ("act2/investigation_morning.json", "bg_grandmother_morning", "snd_invest", "music", "investigation.wav"),
    ("act2/investigation_morning.json", "snd_invest", "snd_village_amb", "ambience", "village_ambience.wav"),

    # ============================================================
    # ACT 2: CHURCH SECRETS (act2/church_secrets.json) - 3 nodes
    # ============================================================
    ("act2/church_secrets.json", "bg_church", "snd_church", "music", "church.wav"),
    ("act2/church_secrets.json", "narration_2", "snd_whispers", "sfx", "whispers.wav"),
    ("act2/church_secrets.json", "narration_5", "snd_heartbeat", "sfx", "heartbeat.wav"),

    # ============================================================
    # ACT 2: KONRAD ENCOUNTER (act2/konrad_encounter.json) - 4 nodes
    # ============================================================
    ("act2/konrad_encounter.json", "bg_village", "snd_village", "music", "village_day.wav"),
    ("act2/konrad_encounter.json", "bg_forest", "snd_forest_amb", "ambience", "forest_night.wav"),
    ("act2/konrad_encounter.json", "snd_forest_amb", "snd_forest", "music", "forest.wav"),
    ("act2/konrad_encounter.json", "konrad_tree_1", "snd_whispers", "sfx", "whispers.wav"),

    # ============================================================
    # ACT 2: HILDE RITUAL (act2/hilde_ritual.json) - 3 nodes
    # ============================================================
    ("act2/hilde_ritual.json", "bg_hilde", "snd_grandmother", "music", "grandmother.wav"),
    ("act2/hilde_ritual.json", "narration_evening", "snd_forest_amb", "ambience", "forest_night.wav"),
    ("act2/hilde_ritual.json", "effect_stalked", "snd_footsteps", "sfx", "footsteps_wood.wav"),

    # ============================================================
    # ACT 2: THE BOOK (act2/the_book.json) - 5 nodes
    # ============================================================
    ("act2/the_book.json", "bg_night", "snd_tension", "music", "tension.wav"),
    ("act2/the_book.json", "effect_basement", "snd_underground", "ambience", "underground.wav"),
    ("act2/the_book.json", "snd_underground", "snd_cosmic", "music", "cosmic_horror.wav"),
    ("act2/the_book.json", "effect_awareness", "snd_whispers", "sfx", "whispers.wav"),
    ("act2/the_book.json", "narration_end_3", "snd_heartbeat", "sfx", "heartbeat.wav"),

    # ============================================================
    # ACT 3: REALITY BREAKS (act3/reality_breaks.json) - 2 nodes
    # ============================================================
    ("act3/reality_breaks.json", "bg_morning", "snd_cosmic", "music", "cosmic_horror.wav"),
    ("act3/reality_breaks.json", "effect_breathing", "snd_heartbeat", "sfx", "heartbeat.wav"),

    # ============================================================
    # ACT 3: ALLIES CHOICE (act3/allies_choice.json) - 1 node
    # ============================================================
    ("act3/allies_choice.json", "bg_village", "snd_tension", "music", "tension.wav"),

    # ============================================================
    # ACT 3: DESCENT (act3/descent.json) - 3 nodes
    # ============================================================
    ("act3/descent.json", "bg_church_night", "snd_tension", "music", "tension.wav"),
    ("act3/descent.json", "descent_start", "snd_underground", "ambience", "underground.wav"),
    ("act3/descent.json", "bg_ritual", "snd_ritual", "music", "ritual.wav"),

    # ============================================================
    # ACT 3: PREPARATION (act3/preparation.json) - 2 nodes
    # ============================================================
    ("act3/preparation.json", "bg_grandmother_night", "snd_grandmother", "music", "grandmother.wav"),
    ("act3/preparation.json", "narration_dawn", "snd_tension_dawn", "music", "tension.wav"),

    # ============================================================
    # ACT 4: RITUAL NIGHT (act4/ritual_night.json) - 2 nodes
    # ============================================================
    ("act4/ritual_night.json", "bg_ritual", "snd_ritual", "music", "ritual.wav"),
    ("act4/ritual_night.json", "snd_ritual", "snd_underground", "ambience", "underground.wav"),

    # ============================================================
    # ENDING: SEAL (act4/ending_seal.json) - 3 nodes
    # ============================================================
    ("act4/ending_seal.json", "narration_1", "snd_ritual_cont", "music", "ritual.wav"),
    ("act4/ending_seal.json", "effect_calm", "snd_stop_amb", "stop_ambience", ""),
    ("act4/ending_seal.json", "snd_stop_amb", "snd_peaceful", "music", "ending_peaceful.wav"),

    # ============================================================
    # ENDING: PACT (act4/ending_pact.json) - 2 nodes
    # ============================================================
    ("act4/ending_pact.json", "narration_1", "snd_cosmic", "music", "cosmic_horror.wav"),
    ("act4/ending_pact.json", "effect_pact_forming", "snd_dark", "music", "ending_dark.wav"),

    # ============================================================
    # ENDING: SACRIFICE (act4/ending_sacrifice.json) - 1 node
    # ============================================================
    ("act4/ending_sacrifice.json", "narration_1", "snd_dark", "music", "ending_dark.wav"),

    # ============================================================
    # ENDING: AWAKENING (act4/ending_awakening.json) - 1 node
    # ============================================================
    ("act4/ending_awakening.json", "narration_1", "snd_cosmic", "music", "cosmic_horror.wav"),

    # ============================================================
    # ENDING: ESCAPE (act4/ending_escape.json) - 2 nodes
    # ============================================================
    ("act4/ending_escape.json", "narration_1", "snd_tension", "music", "tension.wav"),
    ("act4/ending_escape.json", "effect_escape", "snd_peaceful", "music", "ending_peaceful.wav"),

    # ============================================================
    # ENDING: TRUTH (act4/ending_truth.json) - 3 nodes
    # ============================================================
    ("act4/ending_truth.json", "narration_1", "snd_cosmic", "music", "cosmic_horror.wav"),
    ("act4/ending_truth.json", "effect_understanding", "snd_stop_amb", "stop_ambience", ""),
    ("act4/ending_truth.json", "snd_stop_amb", "snd_peaceful", "music", "ending_peaceful.wav"),
]


def insert_sound_node(nodes, after_node_id, new_node_id, sound_type, audio_path):
    """Insert a sound node after the specified node, rewiring the chain."""
    if after_node_id not in nodes:
        return False, f"Node '{after_node_id}' not found"

    if new_node_id in nodes:
        return False, f"Node '{new_node_id}' already exists"

    after_node = nodes[after_node_id]

    # Get the original next
    original_next = after_node.get("next", "")
    if not original_next:
        # Check for scene_end or other terminal nodes
        return False, f"Node '{after_node_id}' has no 'next' field"

    # Create the sound node
    sound_node = {
        "type": "sound",
        "sound_type": sound_type,
        "next": original_next
    }
    if audio_path:
        sound_node["path"] = audio_path

    # Rewire
    after_node["next"] = new_node_id
    nodes[new_node_id] = sound_node

    return True, "OK"


def process_file(rel_path, file_insertions):
    """Process a single JSON file with its insertions."""
    full_path = os.path.join(DATA_DIR, rel_path)

    if not os.path.exists(full_path):
        print(f"  ERROR: File not found: {full_path}")
        return 0, len(file_insertions)

    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = data["nodes"]
    success = 0
    errors = 0

    for after_id, new_id, stype, spath in file_insertions:
        ok, msg = insert_sound_node(nodes, after_id, new_id, stype, spath)
        if ok:
            success += 1
            print(f"    + {new_id} (after {after_id}): {stype} {spath}")
        else:
            errors += 1
            print(f"    ! FAILED {new_id}: {msg}")

    # Write back with nice formatting
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent="\t", ensure_ascii=False)

    return success, errors


def main():
    print("=" * 60)
    print("Sound Node Insertion: Die Stille von Graubach")
    print("=" * 60)
    print()

    # Group insertions by file
    by_file = {}
    for rel_path, after_id, new_id, stype, spath in INSERTIONS:
        if rel_path not in by_file:
            by_file[rel_path] = []
        by_file[rel_path].append((after_id, new_id, stype, spath))

    total_success = 0
    total_errors = 0

    for rel_path, file_insertions in by_file.items():
        print(f"  {rel_path} ({len(file_insertions)} insertions)")
        s, e = process_file(rel_path, file_insertions)
        total_success += s
        total_errors += e
        print()

    print(f"=== Done: {total_success} inserted, {total_errors} errors ===")

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
