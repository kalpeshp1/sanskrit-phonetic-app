# phonetics.py

PHONETIC_MAP = {
    # ------------------ SVARA (Vowels) ------------------
    "अ": {"token": "a", "type": "Hrasva Svara (Short Vowel)", "place": "Kaṇṭhya (Guttural)"},
    "आ": {"token": "aa", "type": "Dīrgha Svara (Long Vowel)", "place": "Kaṇṭhya (Guttural)"},
    "इ": {"token": "i", "type": "Hrasva Svara (Short Vowel)", "place": "Tālavya (Palatal)"},
    "ई": {"token": "ee", "type": "Dīrgha Svara (Long Vowel)", "place": "Tālavya (Palatal)"},
    "उ": {"token": "u", "type": "Hrasva Svara (Short Vowel)", "place": "Oṣṭhya (Labial)"},
    "ऊ": {"token": "oo", "type": "Dīrgha Svara (Long Vowel)", "place": "Oṣṭhya (Labial)"},
    "ऋ": {"token": "ri", "type": "Hrasva Svara (Short Vowel)", "place": "Mūrdhanya (Retroflex)"},
    "ॠ": {"token": "ree", "type": "Dīrgha Svara (Long Vowel)", "place": "Mūrdhanya (Retroflex)"},
    "ऌ": {"token": "lri", "type": "Hrasva Svara (Short Vowel)", "place": "Dantya (Dental)"},
    "ए": {"token": "e", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhatālavya (Palato-Guttural)"},
    "ऐ": {"token": "ai", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhatālavya (Palato-Guttural)"},
    "ओ": {"token": "o", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhoṣṭhya (Labio-Guttural)"},
    "औ": {"token": "au", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhoṣṭhya (Labio-Guttural)"},

    # ------------------ SPARŚA (Consonants) ------------------
    # Kavarga (Guttural)
    "क": {"token": "ka", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "ख": {"token": "kha", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "ग": {"token": "ga", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "घ": {"token": "gha", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Kaṇṭhya (Guttural)"},
    "ङ": {"token": "nga", "type": "Anunāsika (Nasal)", "place": "Kaṇṭhya-Nāsikya (Guttural-Nasal)"},

    # Cavarga (Palatal)
    "च": {"token": "cha", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Tālavya (Palatal)"},
    "छ": {"token": "chha", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Tālavya (Palatal)"},
    "ज": {"token": "ja", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Tālavya (Palatal)"},
    "झ": {"token": "jha", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Tālavya (Palatal)"},
    "ञ": {"token": "nya", "type": "Anunāsika (Nasal)", "place": "Tālavya-Nāsikya (Palatal-Nasal)"},

    # Ṭavarga (Retroflex)
    "ट": {"token": "ta_ret", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "ठ": {"token": "tha_ret", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "ड": {"token": "da_ret", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "ढ": {"token": "dha_ret", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Mūrdhanya (Retroflex)"},
    "ण": {"token": "nna", "type": "Anunāsika (Nasal)", "place": "Mūrdhanya-Nāsikya (Retroflex-Nasal)"},

    # Tavarga (Dental)
    "त": {"token": "ta_den", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Dantya (Dental)"},
    "थ": {"token": "tha_den", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Dantya (Dental)"},
    "द": {"token": "da_den", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Dantya (Dental)"},
    "ध": {"token": "dha_den", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Dantya (Dental)"},
    "न": {"token": "na", "type": "Anunāsika (Nasal)", "place": "Dantya-Nāsikya (Dental-Nasal)"},

    # Pavarga (Labial)
    "प": {"token": "pa", "type": "Sparśa (Alpaprāṇa / Aghoṣa)", "place": "Oṣṭhya (Labial)"},
    "फ": {"token": "pha", "type": "Sparśa (Mahāprāṇa / Aghoṣa)", "place": "Oṣṭhya (Labial)"},
    "ब": {"token": "ba", "type": "Sparśa (Alpaprāṇa / Ghoṣa)", "place": "Oṣṭhya (Labial)"},
    "भ": {"token": "bha", "type": "Sparśa (Mahāprāṇa / Ghoṣa)", "place": "Oṣṭhya (Labial)"},
    "म": {"token": "ma", "type": "Anunāsika (Nasal)", "place": "Oṣṭhya-Nāsikya (Labial-Nasal)"},

    # Antastha (Semivowels)
    "य": {"token": "ya", "type": "Antastha (Semivowel)", "place": "Tālavya (Palatal)"},
    "र": {"token": "ra", "type": "Antastha (Semivowel)", "place": "Mūrdhanya (Retroflex)"},
    "ल": {"token": "la", "type": "Antastha (Semivowel)", "place": "Dantya (Dental)"},
    "व": {"token": "va", "type": "Antastha (Semivowel)", "place": "Dantoṣṭhya (Dento-Labial)"},

    # Ūṣman (Sibilants & Aspirates)
    "श": {"token": "sha_pal", "type": "Ūṣman (Sibilant)", "place": "Tālavya (Palatal)"},
    "ष": {"token": "sha_ret", "type": "Ūṣman (Sibilant)", "place": "Mūrdhanya (Retroflex)"},
    "स": {"token": "sa", "type": "Ūṣman (Sibilant)", "place": "Dantya (Dental)"},
    "ह": {"token": "ha", "type": "Ūṣman (Aspirate)", "place": "Kaṇṭhya (Guttural)"},
    "अं": {"token": "am", "type": "Ayogavāha (Anusvāra)", "place": "Nāsikya (Nasal)"},
    "अः": {"token": "ah", "type": "Ayogavāha (Visarga)", "place": "Kaṇṭhya (Guttural)"}
}

def get_phonetic_details(letter: str) -> dict:
    # Match the base Devanagari character
    cleaned_letter = letter.strip()
    if cleaned_letter in PHONETIC_MAP:
        return {**PHONETIC_MAP[cleaned_letter], "char": cleaned_letter}
    
    # Check first character fallback
    for char in cleaned_letter:
        if char in PHONETIC_MAP:
            return {**PHONETIC_MAP[char], "char": char}

    return {"char": cleaned_letter, "token": "unknown", "type": "General Phoneme", "place": "Undefined Sthāna"}
