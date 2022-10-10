import httpx, json

with httpx.Client() as client:
    response = client.post("http://127.0.0.1:8000/")
    print(json.dumps(response.json(), indent=4))
