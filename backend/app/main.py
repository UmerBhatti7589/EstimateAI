from fastapi import FastAPI
from app.routers.project import router

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "EstimateAI Backend is Running 🚀"
    }

@app.get("/about")
def about():
    return {
        "project": "EstimateAI",
        "version": "1.0.0",
        "developer": "Muhammad Umer"
    }

app.include_router(router)