# 🧪 Playwright + Pytest Automation Framework (OrangeHRM)

## 📌 Overview

This project is a **UI automation testing framework** built using **Playwright with Pytest** for the OrangeHRM demo application.

It demonstrates how to design a **scalable, maintainable, and industry-level test automation framework** using:

* Page Object Model (POM)
* Pytest fixtures
* Storage state (session reuse)
* HTML reporting

---
## Test Result
<img width="1900" height="912" alt="Test_Result" src="https://github.com/user-attachments/assets/440ce2d1-2d18-4d31-8dcf-5afb5fc65fc3" />

---

## 🚀 What This Project Covers

### ✅ UI Automation

* Automated end-to-end user flows
* Login, Dashboard, Claims, and Logout validation
* Assertions using Playwright’s `expect`

### ✅ Framework Design

* Clean folder structure
* Separation of concerns (tests vs pages vs config)
* Reusable components

### ✅ Session Management (Advanced)

* Implemented **storage_state (auth.json)**
* Avoids repeated login for every test
* Improves test speed and efficiency

### ✅ Pytest Features

* Fixtures (`page`, `context`)
* Markers (`smoke`, `claim`)
* Test isolation
* Command-line execution

### ✅ Reporting

* HTML reports using `pytest-html`
* Clear pass/fail visibility

---

## 🧱 Project Structure

```
Playwright-automation/
│
├── pages/                 # Page Object Model (POM)
│   ├── claims.py
│
├── tests/                 # Test cases
│   ├── test_login_page.py
│   ├── test_claim.py
│   ├── test_logout.py
│               
└── auth.json    # Stored session state
│
├── conftest.py            # Pytest fixtures (browser, page setup)
├── pytest.ini             # Pytest configuration & markers
├── create_auth_state.py   # Script to generate auth.json
└── reports/               # HTML reports
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd Playwright-automation
```

### 2. Install dependencies

```
pip install -r requirements.txt
playwright install
```

### 3. Generate login session (IMPORTANT)

```
python create_auth_state.py
```

This creates `auth.json` which stores logged-in session.

---

## ▶️ Running Tests

### Run all tests

```
pytest
```

### Run specific tests using markers

```
pytest -m smoke
pytest -m claim
```

### Run with HTML report

```
pytest --html=reports/report.html --self-contained-html
```

---

## 🧠 Key Learnings

* How to build a **real-world automation framework from scratch**
* Difference between **fresh login tests vs session-based tests**
* Proper use of **fixtures and scopes in Pytest**
* Handling **locators and strict mode in Playwright**
* Importance of **test independence and stability**
* Structuring tests using **Page Object Model (POM)**

---

## ⚠️ Challenges Faced

* Managing session vs fresh login tests
* Handling multiple locators (strict mode issues)
* Fixing flaky tests due to shared state
* Proper fixture design (`context` vs `page`)

---

## 🔥 Future Improvements

* Add API testing integration
* CI/CD integration (Jenkins/GitHub Actions)
* Parallel test execution
* Environment configuration (dev/staging/prod)
* Logging & screenshot capture on failure

---

## 🧑‍💻 Tech Stack

* Python
* Pytest
* Playwright
* pytest-html

---

## 💬 Summary

This project reflects **practical SDET-level skills**, focusing on:

* Automation framework design
* Clean code practices
* Real-world testing scenarios

---

## 📞 Author

**Gurpreet Singh**
Aspiring SDET | QA Automation Engineer
