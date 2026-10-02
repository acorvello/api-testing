import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """URL base da API do Juice Shop.

    Pode ser sobrescrita pela variável de ambiente BASE_URL — por padrão
    aponta para a porta exposta localmente pelo docker-test-env.
    """
    return os.environ.get("BASE_URL", "http://localhost:3001")
