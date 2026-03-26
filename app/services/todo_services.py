from core.config import url
import httpx

class TodoService:
    def __init__(self, client:httpx.AsyncClient):
        self.client = client

    async def fetch_todos(self):
        response = await self.client.get(url)
        response.raise_for_status()
        return response.json()

    async def fetch_todo_by_id(self, item_id: int):
        response = await self.client.get(f"{url}/{item_id}")
        response.raise_for_status()
        return response.json()