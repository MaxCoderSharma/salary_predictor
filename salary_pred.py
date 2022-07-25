import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plr

model = joblib.load('Salary-Prediction.pkl')
st.title("Salary Prediction")
st.subheader("Enter Your Experience")

experiance = st.number_input("Your Experience")
if st.button("Salary"):
    sal = model.predict([[experiance]]).round(2)
    if sal == 0.00:
        sal = 0
    else:
        st.write(f"Your Salary Is Upto {sal}")
st.markdown("<h5 style='text-align: center; color: grey; padding-top: 200px'>Made By Lakshay</h5>",
            unsafe_allow_html=True)
