import streamlit as st

st.title("7. Layout - Sidebar")
st.write("Kelompok: 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227  
""")

st.sidebar.title("Sidebar")
st.sidebar.radio("Apakah Anda Pengguna Baru?", ["Iya", "Tidak"])
st.sidebar.slider("Pilih Nomor", 0,10)