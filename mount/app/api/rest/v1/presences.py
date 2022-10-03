from app.api.rest.context import RequestContext
from app.api.rest.gateway import authentication
from app.api.rest.gateway import forward_request
from app.api.rest.responses import Success
from app.models.presences import Presence
from app.models.presences import PresenceInput
from app.models.presences import PresenceUpdate
from app.models.sessions import Session
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://users-service"


# https://osuakatsuki.atlassian.net/browse/V2-115
@router.post("/v1/presences", response_model=Success[Presence])
async def create_presence(args: PresenceInput,
                          session: Session = Depends(authentication),
                          ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="POST",
                                     url=f"{SERVICE_URL}/v1/presences",
                                     json=args.dict())
    return response


# https://osuakatsuki.atlassian.net/browse/V2-116
@router.get("/v1/presences/self", response_model=Success[Presence])
async def get_self_presence(session: Session = Depends(authentication),
                            ctx: RequestContext = Depends()):
    session_id = session.session_id
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/presences/{session_id}")
    return response


# https://osuakatsuki.atlassian.net/browse/V2-116
@router.get("/v1/presences", response_model=Success[list[Presence]])
async def get_presences(session: Session = Depends(authentication),
                        ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/presences")
    return response


# https://osuakatsuki.atlassian.net/browse/V2-117
@router.patch("/v1/presences/self", response_model=Success[Presence])
async def partial_update_presence(args: PresenceUpdate,
                                  session: Session = Depends(authentication),
                                  ctx: RequestContext = Depends()):
    session_id = session.session_id
    response = await forward_request(ctx,
                                     method="PATCH",
                                     url=f"{SERVICE_URL}/v1/presences/{session_id}",
                                     json=args.dict())
    return response


# @router.delete("/v1/presences/self", response_model=Success[Presence])
# async def delete_presence(session: Session = Depends(authentication),
#                           ctx: RequestContext = Depends()):
#     session_id = session.session_id
#     response = await forward_request(ctx,
#                                      method="DELETE",
#                                      url=f"{SERVICE_URL}/v1/presences/{session_id}")
#     return response
