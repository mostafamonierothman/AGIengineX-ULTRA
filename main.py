# main.py
from fastapi import FastAPI, Request
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity
import gradio as gr

# FastAPI app (still useful if needed)
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

# === Gradio Interface ===

# Example function to wrap in Gradio
def run_next_move():
    return get_next_move()

def run_opportunity():
    return get_opportunity()

# Gradio app
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AGIengineX Interface")
    gr.Markdown("Run the agents below:")

    with gr.Row():
        next_move_btn = gr.Button("Run Next Move Agent")
        next_move_output = gr.Textbox(label="Next Move Result")
    
    with gr.Row():
        opportunity_btn = gr.Button("Run Opportunity Agent")
        opportunity_output = gr.Textbox(label="Opportunity Result")

    # Button actions
    next_move_btn.click(fn=run_next_move, outputs=next_move_output)
    opportunity_btn.click(fn=run_opportunity, outputs=opportunity_output)

# Launch Gradio
if __name__ == "__main__":
    demo.launch()
