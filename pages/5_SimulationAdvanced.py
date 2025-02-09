# pages/5_SimulationAdvanced.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

st.title("Simulation Avancée de Scénarios Économiques")
st.markdown("Modifiez les paramètres pour comparer différents scénarios économiques.")

# Pour cet exemple, nous réutilisons les données de dette publique
@st.cache_data
def load_debt_data():
    filepath = os.path.join("data", "debt_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8", sep=",")
        df["dette_publique"] = pd.to_numeric(
            df["dette_publique"].str.replace(",", "", regex=True), errors="coerce"
        )
        return df
    else:
        return pd.DataFrame()

data = load_debt_data()
if not data.empty:
    st.subheader("Simulation sur la Dette Publique")
    taux_croissance = st.slider("Taux de croissance (%)", min_value=-5.0, max_value=10.0, value=2.0, step=0.1)
    annee_simulation = st.number_input("Année de simulation", min_value=int(data["année"].max())+1, max_value=2050, value=2030)
    try:
        derniere_valeur = data["dette_publique"].iloc[-1]
        annee_courante = data["année"].iloc[-1]
        annees_diff = annee_simulation - annee_courante
        simulation = derniere_valeur * ((1 + taux_croissance/100) ** annees_diff)
        st.write(f"Valeur projetée de la dette publique en {annee_simulation} : {simulation:,.2f}")
    except Exception as e:
        st.error(f"Erreur dans la simulation : {e}")
else:
    st.error("Les données nécessaires pour la simulation ne sont pas disponibles.")
 
