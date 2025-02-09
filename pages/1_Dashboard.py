# pages/1_Dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard Global")
st.markdown("Vue d'ensemble des principaux indicateurs économiques.")

@st.cache_data
def load_debt_data():
    filepath = os.path.join("data", "debt_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8", sep=",")
        # Nettoyage : suppression des virgules et conversion en numérique
        df["dette_publique"] = pd.to_numeric(
            df["dette_publique"].str.replace(",", "", regex=True), errors="coerce"
        )
        return df
    else:
        return pd.DataFrame()

debt_data = load_debt_data()

if not debt_data.empty:
    st.subheader("Dette Publique")
    st.dataframe(debt_data.head())
    fig = px.line(debt_data, x="année", y="dette_publique", title="Évolution de la Dette Publique")
    st.plotly_chart(fig)
else:
    st.error("Les données de dette publique ne sont pas disponibles.")

# Vous pouvez ajouter d'autres indicateurs clés ici (ex. PIB, indices, etc.)
 
