from sqlalchemy.orm import Session
from models.item import Item

class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_items(self, skip: int = 0, limit: int = 10):
        return self.db.query(Item).offset(skip).limit(limit).all()

    def get_item(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def create_item(self, name: str, description: str | None = None):
        db_item = Item(name=name, description=description)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
