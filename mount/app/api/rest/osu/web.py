from app.api.rest.context import RequestContext
from app.api.rest.gateway import forward_request
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import Request

router = APIRouter()


SERVICE_URL = "http://bancho-service"


# @router.get("/web/{rest_of_path:path}")
# @router.post("/web/{rest_of_path:path}")
# async def web(request: Request, rest_of_path: str):
#     print("Caught ", rest_of_path)
#     print(await request.body())
#     return ""


@router.get("/web/osu-osz2-getscores.php")
async def osu_osz2_getscores(request: Request,
                             username: str = Query(..., alias="us"),
                             password: str = Query(..., alias="ha"),
                             ctx: RequestContext = Depends()):

    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/web/osu-osz2-getscores.php",
                                     content=await request.body(),
                                     params=request.query_params)

    return response
