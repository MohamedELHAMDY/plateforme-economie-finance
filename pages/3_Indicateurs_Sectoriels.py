# pages/3_SectorIndicators.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Indicateurs Sectoriels")
st.markdown("Visualisation des indicateurs par secteur d'activité au Maroc.")

@st.cache_data
def load_sector_data():
    filepath = os.path.join("data", "sector_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8")
        return df
    else:
        st.warning("Le fichier sector_data.csv n'a pas été trouvé.")
        return pd.DataFrame()

sector_data = load_sector_data()
if not sector_data.empty:
    st.dataframe(sector_data.head())
    # Sélection dynamique du secteur
    secteurs = sector_data["secteur"].unique()
    secteur_selection = st.selectbox("Choisissez un secteur", secteurs)
    df_filtré = sector_data[sector_data["secteur"] == secteur_selection]
    if "année" in df_filtré.columns and "valeur" in df_filtré.columns:
        fig = px.line(df_filtré, x="année", y="valeur", 
                      title=f"Évolution pour le secteur {secteur_selection}")
        st.plotly_chart(fig)
    else:
        st.error("Les colonnes nécessaires (année, valeur) ne sont pas présentes.")
    
    # Exemple d'histogramme pour la distribution par secteur
    st.subheader("Histogramme des valeurs par secteur")
    fig_hist = px.histogram(sector_data, x="secteur", y="valeur", 
                            title="Distribution des valeurs par secteur",
                            labels={"secteur": "Secteur", "valeur": "Valeur"})
    st.plotly_chart(fig_hist)
else:
    st.info("Aucune donnée sectorielle disponible pour le moment.")
