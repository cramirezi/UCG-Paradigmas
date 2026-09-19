import streamlit as st
import libreria_funciones as lf

st.title("Paradigmas de la programación")

st.sidebar.image("LogoUCG.png")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Carlos Cabello")
capital= st.number_input("Ingrese el capital",value=1000)
tasa_anual_pct= st.number_input("Ingrese la tasa anual",value=0.15)
dias_mora= st.number_input("Ingrese los días mora",value=10)

resultado = lf.calcular_interes_mora(capital,tasa_anual_pct,dias_mora)

st.write("El valor atrasado es:", resultado)
