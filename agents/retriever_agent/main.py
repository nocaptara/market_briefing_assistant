# agents/retriever_agent/main.py
from fastapi import FastAPI
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the embeddings with the API key
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

app = FastAPI()

@app.get("/retrieve")
def retrieve(query: str):
    vectorstore = FAISS.load_local("faiss_index", embeddings)
    results = vectorstore.similarity_search(query, k=3)
    return {"chunks": [r.page_content for r in results]}
