# agents/MetaMemoryAgent.py

import json
import os
import time

MEMORY_FILE = "meta_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update():
    print("[MetaMemoryAgent] Updating memory...")
    memory = load_memory()

    # Example: update with current timestamp
    memory["last_updated"] = time.time()
    memory["last_run"] = "SupervisorAgent Loop"

    save_memory(memory)
    print(f"[MetaMemoryAgent] Memory updated: {memory}")
