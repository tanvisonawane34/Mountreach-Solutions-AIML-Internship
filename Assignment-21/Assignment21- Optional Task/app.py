# Import Streamlit
import streamlit as st

# Import Pandas
import pandas as pd

# Import Joblib
import joblib


# Load trained model
model = joblib.load("LR_house_price.pkl")

# Load scaler
scaler = joblib.load("scaler.pkl")

# Load feature columns
encoded_columns = joblib.load("columns.pkl")

# Page settings
st.set_page_config(
    page_title="House Price Predictor",
    layout="centered"
)

# Title
st.title("🏠House Price Predictor")

# Description
st.write("Enter the house details below to predict its selling price.")


# Numerical inputs
overallQual = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
grLivArea = st.number_input("Ground Living Area (sq ft)", min_value=300, max_value=6000, value=1500)
garageCars = st.number_input("Garage Capacity", min_value=0, max_value=5, value=2)
garageArea = st.number_input("Garage Area (sq ft)", min_value=0, max_value=2000, value=500)
totalBsmtSF = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=4000, value=900)
firstFlrSF = st.number_input("First Floor Area (sq ft)", min_value=300, max_value=4000, value=1200)
fullBath = st.number_input("Number of Full Bathrooms", min_value=0, max_value=5, value=2)
yearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
totRmsAbvGrd = st.number_input("Total Rooms Above Ground", min_value=2, max_value=15, value=6)

# Dropdown for Neighborhood
neighborhood = st.selectbox(
    "Neighborhood",
    [
        "NAmes", "CollgCr", "OldTown",
        "Edwards", "Somerst", "Gilbert",
        "NridgHt", "Sawyer", "NWAmes",
        "BrkSide", "Crawfor", "Mitchel",
        "NoRidge", "Timber", "IDOTRR"
    ]
)

# Predict button
predict_button = st.button("Predict Price")

if predict_button:
    try:
        # Create DataFrame
        input_data = pd.DataFrame({
            "OverallQual": [overallQual],
            "GrLivArea": [grLivArea],
            "GarageCars": [garageCars],
            "GarageArea": [garageArea],
            "TotalBsmtSF": [totalBsmtSF],
            "1stFlrSF": [firstFlrSF],
            "FullBath": [fullBath],
            "YearBuilt": [yearBuilt],
            "TotRmsAbvGrd": [totRmsAbvGrd],
            "Neighborhood": [neighborhood]
        })
        # One-Hot Encoding
        input_encoded = pd.get_dummies(input_data)
        # Match training columns
        input_encoded = input_encoded.reindex(columns=encoded_columns, fill_value=0)

        # Numerical columns
        numerical_columns = [
            "OverallQual",
            "GrLivArea",
            "GarageCars",
            "GarageArea",
            "TotalBsmtSF",
            "1stFlrSF",
            "FullBath",
            "YearBuilt",
            "TotRmsAbvGrd"
        ]
        # Scale numerical columns
        input_encoded[numerical_columns] = scaler.transform(
            input_encoded[numerical_columns]
        )
        # Predict price
        prediction = model.predict(input_encoded)
        
        # Plain & Simple: USD to INR Conversion
        price_in_inr = prediction[0] * 85
        
        # Show prediction
        st.success(f"Predicted House Price: ₹{price_in_inr:,.2f}")
    except Exception as e:
        st.error("Something went wrong. Please check your input values.")           