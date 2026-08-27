# app.py
import io
import pandas as pd
import speech_recognition as sr
import streamlit as st
from phonetics import PHONETIC_MAP, get_phonetic_details

st.set_page_config(page_title="Sanskrit Phonetic Classifier", page_icon="🎙️", layout="wide")

st.title("🎙️ Sanskrit Phonetic Classifier")
st.markdown("Accurately detects spoken Sanskrit/Devanagari letters and identifies their **Pāṇinīya Śikṣā** articulatory classification.")

tab1, tab2 = st.tabs(["🎙️ Voice Classifier", "📖 Master 50-Akshara Chart"])

with tab1:
    audio_input = st.audio_input("Record an isolated Sanskrit sound (e.g., 'क', 'ख', 'अ', 'श', 'त')")

    if audio_input is not None:
        st.audio(audio_input)
        
        with st.spinner("Recognizing phoneme accurately..."):
            recognizer = sr.Recognizer()
            audio_bytes = audio_input.read()
            
            # Convert browser audio stream to WAV audio source
            audio_file = io.BytesIO(audio_bytes)
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
            
            recognized_char = None
            try:
                # Recognize using Indian Devanagari acoustic models (Sanskrit / Hindi)
                text = recognizer.recognize_google(audio_data, language="sa-IN")
                recognized_char = text.strip()
            except Exception:
                try:
                    # Fallback language model for Indian phonetic accents
                    text = recognizer.recognize_google(audio_data, language="hi-IN")
                    recognized_char = text.strip()
                except Exception:
                    recognized_char = None

        if recognized_char:
            info = get_phonetic_details(recognized_char)
            st.success(f"Recognized Sound: **{info['char']}**")

            col1, col2, col3 = st.columns(3)
            col1.metric("Recognized Akshara", f"{info['char']} ({info['token']})")
            col2.metric("Category (Prayatna)", info["type"])
            col3.metric("Place of Articulation (Sthāna)", info["place"])
        else:
            st.warning("Could not clearly isolate the spoken letter. Please speak closer to the microphone and pronounce the letter clearly (e.g. 'क', 'अ').")

with tab2:
    st.subheader("Pāṇinīya Śikṣā 50-Akshara Reference")
    df_data = [
        {"Akshara": k, "Token": v["token"], "Sound Type": v["type"], "Articulation Place (Sthāna)": v["place"]}
        for k, v in PHONETIC_MAP.items()
    ]
    st.dataframe(pd.DataFrame(df_data), use_container_width=True, height=500)
