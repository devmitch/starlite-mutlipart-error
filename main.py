from logging import getLogger
from pydantic import BaseConfig, BaseModel, constr
import uvicorn
from starlite import Body, RequestEncodingType, Starlite, UploadFile, post
from typing import List, Optional

logger = getLogger(__name__)


def after_exception_handler(exc: Exception, _, __) -> None:
    logger.error("help", exc_info=exc)


class ModelA(BaseModel):
    first: str
    last: str


class ModelB(BaseModel):
    file: Optional[UploadFile]

    class Config(BaseConfig):
        arbitrary_types_allowed: bool = True


@post("/")
async def test_route(data: Optional[ModelA] = Body(media_type=RequestEncodingType.MULTI_PART)) ->\
        None:
    pass


app = Starlite(route_handlers=[test_route], after_exception=after_exception_handler)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
