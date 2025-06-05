# supervisor.py
import time
from agents import lead_generation_agent, next_move_agent, opportunity_agent, AutoFixAgent, CommitFix, MetaAgent, MetaMemoryAgent
from dashboard_api import push_update

class SupervisorAgent:
    def run_agents(self):
        print("[Supervisor] Running agents...")
        lead_generation_agent.run()
        next_move_agent.run()
        opportunity_agent.run()

    def auto_fix_if_needed(self):
        print("[Supervisor] Checking for fixes...")
        AutoFixAgent.run()

    def meta_agent_propose(self):
        print("[Supervisor] MetaAgent proposing new agents...")
        MetaAgent.run()

    def update_memory(self):
        print("[Supervisor] Updating MetaMemory...")
        MetaMemoryAgent.update()

    def push_dashboard(self):
        print("[Supervisor] Pushing update to dashboard...")
        push_update()

    async def run_loop(self):
        while True:
            print("\n==== AGIengineX-ULTRA LOOP ====")
            self.run_agents()
            self.auto_fix_if_needed()
            self.meta_agent_propose()
            self.update_memory()
            self.push_dashboard()
            print("Sleeping for 60 seconds...")
            time.sleep(60)
