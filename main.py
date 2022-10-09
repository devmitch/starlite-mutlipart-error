from logging import getLogger

import uvicorn
from starlite import Body, RequestEncodingType, Starlite, UploadFile, post


logger = getLogger(__name__)


def after_exception_handler(exc: Exception, _, __) -> None:
    logger.error("help", exc_info=exc)


@post("/")
async def hello_world(
    data: UploadFile = Body(media_type=RequestEncodingType.MULTI_PART),
) -> dict:
    await data.read()
    return {"message": "ok"}


app = Starlite(route_handlers=[hello_world], after_exception=after_exception_handler)


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
