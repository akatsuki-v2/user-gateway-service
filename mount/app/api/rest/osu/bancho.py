from app.api.rest.context import RequestContext
from app.api.rest.gateway import forward_request
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Header
from fastapi import Request

router = APIRouter()


SERVICE_URL = "http://bancho-service"


@router.post("/")
async def bancho(request: Request,
                 osu_token: str | None = Header(None),
                 ctx: RequestContext = Depends()):
    if osu_token is None:
        # this is a login request from the osu! client
        response = await forward_request(ctx,
                                         method="POST",
                                         url=f"{SERVICE_URL}/v1/login",
                                         content=await request.body())
    else:
        # this is a bancho request from the osu! client
        response = await forward_request(ctx,
                                         method="POST",
                                         url=f"{SERVICE_URL}/v1/bancho",
                                         headers={"osu-token": osu_token},
                                         content=await request.body())

    return response
