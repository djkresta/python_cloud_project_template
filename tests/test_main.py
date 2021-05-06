import pytest
from httpx import AsyncClient
import socket

from fastapi_dev.main import app, get_hostname
URL = "http://httpbin.org/uuid"

hostname = socket.gethostname().split(".")[0]

@pytest.mark.asyncio
async def test_hello_post():
	async with AsyncClient(app=app, base_url="http://test") as ac:
		response = await ac.post("/hn")
		response_data = response.json()
		assert response.status_code == 200
		assert response_data.get("hostname") == hostname


@pytest.mark.asyncio
async def test_ping():
	async with AsyncClient(app=app, base_url="http://test") as ac:
	    response = await ac.get("/ping")
	    assert response.status_code == 200
	    assert response.json() == {"ping": "pong!"}


@pytest.mark.asyncio
async def test_get_url_response():
	async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.post("/", json={"url_info": URL})

	assert response.status_code == 200
