import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Dashboard Dinámico con Streamlit")

# Sidebar para la selección del dataset
st.sidebar.header("Opciones de Visualización")

# Generar un dataset de ejemplo


@st.cache_data
def load_data():
    dates = pd.date_range(start="2023-01-01", periods=100)
    data = pd.DataFrame({
        'Date': dates,
        'Value': np.random.randn(100).cumsum()
    })
    return data


data = load_data()

# Mostrar el dataset en la aplicación
if st.sidebar.checkbox("Mostrar datos"):
    st.subheader("Datos Generados")
    st.write(data)

# Selección del tipo de gráfico
chart_type = st.sidebar.selectbox("Selecciona el tipo de gráfico", [
                                  "Línea", "Barra", "Histograma"])

# Parámetros del histograma
bins = st.sidebar.slider("Número de bins del histograma", min_value=5,
                         max_value=50, value=10) if chart_type == "Histograma" else None

# Generar gráficos según la selección del usuario
st.subheader(f"Gráfico de {chart_type}")

if chart_type == "Línea":
    st.line_chart(data.set_index('Date'))
elif chart_type == "Barra":
    st.bar_chart(data.set_index('Date'))
elif chart_type == "Histograma":
    fig, ax = plt.subplots()
    ax.hist(data['Value'], bins=bins)
    st.pyplot(fig)

# Widgets interactivos
st.sidebar.subheader("Filtros de datos")

# Filtro de fechas
start_date = st.sidebar.date_input("Fecha de inicio", data['Date'].min())
end_date = st.sidebar.date_input("Fecha de fin", data['Date'].max())

# Filtrar datos según las fechas seleccionadas
filtered_data = data[(data['Date'] >= pd.Timestamp(start_date)) & (
    data['Date'] <= pd.Timestamp(end_date))]

if st.sidebar.checkbox("Mostrar datos filtrados"):
    st.subheader("Datos Filtrados")
    st.write(filtered_data)

# Selección de estadísticas
st.sidebar.subheader("Estadísticas")
if st.sidebar.checkbox("Mostrar estadísticas"):
    st.subheader("Estadísticas de los Datos")
    st.write(filtered_data.describe())

# Ejecutar la aplicación
if __name__ == "__main__":
    st.sidebar.header("Configuración del Dashboard")
