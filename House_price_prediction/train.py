# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("house_data.csv")

# Input (Area) and Output (Price)
X = data[["area"]]
y = data["price"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Test model
test_area = [[1500]]
predicted_price = model.predict(test_area)

print("Predicted Price:", predicted_price[0])

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")