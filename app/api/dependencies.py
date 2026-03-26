from fastapi.params import Depends
from services.todo_services import TodoService
import httpx
from typing import AsyncGenerator
async def get_http_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(timeout=10) as client:
        yield client

async def get_todo_service(client:httpx.AsyncClient = Depends(get_http_client))-> TodoService:
    return TodoService(client)
