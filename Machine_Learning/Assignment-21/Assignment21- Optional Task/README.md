# 🏡 House Price Predictor

An interactive web application built with **Streamlit**, **Pandas**, and **Scikit-Learn** that predicts house selling prices based on key property features and location data.

---

## 📌 Features

- **Interactive Input Form:** Easy-to-use sliders and numerical inputs for specs like square footage, quality ratings, build year, and garage size.
- **Location Selection:** Dropdown menu for selecting specific neighborhoods.
- **Dynamic Preprocessing:** Automated One-Hot Encoding and feature scaling on user input to match trained model parameters.
- **Real-time Prediction:** Machine learning inference powered by a pre-trained Linear Regression model.

---

## 🛠️ Project Structure

```text
├── LR_house_price.pkl   # Trained Linear Regression model
├── scaler.pkl           # Saved StandardScaler / MinMaxScaler instance
├── columns.pkl          # Saved list of one-hot encoded training feature columns
├── app.py               # Streamlit web application interface
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have **Python 3.8+** installed.

### 2. Clone or Setup the Project
Navigate to your project directory containing `app.py` and your `.pkl` model files.

### 3. Install Dependencies
Create a virtual environment (optional but recommended) and install the necessary libraries:

```bash
pip install streamlit pandas joblib scikit-learn
```

> **Tip:** You can create a `requirements.txt` file with:
> ```text
> streamlit
> pandas
> joblib
> scikit-learn
> ```
> And run `pip install -r requirements.txt`.

### 4. Run the Streamlit App
Start the app by running the following command in your terminal:

```bash
streamlit run app.py
```

Your default browser should automatically open to `http://localhost:8501`.

---

## 📊 Model & Input Features

The app processes the following user inputs:

| Feature | Description | Range / Type |
| :--- | :--- | :--- |
| **Overall Quality** | Overall material and finish quality | Scale 1–10 |
| **Ground Living Area** | Above grade living area in sq ft | 300 – 6,000 sq ft |
| **Garage Capacity** | Garage size in car capacity | 0 – 5 cars |
| **Garage Area** | Size of garage in sq ft | 0 – 2,000 sq ft |
| **Total Basement Area** | Basement area in sq ft | 0 – 4,000 sq ft |
| **First Floor Area** | 1st floor square feet | 300 – 4,000 sq ft |
| **Full Bathrooms** | Full bathrooms above ground | 0 – 5 |
| **Year Built** | Original construction date | 1800 – 2025 |
| **Total Rooms** | Total rooms above ground (excl. baths) | 2 – 15 |
| **Neighborhood** | Physical locations within city limits | Categorical Selection |

---

## ⚙️ How It Works Behind the Scenes

1. **Data Load:** Model weights (`LR_house_price.pkl`), scaler objects (`scaler.pkl`), and expected feature column structures (`columns.pkl`) are loaded into memory.
2. **Encoding:** The categorical `Neighborhood` input is converted via pandas One-Hot Encoding (`pd.get_dummies`).
3. **Alignment:** Missing dummy variables are aligned with `columns.pkl` using `.reindex()` to maintain the exact feature structure expected by the model.
4. **Scaling:** Numerical columns are transformed via the pre-fitted `scaler`.
5. **Inference:** Scaled features are passed to the Linear Regression model to compute and render the estimated output.
