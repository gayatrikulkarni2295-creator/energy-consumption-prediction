# Energy Consumption Prediction using Machine Learning

## Overview

Energy consumption in industrial environments is influenced by multiple factors such as temperature, humidity, machine workload, and operating hours.
This project uses Machine Learning to predict energy consumption based on these parameters, helping industries analyze and optimize their electricity usage.

---

## Problem Statement

Industries often experience inefficient energy utilization due to lack of predictive insights.
Predicting energy consumption using data-driven models can help reduce energy costs and improve operational efficiency.

---

## Proposed Solution

This project builds a Machine Learning regression model that predicts energy consumption based on environmental and operational variables.

The system analyzes:

* Temperature
* Humidity
* Machine Load
* Working Hours

and predicts the expected **energy consumption of industrial systems**.

---

## Dataset

The dataset contains simulated industrial machine data including:

| Feature            | Description                                       |
| ------------------ | ------------------------------------------------- |
| Temperature        | Ambient temperature in the industrial environment |
| Humidity           | Humidity level                                    |
| Machine Load       | Percentage of machine workload                    |
| Working Hours      | Duration of machine operation                     |
| Energy Consumption | Electricity usage                                 |

---

## Machine Learning Model

Model Used:

* Linear Regression

The model is trained to learn the relationship between machine parameters and energy consumption.

---

## Tech Stack

* Python
* Pandas
* Scikit-learn
* Matplotlib

---

## Project Structure

energy-consumption-prediction
│
├── dataset
│   └── energy_data.csv
│
├── model
│   └── train_model.py
│
├── notebook
│   └── analysis.ipynb
│
├── requirements.txt
└── README.md

---

## How to Run

### 1 Install dependencies

pip install -r requirements.txt

### 2 Run the model

python model/train_model.py

---

## Output

The model predicts industrial energy consumption and visualizes the relationship between predicted and actual energy usage.

Example output:

Predicted Energy Consumption: 225 units

---

## Future Improvements

* Add larger real-world industrial datasets
* Implement advanced models such as Random Forest or Gradient Boosting
* Deploy the model as a web application dashboard
* Integrate real-time sensor data for live prediction

---

## Author

Machine Learning Project developed for AI-based Industrial Energy Optimization.
