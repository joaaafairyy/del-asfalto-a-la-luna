import math 
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(page_title="DEL ASFALTO A LA LUNA", page_icon="🚀", layout="wide")
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top right, #1b2735 0%, #090a0f 100%);
    color: #e0e6ed;
}
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(0, 242, 254, 0.35);
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.12);
}
</style>
""", unsafe_allow_html=True)


st.title("DEL ASFALTO A LA LUNA")


masa = st.number_input("masa de la persona (kg)", value=50.0) 
altura = st.number_input("altura", value=0.25) 
st.write("Masa elegida:", masa)

g_tierra = 9.81
e_tierra = 0.82
dt_tierra = 0.15

v_impacto_tierra = (math.sqrt(2 * g_tierra * altura))
v_rebote_tierra = (e_tierra * v_impacto_tierra )
impulso_tierra = ( masa * (v_rebote_tierra - (-v_impacto_tierra)))
fuerza_tierra = (impulso_tierra / dt_tierra)
st.write("Fuerza media en la Tierra (N):", round(fuerza_tierra, 2))



# LUNAA
g_luna = 1.62
e_luna = 0.60
dt_luna = 0.25

v_impacto_luna = (math.sqrt(2 * g_luna * altura))
v_rebote_luna = (e_luna * v_impacto_luna )
impulso_luna = ( masa * (v_rebote_luna - (-v_impacto_luna)))
fuerza_luna = (impulso_luna / dt_luna)
st.write("Fuerza media en la luna (N):", round(fuerza_luna, 2))


#GRAFICA 
fig, ax = plt.subplots()
# 1. Tarjetas de telemetría con brillo neón
m1, m2 = st.columns(2)
m1.metric("🌍 Fuerza Media en la Tierra", f"{round(fuerza_tierra, 2)} N")
m2.metric("🌕 Fuerza Media en la Luna", f"{round(fuerza_luna, 2)} N", delta=f"{round(fuerza_luna - fuerza_tierra, 2)} N")

# 2. Gráfica modo oscuro y transparente
plt.style.use("dark_background")
fig, ax = plt.subplots()
fig.patch.set_alpha(0.0)
ax.set_facecolor("none")

ax.bar(["Tierra", "Luna"], [fuerza_tierra, fuerza_luna], color=["#00f2fe", "#a855f7"])
ax.set_ylabel("Fuerza Media de Impacto (N)")
ax.set_title("Comparación de Fuerza: Tierra vs. Luna")

st.pyplot(fig)