#!/bin/bash

echo "Starting all agents..."

uvicorn agents.api_agent.main:app --port 8001 --reload &
uvicorn agents.scraping_agent.main:app --port 8002 --reload &
uvicorn agents.retriever_agent.main:app --port 8003 --reload &
uvicorn agents.analysis_agent.main:app --port 8004 --reload &
uvicorn agents.language_agent.main:app --port 8005 --reload &
uvicorn orchestrator.main:app --port 8006 --reload &
uvicorn agents.voice_agent.main:app --port 8007 --reload &

echo "All agents started. Run Streamlit separately:"
echo "streamlit run streamlit_app/app.py"

# to run
# chmod +x run_all.sh
# ./run_all.sh
