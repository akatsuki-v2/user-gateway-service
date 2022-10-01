from app.api.rest.context import RequestContext
from app.api.rest.gateway import authentication
from app.api.rest.gateway import forward_request
from app.models.accounts import Account
from app.models.accounts import AccountUpdate
from app.models.accounts import SignupForm
from app.models.sessions import Session
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://users-service"


# https://osuakatsuki.atlassian.net/browse/V2-10
@router.post("/v1/accounts", response_model=Account)
async def sign_up(args: SignupForm, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="POST",
                                     url=f"{SERVICE_URL}/v1/accounts",
                                     json=args.dict())
    return response


# https://osuakatsuki.atlassian.net/browse/V2-58
@router.get("/v1/accounts/{account_id}", response_model=Account)
async def get_account(account_id: int, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/accounts/{account_id}")
    return response


# https://osuakatsuki.atlassian.net/browse/V2-59
@router.patch("/v1/accounts/self", response_model=Account)
async def partial_update_account(args: AccountUpdate,
                                 session: Session = Depends(authentication),
                                 ctx: RequestContext = Depends()):
    account_id = session.account_id
    response = await forward_request(ctx,
                                     method="PATCH",
                                     url=f"{SERVICE_URL}/v1/accounts/{account_id}",
                                     json=args.dict())
    return response
