import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="App Analizadora de Datasets",
    page_icon="📊",
    layout="wide"
)

# ==============================
# INICIALIZACIÓN DE SESSION STATE
# ==============================

if "data" not in st.session_state:
    st.session_state.data = None

if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None

# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("📊 Menú Principal")

modulo = st.sidebar.selectbox(
    "Seleccione una opción",
    [
        "Home",
        "Carga y Perfil del Dataset",
        "Procesamiento de Datos",
        "Análisis Visual"
    ]
)

# ==============================
# IMÁGENES
# ==============================

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

st.write("Elaborado por MJHC")

# ==============================
# MÓDULO HOME
# ==============================

if modulo == "Home":

    st.title("📊 App Analizadora de Datasets con Streamlit")

    st.markdown("---")

    col1, col2 = st.columns([3,1])

    with col1:

        st.subheader("👨‍💻 Autor")

        st.write("Mario Huaraca")
        st.write("Diploma Business Analyst")
        st.write("2026")

        st.subheader("🎯 Objetivo")

        st.write(
            """
            Desarrollar una aplicación interactiva para
            cargar, procesar, explorar y visualizar
            datasets utilizando Python y Streamlit.
            """
        )

    with col2:

        st.info(
            """
            Tecnologías:
            - Python
            - Pandas
            - Streamlit
            - Plotly
            - Matplotlib
            - Seaborn
            - GitHub
            """
        )

    st.markdown("---")

    st.subheader("📚 Datasets disponibles")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "AI Impact on Jobs",
            "Superstore",
            "E-commerce Risk",
            "Teen Mental Health"
        ]
    )

    with tab1:

        st.write(
            """
            Dataset orientado al impacto de la
            Inteligencia Artificial sobre empleos,
            salarios, habilidades y demanda futura.
            """
        )

    with tab2:

        st.write(
            """
            Dataset de ventas que permite analizar
            pedidos, productos, regiones,
            descuentos y utilidades.
            """
        )

    with tab3:

        st.write(
            """
            Dataset enfocado en riesgo operativo
            dentro de plataformas de comercio
            electrónico.
            """
        )

    with tab4:

        st.write(
            """
            Dataset relacionado con hábitos
            digitales y bienestar emocional
            de adolescentes.
            """
        )

    st.markdown("---")

    st.warning(
        """
        Los resultados presentados tienen fines
        exploratorios y no reemplazan análisis
        profesionales o validaciones técnicas.
        """
    )

    if st.session_state.data is not None:

        st.success(
            f"Dataset cargado: {st.session_state.nombre_archivo}"
        )

    else:

        st.info(
            "Aún no se ha cargado ningún dataset."
        )

# ==============================
# MÓDULO CARGA Y PERFIL
# ==============================
elif modulo == "Carga y Perfil del Dataset":

    st.title("📂 Carga y Perfil del Dataset")

    archivo = st.file_uploader(
        "Seleccione un archivo",
        type=["csv", "xlsx"]
    )

    if archivo is not None:

        st.session_state.nombre_archivo = archivo.name

        if archivo.name.endswith(".csv"):

            st.session_state.data = pd.read_csv(archivo)

        elif archivo.name.endswith(".xlsx"):

            st.session_state.data = pd.read_excel(archivo)

        st.success("Archivo cargado correctamente")

    if st.session_state.data is not None:

        data = st.session_state.data

        st.subheader("Vista previa")

        st.dataframe(data.head())

#Metricas
        filas = data.shape[0]
        columnas = data.shape[1]

        variables_numericas = len(
            data.select_dtypes(
                include="number"
            ).columns
        )

        variables_categoricas = len(
            data.select_dtypes(
                include=["object","category"]
            ).columns
        )

        nulos = data.isnull().sum().sum()

        duplicados = data.duplicated().sum()

        col1,col2,col3 = st.columns(3)

        with col1:
            st.metric("Filas", filas)

        with col2:
            st.metric("Columnas", columnas)

        with col3:
            st.metric(
                "Variables Numéricas",
                variables_numericas
            )

        col4,col5,col6 = st.columns(3)

        with col4:
            st.metric(
                "Variables Categóricas",
                variables_categoricas
            )

        with col5:
            st.metric(
                "Valores Nulos",
                nulos
            )

        with col6:
            st.metric(
                "Duplicados",
                duplicados
            )

#Estructura
        st.subheader("Columnas")

        st.write(
            pd.DataFrame(
                {
                    "Columna": data.columns,
                    "Tipo": data.dtypes.astype(str)
                }
            )
        )

        columnas_seleccionadas = st.multiselect(
            "Seleccione columnas",
            data.columns,
            default=data.columns.tolist()
        )

        st.subheader(
            "Vista previa de columnas seleccionadas"
        )

        st.dataframe(
            data[columnas_seleccionadas].head()
        )

    else:

        st.info(
            "Por favor cargue un archivo CSV o XLSX."
        )






# ==============================
# MÓDULO PROCESAMIENTO DE DATOS
# ==============================

elif modulos == "Procesamiento de datos":

    st.subheader("Procesamiento de datos")

    if st.session_state.data is not None:

        data = st.session_state.data

        st.write("Dataset disponible para procesamiento:")
        st.dataframe(data)

        st.write("Valores nulos por columna:")
        st.write(data.isnull().sum())

    else:

        st.warning(
            "Primero debe cargar un dataset en el módulo "
            "'Carga y perfil del dataset'."
        )

# ==============================
# MÓDULO ANÁLISIS VISUAL
# ==============================

elif modulos == "Análisis visual":

    st.subheader("Análisis visual")

    if st.session_state.data is not None:

        data = st.session_state.data

        st.write("Dataset disponible para análisis visual:")
        st.dataframe(data)

        lista_columna_numerica = data.select_dtypes(
            include="number"
        ).columns.tolist()

        variable_numerica = st.selectbox(
            "Seleccione la columna numérica",
            lista_columna_numerica
        )

        lista_columna_categorica = data.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        variable_categorica = st.selectbox(
            "Seleccione la columna categórica",
            lista_columna_categorica
        )

    else:

        st.warning(
            "Primero debe cargar un dataset en el módulo "
            "'Carga y perfil del dataset'."
        )
