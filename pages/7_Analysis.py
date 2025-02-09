# pages/7_Analysis.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Analyse Avancée et Outils Statistiques")
st.markdown("Explorez les relations entre différents indicateurs économiques grâce aux outils d'analyse.")

@st.cache_data
def load_macro_data():
    filepath = os.path.join("data", "macro_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8")
        return df
    else:
        st.warning("Le fichier macro_data.csv n'a pas été trouvé.")
        return pd.DataFrame()

macro_data = load_macro_data()
if not macro_data.empty:
    st.subheader("Matrice de Corrélation")
    corr = macro_data.corr()
    st.dataframe(corr)
    
    st.subheader("Régression Linéaire Simple")
    # Exemple : Prédire l'indice des prix à la consommation en fonction de l'année
    if "année" in macro_data.columns and "indice_prix_consommation" in macro_data.columns:
        X = macro_data["année"].values.reshape(-1, 1)
        y = macro_data["indice_prix_consommation"].values
        model = LinearRegression()
        model.fit(X, y)
        macro_data["prédiction"] = model.predict(X)
        fig = px.scatter(macro_data, x="année", y="indice_prix_consommation", title="Régression Linéaire")
        fig.add_traces(px.line(macro_data, x="année", y="prédiction").data)
        st.plotly_chart(fig)
    else:
        st.error("Les colonnes nécessaires pour la régression ne sont pas présentes.")
else:
    st.info("Aucune donnée macroéconomique disponible pour l'analyse avancée.")
