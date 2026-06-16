import streamlit as st
import pandas as pd
import numpy as np
import re
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Analisis de Datasets",
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

elif modulo == "Procesamiento de Datos":

    st.title("⚙️ Procesamiento de Datos")

    if st.session_state.data is not None:

        data = st.session_state.data.copy()

#Estandarizacion
        st.subheader("1️⃣ Estandarización de columnas")

        columnas_originales = data.columns.tolist()

        data.columns = [
            re.sub(
                r'[^A-Za-z0-9_]',
                '',
                col.strip().replace(" ", "_").lower()
            )
            for col in data.columns
        ]

        columnas_nuevas = data.columns.tolist()

        st.write(
            pd.DataFrame({
                "Original": columnas_originales,
                "Nueva": columnas_nuevas
            })
        )

#Variables
        st.subheader("2️⃣ Clasificación de variables")

        variables_numericas = data.select_dtypes(
            include="number"
        ).columns.tolist()

        variables_categoricas = data.select_dtypes(
            include=["object","category"]
        ).columns.tolist()

        variables_fecha = data.select_dtypes(
            include=["datetime64"]
        ).columns.tolist()

        col1,col2,col3 = st.columns(3)

        with col1:
            st.metric(
                "Numéricas",
                len(variables_numericas)
            )

        with col2:
            st.metric(
                "Categóricas",
                len(variables_categoricas)
            )

        with col3:
            st.metric(
                "Fechas",
                len(variables_fecha)
            )

#Conversion de fechas
       #Conversion de fechas
        st.subheader("3️⃣ Conversión de fechas")

        columnas_texto = data.select_dtypes(
            include=["object"]
        ).columns.tolist()

        columnas_fecha = st.multiselect(
            "Seleccione columnas fecha",
            columnas_texto
        )

        for col in columnas_fecha:

            data[col] = pd.to_datetime(
                data[col],
                errors="coerce"
            )

#Nulos
        st.subheader("4️⃣ Valores faltantes")

        nulos = data.isnull().sum()

        porcentaje_nulos = (
            nulos / len(data)
        ) * 100

        tabla_nulos = pd.DataFrame(
            {
                "Nulos": nulos,
                "% Nulos": porcentaje_nulos.round(2)
            }
        )

        st.dataframe(
            tabla_nulos.sort_values(
                "Nulos",
                ascending=False
            )
        )

#Duplicados
        st.subheader("5️⃣ Duplicados")

        duplicados = data.duplicated().sum()

        st.metric(
            "Registros duplicados",
            duplicados
        )

#Estadisticas
        st.subheader("6️⃣ Estadística descriptiva")

        if len(variables_numericas) > 0:

            st.dataframe(
                data[
                    variables_numericas
                ].describe()
            )

        else:

            st.warning(
                "No existen variables numéricas."
            )

#Outliers
        st.subheader("7️⃣ Detección de Outliers")

        if len(variables_numericas) > 0:

            columna_outlier = st.selectbox(
                "Seleccione variable",
                variables_numericas
            )

            Q1 = data[columna_outlier].quantile(0.25)
            Q3 = data[columna_outlier].quantile(0.75)

            IQR = Q3 - Q1

            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR

            outliers = data[
                (data[columna_outlier] < limite_inferior)
                |
                (data[columna_outlier] > limite_superior)
            ]

            st.metric(
                "Cantidad de Outliers",
                len(outliers)
            )

            if st.checkbox(
                "Mostrar Outliers"
            ):

                st.dataframe(outliers)

        else:

            st.warning(
                "No existen variables numéricas."
            )

#Filtros
        st.subheader("8️⃣ Filtros dinámicos")

        data_filtrado = data.copy()

        if len(variables_categoricas) > 0:

            columna_cat = st.selectbox(
                "Variable categórica",
                variables_categoricas
            )

            categorias = sorted(
                data[columna_cat]
                .dropna()
                .unique()
                .tolist()
            )

            seleccion = st.multiselect(
                "Seleccione categorías",
                categorias
            )

            if len(seleccion) > 0:

                data_filtrado = (
                    data_filtrado[
                        data_filtrado[
                            columna_cat
                        ].isin(seleccion)
                    ]
                )

        if len(variables_numericas) > 0:

            columna_num = st.selectbox(
                "Variable numérica",
                variables_numericas
            )

            minimo = float(
                data_filtrado[columna_num].min()
            )

            maximo = float(
                data_filtrado[columna_num].max()
            )

            rango = st.slider(
                "Seleccione rango",
                minimo,
                maximo,
                (minimo, maximo)
            )

            data_filtrado = (
                data_filtrado[
                    (
                        data_filtrado[columna_num]
                        >= rango[0]
                    )
                    &
                    (
                        data_filtrado[columna_num]
                        <= rango[1]
                    )
                ]
            )

        st.subheader("Dataset filtrado")

        st.write(
            f"Registros: {len(data_filtrado)}"
        )

        st.dataframe(data_filtrado)

        st.session_state.data_procesado = data_filtrado

    else:

        st.warning(
            "Primero debe cargar un dataset en "
            "'Carga y Perfil del Dataset'."
        )

# ==============================
# MÓDULO ANÁLISIS VISUAL
# ==============================
elif modulo == "Análisis visual":

    st.title("📊 Análisis Visual")

    if st.session_state.data is not None:

        data = st.session_state.data.copy()

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [
                "📋 Resumen",
                "📈 Univariado",
                "📊 Bivariado",
                "🔥 Correlación",
                "📅 Temporal",
                "💡 Insights"
            ]
        )

        with tab1:

            st.subheader("Resumen General")

            col1,col2,col3,col4 = st.columns(4)

            with col1:
                st.metric("Filas", data.shape[0])

            with col2:
                st.metric("Columnas", data.shape[1])

            with col3:
                st.metric(
                    "Nulos",
                    data.isnull().sum().sum()
                )

            with col4:
                st.metric(
                    "Duplicados",
                    data.duplicated().sum()
                )

            st.dataframe(data.head())
