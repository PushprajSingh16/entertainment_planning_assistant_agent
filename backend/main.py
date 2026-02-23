from fastapi import FastAPI
from agent import PlannerAgent

app = FastAPI(title="Entertainment Planning Assistant")

agent = PlannerAgent()

@app.get("/")
def root():
    return {"status": "Backend running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": "2026-02-24"}

@app.get("/plan")
def plan(movie: str, city: str):
    return agent.run(movie, city)