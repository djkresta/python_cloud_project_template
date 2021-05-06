from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import httpx

app = FastAPI()


class Hostname(BaseModel):
    hostname: str


class UrlResponse(BaseModel):
    url_info: str


def get_hostname():
    s2_out = subprocess.check_output(["hostname"]).decode().strip()
    return s2_out


@app.post("/hn/", response_model=Hostname)
async def hostname():
    hostname = get_hostname()
    return {"hostname": hostname}


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.post("/")
async def get_url_response(url: UrlResponse):
    async with httpx.AsyncClient() as client:
        response = await client.get(url.url_info)
    if response.status_code == 200:
        return {"status": "ok"}
    else:
        return {"status": "bad"}
