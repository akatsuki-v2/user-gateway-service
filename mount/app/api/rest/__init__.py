from __future__ import annotations

import time

from app.services import http_client
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from shared_modules import logger


def init_http_client(api: FastAPI) -> None:
    @api.on_event("startup")
    async def startup_http_client() -> None:
        logger.info("Starting up HTTP client")
        service_http_client = http_client.ServiceHTTPClient()
        api.state.http_client = service_http_client
        logger.info("HTTP client started up")

    @api.on_event("shutdown")
    async def shutdown_http_client() -> None:
        logger.info("Shutting down HTTP client")
        await api.state.http_client.aclose()
        del api.state.http_client
        logger.info("HTTP client shut down")


def init_middlewares(api: FastAPI) -> None:
    # NOTE: these run bottom to top

    @api.middleware("http")
    async def add_http_client_to_request(request: Request, call_next):
        request.state.http_client = request.app.state.http_client
        response = await call_next(request)
        return response

    @api.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.perf_counter_ns()
        response = await call_next(request)
        process_time = (time.perf_counter_ns() - start_time) / 1e6
        response.headers["X-Process-Time"] = str(process_time)  # ms
        return response

    origins = [
        "https://frontend-service-two.vercel.app",
        "http://localhost:3000",
    ]

    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routes(api: FastAPI) -> None:
    from .v1 import router as v1_router

    api.include_router(v1_router)

    # TODO: clean up this sacrilege
    from .osu import bancho
    from .osu.web import router as osu_web_router
    for subdomain in ("c", "ce", "c4"):
        api.host(f"{subdomain}.cmyui.xyz", bancho.router)
    api.host("osu.cmyui.xyz", osu_web_router)


def init_api():
    api = FastAPI()

    init_http_client(api)
    init_middlewares(api)
    init_routes(api)

    return api
