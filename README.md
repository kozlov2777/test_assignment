# Test Automation Framework

Automated framework for UI and API testing using Python, Selenium, Requests, and Allure.

## Features

- UI tests with Selenium WebDriver
- API tests using httpx
- API response validation with Pydantic
- Allure report generation
- Docker container execution
- CI/CD integration with GitHub Actions

## Requirements

For running with Docker (recommended):
- Docker
- Docker Compose

For local execution without Docker:
- Python 3.11+
- Poetry
- Chrome browser
- Allure CLI (optional, for report generation)

## Running Tests

### Local execution with Docker (recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/test_assignment.git
   cd test_assignment
   ```

2. Run tests with Docker Compose:
   ```bash
   docker-compose up tests
   ```

3. For running tests and viewing Allure reports:
   ```bash
   docker-compose up
   ```
   
   After execution, open in your browser: http://localhost:5050

### Local execution without Docker

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run all tests:
   ```bash
   poetry run pytest
   ```

3. Run only API tests:
   ```bash
   poetry run pytest test/test_api
   ```

4. Run only UI tests:
   ```bash
   poetry run pytest test/test_ui
   ```

5. Run with Allure report generation:
   ```bash
   poetry run pytest --alluredir=./allure-results
   allure serve ./allure-results
   ```

### Running through GitHub Actions (CI/CD)

Tests are automatically run on each push to the repository via GitHub Actions.

To view results:
1. Go to the "Actions" tab in the GitHub repository
2. Select the latest workflow run
3. In the "Artifacts" section, download "allure-report" for local viewing
4. Or visit the project's GitHub Pages if you are working with the main/master branch: https://your-username.github.io/test_assignment/

## Project Structure

```
├── framework/           # Testing framework
│   ├── api/             # API testing components
│   │   ├── client/      # HTTP clients
│   │   └── models/      # Pydantic models
│   └── ui/              # UI testing components
│       ├── locators/    # Element selectors
│       └── pages/       # Page Objects
├── test/                # Tests
│   ├── test_api/        # API tests
│   └── test_ui/         # UI tests
│       └── fixtures/    # Pytest fixtures
├── .github/workflows/   # GitHub Actions configuration
├── allure-results/      # Test results for Allure
├── Dockerfile           # Image for running tests
├── docker-compose.yml   # Docker Compose configuration
├── pyproject.toml       # Dependencies and Poetry configuration
└── pytest.ini           # Pytest configuration
```