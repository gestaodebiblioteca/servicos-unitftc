import streamlit as st
import pandas as pd
import plotly.express as px  # type: ignore
from pages.minha_biblioteca import minha_biblioteca
from pages.ebsco import page_ebsco

# Inicializar st.session_state.show_data
if 'show_data' not in st.session_state:
    st.session_state.show_data = False

# Função para alternar a visibilidade dos dados
def toggle_data_visibility():
    st.session_state.show_data = not st.session_state.show_data

# Configurar a página
st.set_page_config(layout="wide")

# Adicionar CSS e cabeçalho
# (Coloque o código CSS e o cabeçalho aqui, ou mova para um arquivo separado se preferir)

# Seletor de páginas
page = st.sidebar.selectbox("Escolha a Página", ["Minha Biblioteca", "EBSCO", "Próxima página"])

if page == "Minha Biblioteca":
    minha_biblioteca()

elif page == "EBSCO":
    page_ebsco()

# Botões para mostrar e esconder dados
