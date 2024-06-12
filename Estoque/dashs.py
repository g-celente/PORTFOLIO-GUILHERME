import pandas as pd
import numpy as np
import plotly_express as px
import streamlit as st

df = pd.read_csv('sales.csv')

def sum_sales(dataframe):
    total_sales = dataframe['Faturamento'].sum()
    return total_sales

def total_quantity(dataframe):
    total_vendas = dataframe['Quantidade'].sum()
    return total_vendas

def print_figs(df):
    sales_by_month = (
        df.groupby(by='Mes').sum(numeric_only=True)[['Faturamento']].sort_values('Mes')
    )

    sales_by_product = (
        df.groupby(by='Produto').sum(numeric_only=True)[['Faturamento']].sort_values('Produto')
    )

    fig_sale_pie = px.bar(
        sales_by_product,
        title='Vendas Por Produtos',
        color_discrete_sequence=['#FF4B4B'],
        x = 'Faturamento',
        y=sales_by_product.index,
        width=500
        )
    fig_sale_pie.update_layout(
        xaxis=dict(
            visible=False
        )
    )

    fig_sale = px.pie(
        sales_by_product,
        title='Vendas Por Produtos',
        color_discrete_sequence=['#FF4B4B'],
        names=sales_by_product.index,
        values='Faturamento',
        width=500
    )
    

    fig_sale_by_month = px.area(
        sales_by_month,
        title="Vendas Por Meses",
        color_discrete_sequence=["#FF4B4B"],
        x = sales_by_month.index,
        y= 'Faturamento',
        )

    fig_sale_by_product = px.bar(
        sales_by_product,
        title="Vendas por Produtos",
        x= sales_by_product.index,
        y = 'Faturamento',
        width=500,
        color_discrete_sequence=["#FF4B4B"]
    )

    fig_sales_in_maps = px.choropleth(
        df,
        locations="Estado", 
        locationmode="USA-states", 
        color="Quantidade", 
        scope="usa",
        template="plotly_dark",
        width=1150
    )
    fig_sales_in_maps.update_geos(fitbounds="locations", visible=True)
    fig_sales_in_maps.update_layout(
        title="Vendas Nos Estados Unidos",
        geo=dict(bgcolor= 'rgba(0,0,0,0)', lakecolor="#1f242d"),
        margin={"r":0,"t":25,"l":0,"b":0},
        paper_bgcolor="#1f242d",
        plot_bgcolor="#1f242d",
    )


    col1, col2 = st.columns(2)
    col1.plotly_chart(fig_sale_by_month)
    col2.plotly_chart(fig_sale_by_product)
    col3, col4 = st.columns(2)
    col3.plotly_chart(fig_sale_pie)
    col4.plotly_chart(fig_sale)
    st.plotly_chart(fig_sales_in_maps)


def main (df):
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
        default=df['Mes'].unique().tolist()
    )

    df = df.query("Mes == @month")

    total_sales = round(sum_sales(df),2)
    total_vendas = total_quantity(df)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('Faturamento Total')
        st.header(f"$ {total_sales}")
    with col2:
        st.markdown('Quantidade total de Vendas')
        st.header(f":orange[{total_vendas}]")
    st.markdown("""---""")

    print_figs(df)


if __name__ == '__main__':
    main(df)