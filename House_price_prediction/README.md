# 🏠 House Price Prediction using FastAPI

A Machine Learning project that predicts house prices based on the **area of the house**. The trained Machine Learning model is deployed as a **FastAPI REST API**, allowing users to send house area as input and receive a predicted house price.

## 🚀 Project Overview

This project demonstrates how a Machine Learning model can be trained, saved, and deployed using FastAPI.

The project includes:

* 📊 House price dataset
* 🤖 Machine Learning model
* 💾 Saved trained model
* ⚡ FastAPI REST API
* 🔮 House price prediction endpoint
* 📚 Interactive Swagger API documentation

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **FastAPI**
* **Uvicorn**
* **Pydantic**

## 📁 Project Structure

```text
house-price-prediction-fastapi/
│
├── main.py
├── model.pkl
├── house_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 🤖 Machine Learning Model

A **Linear Regression** model is used to predict house prices based on the area of the house.

### Input

The API accepts:

```text
Area of the house
```

### Output

The API returns:

```text
Predicted house price
```

## ⚡ FastAPI Endpoints

### 1. Home Endpoint

```http
GET /
```

Returns a welcome message.

Example response:

```json
{
  "message": "Welcome to House Price Prediction API"
}
```

### 2. Prediction Endpoint

```http
POST /predict
```

This endpoint accepts the house area and returns the predicted price.

Example request:

```json
{
  "area": 1500
}
```

Example response:

```json
{
  "predicted_price": 250000
}
```

> The predicted value shown above is only an example. The actual prediction depends on the trained model and dataset.

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI allows you to test the API directly from your browser.

## 💻 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/Rameesha fatima/house-price-prediction-fastapi.git
```

### Step 2: Open the project

```bash
cd house-price-prediction-fastapi
```

### Step 3: Create a virtual environment

Windows:

```bash
python -m venv venv
```

### Step 4: Activate the environment

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the FastAPI Server

Start the application using:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔄 How It Works

```text
House Area
    ↓
FastAPI Request
    ↓
Trained ML Model
    ↓
Price Prediction
    ↓
JSON Response
```

## 📌 Example

Send a request to:

```http
POST /predict
```

with:

```json
{
  "area": 2000
}
```

The trained Machine Learning model processes the area and returns the estimated house price.

## 🎯 Project Objectives

The main objectives of this project are:

* Learn Machine Learning model training
* Save and load a trained ML model
* Understand REST APIs
* Build an API using FastAPI
* Deploy a Machine Learning model through an API
* Test API endpoints using Swagger UI

## 🌟 Future Improvements

This project can be further improved by adding:

* Multiple house features such as bedrooms, bathrooms, location, etc.
* A web-based frontend
* Better Machine Learning models
* Model performance evaluation
* Docker deployment
* Cloud deployment
* Database integration

## 👩‍💻 Author

**Rameesha**

Machine Learning & Data Science Project

---

⭐ If you find this project useful, consider giving the repository a star!
