# agents/analysis_agent/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/risk_exposure")
def get_exposure(region: str, sector: str):
    # Dummy static logic for now
    if region == "Asia" and sector == "tech":
        return {"exposure": "22%", "prev_day": "18%"}
    return {"exposure": "N/A"}
