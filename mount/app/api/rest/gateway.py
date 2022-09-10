from typing import Any
from typing import Literal
from typing import Mapping

import httpx
from app.common.context import Context
from app.common.json import preprocess_json
from fastapi import Response
from httpx._types import CookieTypes
from httpx._types import HeaderTypes
from httpx._types import RequestFiles
MethodTypes = Literal["POST", "PUT", "PATCH",
                      "GET", "HEAD", "DELETE", "OPTIONS"]


async def forward_request(ctx: Context,
                          method: MethodTypes,
                          url: str,
                          files: RequestFiles | None = None,
                          json: Any = None,
                          params: Mapping[str, Any] | None = None,
                          headers: HeaderTypes | None = None,
                          cookies: CookieTypes | None = None,
                          # TODO: files?
                          ) -> Any:
    if json is not None:
        json = preprocess_json(json)

    response = await ctx.http_client.request(method=method,
                                             url=url,
                                             files=files,
                                             json=json,
                                             params=params,
                                             headers=headers,
                                             cookies=cookies)

    return Response(content=response.content,
                    status_code=response.status_code,
                    headers=response.headers)
