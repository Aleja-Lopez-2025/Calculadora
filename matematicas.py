# ==========================================================
# CALCULADORA CIENTÍFICA PROFESIONAL
# Streamlit + NumPy + SymPy + Pandas + Plotly
# ==========================================================

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from scipy import stats

import sympy as sp

from math import *
from datetime import datetime

# ==========================================================
# CONFIGURACIÓN STREAMLIT
# ==========================================================

st.set_page_config(
    page_title="Calculadora Científica Pro",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CSS PROFESIONAL
# ==========================================================

st.markdown("""
<style>

:root{
--primary:#2563eb;
--bg:#0f172a;
--card:#1e293b;
--text:#ffffff;
--gray:#94a3b8;
}

.main{
background-color:var(--bg);
color:var(--text);
}

section[data-testid="stSidebar"]{
background:#111827;
}

.card{
background:var(--card);
padding:20px;
border-radius:16px;
box-shadow:0 0 15px rgba(0,0,0,.3);
margin-bottom:15px;
animation:fadeIn .5s ease;
}

@keyframes fadeIn{
from{
opacity:0;
transform:translateY(10px);
}
to{
opacity:1;
transform:translateY(0);
}
}

.big-title{
font-size:36px;
font-weight:700;
color:white;
}

.subtitle{
font-size:18px;
color:#cbd5e1;
}

.stButton button{
background:#2563eb;
color:white;
border:none;
border-radius:10px;
padding:10px 20px;
font-weight:bold;
transition:0.3s;
}

.stButton button:hover{
transform:scale(1.02);
background:#1d4ed8;
}

hr{
border:1px solid #334155;
}

.metric-card{
background:#1e293b;
padding:15px;
border-radius:12px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================================
# HISTORIAL
# ==========================================================

def save_history(operation, result):

    st.session_state.history.append({
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Operación": operation,
        "Resultado": str(result)
    })

# ==========================================================
# UTILIDADES
# ==========================================================

class Utils:

    @staticmethod
    def card(title):

        st.markdown(
            f"""
            <div class="card">
            <h3>{title}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================================
# MOTOR CIENTÍFICO
# ==========================================================

class ScientificCalculator:

    allowed = {
        "sin":sin,
        "cos":cos,
        "tan":tan,
        "asin":asin,
        "acos":acos,
        "atan":atan,

        "sinh":sinh,
        "cosh":cosh,
        "tanh":tanh,

        "sqrt":sqrt,
        "log":log10,
        "ln":log,

        "exp":exp,
        "abs":abs,
        "factorial":factorial,

        "pi":pi,
        "e":e
    }

    @staticmethod
    def calculate(expression):

        try:

            result = eval(
                expression,
                {"__builtins__":{}},
                ScientificCalculator.allowed
            )

            save_history(expression, result)

            return result

        except Exception as e:
            raise ValueError(str(e))

# ==========================================================
# MENÚ LATERAL
# ==========================================================

st.sidebar.markdown("# 🧮 Calculadora Pro")

menu = st.sidebar.radio(
    "Navegación",
    [
        "🧮 Calculadora",
        "📈 Graficador",
        "📊 Estadística",
        "🔢 Ecuaciones",
        "🧱 Matrices",
        "🔄 Conversores",
        "📜 Historial",
        "ℹ️ Ayuda"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Calculadora Científica Profesional

✔ NumPy
✔ SciPy
✔ SymPy
✔ Plotly
✔ Pandas
"""
)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="big-title">
🧮 Calculadora Científica Profesional
</div>

<div class="subtitle">
Python + Streamlit + NumPy + SymPy + Plotly
</div>
""",
unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# SECCIÓN CALCULADORA
# ==========================================================

if menu == "🧮 Calculadora":

    st.subheader("Calculadora Científica")

    expression = st.text_input(
        "Expresión matemática",
        placeholder="Ej: sin(pi/2)+sqrt(25)"
    )

    col1,col2 = st.columns(2)

    with col1:

        if st.button("Calcular"):

            try:

                result = ScientificCalculator.calculate(
                    expression
                )

                st.success(f"Resultado: {result}")

                try:
                    st.latex(
                        sp.latex(
                            sp.sympify(result)
                        )
                    )
                except:
                    pass

            except Exception as e:
                st.error(str(e))

    with col2:

        if st.button("Limpiar"):
            st.rerun()

    st.markdown("---")

    st.subheader("Conversión Angular")

    angle = st.number_input(
        "Ángulo",
        value=0.0
    )

    c1,c2 = st.columns(2)

    with c1:

        if st.button("Grados → Radianes"):

            result = np.deg2rad(angle)

            st.success(result)

            save_history(
                f"deg2rad({angle})",
                result
            )

    with c2:

        if st.button("Radianes → Grados"):

            result = np.rad2deg(angle)

            st.success(result)

            save_history(
                f"rad2deg({angle})",
                result
            )
# ==========================================================
# ECUACIONES
# ==========================================================

elif menu == "🔢 Ecuaciones":

    st.subheader("🔢 Resolución de Ecuaciones")

    tab1, tab2, tab3 = st.tabs(
        [
            "Cuadrática",
            "Sistema 2x2",
            "Sistema 3x3"
        ]
    )

    # ======================================================
    # ECUACIÓN CUADRÁTICA
    # ======================================================

    with tab1:

        st.markdown(
            """
            Resolver:

            ax² + bx + c = 0
            """
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            a = st.number_input(
                "a",
                value=1.0,
                key="qa"
            )

        with col2:
            b = st.number_input(
                "b",
                value=0.0,
                key="qb"
            )

        with col3:
            c = st.number_input(
                "c",
                value=0.0,
                key="qc"
            )

        if st.button(
            "Resolver cuadrática"
        ):

            try:

                x = sp.Symbol("x")

                discriminante = (
                    b**2 - 4*a*c
                )

                st.info(
                    f"Discriminante = {discriminante}"
                )

                expr = (
                    a*x**2 +
                    b*x +
                    c
                )

                soluciones = sp.solve(
                    expr,
                    x
                )

                st.subheader(
                    "Soluciones"
                )

                for i, sol in enumerate(
                    soluciones,
                    start=1
                ):
                    st.write(
                        f"x{i} = {sol}"
                    )

                st.subheader(
                    "Pasos"
                )

                st.latex(
                    f"\\Delta={b}^2-4({a})({c})"
                )

                st.latex(
                    f"\\Delta={discriminante}"
                )

                st.latex(
                    r"x=\frac{-b\pm\sqrt{\Delta}}{2a}"
                )

                save_history(
                    f"{a}x²+{b}x+{c}=0",
                    soluciones
                )

            except Exception as e:
                st.error(str(e))

    # ======================================================
    # SISTEMA 2X2
    # ======================================================

    with tab2:

        st.markdown(
            """
            a1x + b1y = c1

            a2x + b2y = c2
            """
        )

        c1, c2 = st.columns(2)

        with c1:

            a1 = st.number_input(
                "a1",
                value=1.0,
                key="a1"
            )

            b1 = st.number_input(
                "b1",
                value=1.0,
                key="b1"
            )

            c_1 = st.number_input(
                "c1",
                value=1.0,
                key="c1"
            )

        with c2:

            a2 = st.number_input(
                "a2",
                value=1.0,
                key="a2"
            )

            b2 = st.number_input(
                "b2",
                value=1.0,
                key="b2"
            )

            c_2 = st.number_input(
                "c2",
                value=1.0,
                key="c2"
            )

        if st.button(
            "Resolver sistema 2x2"
        ):

            try:

                A = np.array(
                    [
                        [a1,b1],
                        [a2,b2]
                    ]
                )

                B = np.array(
                    [
                        c_1,
                        c_2
                    ]
                )

                sol = np.linalg.solve(
                    A,
                    B
                )

                st.success(
                    f"x = {sol[0]}"
                )

                st.success(
                    f"y = {sol[1]}"
                )

                st.write(
                    "Matriz A"
                )

                st.dataframe(A)

                st.write(
                    "Vector B"
                )

                st.dataframe(B)

                save_history(
                    "Sistema 2x2",
                    sol
                )

            except Exception as e:
                st.error(
                    f"Error: {e}"
                )

    # ======================================================
    # SISTEMA 3X3
    # ======================================================

    with tab3:

        st.markdown(
            """
            Sistema lineal 3x3
            """
        )

        values = []

        cols = st.columns(4)

        labels = [
            "a1","b1","c1","d1",
            "a2","b2","c2","d2",
            "a3","b3","c3","d3"
        ]

        for label in labels:

            values.append(
                st.number_input(
                    label,
                    value=1.0,
                    key=f"3x3_{label}"
                )
            )

        if st.button(
            "Resolver sistema 3x3"
        ):

            try:

                A = np.array(
                    [
                        values[0:3],
                        values[4:7],
                        values[8:11]
                    ]
                )

                B = np.array(
                    [
                        values[3],
                        values[7],
                        values[11]
                    ]
                )

                sol = np.linalg.solve(
                    A,
                    B
                )

                st.success(
                    f"x = {sol[0]}"
                )

                st.success(
                    f"y = {sol[1]}"
                )

                st.success(
                    f"z = {sol[2]}"
                )

                st.dataframe(A)

                save_history(
                    "Sistema 3x3",
                    sol
                )

            except Exception as e:
                st.error(str(e))

# ==========================================================
# MATRICES
# ==========================================================

elif menu == "🧱 Matrices":

    st.subheader("🧱 Operaciones Matriciales")

    rows = st.number_input(
        "Filas",
        min_value=2,
        max_value=10,
        value=3
    )

    cols = st.number_input(
        "Columnas",
        min_value=2,
        max_value=10,
        value=3
    )

    st.markdown("### Matriz A")

    dfA = pd.DataFrame(
        np.zeros((rows, cols))
    )

    matrixA = st.data_editor(
        dfA,
        key="matrixA"
    )

    st.markdown("### Matriz B")

    dfB = pd.DataFrame(
        np.zeros((rows, cols))
    )

    matrixB = st.data_editor(
        dfB,
        key="matrixB"
    )

    A = np.array(
        matrixA,
        dtype=float
    )

    B = np.array(
        matrixB,
        dtype=float
    )

    st.markdown("---")

    c1,c2,c3 = st.columns(3)

    # ======================================================
    # SUMA
    # ======================================================

    with c1:

        if st.button(
            "A + B"
        ):

            try:

                result = A + B

                st.dataframe(result)

                save_history(
                    "A+B",
                    result
                )

            except Exception as e:
                st.error(str(e))

    # ======================================================
    # RESTA
    # ======================================================

    with c2:

        if st.button(
            "A - B"
        ):

            try:

                result = A - B

                st.dataframe(result)

                save_history(
                    "A-B",
                    result
                )

            except Exception as e:
                st.error(str(e))

    # ======================================================
    # MULTIPLICACIÓN
    # ======================================================

    with c3:

        if st.button(
            "A × B"
        ):

            try:

                result = np.matmul(
                    A,
                    B
                )

                st.dataframe(result)

                save_history(
                    "A×B",
                    result
                )

            except Exception as e:
                st.error(str(e))

    st.markdown("---")

    d1,d2,d3 = st.columns(3)

    # ======================================================
    # DETERMINANTE
    # ======================================================

    with d1:

        if st.button(
            "Det(A)"
        ):

            try:

                result = np.linalg.det(
                    A
                )

                st.success(result)

                save_history(
                    "Det(A)",
                    result
                )

            except Exception as e:
                st.error(str(e))

    # ======================================================
    # INVERSA
    # ======================================================

    with d2:

        if st.button(
            "Inv(A)"
        ):

            try:

                result = np.linalg.inv(
                    A
                )

                st.dataframe(result)

                save_history(
                    "Inv(A)",
                    result
                )

            except Exception as e:
                st.error(str(e))

    # ======================================================
    # TRANSPUESTA
    # ======================================================

    with d3:

        if st.button(
            "Aᵀ"
        ):

            try:

                result = A.T

                st.dataframe(result)

                save_history(
                    "Aᵀ",
                    result
                )

            except Exception as e:
                st.error(str(e))

# ==========================================================
# GRAFICADOR MATEMÁTICO
# ==========================================================

elif menu == "📈 Graficador":

    st.subheader("📈 Graficador Matemático")

    expression = st.text_input(
        "Función f(x)",
        value="sin(x)"
    )

    col1, col2 = st.columns(2)

    with col1:

        x_min = st.number_input(
            "Valor mínimo",
            value=-10.0
        )

    with col2:

        x_max = st.number_input(
            "Valor máximo",
            value=10.0
        )

    if st.button("Generar gráfica"):

        try:

            x = sp.Symbol("x")

            expr = sp.sympify(expression)

            f = sp.lambdify(
                x,
                expr,
                modules=["numpy"]
            )

            x_values = np.linspace(
                x_min,
                x_max,
                1000
            )

            y_values = f(x_values)

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode="lines",
                    name="f(x)"
                )
            )

            fig.update_layout(
                template="plotly_dark",
                title=f"f(x) = {expression}",
                xaxis_title="x",
                yaxis_title="y",
                height=650
            )

            fig.update_xaxes(
                showgrid=True
            )

            fig.update_yaxes(
                showgrid=True
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            save_history(
                f"Gráfica {expression}",
                "Generada"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# ==========================================================
# ESTADÍSTICA
# ==========================================================

elif menu == "📊 Estadística":

    st.subheader("📊 Estadística Descriptiva")

    data_input = st.text_area(
        "Datos separados por comas",
        "1,2,3,4,5"
    )

    if st.button(
        "Calcular estadísticas"
    ):

        try:

            data = np.array(
                [
                    float(i.strip())
                    for i in data_input.split(",")
                ]
            )

            media = np.mean(data)

            mediana = np.median(data)

            moda = stats.mode(
                data,
                keepdims=True
            )

            varianza = np.var(data)

            desviacion = np.std(data)

            rango = np.max(data) - np.min(data)

            minimo = np.min(data)

            maximo = np.max(data)

            df = pd.DataFrame(
                {
                    "Métrica":[
                        "Media",
                        "Mediana",
                        "Moda",
                        "Varianza",
                        "Desv. Estándar",
                        "Rango",
                        "Mínimo",
                        "Máximo"
                    ],
                    "Valor":[
                        media,
                        mediana,
                        moda.mode[0],
                        varianza,
                        desviacion,
                        rango,
                        minimo,
                        maximo
                    ]
                }
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            col1,col2,col3,col4 = st.columns(4)

            with col1:
                st.metric(
                    "Media",
                    round(media,4)
                )

            with col2:
                st.metric(
                    "Mediana",
                    round(mediana,4)
                )

            with col3:
                st.metric(
                    "Moda",
                    round(float(moda.mode[0]),4)
                )

            with col4:
                st.metric(
                    "Rango",
                    round(rango,4)
                )

            fig = px.histogram(
                data,
                nbins=20,
                template="plotly_dark",
                title="Distribución"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            save_history(
                "Estadística",
                "Calculada"
            )

        except Exception as e:

            st.error(str(e))

    st.markdown("---")

    st.subheader("🔢 Combinatoria")

    c1,c2 = st.columns(2)

    with c1:

        n_perm = st.number_input(
            "n (Permutaciones)",
            min_value=0,
            value=5,
            key="perm_n"
        )

        r_perm = st.number_input(
            "r",
            min_value=0,
            value=2,
            key="perm_r"
        )

        if st.button(
            "Calcular nPr"
        ):

            try:

                result = (
                    factorial(n_perm)
                    /
                    factorial(
                        n_perm-r_perm
                    )
                )

                st.success(
                    f"nPr = {result}"
                )

                save_history(
                    f"{n_perm}P{r_perm}",
                    result
                )

            except Exception as e:

                st.error(str(e))

    with c2:

        n_comb = st.number_input(
            "n (Combinaciones)",
            min_value=0,
            value=5,
            key="comb_n"
        )

        r_comb = st.number_input(
            "r ",
            min_value=0,
            value=2,
            key="comb_r"
        )

        if st.button(
            "Calcular nCr"
        ):

            try:

                result = (
                    factorial(n_comb)
                    /
                    (
                        factorial(r_comb)
                        *
                        factorial(
                            n_comb-r_comb
                        )
                    )
                )

                st.success(
                    f"nCr = {result}"
                )

                save_history(
                    f"{n_comb}C{r_comb}",
                    result
                )

            except Exception as e:

                st.error(str(e))
                # ==========================================================
# CONVERSORES
# ==========================================================

elif menu == "🔄 Conversores":

    st.subheader("🔄 Conversores de Unidades")

    categoria = st.selectbox(
        "Categoría",
        [
            "Longitud",
            "Masa",
            "Temperatura",
            "Tiempo",
            "Velocidad",
            "Área",
            "Volumen"
        ]
    )

    # ======================================================
    # LONGITUD
    # ======================================================

    if categoria == "Longitud":

        unidades = ["m", "km", "cm", "mm"]

        valor = st.number_input("Valor", value=1.0)

        origen = st.selectbox(
            "Desde",
            unidades
        )

        destino = st.selectbox(
            "Hacia",
            unidades
        )

        factores = {
            "m": 1,
            "km": 1000,
            "cm": 0.01,
            "mm": 0.001
        }

        if st.button("Convertir Longitud"):

            metros = valor * factores[origen]

            resultado = metros / factores[destino]

            st.success(resultado)

            save_history(
                f"{valor} {origen} -> {destino}",
                resultado
            )

    # ======================================================
    # MASA
    # ======================================================

    elif categoria == "Masa":

        unidades = ["kg", "g", "lb"]

        valor = st.number_input(
            "Valor",
            value=1.0,
            key="masa"
        )

        origen = st.selectbox(
            "Desde",
            unidades,
            key="masa1"
        )

        destino = st.selectbox(
            "Hacia",
            unidades,
            key="masa2"
        )

        factores = {
            "kg": 1,
            "g": 0.001,
            "lb": 0.453592
        }

        if st.button("Convertir Masa"):

            kg = valor * factores[origen]

            resultado = kg / factores[destino]

            st.success(resultado)

            save_history(
                "Conversión Masa",
                resultado
            )

    # ======================================================
    # TEMPERATURA
    # ======================================================

    elif categoria == "Temperatura":

        unidades = [
            "Celsius",
            "Fahrenheit",
            "Kelvin"
        ]

        valor = st.number_input(
            "Valor",
            value=0.0,
            key="temp"
        )

        origen = st.selectbox(
            "Desde",
            unidades,
            key="temp1"
        )

        destino = st.selectbox(
            "Hacia",
            unidades,
            key="temp2"
        )

        if st.button("Convertir Temperatura"):

            resultado = valor

            if origen == "Celsius":

                if destino == "Fahrenheit":
                    resultado = (valor * 9/5) + 32

                elif destino == "Kelvin":
                    resultado = valor + 273.15

            elif origen == "Fahrenheit":

                if destino == "Celsius":
                    resultado = (valor - 32) * 5/9

                elif destino == "Kelvin":
                    resultado = ((valor - 32) * 5/9) + 273.15

            elif origen == "Kelvin":

                if destino == "Celsius":
                    resultado = valor - 273.15

                elif destino == "Fahrenheit":
                    resultado = ((valor - 273.15) * 9/5) + 32

            st.success(resultado)

            save_history(
                "Conversión Temperatura",
                resultado
            )

    # ======================================================
    # TIEMPO
    # ======================================================

    elif categoria == "Tiempo":

        unidades = [
            "segundos",
            "minutos",
            "horas",
            "días"
        ]

        valor = st.number_input(
            "Valor",
            value=1.0,
            key="tiempo"
        )

        origen = st.selectbox(
            "Desde",
            unidades,
            key="tiempo1"
        )

        destino = st.selectbox(
            "Hacia",
            unidades,
            key="tiempo2"
        )

        factores = {
            "segundos":1,
            "minutos":60,
            "horas":3600,
            "días":86400
        }

        if st.button("Convertir Tiempo"):

            segundos = valor * factores[origen]

            resultado = segundos / factores[destino]

            st.success(resultado)

            save_history(
                "Conversión Tiempo",
                resultado
            )

    # ======================================================
    # VELOCIDAD
    # ======================================================

    elif categoria == "Velocidad":

        unidades = [
            "km/h",
            "m/s"
        ]

        valor = st.number_input(
            "Valor",
            value=1.0,
            key="vel"
        )

        origen = st.selectbox(
            "Desde",
            unidades,
            key="vel1"
        )

        destino = st.selectbox(
            "Hacia",
            unidades,
            key="vel2"
        )

        if st.button("Convertir Velocidad"):

            if origen == destino:

                resultado = valor

            elif origen == "km/h":

                resultado = valor / 3.6

            else:

                resultado = valor * 3.6

            st.success(resultado)

            save_history(
                "Conversión Velocidad",
                resultado
            )

    # ======================================================
    # ÁREA
    # ======================================================

    elif categoria == "Área":

        valor = st.number_input(
            "Valor",
            value=1.0,
            key="area"
        )

        origen = st.selectbox(
            "Desde",
            ["m²", "km²"],
            key="area1"
        )

        destino = st.selectbox(
            "Hacia",
            ["m²", "km²"],
            key="area2"
        )

        if st.button("Convertir Área"):

            if origen == destino:

                resultado = valor

            elif origen == "km²":

                resultado = valor * 1_000_000

            else:

                resultado = valor / 1_000_000

            st.success(resultado)

            save_history(
                "Conversión Área",
                resultado
            )

    # ======================================================
    # VOLUMEN
    # ======================================================

    elif categoria == "Volumen":

        valor = st.number_input(
            "Valor",
            value=1.0,
            key="vol"
        )

        origen = st.selectbox(
            "Desde",
            ["litros", "m³"],
            key="vol1"
        )

        destino = st.selectbox(
            "Hacia",
            ["litros", "m³"],
            key="vol2"
        )

        if st.button("Convertir Volumen"):

            if origen == destino:

                resultado = valor

            elif origen == "m³":

                resultado = valor * 1000

            else:

                resultado = valor / 1000

            st.success(resultado)

            save_history(
                "Conversión Volumen",
                resultado
            )

# ==========================================================
# HISTORIAL
# ==========================================================

elif menu == "📜 Historial":

    st.subheader("📜 Historial de Operaciones")

    if len(st.session_state.history) == 0:

        st.info(
            "No hay operaciones registradas."
        )

    else:

        df_history = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            df_history,
            use_container_width=True
        )

        csv = df_history.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇ Exportar CSV",
            csv,
            "historial.csv",
            "text/csv"
        )

        if st.button(
            "🗑 Limpiar Historial"
        ):

            st.session_state.history = []

            st.rerun()

# ==========================================================
# AYUDA
# ==========================================================

elif menu == "ℹ️ Ayuda":

    st.subheader("ℹ️ Ayuda")

    st.markdown("""
    ## 🧮 Calculadora

    Ejemplos:

    - 2+2
    - 5*8
    - sqrt(144)
    - sin(pi/2)
    - cos(pi)
    - tan(pi/4)
    - factorial(5)
    - exp(2)

    ---

    ## 📈 Graficador

    Ejemplos:

    - x**2
    - x**3
    - sin(x)
    - cos(x)
    - tan(x)
    - log(x)
    - exp(x)

    ---

    ## 🔢 Ecuaciones

    - Cuadráticas
    - Sistemas 2x2
    - Sistemas 3x3

    ---

    ## 🧱 Matrices

    - Suma
    - Resta
    - Multiplicación
    - Determinante
    - Inversa
    - Transpuesta

    ---

    ## 📊 Estadística

    Datos:

    10,20,30,40,50

    Calcula:

    - Media
    - Mediana
    - Moda
    - Varianza
    - Desviación estándar
    - Rango

    ---

    ## Librerías utilizadas

    - Streamlit
    - NumPy
    - SciPy
    - SymPy
    - Pandas
    - Plotly
    - Math
    - Datetime
    """)

    st.success(
        "Calculadora Científica Profesional lista para producción."
    )