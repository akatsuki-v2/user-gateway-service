from uuid import UUID

from app.api.rest.context import RequestContext
from app.api.rest.gateway import forward_request
from app.models.sessions import LoginForm
from app.models.sessions import Session
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://users-service"


# https://osuakatsuki.atlassian.net/browse/V2-11
@router.post("/v1/sessions", response_model=Session)
async def log_in(args: LoginForm, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="POST",
                                     url=f"{SERVICE_URL}/v1/sessions",
                                     json=args.dict())
    return response


# https://osuakatsuki.atlassian.net/browse/V2-12
@router.patch("/v1/sessions/{session_id}")
async def partial_update_session(session_id: UUID, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="PATCH",
                                     url=f"{SERVICE_URL}/v1/sessions/{session_id}")
    return response


# https://osuakatsuki.atlassian.net/browse/V2-13
@router.delete("/v1/sessions/{session_id}")
async def log_out(session_id: UUID, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="DELETE",
                                     url=f"{SERVICE_URL}/v1/sessions/{session_id}")
    return response
