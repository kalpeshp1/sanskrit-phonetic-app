import unicodedata

PHONETIC_MAP = {
    # --- Vowels (Svara) ---
    "अ": {"token": "a", "type": "Hrasva Svara (Short Vowel)", "place": "Kaṇṭhya (Throat / Guttural)"},
    "आ": {"token": "ā", "type": "Dīrgha Svara (Long Vowel)", "place": "Kaṇṭhya (Throat / Guttural)"},
    "इ": {"token": "i", "type": "Hrasva Svara (Short Vowel)", "place": "Tālavya (Palatal)"},
    "ई": {"token": "ī", "type": "Dīrgha Svara (Long Vowel)", "place": "Tālavya (Palatal)"},
    "उ": {"token": "u", "type": "Hrasva Svara (Short Vowel)", "place": "Oṣṭhya (Labial)"},
    "ऊ": {"token": "ū", "type": "Dīrgha Svara (Long Vowel)", "place": "Oṣṭhya (Labial)"},
    "ऋ": {"token": "ṛ", "type": "Hrasva Svara (Vocalic R)", "place": "Mūrdhanya (Retroflex)"},
    "ॠ": {"token": "ṝ", "type": "Dīrgha Svara (Long Vocalic R)", "place": "Mūrdhanya (Retroflex)"},
    "ऌ": {"token": "ḷ", "type": "Hrasva Svara (Vocalic L)", "place": "Dantya (Dental)"},
    "ए": {"token": "e", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭha-Tālavya (Gutturo-Palatal)"},
    "ऐ": {"token": "ai", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭha-Tālavya (Gutturo-Palatal)"},
    "ओ": {"token": "o", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhoṣṭhya (Gutturo-Labial)"},
    "औ": {"token": "au", "type": "Saṃyukta Svara (Diphthong)", "place": "Kaṇṭhoṣṭhya (Gutturo-Labial)"},
    "अं": {"token": "aṃ", "type": "Anusvāra (Nasal)", "place": "Nāsikya (Nasal)"},
    "अः": {"token": "aḥ", "type": "Visarga (Aspirate)", "place": "Kaṇṭhya (Guttural)"},

    # --- Ka-Varga (Kaṇṭhya / Guttural) ---
    "क": {"token": "ka", "type": "Alpaprāṇa Aghoṣa Sparśa", "place": "Kaṇṭhya (Guttural)"},
    "ख": {"token": "kha", "type": "Mahāprāṇa Aghoṣa Sparśa", "place": "Kaṇṭhya (Guttural)"},
    "ग": {"token": "ga", "type": "Alpaprāṇa Ghoṣa Sparśa", "place": "Kaṇṭhya (Guttural)"},
    "घ": {"token": "gha", "type": "Mahāprāṇa Ghoṣa Sparśa", "place": "Kaṇṭhya (Guttural)"},
    "ङ": {"token": "ṅa", "type": "Anunāsika Sparśa", "place": "Kaṇṭhya & Nāsikya (Guttural-Nasal)"},

    # --- Ca-Varga (Tālavya / Palatal) ---
    "च": {"token": "ca", "type": "Alpaprāṇa Aghoṣa Sparśa", "place": "Tālavya (Palatal)"},
    "छ": {"token": "cha", "type": "Mahāprāṇa Aghoṣa Sparśa", "place": "Tālavya (Palatal)"},
    "ज": {"token": "ja", "type": "Alpaprāṇa Ghoṣa Sparśa", "place": "Tālavya (Palatal)"},
    "झ": {"token": "jha", "type": "Mahāprāṇa Ghoṣa Sparśa", "place": "Tālavya (Palatal)"},
    "ञ": {"token": "ña", "type": "Anunāsika Sparśa", "place": "Tālavya & Nāsikya (Palatal-Nasal)"},

    # --- Ṭa-Varga (Mūrdhanya / Retroflex) ---
    "ट": {"token": "ṭa", "type": "Alpaprāṇa Aghoṣa Sparśa", "place": "Mūrdhanya (Retroflex)"},
    "ठ": {"token": "ṭha", "type": "Mahāprāṇa Aghoṣa Sparśa", "place": "Mūrdhanya (Retroflex)"},
    "ड": {"token": "ḍa", "type": "Alpaprāṇa Ghoṣa Sparśa", "place": "Mūrdhanya (Retroflex)"},
    "ढ": {"token": "ḍha", "type": "Mahāprāṇa Ghoṣa Sparśa", "place": "Mūrdhanya (Retroflex)"},
    "ण": {"token": "ṇa", "type": "Anunāsika Sparśa", "place": "Mūrdhanya & Nāsikya (Retroflex-Nasal)"},

    # --- Ta-Varga (Dantya / Dental) ---
    "त": {"token": "ta", "type": "Alpaprāṇa Aghoṣa Sparśa", "place": "Dantya (Dental)"},
    "थ": {"token": "tha", "type": "Mahāprāṇa Aghoṣa Sparśa", "place": "Dantya (Dental)"},
    "द": {"token": "da", "type": "Alpaprāṇa Ghoṣa Sparśa", "place": "Dantya (Dental)"},
    "ध": {"token": "dha", "type": "Mahāprāṇa Ghoṣa Sparśa", "place": "Dantya (Dental)"},
    "न": {"token": "na", "type": "Anunāsika Sparśa", "place": "Dantya & Nāsikya (Dental-Nasal)"},

    # --- Pa-Varga (Oṣṭhya / Labial) ---
    "प": {"token": "pa", "type": "Alpaprāṇa Aghoṣa Sparśa", "place": "Oṣṭhya (Labial)"},
    "फ": {"token": "pha", "type": "Mahāprāṇa Aghoṣa Sparśa", "place": "Oṣṭhya (Labial)"},
    "ब": {"token": "ba", "type": "Alpaprāṇa Ghoṣa Sparśa", "place": "Oṣṭhya (Labial)"},
    "भ": {"token": "bha", "type": "Mahāprāṇa Ghoṣa Sparśa", "place": "Oṣṭhya (Labial)"},
    "म": {"token": "ma", "type": "Anunāsika Sparśa", "place": "Oṣṭhya & Nāsikya (Labial-Nasal)"},

    # --- Antaḥstha (Semivowels) ---
    "य": {"token": "ya", "type": "Antaḥstha (Semivowel)", "place": "Tālavya (Palatal)"},
    "र": {"token": "ra", "type": "Antaḥstha (Semivowel)", "place": "Mūrdhanya (Retroflex)"},
    "ल": {"token": "la", "type": "Antaḥstha (Semivowel)", "place": "Dantya (Dental)"},
    "व": {"token": "va", "type": "Antaḥstha (Semivowel)", "place": "Dantoṣṭhya (Dento-Labial)"},

    # --- Ūṣma (Sibilants & Aspirate) ---
    "श": {"token": "śa", "type": "Ūṣma (Sibilant)", "place": "Tālavya (Palatal)"},
    "ष": {"token": "ṣa", "type": "Ūṣma (Sibilant)", "place": "Mūrdhanya (Retroflex)"},
    "स": {"token": "sa", "type": "Ūṣma (Sibilant)", "place": "Dantya (Dental)"},
    "ह": {"token": "ha", "type": "Ūṣma (Glottal/Aspirate)", "place": "Kaṇṭhya (Guttural)"},

    # --- Classical Conjuncts (Samyuktakshara) ---
    "क्ष": {"token": "kṣa", "type": "Saṃyuktākṣara (k + ṣ)", "place": "Kaṇṭha-Mūrdhanya"},
    "त्र": {"token": "tra", "type": "Saṃyuktākṣara (t + r)", "place": "Danto-Mūrdhanya"},
    "ज्ञ": {"token": "jña", "type": "Saṃyuktākṣara (j + ñ)", "place": "Tālavya"}
}

COMMON_WORD_ALIASES = {
    "क्या": "क", "का": "क", "की": "क", "के": "क",
    "खा": "ख", "गा": "ग", "घा": "घ", "चा": "च",
    "छा": "छ", "जा": "ज", "झा": "झ", "टा": "ट",
    "ठा": "ठ", "डा": "ड", "ढा": "ढ", "ता": "त",
    "तो": "त", "था": "थ", "दा": "द", "दो": "द",
    "धा": "ध", "ना": "न", "पा": "प", "फा": "फ",
    "बा": "ब", "भा": "भ", "मा": "म", "या": "य",
    "रा": "र", "री": "ऋ", "ऋषि": "ऋ", "ला": "ल",
    "वा": "व", "शा": "श", "षा": "ष", "सा": "स",
    "हा": "ह", "है": "ह", "हो": "ह"
}

def normalize_sanskrit_input(text: str) -> str:
    """
    Normalizes speech-to-text outputs to isolate a single Devanagari Akshara.
    """
    if not text:
        return ""

    text = unicodedata.normalize('NFC', text.strip())

    if text in PHONETIC_MAP:
        return text

    if text in COMMON_WORD_ALIASES:
        return COMMON_WORD_ALIASES[text]

    vowel_matras = set('\u093e\u093f\u0940\u0941\u0942\u0943\u0944\u0947\u0948\u094b\u094c\u094d')
    cleaned_chars = [ch for ch in text if ch not in vowel_matras]
    
    for ch in cleaned_chars:
        if ch in PHONETIC_MAP:
            return ch

    for ch in text:
        if '\u0900' <= ch <= '\u097f' and ch not in vowel_matras:
            return ch

    return text[0] if text else ""

def get_phonetic_details(char: str) -> dict:
    """
    Fetches the Paninian phonetic classification for a given Akshara.
    """
    clean_char = normalize_sanskrit_input(char)
    if clean_char in PHONETIC_MAP:
        info = PHONETIC_MAP[clean_char].copy()
        info["char"] = clean_char
        return info
    
    return {
        "char": clean_char or "?",
        "token": "unknown",
        "type": "Unmapped Phoneme",
        "place": "Unknown / Non-standard Akshara"
    }
