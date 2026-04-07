# 🚀 Web Automation Test Suite

An end-to-end automated testing framework built using **Python, Selenium WebDriver, pytest, and FastAPI**.
This project enables automated UI testing and provides an API to trigger test execution programmatically.

---

## 📌 Features

* ✅ Automated web testing using Selenium
* ✅ Structured test cases with pytest
* ✅ API-based test execution using FastAPI
* ✅ Real-time test results (pass/fail)
* ✅ Scalable and reusable test architecture

---

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **pytest**
* **FastAPI**
* **Uvicorn**
* **Postman** (for API testing)

---

## 📂 Project Structure

```
web-automation-suite/
│
├── api_runner.py        # FastAPI server to trigger tests
├── test_login.py       # Test cases using pytest
├── login_page.py       # Page Object Model (Login page)
├── base_page.py        # Base methods for reusable actions
├── driver_setup.py     # WebDriver configuration
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/Neha-Sharma17/automation-test-suite.git
cd automation-test-suite
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate it:

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests using pytest:

```
pytest -v
```

---

## 🌐 Run API Server

```
python -m uvicorn api_runner:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔌 API Endpoint

### Run Test Suite

**POST** `/run-tests`

#### Response Example:

```
{
  "status": "passed",
  "summary": "1 passed in 9.75s"
}
```

---

## 🧪 Test Scenario Covered

* Login functionality validation
* Form input handling
* UI interaction testing

---

## 💡 Use Cases

* Automate regression testing
* Integrate with CI/CD pipelines
* Replace manual testing workflows
* Trigger tests remotely via API

---

## 🚀 Future Enhancements

* Add multiple test scenarios
* Integrate reporting dashboard
* CI/CD integration (GitHub Actions)
* Parallel test execution

---

## 👩‍💻 Author

**Neha Sharma**

---

## ⭐ Contribution

Feel free to fork this repository and enhance it further!
