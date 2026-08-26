# app.py
import io
import librosa
import numpy as np
import soundfile as sf
import streamlit as st
from phonetics import get_phonetic_details

st.set_page_config(page_title="Sanskrit Phonetic Classifier", page_icon="🎙️", layout="centered")

st.title("🎙️ Sanskrit Phonetic Classifier")
st.write("Record an isolated Sanskrit letter (*Svara* or *Vyanjan*) to classify its place of articulation according to Pāṇinīya Śikṣā.")

# Built-in Streamlit microphone widget
audio_input = st.audio_input("Record your voice")

def extract_features(raw_bytes):
    data, sr = sf.read(io.BytesIO(raw_bytes))
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    trimmed, _ = librosa.effects.trim(data, top_db=20)
    if len(trimmed) < 200:
        trimmed = data
    mfccs = librosa.feature.mfcc(y=trimmed, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

if audio_input is not None:
    st.audio(audio_input)
    with st.spinner("Analyzing pronunciation features..."):
        features = extract_features(audio_input.read())
        
        # Predicted token (mock or plug model)
        predicted_token = "ka"
        info = get_phonetic_details(predicted_token)

    st.success("Analysis Complete!")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Recognized Akshara", f"{info['char']} ({predicted_token})")
    col2.metric("Sound Type", info["type"])
    col3.metric("Place of Articulation", info["place"])
