import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from flask import Flask, request, jsonify

# Generate Dummy Banking Data
np.random.seed(42)
data = pd.DataFrame({
    "amount": np.random.randint(100, 50000, 500),  # Transaction Amount
    "is_fraud": np.random.choice([0, 1], 500, p=[0.95, 0.05])  # 5% fraud cases
})

# Train ML Model
X = data[["amount"]]
y = data["is_fraud"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "fraud_model.pkl")

# Flask API to Serve the Model
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    request_data = request.get_json()
    amount = request_data["amount"]
    model = joblib.load("fraud_model.pkl")
    prediction = model.predict([[amount]])[0]
    return jsonify({"is_fraud": int(prediction)})

if __name__ == "__main__":
    app.run(port=5000)
