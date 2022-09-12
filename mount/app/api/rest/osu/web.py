from fastapi import APIRouter
from fastapi import Request

router = APIRouter()


# @router.get("/web/{rest_of_path:path}")
# @router.post("/web/{rest_of_path:path}")
# async def web(request: Request, rest_of_path: str):
#     print("Caught ", rest_of_path)
#     print(await request.body())
#     return ""
