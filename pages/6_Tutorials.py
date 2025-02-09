# pages/6_Tutorials.py
import streamlit as st

st.title("Tutoriels et Ressources Pédagogiques")
st.markdown("""
Bienvenue dans la section tutoriels.  
Ici, vous trouverez des ressources pour comprendre les différents indicateurs économiques et financiers.

### Comprendre les Indicateurs
- **Indice des prix à la production** : [Article explicatif](https://fr.wikipedia.org/wiki/Indice_des_prix)
- **Indice des prix à la consommation** : [Article explicatif](https://fr.wikipedia.org/wiki/Indice_des_prix)
- **Décomposition du PIB** : [Article explicatif](https://fr.wikipedia.org/wiki/Produit_int%C3%A9rieur_brut)

### Quiz Interactif
Quelle est la principale utilisation de l'indice des prix à la consommation ?
- Financer l'infrastructure publique  
- Mesurer l'inflation  
- Évaluer la compétitivité internationale

Sélectionnez votre réponse ci-dessous :
""")
choice = st.radio("Votre réponse", ("Financer l'infrastructure publique", "Mesurer l'inflation", "Évaluer la compétitivité internationale"))
if st.button("Vérifier la réponse"):
    if choice == "Mesurer l'inflation":
        st.success("Correct !")
    else:
        st.error("Incorrect, réessayez.")
