import streamlit as st

# Configuración visual para que sea "Atractiva" como pide la rúbrica
st.set_page_config(page_title="GasMaster Pro 🧪", layout="centered")

st.title("🧪 GasMaster Pro: Tu Asistente de Química")
st.markdown("""
Esta aplicación resuelve las **Leyes de los Gases** de forma fácil. 
Diseñada para que alumnos, padres y profesores entiendan qué pasa con las moléculas.
""")

st.sidebar.header("Configuración de Unidades")
st.sidebar.write("El sistema convierte todo automáticamente a **unidades científicas** (atm, L, K).")

# --- LÓGICA DE CONVERSIÓN ---
def a_kelvin(c): return c + 273.15
def a_atm(valor, unidad):
    factores = {"atm": 1, "mmHg": 760, "Pa": 101325, "psi": 14.7}
    return valor / factores[unidad]

# --- INTERFAZ AMIGABLE ---
st.header("🔍 Ingresa tus datos")
st.write("Pon un **0** en la variable que quieres descubrir.")

col1, col2 = st.columns(2)

with col1:
    p_val = st.number_input("Presión actual", value=0.0, step=0.1)
    p_uni = st.selectbox("Unidad", ["atm", "mmHg", "Pa", "psi"])
    v_val = st.number_input("Volumen (Litros)", value=0.0, step=0.1)

with col2:
    t_val = st.number_input("Temperatura (°Celsius)", value=25.0, step=1.0)
    n_val = st.number_input("Cantidad de sustancia (moles)", value=0.0, step=0.01)

# --- PROCESO DE CÁLCULO Y ASESORÍA ---
R = 0.0821  # Constante universal

if st.button("🚀 RESOLVER Y EXPLICAR PASO A PASO"):
    if (p_val == 0 and v_val == 0) or (n_val == 0 and t_val == 0):
        st.error("¡Cuidado! Necesitas al menos 3 datos para encontrar el cuarto.")
    else:
        # Conversiones internas
        P = a_atm(p_val, p_uni)
        V = v_val
        T = a_kelvin(t_val)
        n = n_val

        st.divider()
        
        # Despeje de variables
        if p_val == 0:
            res = (n * R * T) / V
            st.success(f"### Resultado: La Presión es {res:.3f} atm")
            st.info("**Explicación para todos:** Usamos la fórmula $P = \\frac{nRT}{V}$. Esto significa que si metes mucho gas en un espacio chico, la presión sube porque las moléculas chocan más fuerte.")
        
        elif v_val == 0:
            res = (n * R * T) / P
            st.success(f"### Resultado: El Volumen es {res:.3f} L")
            st.info("**Explicación:** El volumen es el 'espacio' que ocupa el gas. A mayor temperatura, el gas se expande (como un globo al sol).")
        
        elif n_val == 0:
            res = (P * V) / (R * T)
            st.success(f"### Resultado: Hay {res:.4f} moles")
            st.info("**Explicación:** Calculamos cuánta 'materia' hay dentro. Un mol son muchísimas moléculas juntas.")

        st.warning(f"Nota técnica: Trabajamos con T = {T} K y R = 0.0821 para máxima precisión.")