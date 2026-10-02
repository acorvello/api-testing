import uuid


def _unique_email() -> str:
    return f"qa_{uuid.uuid4().hex[:10]}@example.com"


def test_register_new_user_returns_201(api_client):
    email = _unique_email()
    password = "SenhaForte123!"

    response = api_client.post(
        "/api/Users",
        json={"email": email, "password": password, "passwordRepeat": password},
    )

    assert response.status_code == 201
    assert response.json()["data"]["email"] == email


def test_login_with_newly_registered_user_returns_token(api_client):
    email = _unique_email()
    password = "SenhaForte123!"

    api_client.post(
        "/api/Users",
        json={"email": email, "password": password, "passwordRepeat": password},
    )

    response = api_client.post(
        "/rest/user/login", json={"email": email, "password": password}
    )

    assert response.status_code == 200
    body = response.json()
    assert "authentication" in body
    assert "token" in body["authentication"]


def test_login_with_invalid_credentials_returns_401(api_client):
    response = api_client.post(
        "/rest/user/login",
        json={"email": "nao-existe@example.com", "password": "senhaErrada"},
    )

    assert response.status_code == 401


def test_register_with_mismatched_passwords_returns_error(api_client):
    email = _unique_email()

    response = api_client.post(
        "/api/Users",
        json={
            "email": email,
            "password": "SenhaForte123!",
            "passwordRepeat": "SenhaDiferente456!",
        },
    )

    assert response.status_code >= 400
