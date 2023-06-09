from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Tay"}
    
def test_post_read_main():
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Tay"}
