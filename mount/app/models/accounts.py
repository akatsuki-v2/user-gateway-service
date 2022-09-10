from __future__ import annotations

from datetime import datetime
from uuid import UUID

from . import BaseModel
from . import Status


class BaseAccount(BaseModel):
    account_id: UUID
    username: str
    safe_username: str
    email_address: str
    country: str  # iso-3166-1 alpha-2


class Account(BaseAccount):
    rec_id: int
    status: Status
    created_at: datetime
    updated_at: datetime


class AccountInput(BaseAccount):
    password: str


class AccountUpdate(BaseModel):
    username: str | None
    email_address: str | None
    country: str | None  # iso-3166-1 alpha-2
