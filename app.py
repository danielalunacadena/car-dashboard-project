import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Car Sales Dashboard")

st.write("""
This dashboard explores the relationship between vehicle mileage and price 
using a dataset of used car listings.

Use the buttons below to generate visualizations and analyze how mileage 
affects car prices.
""")

df = pd.read_csv("vehicles_us.csv")

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Cars", df.shape[0])

with col2:
    st.metric("Average Price", f"${df['price'].mean():,.0f}")

with col3:
    st.metric("Average Mileage", f"{df['odometer'].mean():,.0f}")

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Histograma del kilometraje")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

scatter_button = st.button("Construir scatter plot")

if scatter_button:
    st.write("Relación entre precio y kilometraje")
    fig2 = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig2)
    