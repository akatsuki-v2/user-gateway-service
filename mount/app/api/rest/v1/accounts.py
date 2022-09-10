from app.api.rest.context import RequestContext
from app.api.rest.gateway import forward_request
from app.models.accounts import Account
from app.models.accounts import AccountInput
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://user-accounts-service"


# https://osuakatsuki.atlassian.net/browse/V2-10
@router.post("/v1/accounts", response_model=Account)
async def sign_up(args: AccountInput, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="POST",
                                     url=f"{SERVICE_URL}/v1/accounts",
                                     json=args.dict())
    return response
