# main.py
import uvloop
import asyncio
from supervisor import SupervisorAgent
from fastapi import FastAPI
import threading

# Use uvloop for faster event loop
uvloop.install()

app = FastAPI()

supervisor = SupervisorAgent()

# Background loop
def background_loop():
    asyncio.run(supervisor.run_loop())

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=background_loop, daemon=True)
    thread.start()

@app.get("/")
def root():
    return {"status": "AGIengineX-ULTRA is LIVE 🚀"}
