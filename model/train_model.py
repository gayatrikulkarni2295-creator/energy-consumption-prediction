import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("../dataset/energy_data.csv")

# Features
X = data[["temperature", "humidity", "machine_load", "working_hours"]]

# Target
y = data["energy_consumption"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Error
error = mean_absolute_error(y_test, predictions)

print("Model trained successfully")
print("Mean Absolute Error:", error)

# Example prediction
sample = [[34, 63, 58, 8]]
prediction = model.predict(sample)

print("Predicted Energy Consumption:", prediction[0])

# Visualization
plt.scatter(y_test, predictions)
plt.xlabel("Actual Energy")
plt.ylabel("Predicted Energy")
plt.title("Actual vs Predicted Energy Consumption")
plt.show()
