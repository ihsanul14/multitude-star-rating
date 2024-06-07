import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app

endpoint = "/api/ratings"

@pytest.mark.anyio
async def test_get_rating(client: AsyncClient):
    response = await client.get(endpoint)
    assert response.status_code == 200

@pytest.mark.anyio
async def test_post_rating(client: AsyncClient):
    response = await client.post(endpoint, headers={"Content-Type": "application/json"}, json={'rating':6})
    assert response.status_code == 422

    response = await client.post(endpoint, headers={"Content-Type": "application/json"}, json={'rating':0})
    assert response.status_code == 422

    response = await client.post(endpoint, headers={"Content-Type": "application/json"}, json={'rating':3})
    assert response.status_code == 200
    