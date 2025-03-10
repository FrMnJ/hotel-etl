# Hotel Booking Cancellation Prediction

## 📌 Project Overview
This project processes hotel booking data to predict whether a reservation will be canceled. The pipeline follows an **ETL + Machine Learning** approach, using **Prefect** for orchestration.

Dataset: https://www.kaggle.com/datasets/mojtaba142/hotel-booking

## 🎯 Objectives
1. **ETL 1: Data Cleaning & Preprocessing**  
   - Remove duplicates & handle missing values.  
   - Convert categorical variables into numeric format.  
   - Store the cleaned dataset for further processing.  

2. **ETL 2: Model Training**  
   - Train a **machine learning model** to predict booking cancellations.  
   - Save the trained model for future use.  

3. **ETL 3: Prediction on New Data**  
   - Load the trained model and process new bookings.  
   - Predict cancellations and store results.  

## 🔹 Data Exploration
Before building the ETL pipeline, we perform **Exploratory Data Analysis (EDA)** to understand the dataset. Key questions include:  
- What is the **cancellation rate** for each hotel type?  
- Are **seasonal trends** influencing cancellations?  
- Do **previous cancellations** predict future cancellations?  
- Correlation between the columns
