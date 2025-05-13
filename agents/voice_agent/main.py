# agents/voice_agent/main.py
from fastapi import FastAPI, UploadFile
import whisper
import pyttsx3

app = FastAPI()
model = whisper.load_model("base")
tts_engine = pyttsx3.init()

@app.post("/stt")
async def stt(audio: UploadFile):
    audio_path = f"/tmp/{audio.filename}"
    with open(audio_path, "wb") as f:
        f.write(await audio.read())
    result = model.transcribe(audio_path)
    return {"text": result["text"]}

@app.post("/tts")
async def tts(text: str):
    tts_engine.save_to_file(text, "response.mp3")
    tts_engine.runAndWait()
    return {"audio_file": "response.mp3"}
