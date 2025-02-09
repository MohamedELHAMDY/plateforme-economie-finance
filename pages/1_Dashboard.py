# pages/1_Dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard Global")
st.markdown("Vue d'ensemble des principaux indicateurs économiques du Maroc.")

@st.cache_data
def load_debt_data():
    filepath = os.path.join("data", "debt_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8", sep=",")
        # Nettoyage : suppression des virgules dans la colonne dette_publique et conversion en numérique
        df["dette_publique"] = pd.to_numeric(
            df["dette_publique"].str.replace(",", "", regex=True), errors="coerce"
        )
        return df
    else:
        return pd.DataFrame()

debt_data = load_debt_data()

if not debt_data.empty:
    st.subheader("Dette Publique (en millions de DH)")
    st.dataframe(debt_data.head())
    fig = px.line(debt_data, x="année", y="dette_publique", 
                  title="Évolution de la Dette Publique au Maroc")
    st.plotly_chart(fig)
    
    # Updated image display with use_container_width
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Flag_of_Morocco.svg/1200px-Flag_of_Morocco.svg.png"
    st.image(image_url, caption="Drapeau du Maroc", use_container_width=True)
else:
    st.error("Les données de dette publique ne sont pas disponibles.")
