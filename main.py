from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Secweb import SecWeb

from config import config


app = FastAPI(title=config["PROJECT_NAME"])

is_prod = config["ENVIRONMENT"] == "PROD"

if is_prod:
    SecWeb(app=app)


@app.get("/")
async def read_root():
    if is_prod:
        return {"message": "Endpoint works fine."}
    else:
        return RedirectResponse(url="/docs")

from router import middleware