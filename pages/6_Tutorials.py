# pages/6_Tutorials.py
import streamlit as st

st.title("Tutoriels et Ressources Pédagogiques")
st.markdown("""
Bienvenue dans la section tutoriels.  
Vous trouverez ci-dessous des ressources pour comprendre les indicateurs économiques et financiers :

### Comprendre les Indicateurs
- **Indice des prix à la consommation** : [Article explicatif](https://fr.wikipedia.org/wiki/Indice_des_prix)
- **Indice des prix à la production** : [Article explicatif](https://fr.wikipedia.org/wiki/Indice_des_prix)
- **Décomposition du PIB** : [Article explicatif](https://fr.wikipedia.org/wiki/Produit_int%C3%A9rieur_brut)

### Ressources Vidéo
Voici une vidéo explicative sur l'économie marocaine :
""")
video_url = "https://www.youtube.com/embed/6XpA2i3NAbM"  # Remplacez par une URL YouTube appropriée
st.video(video_url)

st.markdown("### Quiz Interactif")
st.markdown("Accédez à la section Quiz pour tester vos connaissances.")
