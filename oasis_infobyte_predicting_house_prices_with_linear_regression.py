# -*- coding: utf-8 -*-
"""OASIS_InfoByte_Predicting_House_Prices_with_Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KvaVeBykhjbJDu3799F04Rc89sBsDQmj

#**Predicting House Prices with Linear Regression**

Import libraries
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import matplotlib.pyplot as plt

"""Load the dataset"""

housing = pd.read_csv("/content/Housing.csv")

"""Explore the data"""

print(housing.info())

print(housing.describe())

print(housing.dtypes)

print(housing.head())

print(housing.tail())

print(housing.isnull())

print(housing.isnull().sum())

print(housing.isnull().sum().sum())

"""Data Preparation

One-hot encode categorical variables
"""

categorical_features = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
numerical_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

"""Create the pipeline"""

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

"""Prepare the data"""

X = housing.drop('price', axis=1)
y = housing['price']

"""Split the data into training and testing sets"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

""" Train the model"""

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

"""Evaluate the model

Evaluate the model's performance by predicting on the test set and calculating the Mean Squared Error (MSE) and R-squared (R^2) score.
"""

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

"""Visualize the results"""

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.3)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.show()

residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.3)
plt.xlabel('Predicted Prices')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Prices')
plt.axhline(y=0, color='r', linestyle='--')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.show()

"""Summary

The code implements a linear regression model to predict house prices using a dataset. It begins by importing necessary libraries and loading the dataset from a CSV file. The data is explored for structure, summary statistics, and missing values. Categorical and numerical features are identified, and a preprocessing pipeline is created using ColumnTransformer and OneHotEncoder. The dataset is split into training and testing sets, and the linear regression model is trained using the pipeline. After making predictions on the test set, the model's performance is evaluated using Mean Squared Error (MSE) and R-squared metrics. Finally, several visualizations are created to illustrate the relationship between actual and predicted prices, as well as the residuals, providing insights into the model's effectiveness.
"""