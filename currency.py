import streamlit as st
import requests

st.title("💱 Currency Converter")

amount = st.number_input("Enter amount", min_value=1.0)
from_currency = st.text_input("From Currency (e.g. USD)", "USD")
to_currency = st.text_input("To Currency (e.g. INR)", "INR")

if st.button("Convert"):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url).json()
    
    if "result" in response:
        st.success(f"{amount} {from_currency} = {response['result']:.2f} {to_currency}")
    else:
        st.error("Conversion failed. Please check currency codes.")
