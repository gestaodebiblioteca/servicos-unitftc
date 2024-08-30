import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv('dados_mb_biblioteca.csv')
df_detalhado = pd.read_csv('dados_categorias.csv')
df_stundents_views = pd.read_csv('StudentsViews.csv')
df_page_views = pd.read_csv('PageViews.csv')

# Inicializar o estado da sessão se não estiver definido
if 'show_data' not in st.session_state:
    st.session_state.show_data = False

# Função para exibir a página "Minha Biblioteca"
def minha_biblioteca():
    # Configurar a sidebar
    st.sidebar.title("Opções")
    
    # Checkbox para mostrar ou esconder os dados
    if st.sidebar.checkbox("Mostrar Dados", value=st.session_state.show_data):
        st.session_state.show_data = True
    else:
        st.session_state.show_data = False

    # Dividir a tela em quatro colunas
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Gráficos e tabelas
    with col1:
        st.subheader("Total de Livros por Editora")
        fig_total = px.bar(df, x="Editora", y="Total", title="Total de Livros por Editora")
        st.plotly_chart(fig_total)

    with col2:
        st.subheader("Novos Livros por Editora")
        fig_categoria = px.pie(df_detalhado, names="Categoria", values=df_detalhado.columns[1],
                              title="Distribuição por Categoria")
        st.plotly_chart(fig_categoria)

    with col3:
        st.subheader("Visualizações dos Estudantes por Dispositivo")
        fig_students = px.bar(df_stundents_views, x="Device", y="Sessions",
                              title="Visualizações dos Estudantes por Dispositivo")
        st.plotly_chart(fig_students)
    
    with col4:
        st.subheader("Visualizações de Páginas por Dispositivo")
        fig_page = px.line(df_page_views, x="Device", y="PageViews",
                           title="Visualizações de Páginas por Dispositivo")
        st.plotly_chart(fig_page)

    # Mostrar ou esconder dados com base na seleção do checkbox
    if st.session_state.show_data:
        st.write(df)

# Executar a função
if __name__ == "__main__":
    minha_biblioteca()
