# main.py

from agents.next_move_agent import get_next_move
from agents.opportunity_agent import get_opportunity
import gradio as gr

# === Gradio Functions ===

def run_next_move_ui():
    result = get_next_move()
    return f"Next Move Result: {result}"

def run_opportunity_ui():
    result = get_opportunity()
    return f"Opportunity Result: {result}"

def run_any_agent(agent_name, input_text):
    if agent_name == "next_move_agent":
        result = get_next_move()
    elif agent_name == "opportunity_agent":
        result = get_opportunity()
    else:
        result = f"Unknown agent: {agent_name}"
    return f"Agent [{agent_name}] Result: {result} | Input: {input_text}"

# === Gradio Blocks UI ===

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AGIengineX Ultra — PURE Gradio UI 🚀")
    gr.Markdown("Test your agents below:")

    # --- Next Move Agent ---
    gr.Markdown("### Run Next Move Agent")
    next_move_btn = gr.Button("Run Next Move Agent")
    next_move_output = gr.Textbox(label="Next Move Output")

    next_move_btn.click(fn=run_next_move_ui, outputs=next_move_output)

    # --- Opportunity Agent ---
    gr.Markdown("### Run Opportunity Agent")
    opp_btn = gr.Button("Run Opportunity Agent")
    opp_output = gr.Textbox(label="Opportunity Output")

    opp_btn.click(fn=run_opportunity_ui, outputs=opp_output)

    # --- Generic Run Agent ---
    gr.Markdown("### Run Any Agent")
    agent_name_input = gr.Textbox(label="Agent Name (e.g. next_move_agent)")
    agent_input_text = gr.Textbox(label="Input (optional, free text)")
    run_agent_btn = gr.Button("Run Agent")
    run_agent_output = gr.Textbox(label="Agent Result")

    run_agent_btn.click(
        fn=run_any_agent,
        inputs=[agent_name_input, agent_input_text],
        outputs=run_agent_output
    )

# === Launch Gradio app ===
if __name__ == "__main__":
    demo.launch()
