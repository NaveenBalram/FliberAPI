
def test_root(test_app):

    response = test_app.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
