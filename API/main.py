from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Initialize the FastAPI application
app = FastAPI(title="Customer Churn Prediction API")

# 2. Load the trained Logistic Regression model
# (This assumes you are running the server from your main project folder)
model = joblib.load('models/churn_model.pkl')

# 3. Define the expected input data structure
# Our model expects exactly 31 numerical features
class CustomerData(BaseModel):
    features: list[float]

# 4. Create a basic home endpoint to check if the API is running
@app.get("/")
def home():
    return {"message": "Welcome to the Telco Customer Churn API! The server is active."}

# 5. Create the prediction endpoint
@app.post("/predict")
def predict_churn(data: CustomerData):
    # Convert the incoming list of features into a 2D NumPy array
    input_array = np.array(data.features).reshape(1, -1)
    
    # Generate the prediction (0 or 1) and the probability percentages
    prediction = model.predict(input_array)
    probability = model.predict_proba(input_array)
    
    # Format the results
    result = "Churn" if prediction[0] == 1 else "No Churn"
    churn_risk = round(probability[0][1] * 100, 2)
    
    return {
        "prediction": result,
        "churn_risk_percentage": churn_risk
    }