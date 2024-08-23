import streamlit as st
import pandas as pd
import plotly.express as px

df_usouptodat = pd.read_excel('usousptodat.xlsx')
df_contastauptodat = pd.read_excel('contastauptodat.xlsx')

def page_uptodat():
    st.write("Visualização dos dados da UptoDat")