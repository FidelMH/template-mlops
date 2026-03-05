def test_post_data(client):
    response = client.post("/data", json={"name": "Alice", "age": 30, "score": 100})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    
def test_get_data(client_with_data):
    response = client_with_data.get("/data")
    assert response.status_code == 200
    assert len(response.json()) > 0