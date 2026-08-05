from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using Linear Regression",
    version="1.0"
)

model = joblib.load("model.pkl")

class House(BaseModel):
    area: float

@app.get("/")
def home():
    return {
        "message": "Welcome to House Price Prediction API"
    }

@app.post("/predict")
def predict(data: House):
    prediction = model.predict([[data.area]])

    return {
        "area": data.area,
        "predicted_price": round(float(prediction[0]), 2)
    }