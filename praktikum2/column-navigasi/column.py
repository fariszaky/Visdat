import streamlit as st

st.title("Columns")
st.write("Kelompok : 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227 """)

col1, col2 = st.columns(2)

col1.write("ini adalah kolom pertama")
col1.image("../../praktikum1/singa.jpg")

col2.write("ini adalah kolom kedua")
col2.image("../../praktikum1/singa.jpg")
