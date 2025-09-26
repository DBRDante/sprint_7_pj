import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')
df.info()
st.header('Visualización Interactiva de Vehículos Usados en EE.UU.')

# Checkbox para histograma de precios
if st.checkbox('Mostrar histograma de precios'):
    st.write('Distribución de precios de los vehículos')
    fig_price = px.histogram(df, x='price', nbins=50,
                             title='Distribución de Precios')
    st.plotly_chart(fig_price, use_container_width=True)

# Checkbox para gráfico de dispersión: Precio vs Odómetro
if st.checkbox('Mostrar gráfico de dispersión: Precio vs Odómetro'):
    st.write('Relación entre precio y kilometraje')
    fig_scatter = px.scatter(df, x='odometer', y='price',
                             title='Precio vs Odómetro')
    st.plotly_chart(fig_scatter, use_container_width=True)
