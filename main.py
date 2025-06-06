# main.py

from fastapi import FastAPI, Request
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity
import gradio as gr

# FastAPI app (still useful for API calls)
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

# === Gradio UI ===

# Simple function to expose in Gradio
def run_next_move_ui():
    result = get_next_move()
    return f"Next Move Result: {result}"

def run_opportunity_ui():
    result = get_opportunity()
    return f"Opportunity Result: {result}"

# Create Gradio Blocks Interface
with gr.Blocks() as demo:
    gr.Markdown("# AGIengineX Ultra 🚀")
    gr.Markdown("Test your agents below:")

    next_move_btn = gr.Button("Run Next Move Agent")
    next_move_output = gr.Textbox(label="Next Move Output")

    next_move_btn.click(fn=run_next_move_ui, outputs=next_move_output)

    opp_btn = gr.Button("Run Opportunity Agent")
    opp_output = gr.Textbox(label="Opportunity Output")

    opp_btn.click(fn=run_opportunity_ui, outputs=opp_output)

# Final Gradio app object (for HF Spaces)
if __name__ == "__main__":
    demo.launch()
