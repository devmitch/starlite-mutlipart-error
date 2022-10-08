"""Minimal Starlite application."""
from logging import getLogger
from typing import Any
from starlite import Body, RequestEncodingType, Starlite, UploadFile, post
from starlite.testing import TestClient


logger = getLogger(__name__)


def after_exception_handler(exc: Exception, scope, state) -> None:
    logger.error("help", exc_info=exc)
    print(scope, state)


@post("/")
async def hello_world(
    data: UploadFile = Body(media_type=RequestEncodingType.MULTI_PART),
) -> dict[str, Any]:
    form_data = await data.read()
    print(len(form_data))
    return {"hello": "world"}


app = Starlite(route_handlers=[hello_world], after_exception=after_exception_handler)

if __name__ == "main":
    with open("flower.jpg", "rb") as f:
        data = f.read()

    with TestClient(app=app) as client:
        resp = client.post("/", files={"data": data})
        print(resp.headers)
