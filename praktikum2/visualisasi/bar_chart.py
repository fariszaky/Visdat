import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.write("Kelompok : 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky- 011022227 """)

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.bar_chart(df)
