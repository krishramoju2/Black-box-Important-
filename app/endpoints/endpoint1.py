# app/endpoints/endpoint1.py
from fastapi import APIRouter, Request
import base64

router = APIRouter()

@router.post("/endpoint1")
async def reverse_engineered_endpoint1(request: Request):
    data = await request.json()
    input_text = data.get("input", "")
    encoded = base64.b64encode(input_text.encode()).decode()
    return {"result": encoded}
