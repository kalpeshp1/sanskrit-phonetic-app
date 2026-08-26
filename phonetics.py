# phonetics.py

PHONETIC_MAP = {
    # ------------------ SVARA (Vowels - 13) ------------------
    "a": {"char": "अ", "type": "Hrasva Svara (Short Vowel)", "place": "Kanthya (Guttural)"},
    "aa": {"char": "आ", "type": "Dīrgha Svara (Long Vowel)", "place": "Kanthya (Guttural)"},
    "i": {"char": "इ", "type": "Hrasva Svara (Short Vowel)", "place": "Tālavya (Palatal)"},
    "ee": {"char": "ई", "type": "Dīrgha Svara (Long Vowel)", "place": "Tālavya (Palatal)"},
    "u": {"char": "उ", "type": "Hrasva Svara (Short Vowel)", "place": "Oṣṭhya (Labial)"},
    "oo": {"char": "ऊ", "type": "Dīrgha Svara (Long Vowel)", "place": "Oṣṭhya (Labial)"},
    "ri": {"char": "ऋ", "type": "Hrasva Svara (Short Vowel)", "place": "Mūrdhanya (Retroflex)"},
    "ree": {"char": "ॠ", "type": "Dīrgha Svara (Long Vowel)", "place": "Mūrdhanya (Retroflex)"},
    "lri": {"char": "ऌ", "type": "Hrasva Svara (Short Vowel)", "place": "Dantya (Dental)"},
    "e": {"char": "ए", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhatālavya (Palato-Guttural)"},
    "ai": {"char": "ऐ", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhatālavya (Palato-Guttural)"},
    "o": {"char": "ओ", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhoṣṭhya (Labio-Guttural)"},
    "au": {"char": "औ", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhoṣṭhya (Labio-Guttural)"},

    # ------------------ SPARŚA (Consonants - 25) ------------------
    # 1. Kavarga (Guttural / Kaṇṭhya)
    "ka": {"char": "क", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "kha": {"char": "ख", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "ga": {"char": "ग", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "gha": {"char": "घ", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "nga": {"char": "ङ", "type": "Anunāsika (Nasal)", "place": "Kaṇṭhya-Nāsikya (Guttural-Nasal)"},

    # 2. Cavarga (Palatal / Tālavya)
    "cha": {"char": "च", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Tālavya (Palatal)"},
    "chha": {"char": "छ", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Tālavya (Palatal)"},
    "ja": {"char": "ज", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Tālavya (Palatal)"},
    "jha": {"char": "झ", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Tālavya (Palatal)"},
    "nya": {"char": "ञ", "type": "Anunāsika (Nasal)", "place": "Tālavya-Nāsikya (Palatal-Nasal)"},

    # 3. Ṭavarga (Retroflex / Mūrdhanya)
    "ta_ret": {"char": "ट", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "tha_ret": {"char": "ठ", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "da_ret": {"char": "ड", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "dha_ret": {"char": "ढ", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "nna": {"char": "ण", "type": "Anunāsika (Nasal)", "place": "Mūrdhanya-Nāsikya (Retroflex-Nasal)"},

    # 4. Tavarga (Dental / Dantya)
    "ta_den": {"char": "त", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Dantya (Dental)"},
    "tha_den": {"char": "थ", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Dantya (Dental)"},
    "da_den": {"char": "द", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Dantya (Dental)"},
    "dha_den": {"char": "ध", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Dantya (Dental)"},
    "na": {"char": "न", "type": "Anunāsika (Nasal)", "place": "Dantya-Nāsikya (Dental-Nasal)"},

    # 5. Pavarga (Labial / Oṣṭhya)
    "pa": {"char": "प", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Oṣṭhya (Labial)"},
    "pha": {"char": "फ", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Oṣṭhya (Labial)"},
    "ba": {"char": "ब", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Oṣṭhya (Labial)"},
    "bha": {"char": "भ", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Oṣṭhya (Labial)"},
    "ma": {"char": "म", "type": "Anunāsika (Nasal)", "place": "Oṣṭhya-Nāsikya (Labial-Nasal)"},

    # ------------------ ANTASTHA (Semivowels - 4) ------------------
    "ya": {"char": "य", "type": "Antastha (Semivowel)", "place": "Tālavya (Palatal)"},
    "ra": {"char": "र", "type": "Antastha (Semivowel)", "place": "Mūrdhanya (Retroflex)"},
    "la": {"char": "ल", "type": "Antastha (Semivowel)", "place": "Dantya (Dental)"},
    "va": {"char": "व", "type": "Antastha (Semivowel)", "place": "Dantoṣṭhya (Dento-Labial)"},

    # ------------------ ŪṢMAN (Sibilants & Aspirate - 4) ------------------
    "sha_pal": {"char": "श", "type": "Ūṣman (Sibilant)", "place": "Tālavya (Palatal)"},
    "sha_ret": {"char": "ष", "type": "Ūṣman (Sibilant)", "place": "Mūrdhanya (Retroflex)"},
    "sa": {"char": "स", "type": "Ūṣman (Sibilant)", "place": "Dantya (Dental)"},
    "ha": {"char": "ह", "type": "Ūṣman (Aspirate)", "place": "Kaṇṭhya / Urasya (Guttural/Glottal)"},

    # ------------------ AYOGAVĀHA (Modifiers - 4) ------------------
    "am": {"char": "अं (Anusvāra)", "type": "Ayogavāha", "place": "Nāsikya (Nasal)"},
    "ah": {"char": "अः (Visarga)", "type": "Ayogavāha", "place": "Kaṇṭhya (Guttural)"},
    "jihva": {"char": "ᳵ (Jihvāmūlīya)", "type": "Ayogavāha", "place": "Jihvāmūla (Root of Tongue)"},
    "upadh": {"char": "ᳶ (Upadhmānīya)", "type": "Ayogavāha", "place": "Oṣṭhya (Labial)"},
}

def get_phonetic_details(label: str) -> dict:
    return PHONETIC_MAP.get(
        label.lower().strip(),
        {"char": label, "type": "Standard Sound", "place": "General Articulation"}
    )
