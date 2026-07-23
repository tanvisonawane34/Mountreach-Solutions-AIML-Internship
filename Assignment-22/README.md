# ❤️ Heart Disease Prediction App

An interactive Machine Learning web application built with **Streamlit** that predicts the likelihood of heart disease based on clinical data and medical diagnostic parameters.

---

## 📌 Features

- 🎛️ **Interactive Clinical Input:** Easy-to-use input fields for entering clinical metrics (e.g., Blood Pressure, Cholesterol, ECG results).
- ⚙️ **Automatic One-Hot Encoding:** Automatically handles categorical medical variables (`Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope`) using `pd.get_dummies()`.
- 📐 **Schema Alignment & Feature Scaling:** Reindexes dummy features against saved model columns (`columns.pkl`) and scales inputs via standard scaling (`scaler.pkl`).
- ⚡ **Real-time Prediction:** Instant output displaying whether the input parameters indicate presence or absence of heart disease.

---

## 📁 Repository Structure

```text
.
├── app.py                 # Streamlit web application code
├── heart_model.pkl        # Pre-trained Classification Model
├── scaler.pkl             # Fitted Feature Scaler
├── columns.pkl            # Expected feature column layout
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Installation & Local Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Install Dependencies
Create a `requirements.txt` file containing:
```text
streamlit
pandas
joblib
scikit-learn
```

Then install the dependencies using pip:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

Launch the Streamlit app locally by executing:

```bash
streamlit run app.py
```

The application will open automatically in your web browser at `http://localhost:8501`.

---

## 📊 Feature Reference Table

| Feature Name | Type | Options / Range | Description |
| :--- | :--- | :--- | :--- |
| **Age** | Numerical | Age in years | Passenger / Patient age |
| **RestingBP** | Numerical | mm Hg | Resting blood pressure |
| **Cholesterol** | Numerical | mm/dl | Serum cholesterol |
| **MaxHR** | Numerical | 60 - 220 | Maximum heart rate achieved |
| **Oldpeak** | Numerical | Numeric value | ST depression induced by exercise relative to rest |
| **Sex** | Categorical | `M`, `F` | Gender of the patient |
| **ChestPainType**| Categorical | `ATA`, `NAP`, `ASY`, `TA` | Chest pain type (Atypical Angina, Non-Anginal Pain, Asymptomatic, Typical Angina) |
| **FastingBS** | Categorical | `0`, `1` | Fasting blood sugar (> 120 mg/dl: 1 = true; 0 = false) |
| **RestingECG** | Categorical | `Normal`, `ST`, `LVH` | Resting electrocardiographic results |
| **ExerciseAngina**| Categorical | `N`, `Y` | Exercise induced angina |
| **ST_Slope** | Categorical | `Up`, `Flat`, `Down` | The slope of the peak exercise ST segment |

---

## ⚙️ Model & Feature Pipeline Details

1. **One-Hot Encoding:** Transforms text inputs into dummy binary features using `pd.get_dummies()`.
2. **Column Reindexing:** Realigns features using `input_data.reindex(columns=columns, fill_value=0)` to ensure exact feature count and ordering match the trained model.
3. **Scaling & Inference:** Applies `scaler.transform()` before sending preprocessed data into `heart_model.pkl`.
