import streamlit as st
import requests

st.title("Live Currency converter")

amount = st.number_input("Enter the amount in INR")

target_cuurency = st.selectbox("Convert to:", ["USD","EUR", "JPY", "GBP" ])

if st.button("Convert Now"):
    url = "https://v6.exchangerate-api.com/v6/f7115bbc2c6f0db9e27806cf/latest/INR"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        rate = data["conversion_rates"][target_cuurency]
        converted = rate * amount
        st.success(f"{amount}INR = {converted : .2f}{target_cuurency}")
    else:
        st.error("Failed to Fetch")