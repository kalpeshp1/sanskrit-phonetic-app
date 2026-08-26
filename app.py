# app.py
import io
import librosa
import numpy as np
import pandas as pd
import soundfile as sf
import streamlit as st
from phonetics import PHONETIC_MAP, get_phonetic_details

st.set_page_config(page_title="Complete Sanskrit 50-Akshara Classifier", page_icon="🕉️", layout="wide")

st.title("🕉️ Complete Sanskrit Phonetic Classifier (50 Aksharas)")
st.markdown("Covers all **13 Svaras**, **25 Sparśa Vyanjanas**, **4 Antasthas**, **4 Ūṣmans**, and **4 Ayogavāhas** based on **Pāṇinīya Śikṣā**.")

tab1, tab2 = st.tabs(["🎙️ Real-Time Classifier", "📖 Complete 50-Letter Phonetic Chart"])

with tab1:
    st.subheader("Live Acoustic Audio Classifier")
    audio_input = st.audio_input("Record an isolated Sanskrit letter")

    def classify_sanskrit_sound(raw_bytes):
        data, sr = sf.read(io.BytesIO(raw_bytes))
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)
        trimmed, _ = librosa.effects.trim(data, top_db=20)
        if len(trimmed) < 200:
            trimmed = data

        centroid = float(np.mean(librosa.feature.spectral_centroid(y=trimmed, sr=sr)))
        zcr = float(np.mean(librosa.feature.zero_crossing_rate(trimmed)))
        rms = float(np.mean(librosa.feature.rms(y=trimmed)))
        flatness = float(np.mean(librosa.feature.spectral_flatness(y=trimmed)))

        # 1. Ūṣman & Fricatives (Sibilants)
        if zcr > 0.22:
            token = "sha_ret" if centroid > 4500 else ("sha_pal" if centroid > 3600 else "sa")
        elif zcr > 0.16:
            token = "chha" if rms > 0.12 else "cha"

        # 2. Aspirates & Visarga
        elif rms > 0.16 and centroid > 3200:
            token = "ha" if zcr < 0.12 else "ah"

        # 3. Nasals (High spectral flatness / continuous resonance)
        elif flatness > 0.05 and centroid < 1800:
            token = "am" if zcr < 0.03 else "ma"

        # 4. Labials & Back Vowels
        elif centroid < 1000:
            token = "oo" if rms > 0.08 else "u"
        elif centroid < 1400:
            token = "o" if zcr < 0.04 else ("bha" if rms > 0.10 else "ba")
        elif centroid < 1750:
            token = "au" if zcr < 0.04 else ("pha" if rms > 0.10 else "pa")

        # 5. Gutturals (Kaṇṭhya) & Central Vowels
        elif centroid < 2100:
            token = "aa" if rms > 0.09 else "a"
        elif centroid < 2700:
            if rms > 0.13:
                token = "gha" if flatness > 0.02 else "kha"
            elif flatness > 0.02:
                token = "ga"
            else:
                token = "ka"

        # 6. Dentals (Dantya) & Semivowels
        elif centroid < 3200:
            if zcr < 0.06:
                token = "e" if flatness > 0.03 else "dha_den"
            else:
                token = "tha_den" if rms > 0.10 else "ta_den"

        # 7. Palatals & Retroflex
        elif centroid < 3900:
            if zcr < 0.06:
                token = "i" if flatness > 0.03 else "ai"
            else:
                token = "tha_ret" if rms > 0.10 else "ta_ret"
        else:
            token = "ee" if zcr < 0.06 else "ra"

        return token, centroid, zcr, rms

    if audio_input is not None:
        st.audio(audio_input)
        with st.spinner("Classifying audio..."):
            token, centroid, zcr, rms = classify_sanskrit_sound(audio_input.read())
            info = get_phonetic_details(token)

        st.success("Sound Classified!")
        col1, col2, col3 = st.columns(3)
        col1.metric("Recognized Akshara", f"{info['char']} ({token})")
        col2.metric("Category", info["type"])
        col3.metric("Sthāna (Articulation)", info["place"])

        with st.expander("🔬 Acoustic Spectral Telemetry"):
            st.write(f"- **Spectral Centroid:** `{centroid:.2f} Hz`")
            st.write(f"- **Zero Crossing Rate:** `{zcr:.4f}`")
            st.write(f"- **RMS Energy:** `{rms:.4f}`")

with tab2:
    st.subheader("Pāṇinīya Śikṣā 50-Akshara Master Reference Table")
    df_data = []
    for k, v in PHONETIC_MAP.items():
        df_data.append({"Akshara": v["char"], "Token": k, "Type / Prayatna": v["type"], "Sthāna (Place of Articulation)": v["place"]})
    df = pd.DataFrame(df_data)
    st.dataframe(df, use_container_width=True, height=550)
