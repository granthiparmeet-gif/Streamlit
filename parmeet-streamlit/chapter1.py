import streamlit as st

st.title("This is Parmeet SInghs website")
st.subheader("Made with streamlit")
st.header("This is the header")

st.text("Welcome to first streamlit website")
st.write("Choose your favorite variety of **chai**")
st.write({'a':'Parmeet', 'b':'Harshjot'})

sex = st.selectbox("My selectbox", ["Male", "Female"])

st.write(f"You are a {sex}")


st.success("You have selected your sex")
st.warning("This is a warning")
st.warning("Make sure you are right")
st.info("This is an info")
st.error("You have put a wrong value")
st.exception(exception=True)


lang=st.selectbox("Select your favorite langugae", ["C","C+","Java", "PHP"])
st.write(f"You have selected your favorite langugae as {lang}")