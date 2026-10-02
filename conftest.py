import os

import pytest
import requests


class ApiClient:
    """Pequeno wrapper sobre requests.Session que já prefixa a base_url."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, path: str, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path: str, **kwargs):
        return self.session.post(f"{self.base_url}{path}", **kwargs)


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    base_url = os.environ.get("BASE_URL", "http://localhost:3001")
    return ApiClient(base_url)
