# pages/3_SectorIndicators.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Indicateurs Sectoriels")
st.markdown("Visualisation des indicateurs par secteur d'activité.")

@st.cache_data
def load_sector_data():
    filepath = os.path.join("data", "sector_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8")
        # Par exemple, le fichier peut contenir : "année", "secteur", "valeur", etc.
        return df
    else:
        st.warning("Le fichier sector_data.csv n'a pas été trouvé.")
        return pd.DataFrame()

sector_data = load_sector_data()
if not sector_data.empty:
    st.dataframe(sector_data.head())
    # Filtre de sélection du secteur
    secteurs = sector_data["secteur"].unique()
    secteur_selection = st.selectbox("Choisissez un secteur", secteurs)
    df_filtré = sector_data[sector_data["secteur"] == secteur_selection]
    if "année" in df_filtré.columns and "valeur" in df_filtré.columns:
        fig = px.line(df_filtré, x="année", y="valeur", title=f"Évolution pour le secteur {secteur_selection}")
        st.plotly_chart(fig)
    else:
        st.error("Les colonnes nécessaires (année, valeur) ne sont pas présentes.")
else:
    st.info("Aucune donnée sectorielle disponible pour le moment.")
 
