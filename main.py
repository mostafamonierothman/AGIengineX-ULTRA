# app.py

from fastapi import FastAPI, Request
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"status": "AGIengineX-ULTRA is LIVE 🚀"}

# next_move endpoint
@app.get("/next_move")
def next_move_endpoint():
    result = get_next_move()
    return {"next_move": result}

# opportunity endpoint
@app.get("/opportunity")
def opportunity_endpoint():
    result = get_opportunity()
    return {"opportunity": result}

# run_agent endpoint (POST)
@app.post("/run_agent")
async def run_agent(request: Request):
    data = await request.json()
    agent_name = data.get("agent_name")
    input_data = data.get("input", {})

    if agent_name == "next_move_agent":
        result = get_next_move()
        return {"next_move": result}

    elif agent_name == "opportunity_agent":
        result = get_opportunity()
        return {"opportunity": result}

    else:
        return {"error": "Unknown agent"}
