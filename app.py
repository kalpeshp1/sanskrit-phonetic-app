import io
import os
import re
import json
import base64
import requests
import pandas as pd
import speech_recognition as sr
import streamlit as st
import unicodedata
from phonetics import PHONETIC_MAP, get_phonetic_details, normalize_sanskrit_input

st.set_page_config(
    page_title="Sanskrit Phonetic Classifier",
    page_icon="🕉️",
    layout="wide"
)

def recognize_sanskrit_sound_gemini(audio_bytes: bytes) -> dict:
    """
    Classifies isolated Sanskrit phonemes/aksharas using Gemini multimodal audio analysis.
    This eliminates Google ASR's whole-word bias (e.g. converting 'त' into 'तो' or 'क' into 'क्या').
    """
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return None

    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
    encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")
    
    system_prompt = """You are a Pāṇinīya Śikṣā and Sanskrit phonetics expert.
Identify the single isolated Sanskrit sound/letter (Akshara) spoken in the audio recording.
Do not transcribe full words. Identify the exact letter from the standard 50-Akshara Sanskrit alphabet:
- Vowels (Svara): अ, आ, इ, ई, उ, ऊ, ऋ, ॠ, ऌ, ए, ऐ, ओ, औ, अं, अः
- Sparśa (Consonants):
  * Kaṇṭhya (Guttural): क, ख, ग, घ, ङ
  * Tālavya (Palatal): च, छ, ज, झ, ञ
  * Mūrdhanya (Retroflex): ट, ठ, ड, ढ, ण
  * Dantya (Dental): त, थ, द, ध, न
  * Oṣṭhya (Labial): प, फ, ब, भ, म
- Antaḥstha (Semivowels): य, र, ल, व
- Ūṣma (Sibilants/Aspirate): श (Palatal), ष (Retroflex), स (Dental), ह (Glottal)

Respond strictly with valid JSON in this structure:
{
  "letter": "<single Devanagari character, e.g. 'क' or 'ऋ'>",
  "confidence": "<high | medium | low>",
  "explanation": "<brief note on articulation features heard>"
}"""

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    { "text": "Identify the isolated Sanskrit letter (Akshara) pronounced in this audio clip. Return JSON only." },
                    {
                        "inlineData": {
                            "mimeType": "audio/wav",
                            "data": encoded_audio
                        }
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json"
        },
        "systemInstruction": {
            "parts": [{ "text": system_prompt }]
        }
    }

    try:
        response = requests.post(api_url, headers={"Content-Type": "application/json"}, json=payload, timeout=12)
        if response.status_code == 200:
            result = response.json()
            raw_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(raw_text)
    except Exception:
        pass
    return None

def recognize_sanskrit_speech_recognition(audio_bytes: bytes) -> str:
    """
    Uses Google ASR with multi-language fallback and extracts the base root akshara.
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    audio_file = io.BytesIO(audio_bytes)
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        for lang in ["sa-IN", "hi-IN", "mr-IN"]:
            try:
                text = recognizer.recognize_google(audio_data, language=lang)
                if text and len(text.strip()) > 0:
                    cleaned = normalize_sanskrit_input(text.strip())
                    if cleaned:
                        return cleaned
            except Exception:
                continue
    except Exception:
        pass
    return None

st.title("🎙️ Sanskrit Phonetic Classifier & Articulation Analyzer")
st.markdown("Accurately detects spoken Sanskrit/Devanagari letters and maps their **Pāṇinīya Śikṣā** articulatory classification.")

tab1, tab2, tab3 = st.tabs(["🎙️ Voice Classifier", "📖 Master 50-Akshara Chart", "🛠️ Manual Test & Normalizer"])

with tab1:
    st.info("💡 **Tip for Best Accuracy:** Speak a single isolated sound clearly (e.g. *'क'*, *'ख'*, *'ध'*, *'ष'*, *'ऋ'*).")
    
    col_input, col_result = st.columns([1, 1], gap="medium")

    with col_input:
        audio_input = st.audio_input("Record an isolated Sanskrit sound:")
        engine_choice = st.radio(
            "Recognition Engine:",
            ["✨ Enhanced Phoneme Matcher (Auto)", "🌐 Google Speech API Only"],
            horizontal=True
        )

    with col_result:
        if audio_input is not None:
            st.audio(audio_input)
            
            with st.spinner("Analyzing sound acoustics..."):
                audio_bytes = audio_input.read()
                recognized_char = None
                details = None
                gemini_meta = None

                if "Enhanced" in engine_choice:
                    gemini_meta = recognize_sanskrit_sound_gemini(audio_bytes)
                    if gemini_meta and "letter" in gemini_meta:
                        recognized_char = normalize_sanskrit_input(gemini_meta["letter"])

                if not recognized_char:
                    recognized_char = recognize_sanskrit_speech_recognition(audio_bytes)

                if recognized_char:
                    details = get_phonetic_details(recognized_char)

            if details and details.get("char") and details["char"] != "?":
                st.success(f"Recognized Sound: **{details['char']}** ({details['token']})")
                
                m1, m2 = st.columns(2)
                m1.metric("Akshara", f"{details['char']}")
                m2.metric("IAST Token", f"{details['token']}")
                
                st.markdown("---")
                c1, c2 = st.columns(2)
                c1.markdown(f"**Sound Type (Prayatna):**\n`{details['type']}`")
                c2.markdown(f"**Place of Articulation (Sthāna):**\n`{details['place']}`")
                
                if gemini_meta and gemini_meta.get("explanation"):
                    st.caption(f"Note: {gemini_meta['explanation']}")
            else:
                st.warning("⚠️ Could not isolate a single Sanskrit sound. Please try again speaking a little louder.")

with tab2:
    st.subheader("Pāṇinīya Śikṣā 50-Akshara Reference Chart")
    df_data = [
        {
            "Akshara": k,
            "IAST Token": v["token"],
            "Category (Prayatna)": v["type"],
            "Place of Articulation (Sthāna)": v["place"]
        }
        for k, v in PHONETIC_MAP.items()
    ]
    st.dataframe(pd.DataFrame(df_data), use_container_width=True, height=500)

with tab3:
    st.subheader("Manual Lookup & Normalization Diagnostic")
    test_input = st.text_input("Test any recognized word or character:", value="घ")
    if test_input:
        normalized = normalize_sanskrit_input(test_input)
        info = get_phonetic_details(normalized)
        st.write(f"**Input:** `{test_input}` $\\rightarrow$ **Normalized Akshara:** `{normalized}`")
        st.json(info)
