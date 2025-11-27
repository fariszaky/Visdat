import streamlit as st 
from PIL import Image
img = Image.open("../../praktikum1/GreenSeaTurtle-2.jpg")

st.title("Padding")
st.write("Kelompok: 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227  
""")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)