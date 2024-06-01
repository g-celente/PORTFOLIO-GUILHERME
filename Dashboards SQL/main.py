import pyodbc 
import pandas as pd
import numpy as np
import plotly_express as px
import streamlit as st

conection = (
    "Driver={SQL Server};"
    "Server=DESKTOP-4V72RH2;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)

conexao = pyodbc.connect(conection)

querys = 'SELECT * FROM vendas'

df = pd.read_sql(querys,conexao)

def sum_sales(dataframe):
    total_sales = dataframe['Faturamento'].sum()
    return total_sales

def total_quantity(dataframe):
    total_vendas = dataframe['Quantidade'].sum()
    return total_vendas

def print_figs():
    sales_by_month = (
        df.groupby(by='Mes').sum(numeric_only=True)[['Faturamento']].sort_values('Mes')
    )

    sales_by_product = (
        df.groupby(by='Produto').sum(numeric_only=True)[['Faturamento']].sort_values('Produto')
    )

    sales_by_store = (
        df.groupby(by='Loja').sum(numeric_only=True)[['Faturamento']].sort_values('Loja')
    )


    fig_sale_by_month = px.area(
        sales_by_month,
        title="Vendas Por Meses",
        color_discrete_sequence=["#FF4B4B"]
        )

    fig_sale_by_product = px.bar(
        sales_by_product,
        title="Vendas por Produtos",
        width=500,
        color_discrete_sequence=["#FF4B4B"]
    )

    fig_sale_by_store = px.bar(
        sales_by_store,
        title="Vendas Por Loja",
        width=500,
        color_discrete_sequence=["#FF4B4B"]
    )
    col1, col2 = st.columns(2)
    st.plotly_chart(fig_sale_by_month)
    col1.plotly_chart(fig_sale_by_product)
    col2.plotly_chart(fig_sale_by_store)

st.set_page_config(
    page_title="Dashboard Vendas",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state='collapsed'
)

st.header(":bar_chart: Dashboard Faturamento Total")

month = st.sidebar.multiselect(
    key= 1,
    label='Mês',
    options=df['Mes'].unique().tolist(),
    default=df['Mes'].unique().tolist(),
)

df = df.query("Mes == @month")

total_sales = round(sum_sales(df),2)
total_vendas = total_quantity(df)

col1, col2 = st.columns(2)
col1.metric('Faturamente Total', total_sales)
col2.metric('Quantidade de Vendas', total_vendas)
st.markdown("""---""")


print_figs()