import streamlit as st 
import numpy as np

st.title("Containers")
st.write("Kelompok: 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227  
""")

with st.container():
    st.write("Elemen Di Dalam Kontainer")
    st.line_chart(np.random.randn(40, 4))
    st.write("Elemen di Luar kontainer")