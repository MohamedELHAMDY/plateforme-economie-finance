# pages/4_FinancesPublic.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Finances Publiques et Budgets")
st.markdown("Analyse des dépenses, recettes et budgets publics.")

@st.cache_data
def load_finances_data():
    filepath = os.path.join("data", "finances_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8")
        return df
    else:
        st.warning("Le fichier finances_data.csv n'a pas été trouvé.")
        return pd.DataFrame()

finances_data = load_finances_data()
if not finances_data.empty:
    st.dataframe(finances_data.head())
    # Exemple : graphique du budget de fonctionnement
    if "année" in finances_data.columns and "budget_fonctionnement" in finances_data.columns:
        fig = px.line(finances_data, x="année", y="budget_fonctionnement", title="Budget de Fonctionnement")
        st.plotly_chart(fig)
    else:
        st.error("Les colonnes nécessaires ne sont pas présentes dans les données.")
else:
    st.info("Aucune donnée financière disponible pour le moment.")
 
