import csv

import streamlit as st
import os.path
import pathlib

from csv_read import serialize_bofa_csv_data

st.write("""
# File Picker
""")
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])


if uploaded_file:
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Saved File")

    serialize_bofa_csv_data(uploaded_file)



    # with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
    #     f.write(uploaded_file.getbuffer())
    # st.success("Saved File")



