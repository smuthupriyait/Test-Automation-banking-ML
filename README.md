# 🚀 Banking Fraud Detection & Playwright Automation  

This project integrates **Machine Learning (ML) for Fraud Detection** with **Playwright Automated Testing** to validate banking transactions.  

## Features  
-  **User Login & Fund Transfer Automation**  
-  **Fraud Detection using ML Model & API Testing**  
-  **Automated Test Execution via Playwright**  

---

## Project Overview  
This project consists of two main components:  
1**Fraud Detection Model**: A **Logistic Regression model** trained to identify fraudulent transactions.  
2**Automated Banking Tests**: Playwright tests that interact with a **mock banking UI** and validate fraud detection using the ML API.  

---

##  Tech Stack  
- **Python** (`Flask`, `scikit-learn`, `requests`, `Playwright`, `pytest`)  
- **Machine Learning** (`Logistic Regression`)  
- **Automation** (`Playwright`)  
- **Frontend** (Simple HTML for UI testing)  

---

## Installation & Setup  
### 1 Clone the Repository  
```bash
git clone https://github.com/your-username/banking-fraud-playwright.git
cd banking-fraud-playwright

**Install Dependencies**
pip install -r requirements.txt

**Start the Fraud Detection API**
python fraud_detection.py

** Run Playwright Tests**
pytest test_bank.py --html=report.html

How It Works
Fraud Detection API
Uses transaction amount as input.
Predicts whether the transaction is fraudulent.
Returns API response (is_fraud: 0 or 1).

Playwright Test Automation
Tests banking app UI for Login, Transfer & Fraud Detection.
Calls the ML API to validate fraudulent transactions.

Sample API Response (json)
Request:
{
  "amount": 20000
}
Response:
{
  "is_fraud": 1
}











