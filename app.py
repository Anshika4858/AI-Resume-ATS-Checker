"""
FastAPI version of the ATS API.

Differences vs Flask (high level):
- FastAPI is built on ASGI (async-capable), while Flask is WSGI (sync-only).
- FastAPI uses Pydantic models for validation + typed schemas automatically.
- Swagger/OpenAPI docs are generated automatically at `/docs` and `/openapi.json`.
- Async endpoints + threadpool offloading helps keep the server responsive under load.
"""

from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from api import create_api_router
from api.db import init_db


def create_app() -> FastAPI:
    init_db()

    app = FastAPI(title="ATS Resume Checker API", version="1.0.0")
    app.include_router(create_api_router())

    # Serve the modern frontend (same paths as before)
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    @app.get("/")
    async def index():
        return RedirectResponse(url="/static/index.html")

    return app


app = create_app()