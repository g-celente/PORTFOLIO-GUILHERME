import pandas as pd
from database import Connection
import streamlit as st
import plotly_express as px
from api import start_data_collection
import threading

class Dashs:
    def __init__(self):
        self.db = Connection()
    
    def get_df(self):
        conn = self.db.get_connection()
        self.df = pd.read_sql("SELECT * FROM coins", conn)
        return self.df

    def show_graph(self):
        df_moeda = self.df[self.df['moeda'] == 'Dolar']

        fig_dolar = px.area(
            df_moeda,
            title='Cotação Dólar',
            color_discrete_sequence=['#FF4B4B'],
            x='ultima_att',
            y='cotação'
        )

        df_euro = self.df[self.df['moeda'] == 'Euro']

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

    month = st.sidebar.multiselect(
        key=1,
        label='Data',
        options=df['data'].unique().tolist(),
        default=df['data'].unique().tolist()
    )

    cotacao_dolar = df[df['moeda'] == 'Dolar']
    cotacao_euro = df[df['moeda'] == 'Euro']

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('Cotação Dólar')
        st.header(f"$ {cotacao_dolar['cotação'].values[0]}")
    with col2:
        st.markdown('Cotação Euro')
        st.header(f":orange[{cotacao_euro['cotação'].values[0]}]")
    st.markdown("""---""")

    dashs.show_graph()

if __name__ == "__main__":
    # Iniciar o thread para coleta de dados
    threading.Thread(target=start_data_collection, daemon=True).start()
    
    main()