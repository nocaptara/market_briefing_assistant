# agents/api_agent/main.py
from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/market_data")
def get_market_data(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    return hist.tail(1).to_dict()
