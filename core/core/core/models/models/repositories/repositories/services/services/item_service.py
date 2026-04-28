from repositories.item_repo import ItemRepository
from domain.exceptions import NotFoundException

class ItemService:
    def __init__(self, item_repo: ItemRepository):
        self.item_repo = item_repo

    def get_items(self):
        return self.item_repo.get_items()

    def get_item(self, item_id: int):
        item = self.item_repo.get_item(item_id)
        if not item:
            raise NotFoundException(detail="Item not found")
        return item

    def create_item(self, name: str, description: str | None = None):
        if not name:
            raise ValueError("Name is required")
        return self.item_repo.create_item(name, description)
