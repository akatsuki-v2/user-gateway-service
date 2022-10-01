from __future__ import annotations

from fastapi import APIRouter

from . import accounts
from . import chat_members
from . import chats
from . import clans
from . import sessions
from . import stats

router = APIRouter()

router.include_router(accounts.router, tags=["accounts"])
router.include_router(chat_members.router, tags=["chat members"])
router.include_router(chats.router, tags=["chats"])
router.include_router(clans.router, tags=["clans"])
router.include_router(sessions.router, tags=["sessions"])
router.include_router(stats.router, tags=["stats"])
