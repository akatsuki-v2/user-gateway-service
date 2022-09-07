from __future__ import annotations

from app.common import logging
from fastapi import FastAPI


def init_routes(api: FastAPI) -> None:
    from .v1 import router as v1_router

    api.include_router(v1_router, prefix="/v1")


def init_api():
    api = FastAPI()

    init_routes(api)

    return api
