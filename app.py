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

st.sidebar.header("Filters")

fuel_filter = st.sidebar.multiselect(
    "Fuel Type",
    options=df["fuel"].dropna().unique(),
    default=df["fuel"].dropna().unique()
)

df = df[df["fuel"].isin(fuel_filter)]

st.sidebar.header("Filters")

fuel = st.sidebar.multiselect(
    "Fuel Type",
    options=df["fuel"].dropna().unique(),
    default=df["fuel"].dropna().unique()
)

df = df[df["fuel"].isin(fuel)]

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
    
    st.subheader("Average Price by Year")

price_year = df.groupby("model_year")["price"].mean().reset_index()

fig_year = px.line(price_year, x="model_year", y="price")

st.plotly_chart(fig_year)

st.subheader("Price by Fuel Type")

fig_fuel = px.box(df, x="fuel", y="price", color="transmission")

st.plotly_chart(fig_fuel)