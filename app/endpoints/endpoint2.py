from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/endpoint2")
async def handle_endpoint2(request: Request):
    data = await request.json()
    input_text = data.get("input", "")

    if len(input_text) % 2 == 0:
        # If even length, return reversed string
        result = input_text[::-1]
    else:
        # If odd length, return string in uppercase
        result = input_text.upper()

    return {"result": result}
