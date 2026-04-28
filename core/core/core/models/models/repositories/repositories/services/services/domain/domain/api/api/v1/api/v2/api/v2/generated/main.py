from fastapi import FastAPI
from core.config import settings
from core.database import engine, Base
from api.v1.router_v1 import router as router_v1
from api.v2.router_v2 import router as router_v2

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
)

app.include_router(router_v1)
app.include_router(router_v2)
