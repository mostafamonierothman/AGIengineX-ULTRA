# main.py
from fastapi import FastAPI, Request
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity
import gradio as gr

# FastAPI backend (can also be used by Gradio backend)
app = FastAPI()

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

# Now wrap in Gradio so HF can serve it properly
def run_next_move():
    return get_next_move()

def run_opportunity():
    return get_opportunity()

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 AGIengineX Control Panel")

    with gr.Row():
        btn_next_move = gr.Button("Run Next Move Agent")
        output_next_move = gr.Textbox(label="Next Move Result")

    with gr.Row():
        btn_opportunity = gr.Button("Run Opportunity Agent")
        output_opportunity = gr.Textbox(label="Opportunity Result")

    btn_next_move.click(fn=run_next_move, outputs=output_next_move)
    btn_opportunity.click(fn=run_opportunity, outputs=output_opportunity)

# Gradio runs this app
demo.launch()
