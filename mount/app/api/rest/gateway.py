from typing import Any
from typing import Literal
from typing import Mapping

from app.common.context import Context
from app.common.json import preprocess_json
from fastapi import Response
from httpx._types import CookieTypes
from httpx._types import HeaderTypes
from httpx._types import QueryParamTypes
from httpx._types import RequestContent
from httpx._types import RequestData
from httpx._types import RequestFiles
from httpx._types import URLTypes
MethodTypes = Literal["POST", "PUT", "PATCH",
                      "GET", "HEAD", "DELETE", "OPTIONS"]


# TODO: read & implement things from
# https://www.python-httpx.org/advanced

async def forward_request(ctx: Context,
                          method: MethodTypes,
                          url: URLTypes,
                          content: RequestContent | None = None,
                          data: RequestData | None = None,
                          files: RequestFiles | None = None,
                          json: Any | None = None,
                          params: QueryParamTypes | None = None,
                          headers: HeaderTypes | None = None,
                          cookies: CookieTypes | None = None,
                          ) -> Response:
    if json is not None:
        json = preprocess_json(json)

    response = await ctx.http_client.request(method=method,
                                             content=content,
                                             data=data,
                                             url=url,
                                             files=files,
                                             json=json,
                                             params=params,
                                             headers=headers,
                                             cookies=cookies)

    return Response(content=response.content,
                    status_code=response.status_code,
                    headers=response.headers)
