import pandas as pd

def load_data():
    try:
        df = pd.read_csv('dados_mb_biblioteca.csv')
        df_detalhado = pd.read_csv('dados_categorias.csv')
        df_stundents_views = pd.read_csv('StudentsViews.csv')
        df_page_views = pd.read_csv('PageViews.csv')
        df_dadoebsco = pd.read_excel('EBSCO_Data.xlsx')
        return df, df_detalhado, df_stundents_views, df_page_views, df_dadoebsco
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Erro ao carregar o arquivo: {e}")
