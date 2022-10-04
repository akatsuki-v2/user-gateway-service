from uuid import UUID

from app.api.rest.context import RequestContext
from app.api.rest.gateway import forward_request
from app.api.rest.responses import Success
from app.common import settings
from app.models.queued_packets import EnqueuePacket
from app.models.queued_packets import QueuedPacket
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()

SERVICE_URL = "http://users-service"


# https://osuakatsuki.atlassian.net/browse/V2-10
@router.post("/v1/sessions/{session_id}/queued-packets", response_model=Success[QueuedPacket])
async def enqueue(session_id: UUID, args: EnqueuePacket, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="POST",
                                     url=f"{SERVICE_URL}/v1/sessions/{session_id}/queued-packets",
                                     json=args.dict())
    return response


# https://osuakatsuki.atlassian.net/browse/V2-58
@router.get("/v1/sessions/self/queued-packets", response_model=Success[list[QueuedPacket]])
async def dequeue_all(session_id: UUID, ctx: RequestContext = Depends()):
    response = await forward_request(ctx,
                                     method="GET",
                                     url=f"{SERVICE_URL}/v1/sessions/{session_id}/queued-packets")
    return response
