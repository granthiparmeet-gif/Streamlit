import streamlit as st

st.title("Chai Poll")
st.image("parmeet.jpeg", width=100)

col1, col2 = st.columns(2)

with col1:
    st.header("Masla Chai")
    vote1 = st.button("Vote for Msala Chai")

with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote for Adrak Chai")

if vote1:
    st.success("Thanks for voting masla chai")

elif vote2:
    st.success("Thanks for voting Adrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai",["Masala", "Kesar"])


with st.expander("Show Chai Making Process"):
    st.write("This content is hidden until you expand the box.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo")
    st.code("print('Hello from inside the expander!')", language="python")

st.markdown('# Heading 1')
st.markdown('## Heading2')
st.markdown('### Heading3')


st.markdown("""
- Item 1
- Item 2
  - Sub-item
- Item 3
""")

st.markdown("""**bold text**  
*italic text*  
~~strikethrough~~  
`inline code`""")