import streamlit as st
<<<<<<< HEAD
import pandas as pd
import plotly.express as px # type: ignore
=======
from pages.minha_biblioteca import minha_biblioteca
from pages.ebsco import page_ebsco
>>>>>>> 2d5a6d2 (Separendo por pastas)

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
<<<<<<< HEAD
    # Botões para mostrar e esconder dados
    st.sidebar.button("Mostrar Dados", on_click=toggle_data_visibility)
    #if st.session_state.show_data:
        #st.write(df_detalhado)
        #st.sidebar.button("Esconder Dados", on_click=toggle_data_visibility)
=======
>>>>>>> 2d5a6d2 (Separendo por pastas)
