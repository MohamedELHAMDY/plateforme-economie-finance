# app.py
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mizaniyatona : Open Budget Lab", layout="wide")

# Branding Mizaniyatona
st.title("Mizaniyatona : Open Budget Lab pour une Transparence Participative")
st.subheader("Mizaniyatona, notre budget, notre voix !")

st.markdown("""
Bienvenue sur **Mizaniyatona**, une plateforme interactive conçue pour exploiter les **données ouvertes** et permettre aux citoyens de **consulter, analyser et participer** activement à la gestion du budget public.

### Sections disponibles :
- 📊 **Dashboard** : Vue d'ensemble des finances publiques.
- 💰 **Budgets & Dépenses** : Analyse détaillée des budgets sectoriels.
- 🗳️ **Participation citoyenne** : Votez sur les priorités budgétaires.
- 📚 **Éducation financière** : Comprendre les finances publiques à travers des contenus interactifs.
- 🔍 **Analyse avancée** : Explorez les tendances et les corrélations.

### Ressources ouvertes :
🔗 [Portail national des données ouvertes](https://www.data.gov.ma)  
🔗 [Bulletin Mensuel des Statistiques des Finances Publiques](https://www.tgr.gov.ma)  
🔗 [Budget Citoyen](https://www.finances.gov.ma/fr/Nos-metiers/Pages/Budget-citoyen.aspx)  
🔗 [Note de Conjoncture](https://depf.finances.gov.ma)

---
💡 **Avec Mizaniyatona, chaque citoyen devient acteur de la transparence budgétaire !**
""")
