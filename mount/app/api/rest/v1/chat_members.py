from app.api.rest.context import RequestContext
from app.api.rest.gateway import authentication
from app.api.rest.gateway import forward_request
from app.api.rest.responses import Success
from app.models.chat_members import Member
from app.models.chat_members import MemberInput
from app.models.sessions import Session
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://chat-service"


# https://osuakatsuki.atlassian.net/browse/V2-86
@router.post("/v1/chats/{chat_id}/members", response_model=Success[Member])
async def join_chat(chat_id: int, args: MemberInput,
                    session: Session = Depends(authentication),
                    ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="POST",
                                     url=f"{SERVICE_URL}/v1/chats/{chat_id}/members",
                                     json=args.dict())
    return response


# https://osuakatsuki.atlassian.net/browse/V2-87
@router.delete("/v1/chats/{chat_id}/members", response_model=Success[Member])
async def leave_chat(chat_id: int,
                     session: Session = Depends(authentication),
                     ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="DELETE",
                                     url=f"{SERVICE_URL}/v1/chats/{chat_id}/members")
    return response


# https://osuakatsuki.atlassian.net/browse/V2-88
@router.get("/v1/chats/{chat_id}/members", response_model=Success[list[Member]])
async def get_chat_members(chat_id: int,
                           # TODO: should this not be authenticated?
                           session: Session = Depends(authentication),
                           ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/chats/{chat_id}/members")
    return response
