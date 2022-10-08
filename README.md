## Installation
Install poetry:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
```shell
poetry config virtualenvs.in-project true
```
```shell
poetry env use python3
poetry shell
poetry install
```
Run server:
```shell
poetry run python3 -m uvicorn main:app
```
To reproduce the error, in a separate python instance/interpreter run:
```
>>> with open("flower.jpg", "rb") as f:
...     data = f.read()
... 
>>> import httpx
>>> with httpx.Client() as client:
...     client.post("http://localhost:8000/", files={"data": data})
... 
<Response [500 Internal Server Error]>
```