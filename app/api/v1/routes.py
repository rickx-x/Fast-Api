from fastapi import APIRouter, Depends
from api.dependencies import get_todo_service
from services.todo_services import TodoService
router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/todo/{item_id}")
async def read_todo(
    item_id: int, 
    todo_service:TodoService=Depends(get_todo_service)):
    return await todo_service.fetch_todo_by_id(item_id) 

@router.get("/todos")
async def read_todos(todo_service:TodoService=Depends(get_todo_service)):
     return await todo_service.fetch_todos()