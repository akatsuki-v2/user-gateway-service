from __future__ import annotations

from fastapi import APIRouter

from . import accounts
from . import chats
from . import sessions

router = APIRouter()

router.include_router(accounts.router, tags=["accounts"])
router.include_router(chats.router, tags=["chats"])
router.include_router(sessions.router, tags=["sessions"])
