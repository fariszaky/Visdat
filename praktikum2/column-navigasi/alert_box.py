import streamlit as st

st.title("9. Notification - Alert")
st.write("Kelompok: 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky - 011022227  """)

st.success("Data berhasil dimuat")
st.warning("Perhatikan! Data yang anda masukkan belum lengkap")
st.info("Silakan masukkan data anda terlebih dahulu sebelum melanjutkan")
st.error("Terjadi kesalahan saat memuat file!")
st.exception("It is an exception")