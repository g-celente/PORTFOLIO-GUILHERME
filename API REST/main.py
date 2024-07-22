import pandas as pd
from database import Connection
import streamlit as st
import plotly_express as px
from api import start_data_collection
import threading
from datetime import date

class Dashs:
    def __init__(self):
        self.db = Connection()
    
    def get_df(self):
        conn = self.db.get_connection()
        self.df = pd.read_sql("SELECT * FROM coins", conn)
        # Garantir que a coluna 'data' seja do tipo datetime
        self.df['data'] = pd.to_datetime(self.df['data'])
        return self.df

    def show_graph(self, df):
        df_moeda = df[df['moeda'] == 'Dolar']

        fig_dolar = px.area(
            df_moeda,
            title='Cotação Dólar',
            color_discrete_sequence=['#FF4B4B'],
            x='ultima_att',
            y='cotação'
        )

        df_euro = df[df['moeda'] == 'Euro']

        fig_euro = px.area(
            df_euro,
            title='Cotação Euro',
            color_discrete_sequence=['#FF4B4B'],
            x='ultima_att',
            y='cotação'
        )

        st.plotly_chart(fig_dolar)
        st.plotly_chart(fig_euro)

def main():
    dashs = Dashs()
    df = dashs.get_df()
        
    st.set_page_config(
        page_title="Cotação em Tempo Real",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state='collapsed'
    )

    st.header(":bar_chart: Cotação das Moedas")

    # Seleção de data na barra lateral
    selected_date = st.sidebar.date_input(
        label='Selecione a data',
        value=date.today()
    )

    # Filtrando o DataFrame pela data selecionada
    df_filtered = df[df['data'] == pd.to_datetime(selected_date)]

    if df_filtered.empty:
        st.write("Nenhum dado disponível para a data selecionada.")
    else:
        cotacao_dolar = df_filtered[df_filtered['moeda'] == 'Dolar']
        cotacao_euro = df_filtered[df_filtered['moeda'] == 'Euro']

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('Cotação Dólar')
            if not cotacao_dolar.empty:
                st.header(f"$ {cotacao_dolar['cotação'].values[0]}")
            else:
                st.header("Sem dados")

        with col2:
            st.markdown('Cotação Euro')
            if not cotacao_euro.empty:
                st.header(f":orange[{cotacao_euro['cotação'].values[0]}]")
            else:
                st.header("Sem dados")

        st.markdown("""---""")

        dashs.show_graph(df_filtered)

if __name__ == "__main__":
    # Iniciar o thread para coleta de dados
    threading.Thread(target=start_data_collection, daemon=True).start()
    
    main()