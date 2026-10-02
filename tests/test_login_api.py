import requests


def test_login_with_invalid_credentials_returns_401(base_url):
    response = requests.post(
        f"{base_url}/rest/user/login",
        json={"email": "usuario_invalido@teste.com", "password": "senhaErrada123"},
    )

    assert response.status_code == 401


def test_login_without_body_returns_error(base_url):
    response = requests.post(f"{base_url}/rest/user/login", json={})

    assert response.status_code in (400, 401)


def test_login_response_does_not_leak_stack_trace(base_url):
    response = requests.post(
        f"{base_url}/rest/user/login",
        json={"email": "usuario_invalido@teste.com", "password": "senhaErrada123"},
    )

    # Mesmo em caso de erro, a API não deve expor detalhes internos
    # (stack trace, caminho de arquivo) na resposta ao cliente.
    assert "at " not in response.text
    assert ".js:" not in response.text
