# agents/scraping_agent/main.py
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/earnings_surprises")
def get_surprises():
    url = "https://finance.yahoo.com/calendar/earnings"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # Dummy placeholder – parse actual earnings surprises here
    return {"TSMC": "+4%", "Samsung": "-2%"}
