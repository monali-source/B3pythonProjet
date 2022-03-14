from turtle import pd
import requests
from pathlib import Path
import pandas as pd
import streamlit as st


url = 'http://127.0.0.1:5000'

def load_data() :

    data = pd.read_json(url)
    return data

df = load_data()
st.dataframe(df)



