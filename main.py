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
    first: Optional[str]
    last: str


@post("/modelA")
async def test_modelA(data: ModelA = Body(media_type=RequestEncodingType.MULTI_PART)) ->\
        None:
    print("Passed validation for ModelA")


@post("/optional_modelA")
async def test_optional_modelA(data: Optional[ModelA] = Body(
    media_type=RequestEncodingType.MULTI_PART)) -> None:
    print("Passed validation for Optional ModelA")


@post("/modelB")
async def test_modelB(data: ModelB = Body(media_type=RequestEncodingType.MULTI_PART)) ->\
        None:
    print("Passed validation for ModelB")


@post("/optional_modelB")
async def test_optional_modelB(data: Optional[ModelB] = Body(
    media_type=RequestEncodingType.MULTI_PART)) ->\
        None:
    print("Passed validation for Optional ModelB")


app = Starlite(route_handlers=[test_modelA, test_optional_modelA, test_modelB, test_optional_modelB],
               after_exception=after_exception_handler)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
