import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok : 12")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky- 011022227 """)

st.graphviz_chart("""
    digraph{
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"    
    }
""")

