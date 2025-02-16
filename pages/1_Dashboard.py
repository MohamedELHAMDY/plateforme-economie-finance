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
        st.write("Colonnes disponibles :", df.columns)  # Debugging step
        budget_col = [col for col in df.columns if "budget" in col.lower()]
        if budget_col:
            df["budget"] = pd.to_numeric(df[budget_col[0]].str.replace(",", "", regex=True), errors="coerce")
            return df
        else:
            st.error("La colonne contenant les données budgétaires est introuvable.")
            return pd.DataFrame()
    else:
        st.error("Le fichier des données budgétaires est manquant.")
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
