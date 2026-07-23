import streamlit as st
import pandas as pd
import joblib

# Load saved model and preprocessing objects
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("❤️ Heart Disease Prediction")

age = st.number_input("Age")
resting_bp = st.number_input("Resting Blood Pressure")
cholesterol = st.number_input("Cholesterol")
max_hr = st.number_input("Maximum Heart Rate")
oldpeak = st.number_input("Oldpeak")

sex = st.selectbox("Sex", ["M", "F"])
chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
exercise_angina = st.selectbox("Exercise Angina", ["N", "Y"])
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    # Create input data
    input_data = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain_type,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope
    }])

    # Encode categorical columns
    input_data = pd.get_dummies(input_data)                                                                   

    # Match training columns
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )
    # Scale input data
    input_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction[0] == 1:
        st.error("Heart Disease: Yes")
    else:
        st.success("Heart Disease: No")
