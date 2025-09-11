import streamlit as st

st.title("Chai Maker App")

st.link_button("Go to my Linkedin", "https://www.linkedin.com/in/parmeet-singh-granthi/")

masala= st.checkbox("Add Masala")

if masala:
    st.write("**Masala** Added")


chai_base = st.radio("Pick your chai base", ["Adrak chai","Elaichi Chai","Lemon tea","Darjeling Tea"])


if chai_base=="Adrak chai":
    st.write("This is Adrak Base")

if chai_base=="Elaichi Chai":
    st.write("This is Elaichi Base")


sugar = st.slider("Sugar level", 1, 10, 5)

st.write(f"Sugar Level {sugar}")

cups = st.number_input("Number of cups", min_value=1, max_value=10, step=2)

st.write(f"The number of cups are {cups}")


name= st.text_input("Enter your name")

if name:
    st.write(f"Welcome {name}")

st.date_input("Select the birth date")

