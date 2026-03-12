# Python Selenium Login Test Framework

![Python](https://img.shields.io/badge/python-3.x-blue)
![Selenium](https://img.shields.io/badge/selenium-automation-green)
![PyTest](https://img.shields.io/badge/pytest-testing-orange)

A small UI automation framework built with **Python, Selenium WebDriver and PyTest** to validate the login functionality of the test site:

https://the-internet.herokuapp.com/login

This project was created as a practice exercise while learning **UI automation testing and framework design** using the Page Object Model pattern.

The goal was to build a simple but maintainable test structure that reflects how real automation frameworks are organized.

---

## Tech Stack

* Python
* Selenium WebDriver
* PyTest
* PyTest HTML Reports

---

## Test Scenarios Covered

The automation suite currently validates the following login scenarios:

* Successful login with valid credentials
* Login attempt with invalid username
* Login attempt with incorrect password
* Login attempt with empty credentials

Each test verifies the appropriate success or error message returned by the application.

---

## Project Structure

```
python-selenium-login-test-framework
│
├── config
│   └── config.py              # Environment configuration
│
├── pages
│   └── login_page.py          # Page Object for login page
│
├── tests
│   └── test_login.py          # Login test cases
│
├── utils
│   ├── wait_utils.py          # Explicit wait helper
│   └── logger.py              # Logging utility
│
├── logs                       # Execution logs
├── screenshots                # Failure screenshots
├── reports                    # HTML test reports
│
├── conftest.py                # PyTest fixtures and hooks
├── pytest.ini                 # PyTest configuration
└── requirements.txt           # Project dependencies
```

---

## Framework Features

* Page Object Model (POM) design pattern
* Explicit waits for stable UI interactions
* Config-driven environment setup
* PyTest fixtures for browser management
* Automatic screenshots on test failure
* HTML test reports
* Logging for test execution
* Clean and modular project structure

---

## Installation

Clone the repository:

```
git clone https://github.com/CypherMorgan/python-selenium-login-test-framework.git
```

Navigate into the project directory:

```
cd python-selenium-login-test-framework
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment.

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Tests

Run the test suite using PyTest:

```
pytest
```

Test execution results will appear in the terminal and an HTML report will be generated.

---

## Test Reports

After running tests, an HTML report will be generated in:

```
reports/report.html
```

Open this file in a browser to view the detailed test results.

---

## Screenshots on Failure

If a test fails, a screenshot is automatically captured and stored in:

```
screenshots/
```

This helps with debugging test failures and reviewing UI state at the time of failure.

---

## Logging

Execution logs are written to:

```
logs/test_run.log
```

Logs include key actions such as entering credentials, clicking login, and retrieving messages.

---

## Possible Improvements

Future enhancements could include:

* CI/CD integration with GitHub Actions
* Parallel test execution
* Support for multiple browsers
* Allure reporting
* Test data management
* Environment-based configurations

---

## Author

Automation framework created as part of QA automation practice while learning Selenium WebDriver and Python.
