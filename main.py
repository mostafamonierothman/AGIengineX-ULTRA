# app.py
from fastapi import FastAPI, Request
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity

# Optional: import supervisor if needed later
# import supervisor

app = FastAPI()

# Enable CORS (for Lovable, local frontend, etc.)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROOT endpoint → Health check
@app.get("/")
def root():
    return {"message": "AGIengineX is LIVE!", "status": "OK"}

# NEXT_MOVE endpoint → calls next_move_agent
@app.get("/next_move")
def next_move_endpoint():
    result = get_next_move()
    return {"next_move": result}

# OPPORTUNITY endpoint → calls opportunity_agent
@app.get("/opportunity")
def opportunity_endpoint():
    result = get_opportunity()
    return {"opportunity": result}

# RUN_AGENT → Dynamic agent runner
@app.post("/run_agent")
async def run_agent(request: Request):
    data = await request.json()
    agent_name = data.get("agent_name")
    input_data = data.get("input", {})

    # Dispatch logic → Add any agent here
    if agent_name == "next_move_agent":
        result = get_next_move()
    elif agent_name == "opportunity_agent":
        result = get_opportunity()
    else:
        result = f"Unknown agent: {agent_name}"

    return {
        "agent_name": agent_name,
        "input": input_data,
        "result": result
    }
