# api-testing

API test suite built with **Python + pytest + requests**, validating REST
endpoints of the [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/),
used here as a target application for test automation practice.

## Stack

- Python
- pytest
- requests

## Project structure

```
api-testing/
├── requirements.txt
├── pytest.ini
├── conftest.py
└── tests/
    ├── test_products_api.py
    └── test_user_api.py
```

## Running locally

Prerequisite: Python 3.10+ and a running instance of Juice Shop (locally
or in a container).

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

BASE_URL=http://localhost:3001 pytest
```

## Running via Docker (no local Python install required)

This repository is consumed by the
[docker-test-env](https://github.com/acorvello/docker-test-env)
orchestration project, which spins up Juice Shop and runs this suite
inside a lightweight Python container, triggered by a Jenkins pipeline.
See that project's `docker-compose.yml` for the full setup.

## Covered scenarios

- Product listing returns data with the expected fields
- Product search returns matching results, and an empty list for
  non-matching queries
- New user registration succeeds and returns the created user
- A newly registered user can log in and receives an auth token
- Login with invalid credentials returns `401`
- Registration with mismatched passwords is rejected

## Next steps

- Cover basket/cart endpoints (add item, view basket, checkout)
- Add schema validation (e.g. with `jsonschema` or `pydantic`)
- Negative tests for malformed payloads and injection attempts
