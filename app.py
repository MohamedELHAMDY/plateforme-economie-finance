# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

st.title("Plateforme Interactive d’Apprentissage de l’Économie et de la Finance")

@st.cache_data
def load_data():
    filepath = "data/debt_data.csv"
    if not os.path.exists(filepath):
        st.error(f"Le fichier {filepath} n'existe pas. Veuillez vérifier que le fichier est bien présent.")
        return pd.DataFrame()  # Retourne un DataFrame vide
    try:
        # Si nécessaire, spécifiez l'encodage ou le séparateur
        df = pd.read_csv(filepath, encoding="utf-8")
        if df.empty:
            st.error(f"Le fichier {filepath} est vide. Veuillez le remplir avec des données valides.")
        return df
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier {filepath}: {e}")
        return pd.DataFrame()

data = load_data()

if not data.empty:
    st.subheader("Données brutes : Dette Publique")
    st.dataframe(data.head())

    # Afficher les colonnes du DataFrame pour diagnostic
    st.write("Colonnes du DataFrame :", data.columns.tolist())

    # Vérifiez que les colonnes existent bien avant de créer le graphique
    if "année" in data.columns and "dette_publique" in data.columns:
        fig = px.line(data, x='année', y='dette_publique', title="Évolution de la Dette Publique")
        st.plotly_chart(fig)
    else:
        st.error("Les colonnes 'année' et/ou 'dette_publique' sont introuvables dans les données.")
    
    # Simulateur de scénarios
    st.subheader("Simulateur de Scénarios")
    st.write("Ajustez les paramètres pour simuler l’impact sur la dette publique.")

    taux_croissance = st.slider("Taux de croissance (%)", min_value=-5.0, max_value=10.0, value=2.0, step=0.1)
    annee_simulation = st.number_input("Année de simulation", min_value=2025, max_value=2050, value=2030)

    # Assurez-vous qu'il y a au moins une ligne de données
    if len(data) > 0:
        derniere_valeur = data['dette_publique'].iloc[-1]
        annee_courante = data['année'].iloc[-1]
        annees_diff = annee_simulation - annee_courante
        simulation = derniere_valeur * ((1 + taux_croissance/100) ** annees_diff)
        st.write(f"Valeur projetée de la dette publique en {annee_simulation} : {simulation:,.2f}")
    else:
        st.error("Pas de données suffisantes pour effectuer la simulation.")

    # Section pédagogique
    st.subheader("Apprendre les Concepts")
    st.markdown("""
    **Dette Publique :**  
    La dette publique est l'ensemble des emprunts contractés par un État pour financer ses dépenses.  

    **Échanges Extérieurs :**  
    Ils représentent les flux d’exportations et d’importations entre pays, influençant la balance des paiements.
    """)
else:
    st.error("Aucune donnée à afficher.")
