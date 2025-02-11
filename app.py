import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load encoder and trained model
model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\liver_cancer_prediction.pkl")
encoder = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\encoder.pkl")

# Ensure encoder is a valid transformer
if not hasattr(encoder, "transform"):
    st.error("Loaded encoder is not a valid transformer. Check the encoder file.")
    st.stop()

def encode_input(user_input):
    """Encodes user input using the trained encoder."""
    input_df = pd.DataFrame([user_input])
    encoded_input = encoder.transform(input_df)
    return encoded_input

# Streamlit UI
def main():
    st.title("Liver Cancer Prediction API")
    st.write("Enter patient details to predict liver cancer risk.")
    
    # User inputs
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    gender = st.selectbox("Gender", ["Male", "Female"])
    alcohol_consumption = st.selectbox("Alcohol Consumption", ["Yes", "No"])
    smoking_status = st.selectbox("Smoking Status", ["Smoker", "Non-Smoker"])
    hepatitis_b = st.selectbox("Hepatitis B Status", ["Positive", "Negative"])
    hepatitis_c = st.selectbox("Hepatitis C Status", ["Positive", "Negative"])
    obesity = st.selectbox("Obesity", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    seafood_consumption = st.selectbox("Seafood Consumption", ["High", "Moderate", "Low"])
    herbal_medicine_use = st.selectbox("Herbal Medicine Use", ["Yes", "No"])
    healthcare_access = st.selectbox("Healthcare Access", ["Good", "Average", "Poor"])
    preventive_care = st.selectbox("Preventive Care", ["Yes", "No"])
    
    # Convert input into dictionary
    user_data = {
        "Age": age,
        "Gender": gender,
        "Alcohol_Consumption": alcohol_consumption,
        "Smoking_Status": smoking_status,
        "Hepatitis_B_Status": hepatitis_b,
        "Hepatitis_C_Status": hepatitis_c,
        "Obesity": obesity,
        "Diabetes": diabetes,
        "Seafood_Consumption": seafood_consumption,
        "Herbal_Medicine_Use": herbal_medicine_use,
        "Healthcare_Access": healthcare_access,
        "Preventive_Care": preventive_care,
    }
    
    if st.button("Predict Cancer Risk"):
        try:
            # Encode input
            encoded_input = encode_input(user_data)
            prediction = model.predict(encoded_input)
            
            # Display result
            st.write("### Prediction Result:")
            if prediction[0] == 1:
                st.error("High Risk of Liver Cancer! Consult a doctor immediately.")
            else:
                st.success("Low Risk of Liver Cancer. Maintain a healthy lifestyle.")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == "__main__":
    main()

