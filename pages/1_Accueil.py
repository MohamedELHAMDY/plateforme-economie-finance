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
        secteur_col = [col for col in df.columns if "secteur" in col.lower()]
        if budget_col and secteur_col:
            budget_col_name = budget_col[0]
            secteur_col_name = secteur_col[0]
            if df[budget_col_name].dtype == 'object':
                df[budget_col_name] = df[budget_col_name].str.replace(",", "", regex=True)
            df["budget"] = pd.to_numeric(df[budget_col_name], errors="coerce")
            df.rename(columns={secteur_col_name: "secteur"}, inplace=True)
            return df
        else:
            st.error("Les colonnes nécessaires (budget et secteur) sont introuvables.")
            return pd.DataFrame()
    else:
        st.error("Le fichier des données budgétaires est manquant.")
        return pd.DataFrame()

budget_data = load_budget_data()

if not budget_data.empty:
    st.subheader("Budget par Secteur (en millions de DH)")
    st.dataframe(budget_data.head())
    if "secteur" in budget_data.columns and "budget" in budget_data.columns:
        fig = px.bar(budget_data, x="secteur", y="budget", title="Répartition du Budget par Secteur")
        st.plotly_chart(fig)
    else:
        st.error("Les données nécessaires pour le graphique sont absentes.")
else:
    st.error("Les données budgétaires ne sont pas disponibles.")

st.markdown("""
### 📌 Sources de Données Ouvertes :
🔗 [Portail national des données ouvertes](https://www.data.gov.ma)  
🔗 [Bulletin Mensuel des Statistiques des Finances Publiques](https://www.tgr.gov.ma)  
🔗 [Budget Citoyen](https://www.finances.gov.ma/fr/Nos-metiers/Pages/Budget-citoyen.aspx)  
🔗 [Note de Conjoncture](https://depf.finances.gov.ma)
""")
