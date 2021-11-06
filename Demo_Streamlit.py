import streamlit as st
import pandas as pd

path1 = "D:\Python\Main_Project_Jina\Dictionary.csv"
df = pd.read_csv(path1)

st.title('Demo Text Search')

df = df.drop(columns=['POS' , 'Count'])

Input = st.text_input("Enter your text :")
st.text(Input)



Out = df.loc[( df['Word'] == Input)]
st.table(Out)
