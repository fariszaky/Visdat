import streamlit as st
import time

st.title("Empety Containers")
st.write("Kelompok: 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227  
""")

with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} detik telah berlalu")
        time.sleep(1)
        st.write("Waktunya habis!")