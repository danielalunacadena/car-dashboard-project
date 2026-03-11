import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Car Sales Dashboard")

df = pd.read_csv("vehicles_us.csv")

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