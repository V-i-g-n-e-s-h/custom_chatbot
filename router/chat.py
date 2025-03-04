from fastapi import (APIRouter, status,)
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.get(path="/")
def get_chat():
    return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED, content="Working on it")

