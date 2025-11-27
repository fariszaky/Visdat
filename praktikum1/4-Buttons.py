
#import library
import pandas as pd
import streamlit as st
import numpy as np 
import altair as alt 

# Menampilkan judul dan deskripsi
st.title("Praktikum 1 - Visualisasi Data") #menampilkan judul halaman diutama
st.caption("Bagian 4 : Buttons") #menampilkan keterangan bagian

#st.markdown digunakan untuk menampilkan teks dengan format Markdown (bullet list, bold, italic, dll.)
st.markdown("""
1.	Distia Fajar Familiati - 0110222163
2.	Sabrina Ramadhani - 0110222068
3.	Muhammad Fariz Zacky- 011022227 
""")

#  Buttons
 
import streamlit as st
st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')


# Radio Buttons
import streamlit as st
st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
"Select your Gender", ('Pria', 'Wanita', 'Others'))
if gender == 'Pria':
    st.write('You have selected Male.')
elif gender == 'Wanita':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

# Check Boxes
import streamlit as st
st.title('Creating Checkboxes')
st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('painting')
check_2 = st.checkbox('cooking')
check_3 = st.checkbox('Sports')

# Drop-Downs
import streamlit as st
st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby:',
('painting ', 'cooking', 'Sports'))

# Multiselects
import streamlit as st
st.title('Multi-Select')
# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])

# Download Buttons
import streamlit as st
st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
label="Download Image",
data=open("GreenSeaTurtle-2.jpg", "rb"),
file_name="tiger.jpg",
mime="image/jpg"
)

import streamlit as st
import time
st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress (percentage+1)
st.write('Download Complete')

# Spinners

import streamlit as st
import time
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')
