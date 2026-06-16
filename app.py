import streamlit as st

##Titulo
st.title("Proyecto Final Diploma BI")

##Sidebar
st.sidebar.title("Parámetros")

##Images
st.image("Python_logo.png")
st.sidebar.image("DMC.png")

st.write("Elaborado por MJHC")

##Carga de Archivo
archivo = st.file_uploader("Cargue el archivo excel o csv")


