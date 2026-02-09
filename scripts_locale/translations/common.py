"""Shared helpers and character name data for translations."""

CHARACTER_NAMES = {
    "en": {
        "voss": "Pastor Voss",
        "otto": "Mayor",
        "margarethe": "Grandmother",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
    "fr": {
        "voss": "Pasteur Voss",
        "otto": "Maire",
        "margarethe": "Grand-mère",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
    "es": {
        "voss": "Pastor Voss",
        "otto": "Alcalde",
        "margarethe": "Abuela",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
    "it": {
        "voss": "Pastore Voss",
        "otto": "Sindaco",
        "margarethe": "Nonna",
        "georg": "Georg",
        "elise": "Elise",
        "konrad": "Konrad",
        "hilde": "Hilde",
        "anna": "Anna",
    },
}



def _t(translations, file_key, node_id, en="", fr="", es="", it="", field="text"):
    """Helper to add a translation entry for all 4 languages."""
    for lang, text in [("en", en), ("fr", fr), ("es", es), ("it", it)]:
        if text:
            translations[lang].setdefault(file_key, {}).setdefault(node_id, {})[field] = text



def _tc(translations, file_key, node_id, en_choices=None, fr_choices=None, es_choices=None, it_choices=None):
    """Helper to add choice translations."""
    for lang, choices in [("en", en_choices), ("fr", fr_choices), ("es", es_choices), ("it", it_choices)]:
        if choices:
            translations[lang].setdefault(file_key, {}).setdefault(node_id, {})["choices"] = choices


