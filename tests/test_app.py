from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Azure App Service via Github Actions, using Flask!" in response.data