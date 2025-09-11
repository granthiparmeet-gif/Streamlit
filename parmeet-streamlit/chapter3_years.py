import streamlit as st
from datetime import date

st.title("Age Calculator")

name = st.text_input ("Enter your name")
sex = st.selectbox("Enter your sex", ["Male", "Female"])
st.radio("Are you a adult", ["Yes", "No"])
dob = st.date_input("Enter your DOB")
todays_date= date.today()

years = todays_date.year - dob.year

st.write(f"Hey {name}, You are a {sex} and  The age is {years}")


