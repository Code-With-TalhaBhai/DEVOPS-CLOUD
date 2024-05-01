from fastapi.testclient import TestClient
# from fastapi_poetry.main import app # acutal app object
from main import app

client = TestClient(app=app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greetings":"hello world"}

def test_hello():
    response = client.get("/hello/")
    assert response.json() == {"greetings":"Assalam u Alaikum from FASTAPI"}






