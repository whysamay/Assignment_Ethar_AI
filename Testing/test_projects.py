import pytest
from fastapi.testclient import TestClient
from test_auth import Test_user_1

Test_admin = {
    "email": "admin@example.com",
    "phone_number": "123456",
    "password": "password",
    "role": "admin"
}

def get_auth_headers(client: TestClient, user_data: dict):
    # Attempting register first
    client.post("/auth/register", json=user_data)
    # logging in
    response = client.post("/auth/token", data={
        "username": user_data["email"],
        "password": user_data["password"]
    })
    token = response.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}

def test_admin_create_project(client: TestClient):
    headers = get_auth_headers(client, Test_admin)
    payload = {"title": "Admin Project", "description": "This is a test project."}
    response = client.post("/projects/", json=payload, headers=headers)
    
    assert response.status_code == 201
    assert response.json()["title"] == "Admin Project"

def test_member_cannot_create_project(client: TestClient):
    headers = get_auth_headers(client, Test_user_1)
    payload = {"title": "Member Project", "description": "Members cannot create projects."}
    response = client.post("/projects/", json=payload, headers=headers)
    
    # Should be forbidden by our require_admin dependency
    assert response.status_code == 403

def test_list_projects(client: TestClient):
    headers = get_auth_headers(client, Test_user_1)
    response = client.get("/projects/", headers=headers)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
