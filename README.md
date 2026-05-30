# Fleet Demo Automation Framework

## Overview

This project demonstrates a Playwright-based UI automation framework implemented with Python, Pytest, and Allure Reporting.

The framework was created as part of the Lead QA Automation Engineer assessment and focuses on maintainability, scalability, and clear separation of responsibilities.

## Framework Structure

```text
automation/
├── tests/
│   ├── test_auth.py
│   ├── test_dashboard.py
│   ├── test_vehicle_details.py
│   ├── test_report_generation.py
│   ├── test_report_defects.py
│   └── test_vehicle_defects.py
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── vehicle_page.py
│   └── report_page.py
├── fixtures/
│   ├── users.py
│   └── vehicles.py
├── utils/
│   └── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── DEFECTS.md
```

## Design Principles

* Page Object Model for UI abstraction
* Pytest fixtures for browser and session management
* Centralized test data
* Environment configuration through configuration files
* Allure reporting
* Separation of smoke and defect test suites

## Test Suites

### Smoke Suite

The smoke suite contains stable business-critical scenarios:

* Successful authentication
* Authentication validation
* Dashboard filtering
* Vehicle details navigation
* Report generation

Run smoke tests:

pytest -m smoke

### Defect Suite

The defect suite contains automated reproductions of known product defects.

Run defect tests:

pytest -m defect


## Running the Application

Start the demo application:

npm run serve


Application URL:

http://localhost:3000


Credentials:

admin / admin123

## Running Tests

Run all tests:

pytest


Run smoke tests only:

pytest -m smoke


Run defect tests only:

pytest -m defect


## Allure Reporting

Generate smoke report:

pytest -m smoke --alluredir=allure-results/smoke
allure generate allure-results/smoke -o allure-report/smoke --clean
allure open allure-report/smoke


Generate defect report:

pytest -m defect --alluredir=allure-results/defects || true
allure generate allure-results/defects -o allure-report/defects --clean
allure open allure-report/defects

## Known Defects

During the assessment, two product defects were identified and automated separately from the smoke suite:

- DEF-001: Invalid report date range validation
- DEF-002: Driver removal without confirmation

Defects details can be found in DEFECTS.md file.

## Future Improvements

* API test layer
* CI/CD integration with GitLab
* Parallel execution
* Cross-browser execution
* Test data factories
* Visual regression testing
* Automatic defect reporting
