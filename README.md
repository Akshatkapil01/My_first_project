# Vitamin Deficiency Prediction and Recommendation System

## Project Overview

This project is a Machine Learning based system designed to predict vitamin deficiency levels using basic health information. The model analyzes vitamin test values and predicts whether a person may have a deficiency.

Based on the prediction result, the system also provides recommendations such as foods, fruits, vegetables, exercises, and lifestyle suggestions that may help improve vitamin levels.

The goal of this project is to demonstrate how Machine Learning can assist in identifying potential nutritional deficiencies using simple input data.

---

## Dataset

The dataset used in this project contains the following features:

Gender – Male or Female
Vitamin Type – Type of vitamin (Vitamin A, B12, C, D, Iron)
Vitamin Value – Measured level of the vitamin in the body

These features are used to train the machine learning model to classify deficiency levels.

---

## Machine Learning Model

The project uses Logistic Regression for classification.

Logistic Regression is a supervised machine learning algorithm commonly used for classification problems. It predicts the probability of a particular outcome based on input features.

In this project, the model predicts whether the vitamin level indicates deficiency or a normal condition.

---

## Model Files

The trained models are saved using Joblib format.

Each vitamin type has its own trained model file:

model_B12.joblib
model_VitA.joblib
model_VitC.joblib
model_VitD.joblib
model_Iron.joblib

These models are loaded in the application to perform predictions without retraining the models.

---

## Machine Learning Workflow

1. Data collection and dataset preparation
2. Data preprocessing and feature encoding
3. Training Logistic Regression models for different vitamins
4. Model evaluation and accuracy checking
5. Saving trained models using Joblib
6. Integrating models into the prediction application

---

## Technologies Used

Python
Pandas
NumPy
Scikit-learn
Streamlit
Joblib

---

## Features

Predict vitamin deficiency based on vitamin test values
Supports multiple vitamins such as Vitamin A, B12, C, D, and Iron
Provides recommendation suggestions including foods, fruits, vegetables, and lifestyle tips
Simple and user-friendly interface

---

## Running the Application

1. Install required libraries

pip install -r requirements.txt

2. Run the application

streamlit run app.py

The application will automatically load the trained models and predict vitamin deficiency based on user input.

---

## Future Improvements

Use larger real-world clinical datasets
Add more health indicators such as age, diet, and medical history
Experiment with advanced machine learning models
Deploy the application as a web API

---

## Author

Akshat Kapil

AI / Machine Learning Enthusiast
