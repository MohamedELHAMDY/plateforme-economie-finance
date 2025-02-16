# pages/1_Dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Mizaniyatona : Transparence Budgétaire en Action")
st.markdown("""
Vue d'ensemble des finances publiques marocaines avec des données ouvertes et interactives.
Accédez aux informations clés et participez à la gestion budgétaire !
""")

@st.cache_data
def load_budget_data():
    filepath = os.path.join("data", "finances_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8", sep=",")
        df["budget"] = pd.to_numeric(df["budget"].str.replace(",", "", regex=True), errors="coerce")
        return df
    else:
        return pd.DataFrame()

budget_data = load_budget_data()

if not budget_data.empty:
    st.subheader("Budget par Secteur (en millions de DH)")
    st.dataframe(budget_data.head())
    fig = px.bar(budget_data, x="secteur", y="budget", title="Répartition du Budget par Secteur")
    st.plotly_chart(fig)
else:
    st.error("Les données budgétaires ne sont pas disponibles.")

st.markdown("""
### 📌 Sources de Données Ouvertes :
🔗 [Portail national des données ouvertes](https://www.data.gov.ma)  
🔗 [Bulletin Mensuel des Statistiques des Finances Publiques](https://www.tgr.gov.ma)  
🔗 [Budget Citoyen](https://www.finances.gov.ma/fr/Nos-metiers/Pages/Budget-citoyen.aspx)  
🔗 [Note de Conjoncture](https://depf.finances.gov.ma)
""")
