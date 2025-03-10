from playwright.sync_api import sync_playwright
import pytest
import requests

# Test Data
VALID_USER = "testuser"
VALID_PASSWORD = "password123"
API_URL = "http://127.0.0.1:5000/predict"  # Flask API for ML Fraud Detection

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_login(browser):
    page = browser.new_page()
    page.goto("http://localhost:8000/login.html")  # Banking UI

    page.fill("#username", VALID_USER)
    page.fill("#password", VALID_PASSWORD)
    page.click("#login")

    assert "Welcome" in page.inner_text("#status")
    page.close()

def test_fund_transfer(browser):
    page = browser.new_page()
    page.goto("http://localhost:8000/transfer.html")

    page.fill("#amount", "500")
    page.fill("#recipient", "JohnDoe")
    page.click("#transfer")

    assert "Transfer Successful" in page.inner_text("#status")
    page.close()

def test_fraud_detection(browser):
    page = browser.new_page()
    page.goto("http://localhost:8000/transfer.html")

    transaction_amount = 20000  # Example high-risk amount

    # Call ML API to check fraud status
    response = requests.post(API_URL, json={"amount": transaction_amount})
    fraud_result = response.json()["is_fraud"]

    page.fill("#amount", str(transaction_amount))
    page.fill("#recipient", "UnknownUser")
    page.click("#transfer")

    if fraud_result == 1:
        assert "Transaction Blocked! Fraud Alert!" in page.inner_text("#status")
    else:
        assert "Transfer Successful" in page.inner_text("#status")

    page.close()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
