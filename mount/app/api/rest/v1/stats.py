from app.api.rest.context import RequestContext
from app.api.rest.gateway import authentication
from app.api.rest.gateway import forward_request
from app.api.rest.responses import Success
from app.models.sessions import Session
from app.models.stats import Stats
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://users-service"


# https://osuakatsuki.atlassian.net/browse/V2-78
@router.get("/v1/accounts/self/stats", response_model=Success[list[Stats]])
async def get_self_stats(session: Session = Depends(authentication),
                         ctx: RequestContext = Depends()):
    account_id = session.account_id
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/accounts/{account_id}/stats")
    return response


# https://osuakatsuki.atlassian.net/browse/V2-78
@router.get("/v1/accounts/{account_id}/stats", response_model=Success[list[Stats]])
async def get_stats(account_id: int,
                    ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/accounts/{account_id}/stats")
    return response
