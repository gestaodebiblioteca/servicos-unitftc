import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df_dadoebsco = pd.read_excel('EBSCO_Data.xlsx')

def page_ebsco():
    st.write("Visualização dos dados do EBSCO")

    colunas = df_dadoebsco.columns
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.subheader("Total de Sessões por Banco de Dados")
        fig_sessions = px.bar(df_dadoebsco, x=colunas[0], y=colunas[3],
                              title="Total de Sessões por Banco de Dados", color=colunas[0])
        st.plotly_chart(fig_sessions)

    with col2:
        st.subheader("Total de Pesquisas por Banco de Dados")
        fig_searches = px.pie(df_dadoebsco, names=colunas[0], values=colunas[4],
                              title="Distribuição de Pesquisas por Banco de Dados")
        st.plotly_chart(fig_searches)

    with col3:
        st.subheader("Total de Requisições por Banco de Dados")
        fig_requests = px.line(df_dadoebsco, x=colunas[0], y=colunas[5],
                               title="Total de Requisições por Banco de Dados", markers=True)
        st.plotly_chart(fig_requests)

    with col4:
        st.subheader("Total de Requisições de Texto Completo por Banco de Dados")
        fig_full_text_requests = px.scatter(df_dadoebsco, x=colunas[0], y=colunas[6],
                                            title="Requisições de Texto Completo por Banco de Dados", color=colunas[0])
        st.plotly_chart(fig_full_text_requests)

    st.write("Os dados apresentados são baseados no uso do EBSCO pela instituição no período de 01/06/2024 a 09/08/2024.")

    if 'show_data' not in st.session_state:
        st.session_state.show_data = False

    if st.sidebar.button("Mostrar Dados"):
        st.session_state.show_data = True

    if st.sidebar.button("Esconder Dados"):
        st.session_state.show_data = False

    if st.session_state.show_data:
        st.write(df_dadoebsco)

# Não execute a função se o módulo for importado
if __name__ == "__main__":
    page_ebsco()
