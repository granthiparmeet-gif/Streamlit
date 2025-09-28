import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Add some text
st.write("Hello, welcome to my simple Streamlit app!")

# Input from user
name = st.text_input("Enter your name:")

# Button to trigger action
if st.button("Submit"):
    st.success(f"Hello {name}, nice to meet you! 🎉")

# Slider
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"Your age is {age}")

# Display a chart
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["Column A", "Column B"]
)

st.line_chart(data)
