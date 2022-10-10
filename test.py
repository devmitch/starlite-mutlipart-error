import httpx, json

with httpx.Client() as client:
    # ModelA
    response = client.post("http://127.0.0.1:5000/modelA", data={"first": "hi", "last": "hello"})
    if not response.is_success:
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)

    # optional ModelA
    response = client.post("http://127.0.0.1:5000/optional_modelA")
    if not response.is_success:
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)

    # ModelB
    response = client.post("http://127.0.0.1:5000/modelB", data={"last": "hello"})
    if not response.is_success:
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)

    # optional ModelB
    response = client.post("http://127.0.0.1:5000/optional_modelB")
    if not response.is_success:
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)

