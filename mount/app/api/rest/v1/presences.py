from app.api.rest.context import RequestContext
from app.api.rest.gateway import authentication
from app.api.rest.gateway import forward_request
from app.api.rest.responses import Success
from app.models.presences import Presence
from app.models.sessions import Session
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://users-service"


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
