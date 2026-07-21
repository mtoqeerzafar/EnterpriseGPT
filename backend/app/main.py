
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="EnterpriseGPT",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "application": "EnterpriseGPT",
        "status": "Running",
        "time": datetime.utcnow()
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }