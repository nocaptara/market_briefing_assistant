# agents/language_agent/main.py
from fastapi import FastAPI, Request
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM with API key
llm = OpenAI(openai_api_key=openai_api_key)

app = FastAPI()

@app.post("/generate_brief")
async def generate_brief(request: Request):
    data = await request.json()
    exposure = data.get("exposure", "")
    surprises = data.get("surprises", {})
    prompt = f"""Generate a 2-line market brief for:
    - Exposure: {exposure}
    - Surprises: {surprises}"""
    return {"brief": llm(prompt)}
