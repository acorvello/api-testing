# api-testing

API test suite built with **pytest + requests**, validating REST endpoints
of the [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), used
here as a target application for test automation practice.

## Stack

- Python
- pytest
- requests

## Project structure

```
api-testing/
├── requirements.txt
├── pytest.ini
└── tests/
    ├── conftest.py
    ├── test_products_api.py
    ├── test_login_api.py
    └── test_registration_api.py
```

## Covered scenarios

**Products**
- Listing products returns results
- Searching products by term
- Fetching a single product by id
- Fetching a non-existent product returns 404

**Login**
- Invalid credentials are rejected with 401
- Missing request body returns an error
- Error responses don't leak internal stack traces

**User registration**
- A newly registered user can log in immediately after
- Registration fails when password confirmation doesn't match
- Registration fails for a duplicate email

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
inside a lightweight Python container image, triggered by a Jenkins
pipeline alongside the Cypress and Playwright suites. See that project's
`docker-compose.yml` for the full setup.

## Next steps

- Add schema validation for response payloads
- Cover basket/cart endpoints
- Add authenticated requests using the token from the login endpoint
