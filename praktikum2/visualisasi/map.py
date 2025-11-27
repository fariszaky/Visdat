import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok : 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky- 011022227 """)

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df) 
   