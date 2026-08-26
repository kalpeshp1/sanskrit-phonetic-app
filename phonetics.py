# phonetics.py

PHONETIC_MAP = {
    # Vowels (Svaras)
    "a": {"char": "अ", "type": "Vowel (Svara)", "place": "Guttural (Kanthya)"},
    "aa": {"char": "आ", "type": "Vowel (Svara)", "place": "Guttural (Kanthya)"},
    "i": {"char": "इ", "type": "Vowel (Svara)", "place": "Palatal (Talavya)"},
    "ee": {"char": "ई", "type": "Vowel (Svara)", "place": "Palatal (Talavya)"},
    "u": {"char": "उ", "type": "Vowel (Svara)", "place": "Labial (Oshthya)"},
    "oo": {"char": "ऊ", "type": "Vowel (Svara)", "place": "Labial (Oshthya)"},
    "ru": {"char": "ऋ", "type": "Vowel (Svara)", "place": "Retroflex (Murdhanya)"},
    "e": {"char": "ए", "type": "Vowel (Svara)", "place": "Guttural-Palatal (Kanthatalavya)"},
    "ai": {"char": "ऐ", "type": "Vowel (Svara)", "place": "Guttural-Palatal (Kanthatalavya)"},
    "o": {"char": "ओ", "type": "Vowel (Svara)", "place": "Guttural-Labial (Kanthoshthya)"},
    "au": {"char": "औ", "type": "Vowel (Svara)", "place": "Guttural-Labial (Kanthoshthya)"},

    # Consonants (Vyanjan)
    "ka": {"char": "क", "type": "Consonant (Vyanjan)", "place": "Guttural (Kanthya)"},
    "kha": {"char": "ख", "type": "Consonant (Vyanjan)", "place": "Guttural (Kanthya)"},
    "ga": {"char": "ग", "type": "Consonant (Vyanjan)", "place": "Guttural (Kanthya)"},
    "gha": {"char": "घ", "type": "Consonant (Vyanjan)", "place": "Guttural (Kanthya)"},
    "cha": {"char": "च", "type": "Consonant (Vyanjan)", "place": "Palatal (Talavya)"},
    "chha": {"char": "छ", "type": "Consonant (Vyanjan)", "place": "Palatal (Talavya)"},
    "ja": {"char": "ज", "type": "Consonant (Vyanjan)", "place": "Palatal (Talavya)"},
    "jha": {"char": "झ", "type": "Consonant (Vyanjan)", "place": "Palatal (Talavya)"},
    "ta_ret": {"char": "ट", "type": "Consonant (Vyanjan)", "place": "Retroflex (Murdhanya)"},
    "tha_ret": {"char": "ठ", "type": "Consonant (Vyanjan)", "place": "Retroflex (Murdhanya)"},
    "da_ret": {"char": "ड", "type": "Consonant (Vyanjan)", "place": "Retroflex (Murdhanya)"},
    "dha_ret": {"char": "ढ", "type": "Consonant (Vyanjan)", "place": "Retroflex (Murdhanya)"},
    "ta_den": {"char": "त", "type": "Consonant (Vyanjan)", "place": "Dental (Dantya)"},
    "tha_den": {"char": "थ", "type": "Consonant (Vyanjan)", "place": "Dental (Dantya)"},
    "da_den": {"char": "द", "type": "Consonant (Vyanjan)", "place": "Dental (Dantya)"},
    "dha_den": {"char": "ध", "type": "Consonant (Vyanjan)", "place": "Dental (Dantya)"},
    "pa": {"char": "प", "type": "Consonant (Vyanjan)", "place": "Labial (Oshthya)"},
    "pha": {"char": "फ", "type": "Consonant (Vyanjan)", "place": "Labial (Oshthya)"},
    "ba": {"char": "ब", "type": "Consonant (Vyanjan)", "place": "Labial (Oshthya)"},
    "bha": {"char": "भ", "type": "Consonant (Vyanjan)", "place": "Labial (Oshthya)"},
    "ma": {"char": "म", "type": "Consonant (Vyanjan)", "place": "Labial (Oshthya)"}
}

def get_phonetic_details(label: str) -> dict:
    return PHONETIC_MAP.get(
        label.lower().strip(),
        {"char": label, "type": "Unknown", "place": "Unknown Articulation"}
    )
