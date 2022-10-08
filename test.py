import httpx


with open("flower.jpg", "rb") as f, httpx.Client() as client:
    image = f.read()
    response = client.post("http://0.0.0.0:5000/", files={"data": image})
    print(response.status_code)
    print(response.json())
