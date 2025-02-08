 # app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Plateforme Interactive d’Apprentissage de l’Économie et de la Finance")

@st.cache_data
def load_data():
    df = pd.read_csv("data/debt_data.csv")
    return df

data = load_data()

st.subheader("Données brutes : Dette Publique")
st.dataframe(data.head())

fig = px.line(data, x='année', y='dette_publique', title="Évolution de la Dette Publique")
st.plotly_chart(fig)

st.subheader("Simulateur de Scénarios")
st.write("Ajustez les paramètres pour simuler l’impact sur la dette publique.")

taux_croissance = st.slider("Taux de croissance (%)", min_value=-5.0, max_value=10.0, value=2.0, step=0.1)
annee_simulation = st.number_input("Année de simulation", min_value=2025, max_value=2050, value=2030)

derniere_valeur = data['dette_publique'].iloc[-1]
annee_courante = data['année'].iloc[-1]
annees_diff = annee_simulation - annee_courante
simulation = derniere_valeur * ((1 + taux_croissance/100) ** annees_diff)

st.write(f"Valeur projetée de la dette publique en {annee_simulation} : {simulation:,.2f}")

st.subheader("Apprendre les Concepts")
st.markdown("""
**Dette Publique :**  
La dette publique est l'ensemble des emprunts contractés par un État pour financer ses dépenses.  

**Échanges Extérieurs :**  
Ils représentent les flux d’exportations et d’importations entre pays, influençant la balance des paiements.
""")

