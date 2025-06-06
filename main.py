# main.py
from fastapi import FastAPI, Request
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity
import gradio as gr

# FastAPI app (backend for API)
app = FastAPI()

# API Endpoints
@app.get("/")
def root():
    return {"message": "AGIengineX is LIVE!", "status": "OK"}

@app.get("/next_move")
def next_move_endpoint():
    result = get_next_move()
    return {"next_move": result}

@app.get("/opportunity")
def opportunity_endpoint():
    result = get_opportunity()
    return {"opportunity": result}

@app.post("/run_agent")
async def run_agent(request: Request):
    data = await request.json()
    agent_name = data.get("agent_name")
    input_data = data.get("input", {})

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

# Gradio Interface (this is required so HF "sees" something to run)
def run_next_move():
    result = get_next_move()
    return result

def run_opportunity():
    result = get_opportunity()
    return result

with gr.Blocks() as demo:
    gr.Markdown("## 🚀 AGIengineX Control Panel")
    with gr.Row():
        move_button = gr.Button("Get Next Move")
        opportunity_button = gr.Button("Get Opportunity")
    output = gr.Textbox(label="Result")

    move_button.click(fn=run_next_move, outputs=output)
    opportunity_button.click(fn=run_opportunity, outputs=output)

# For HF Spaces
if __name__ == "__main__":
    demo.launch()
