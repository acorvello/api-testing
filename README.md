# 🧪 Automated REST API Testing Framework
### High-Coverage Component & Contract Validation Built with Python and Pytest

This repository hosts a production-grade automated API testing suite designed to validate the robust RESTful services of the **OWASP Juice Shop** application. The architecture is engineered to test authentication, product catalogs, and user lifecycle workflows under isolation, serving as a clean data generator for continuous quality telemetry.

## 💡 Engineering Highlights
* **Advanced Fixturing:** Leveraging `pytest` dependency injection via optimized scopes to manage authentication tokens securely, avoiding redundant state instantiation.
* **Contract and Schema Validation:** Verification of HTTP status codes, error response integrity, and prevention of internal stack trace leakage.
* **CI/CD Integration:** Engineered natively to run inside a headless Docker container orchestrated by a global Jenkins Pipeline, merging output logs seamlessly into unified JUnit reports.

## 🛠️ Tech Stack & Dependencies
- **Core Language:** Python 3.10+
- **Test Runner:** `pytest` (Headless automation, filtering, and structural hooks)
- **HTTP Client:** `requests` (Session management and connection pooling)

## 📁 Project Structure
api-testing/
├── requirements.txt
├── pytest.ini
└── tests/
├── conftest.py
├── test_products_api.py
├── test_login_api.py
└── test_registration_api.py

## 🔍 Covered Scenarios

**Products**
- Listing products returns valid response payloads
- Searching products by structural term filters
- Fetching a single product component by ID
- Boundary validation: Fetching a non-existent product returns a clean 404

**Login**
- Security Validation: Invalid credentials are rejected with a strict 401
- Missing request body payload returns handled exceptions
- Error handling verification: Responses do not leak internal stack traces

**User Registration**
- Lifecycle validation: A newly registered user can log in immediately after
- Validation failure when password confirmation doesn't match
- Data integrity check: Registration fails for a duplicate email entry

## 🚀 Running Locally

**Prerequisite:** Python 3.10+ and a running instance of Juice Shop (locally or in a container).

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

BASE_URL=http://localhost:3001 pytest
```

## 🐳 Running via Docker (CI/CD Orchestration)

This repository is actively consumed by the [docker-test-env](https://github.com) orchestration project. It spins up Juice Shop and runs this suite inside a lightweight Python container image, triggered by a **Jenkins pipeline** alongside the Cypress and Playwright suites. See that project's `docker-compose.yml` for the full architecture setup.

## 📈 Roadmap & Next Steps
- Implement rigid JSON Schema validation for response payloads
- Expand coverage into basket, cart, and checkout endpoints
- Inject authenticated requests utilizing automated token recycling from the login endpoint

## ⚖️ License
This repository is licensed under the **MIT License**. Feel free to clone, study, modify, and distribute the code for educational or portfolio purposes.

---
<sub>Keywords: API Testing, Python, Pytest, REST API, JSON Validation, Contract Testing, Docker, Jenkins CI/CD, Automated QA, Software Engineering, Telemetry, Data Integrity.</sub>

