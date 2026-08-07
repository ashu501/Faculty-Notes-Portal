from app import app

def test_login():

    client = app.test_client()

    response = client.get("/login")

    assert response.status_code == 200