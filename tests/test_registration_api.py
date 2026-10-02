import random
import string

import requests


def _random_email() -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"qa.test.{suffix}@example.com"


def test_register_new_user_and_login(base_url):
    questions_response = requests.get(f"{base_url}/api/SecurityQuestions")
    assert questions_response.status_code == 200
    question_id = questions_response.json()["data"][0]["id"]

    email = _random_email()
    password = "Teste@12345"

    register_response = requests.post(
        f"{base_url}/api/Users/",
        json={
            "email": email,
            "password": password,
            "passwordRepeat": password,
            "securityQuestion": {"id": question_id},
            "securityAnswer": "resposta de teste",
        },
    )
    assert register_response.status_code == 201

    login_response = requests.post(
        f"{base_url}/rest/user/login",
        json={"email": email, "password": password},
    )
    assert login_response.status_code == 200
    assert login_response.json()["authentication"]["token"]


def test_register_with_mismatched_passwords_is_accepted_by_api(base_url):
    # Achado de teste: a confirmação de senha (passwordRepeat) só é
    # validada no frontend do Juice Shop. A API aceita o cadastro mesmo
    # com senhas diferentes — este teste documenta esse comportamento
    # real, em vez de assumir uma validação que a API não implementa.
    email = _random_email()

    response = requests.post(
        f"{base_url}/api/Users/",
        json={
            "email": email,
            "password": "Teste@12345",
            "passwordRepeat": "SenhaDiferente123",
        },
    )

    assert response.status_code == 201


def test_register_with_duplicate_email_fails(base_url):
    email = _random_email()
    password = "Teste@12345"
    payload = {
        "email": email,
        "password": password,
        "passwordRepeat": password,
    }

    first_attempt = requests.post(f"{base_url}/api/Users/", json=payload)
    assert first_attempt.status_code == 201

    second_attempt = requests.post(f"{base_url}/api/Users/", json=payload)
    assert second_attempt.status_code != 201
