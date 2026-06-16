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

##Validación de archivo
if archivo is not None :
  if archivo.name.endswith(".csv"):
    data = pd.read_csv(archivo)
    st.write(data)
  elif archivo.name.endswith(".xlsx"):
    data = pd.read_excel(archivo)
    st.write(data)
  else:
    st.write("Formato no válido")
else :
  st.write("Por favor cargue su archivo")
