# tests/test_tweet.py
import pytest
from httpx import AsyncClient
from app.main import app  # adjust the import path according to your project structure

@pytest.mark.asyncio
async def test_create_tweet():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.post("/tweets/", json={"content": "Hello, World!", "author_id": 1})  # assuming a user with id 1 exists
    assert response.status_code == 200
    assert response.json()["content"] == "Hello, World!"

@pytest.mark.asyncio
async def test_read_tweet():
    tweet_id = 1  # assuming there is already a tweet with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get(f"/tweets/{tweet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == tweet_id

@pytest.mark.asyncio
async def test_update_tweet():
    tweet_id = 1  # assuming there is already a tweet with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.put(f"/tweets/{tweet_id}", json={"content": "Updated content!"})
    assert response.status_code == 200
    assert response.json()["content"] == "Updated content!"

@pytest.mark.asyncio
async def test_delete_tweet():
    tweet_id = 1  # assuming there is already a tweet with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.delete(f"/tweets/{tweet_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Tweet deleted successfully"
