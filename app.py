import streamlit as st
from pages.minha_biblioteca import minha_biblioteca
from pages.ebsco import page_ebsco
from pages.uptodat import page_uptodat

# Inicializar st.session_state.show_data
if 'show_data' not in st.session_state:
    st.session_state.show_data = False

# Função para alternar a visibilidade dos dados
def toggle_data_visibility():
    st.session_state.show_data = not st.session_state.show_data

# Configurar a página
st.set_page_config(layout="wide")

# Seletor de páginas
page = st.sidebar.selectbox("Escolha a Página", ["EBSCO", "Minha Biblioteca", "UpTodat"])

# Mostrar a página correspondente
if page == "EBSCO":
    page_ebsco()
elif page == "Minha Biblioteca":
    minha_biblioteca()
elif page == "UpTodat":
    page_uptodat()

# Exibir dados com base no estado
if st.session_state.show_data:
    st.write("Dados Exibidos:")
