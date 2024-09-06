import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados das planilhas Excel
df_usouptodat = pd.read_excel('usousptodat.xlsx')
df_contastauptodat = pd.read_excel('contastauptodat.xlsx')

# Renomear as colunas, se necessário
df_usouptodat.columns = ["USAGE KPI", "USAGE BY MONTH", "% OF ALL USE", "PERIOD USAGE", "PoP CHANGE"]
df_contastauptodat.columns = ["Month", "Current Usage", "Previous Usage"]

def page_uptodat():
    st.write("Visualização dos dados da UptoDat")

    

    # Layout dos gráficos - 2 por linha
    col1, col2 = st.columns(2)

    with col1:
        # Gráfico 1: Gráfico de Pizza para % OF ALL USE
        fig_pie = px.pie(df_usouptodat, names="USAGE KPI", values="% OF ALL USE", title="% de Uso por Tipo de Plataforma")
        st.plotly_chart(fig_pie)

        # Gráfico 2: Gráfico de Barras para USAGE BY MONTH
        fig_bar_usage_month = px.bar(df_usouptodat, x="USAGE KPI", y="USAGE BY MONTH", title="Uso Mensal por Tipo de Plataforma")
        st.plotly_chart(fig_bar_usage_month)

    with col2:
        # Gráfico 3: Gráfico de Barras para PERIOD USAGE
        fig_bar_period_usage = px.bar(df_usouptodat, x="USAGE KPI", y="PERIOD USAGE", title="Uso por Período por Tipo de Plataforma")
        st.plotly_chart(fig_bar_period_usage)

        # Gráfico 4: Gráfico de Linhas para comparação temporal
        # Verifique o formato das datas na coluna 'Month'
        print(df_contastauptodat['Month'].head())  # Adicione isto para debug

        # Ajustar o formato da data
        df_contastauptodat['Month'] = pd.to_datetime(df_contastauptodat['Month'], format='%B %Y', errors='coerce')

        # Caso o formato não seja coerente, trate as datas manualmente
        if df_contastauptodat['Month'].isnull().any():
            df_contastauptodat['Month'] = pd.to_datetime(df_contastauptodat['Month'], format='%B %Y', errors='coerce')

        fig_line = px.line(
            df_contastauptodat,
            x="Month",
            y=["Current Usage", "Previous Usage"],
            title="Tendência de Uso por Período",
            labels={"value": "Uso", "variable": "Tipo de Uso"}
        )
        fig_line.update_traces(mode='lines+markers', hovertemplate='<b>%{x}</b><br>Uso: %{y}<extra></extra>')
        st.plotly_chart(fig_line)

# Verificando se o script está sendo executado diretamente para chamar a função

# Configuração para mostrar ou esconder dados usando st.session_state
    if 'show_data' not in st.session_state:
        st.session_state.show_data = False

    if st.sidebar.button("Mostrar Dados"):
        st.session_state.show_data = True

    if st.sidebar.button("Esconder Dados"):
        st.session_state.show_data = False

    # Mostrar os dados se o botão for pressionado
    if st.session_state.show_data:
        st.write(df_usouptodat)
if __name__ == "__main__":
    page_uptodat()
