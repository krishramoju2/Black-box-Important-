# app/main.py
from fastapi import FastAPI, Request
from app.endpoints import endpoint1, endpoint2  # Import your reverse-engineered endpoints

app = FastAPI()

app.include_router(endpoint1.router)
app.include_router(endpoint2.router)
