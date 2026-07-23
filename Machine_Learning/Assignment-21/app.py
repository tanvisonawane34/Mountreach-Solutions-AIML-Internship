# Importing Streamlit library 
import streamlit as st

# Importing Pandas library
import pandas as pd

# Importing Joblib library 
import joblib



# Loading the trained Linear Regression model
model = joblib.load("LR_ford_car.pkl")

# Loading the StandardScaler object 
scaler = joblib.load("scaler.pkl")

# Loading the list of encoded column names
encoded_columns = joblib.load("columns.pkl")



# Setting the page title and layout for the Streamlit app
st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)
# These settings give the app a proper title and keep the content centered.


# Set Title and description
st.title("Ford Car Price Predictor")
st.write("Enter the car details below to predict its selling price.")


# Numerical Input fields
year = st.number_input("Manufacturing Year", min_value=2000, max_value=2025, value=2018)
mileage = st.number_input("Mileage", min_value=0, max_value=200000, value=50000)
tax = st.number_input("Road Tax", min_value=0, max_value=600, value=150)
mpg = st.number_input("MPG", min_value=0.0, max_value=150.0, value=50.0)
engineSize = st.number_input("Engine Size", min_value=0.0, max_value=10.0, value=1.5)



# Categorical Inputs
transmission = st.selectbox("Transmission", ["Automatic", "Manual", "Semi-Auto"])
fuelType = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Hybrid"])

# Selectbox allows users to select from given options easily
# Selectbox provides fixed choices and avoids wrong input



# Taking car model name from the user
model_name = st.text_input("Enter Car Model")

# Creating a button to predict the car price
predict_button = st.button("Predict Price")



if predict_button:
    try:
        # Creating DataFrame from user input values
        input_data = pd.DataFrame({
        "model": [model_name],
        "year": [year],
        "transmission": [transmission],
        "mileage": [mileage],
        "fuelType": [fuelType],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engineSize]
    })

        # Performing One-Hot Encoding on categorical columns
        input_encoded = pd.get_dummies(input_data)

        # Aligning input columns with training columns
        input_encoded = input_encoded.reindex(columns=encoded_columns, fill_value=0)



        # Identifying numerical columns for scaling
        numerical_columns = ["year", "mileage", "tax", "mpg", "engineSize"]

        # Applying the loaded scaler on numerical columns
        input_encoded[numerical_columns] = scaler.transform(input_encoded[numerical_columns])
        prediction = model.predict(input_encoded)
        st.success(f"Predicted Price: £{prediction[0]:,.2f}")  

    except Exception as e:
        st.error("Something went wrong. Please check your input values.") 




    