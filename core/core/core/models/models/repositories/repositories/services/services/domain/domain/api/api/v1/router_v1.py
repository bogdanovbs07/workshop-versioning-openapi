from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from repositories.item_repo import ItemRepository
from services.item_service import ItemService
from domain.exceptions import NotFoundException

router = APIRouter(prefix="/v1")

def get_item_service(db: Session = Depends(get_db)) -> ItemService:
    repo = ItemRepository(db)
    return ItemService(repo)

@router.get("/items")
def read_items(service: ItemService = Depends(get_item_service)):
    return service.get_items()

@router.get("/items/{item_id}")
def read_item(item_id: int, service: ItemService = Depends(get_item_service)):
    try:
        return service.get_item(item_id)
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.detail)

@router.post("/items")
def create_item(name: str, description: str | None = None, service: ItemService = Depends(get_item_service)):
    return service.create_item(name, description)
