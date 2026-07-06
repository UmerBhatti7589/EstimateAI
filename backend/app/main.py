from fastapi import FastAPI

from app.database.database import engine
from app.models.project import Base
from app.routers.project import router

app = FastAPI(
    title="EstimateAI API",
    version="1.0"
)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Include Router
app.include_router(router)


# Home API
@app.get("/")
def home():
    return {
        "message": "EstimateAI Backend is Running 🚀"
    }


# About API
@app.get("/about")
def about():
    return {
        "project": "EstimateAI",
        "version": "1.0",
        "developer": "Muhammad Umer"
    }