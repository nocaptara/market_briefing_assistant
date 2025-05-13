# orchestrator/main.py
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/market_brief")
def market_brief():
    stx = requests.get("http://localhost:8004/risk_exposure?region=Asia&sector=tech").json()
    surprises = requests.get("http://localhost:8002/earnings_surprises").json()
    brief = requests.post("http://localhost:8005/generate_brief", json={
        "exposure": stx,
        "surprises": surprises
    }).json()
    return brief
