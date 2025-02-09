# pages/2_MacroIndicators.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Indicateurs Macroéconomiques")
st.markdown("Visualisation et analyse des indices macroéconomiques.")

@st.cache_data
def load_macro_data():
    filepath = os.path.join("data", "macro_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8")
        # Par exemple, le fichier peut contenir : "année", "indice_prix_consommation", "indice_prix_production", etc.
        return df
    else:
        st.warning("Le fichier macro_data.csv n'a pas été trouvé.")
        return pd.DataFrame()

macro_data = load_macro_data()
if not macro_data.empty:
    st.dataframe(macro_data.head())
    # Exemple de graphique pour l'indice des prix à la consommation
    if "indice_prix_consommation" in macro_data.columns:
        fig = px.line(macro_data, x="année", y="indice_prix_consommation", title="Indice des Prix à la Consommation")
        st.plotly_chart(fig)
    else:
        st.error("La colonne 'indice_prix_consommation' n'existe pas dans les données.")
else:
    st.info("Aucune donnée macroéconomique disponible pour le moment.")
 
