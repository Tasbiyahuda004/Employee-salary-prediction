# app.py
import streamlit as st
import pandas as pd
from model import train_model, evaluate_model
import datetime

st.set_page_config(page_title="Employee Salary Predictor", layout="centered")

model = train_model()
mse, r2 = evaluate_model(model)

st.title("👩‍💼 Employee Salary Predictor")

with st.form("prediction_form"):
    st.subheader("📋 Personal Details")
    name = st.text_input("Full Name")
    location = st.selectbox("Location", ["New York", "San Francisco", "London", "Bangalore", "Berlin"])
    
    st.subheader("🏢 Work & Education")
    company = st.text_input("Company")
    job_title = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "Manager", "Analyst", "HR"])
    education = st.selectbox("Education Level", ["High School", "Bachelors", "Masters", "PhD"])
    experience = st.slider("Years of Experience", 0, 30, 1)

    submit = st.form_submit_button("Predict Salary")

if submit:
    input_data = pd.DataFrame({
        'Company': [company],
        'Job Title': [job_title],
        'Education': [education],
        'Experience': [experience],
        'Location': [location]
    })

    prediction = model.predict(input_data)[0]
    
    st.success(f"👤 {name}, your predicted salary is: **₹{prediction:,.2f}**")

    st.subheader("📊 Model Performance")
    st.write(f"🔹 Mean Squared Error (MSE): `{mse:.2f}`")
    st.write(f"🔹 R-squared (R² Score): `{r2:.2f}`")

    st.subheader("📈 Prediction Summary")
    chart_data = pd.DataFrame({
        'Actual': [None],
        'Predicted': [prediction]
    })

    st.bar_chart(chart_data.rename(columns={'Predicted': f'{name}'}))

    st.download_button(
        label="📥 Download Prediction",
        data=input_data.assign(Predicted_Salary=prediction).to_csv(index=False).encode(),
        file_name=f"{name}_salary_prediction.csv",
        mime='text/csv'
    )
