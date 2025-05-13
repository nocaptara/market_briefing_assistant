import subprocess
import os

# List of agents and their respective ports
agents = [
    ("api_agent", 8001),
    ("scraping_agent", 8002),
    ("retriever_agent", 8003),
    ("analysis_agent", 8004),
    ("language_agent", 8005),
    ("orchestrator", 8006),
    ("voice_agent", 8007)
]

# Check if the agents directory exists
base_dir = os.path.dirname(os.path.abspath(__file__))

# Function to start an agent
def start_agent(agent, port):
    if agent == "orchestrator":
        path = f"{base_dir}/{agent}/main.py"  # Orchestrator is outside 'agents/'
    else:
        path = f"{base_dir}/agents/{agent}/main.py"  # Other agents are under 'agents/'
    
    if os.path.exists(path):  # Ensure the path exists before running
        print(f"Starting agent {agent} with path: {path}")  # Debug line to print the path
        subprocess.Popen(["uvicorn", f"{agent}.main:app", "--port", str(port), "--reload"])
        print(f"✅ {agent} started on port {port}.")
    else:
        print(f"❌ {agent} not found at {path}.")

# Iterate through each agent and start them
for agent, port in agents:
    start_agent(agent, port)

print("✅ All agents have been started.")
print("ℹ️ Run Streamlit separately with: `streamlit run streamlit_app/app.py`")
