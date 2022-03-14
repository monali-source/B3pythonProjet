from pathlib import Path
import pandas as pd
import streamlit as st
import requests


@st.cache
def load_data():
   data = Path() / 'result.csv'
   data = pd.read_csv(data)
   return data

df = load_data()
st.write(df)

title = st.text_input('Movie title', 'prix')
st.write('The current movie title is', title)


# You can access the value at any point with:
st.dataframe(df[df['title'] == st.session_state.film])


st.title('Insertion d un titre')

st.text_input("Ajouter du titre", key="titre")