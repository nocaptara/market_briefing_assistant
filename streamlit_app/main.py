import streamlit as st
import requests
import tempfile
import os

st.title("🎙️ Voice Input Market Brief")

audio_bytes = st.audio_recorder("Click to record", sample_rate=16000)

if audio_bytes and st.button("Send Voice"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        tmp_file_path = tmp_file.name

    with open(tmp_file_path, "rb") as f:
        files = {'audio': f}
        r = requests.post("http://localhost:8007/stt", files=files)
        transcription = r.json()["text"]
        st.write(f"🗣️ Transcribed: {transcription}")

    os.remove(tmp_file_path)
