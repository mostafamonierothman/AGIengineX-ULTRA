# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity
import gradio as gr

# === FastAPI App ===
app = FastAPI()

# === FastAPI Endpoints ===

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

# Gradio Functions
def run_next_move_ui():
    result = get_next_move()
    return f"Next Move Result: {result}"

def run_opportunity_ui():
    result = get_opportunity()
    return f"Opportunity Result: {result}"

# Gradio Blocks Interface
gradio_app = gr.Blocks()

with gradio_app:
    gr.Markdown("# AGIengineX Ultra 🚀 — Gradio UI")
    gr.Markdown("Test your agents below:")

    next_move_btn = gr.Button("Run Next Move Agent")
    next_move_output = gr.Textbox(label="Next Move Output")
    next_move_btn.click(fn=run_next_move_ui, outputs=next_move_output)

    opp_btn = gr.Button("Run Opportunity Agent")
    opp_output = gr.Textbox(label="Opportunity Output")
    opp_btn.click(fn=run_opportunity_ui, outputs=opp_output)

# === Mount Gradio app into FastAPI ===
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.responses import RedirectResponse

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Optional: restrict if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Gradio at /gradio
@app.get("/gradio", response_class=HTMLResponse)
async def gradio_root():
    return RedirectResponse(url="/gradio/")

app.mount("/gradio", gradio_app.to_mountable())
