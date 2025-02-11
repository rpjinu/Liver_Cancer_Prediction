# Liver_Cancer_Prediction
A Streamlit-based Liver Cancer Prediction API that takes patient details, encodes categorical features, and uses a trained machine learning model to predict liver cancer risk. 🚀

<img src="https://github.com/rpjinu/Liver_Cancer_Prediction/blob/main/project_img.png">

# 🏥 Liver Cancer Prediction API

## 📌 Overview
This **Streamlit-based Liver Cancer Prediction API** takes patient details, encodes categorical features, and utilizes a trained machine learning model to predict the risk of liver cancer. 🚀

## 🛠 Features
- ✅ **User-Friendly Interface** powered by **Streamlit**
- 🔍 **Encodes categorical inputs** using a pre-trained encoder
- 🏥 **Predicts liver cancer risk** using a **machine learning model**
- 📊 **Provides instant feedback** based on user input
- 🎯 **Deployable** for real-world applications

## 📂 Project Structure
```
📦 liver_cancer_prediction
├── 📄 app.py                   # Streamlit application
├── 📂 models                   # Folder to store ML model & encoder
│   ├── liver_cancer_model.pkl  # Trained model file
│   ├── encoder.pkl             # Pre-trained encoder
├── 📂 data                     # Sample dataset (optional)
├── 📜 README.md                # Project documentation
└── 📝 requirements.txt          # Python dependencies
```

## 🚀 How to Run the Project
### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

### 3️⃣ Enter Patient Details & Get Prediction 🎯
- Enter **Age, Gender, Medical History, Lifestyle Factors, and Health Conditions**
- Click **Predict Cancer Risk** button
- Get instant **high/low risk prediction** ⚠️

## 🔧 Technologies Used
- 🐍 **Python** - Main programming language
- 📊 **Pandas, NumPy** - Data handling
- 🎯 **Scikit-learn** - Machine learning model & encoding
- 🎨 **Streamlit** - Web interface
- 📦 **Joblib** - Model & encoder serialization

## 📝 Example Usage
```python
import joblib
import numpy as np

# Load model & encoder
model = joblib.load("models/liver_cancer_model.pkl")
encoder = joblib.load("models/encoder.pkl")

# Sample patient data
user_input = {
    "Age": 50,
    "Gender": "Male",
    "Alcohol_Consumption": "Yes",
    "Smoking_Status": "Smoker",
    "Hepatitis_B_Status": "Positive",
    "Hepatitis_C_Status": "Negative",
    "Obesity": "Yes",
    "Diabetes": "No",
    "Seafood_Consumption": "Moderate",
    "Herbal_Medicine_Use": "No",
    "Healthcare_Access": "Good",
    "Preventive_Care": "Yes"
}

# Encode input & predict
encoded_input = encoder.transform([user_input])
prediction = model.predict(encoded_input)

print("Liver Cancer Risk:", "High" if prediction[0] == 1 else "Low")
```

## 📌 Future Improvements
- 📈 Improve model accuracy with **feature selection & hyperparameter tuning**
- 🌎 Deploy as **cloud-based API** (FastAPI, Flask, etc.)
- 📱 Convert to **mobile-friendly UI**

## 🤝 Contribution
Feel free to fork, improve, and contribute! 🎉

## 📜 License
MIT License 📄

---
💡 *Stay Healthy, Stay Aware!* 🚑

