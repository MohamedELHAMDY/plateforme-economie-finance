import streamlit as st
import pandas as pd
import os

st.title("🗳️ Vote Citoyen - Mizaniyatona")
st.markdown("""
Participez activement à la gestion budgétaire en votant pour les secteurs qui vous semblent prioritaires.
Chaque vote aide à comprendre les attentes des citoyens et à renforcer la transparence budgétaire !
""")

# Charger les secteurs budgétaires
@st.cache_data
def load_sectors():
    filepath = os.path.join("data", "finances_data.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, encoding="utf-8", sep=",")
        secteur_col = [col for col in df.columns if "secteur" in col.lower()]
        if secteur_col:
            return df[secteur_col[0]].unique().tolist()
        else:
            st.error("Aucune colonne 'secteur' trouvée dans les données.")
            return []
    else:
        st.error("Fichier des données budgétaires non trouvé.")
        return []

sectors = load_sectors()

# Interface de vote
if sectors:
    selected_sector = st.selectbox("🔍 Choisissez le secteur que vous souhaitez prioriser :", sectors)
    if st.button("✅ Voter"):
        # Enregistrer le vote (simulation dans un fichier CSV)
        vote_filepath = os.path.join("data", "votes.csv")
        if os.path.exists(vote_filepath):
            votes_df = pd.read_csv(vote_filepath)
        else:
            votes_df = pd.DataFrame(columns=["secteur", "votes"])
        
        if selected_sector in votes_df["secteur"].values:
            votes_df.loc[votes_df["secteur"] == selected_sector, "votes"] += 1
        else:
            new_vote = pd.DataFrame([[selected_sector, 1]], columns=["secteur", "votes"])
            votes_df = pd.concat([votes_df, new_vote], ignore_index=True)
        
        votes_df.to_csv(vote_filepath, index=False)
        st.success(f"Merci pour votre vote en faveur du secteur '{selected_sector}' !")

    # Afficher les résultats
    if os.path.exists("data/votes.csv"):
        votes_df = pd.read_csv("data/votes.csv")
        st.subheader("📊 Résultats des Votes")
        st.bar_chart(votes_df.set_index("secteur"))
else:
    st.error("Impossible de charger les secteurs budgétaires.")

# Ajouter des questions génériques
st.subheader("🗣️ Questions Génériques")

# Question 1: Satisfaction with the current budget allocation
satisfaction = st.selectbox("Comment vous sentez-vous à propos de l'allocation actuelle du budget national parmi les différents secteurs ?", 
                            ["Très satisfait", "Satisfait", "Neutre", "Insatisfait", "Très insatisfait"])

# Question 2: Sector funding prioritization
priority_sector = st.multiselect("Parmi les secteurs suivants, lequel(s) devraient recevoir plus de financement l'année prochaine ?", 
                                 ["Éducation", "Santé", "Infrastructure", "Environnement", "Sécurité", "Autre (veuillez spécifier)"])

# Question 3: Social vs Economic Growth Programs
social_vs_growth = st.radio("Pensez-vous que le gouvernement devrait privilégier les programmes sociaux par rapport aux initiatives de croissance économique ?", 
                            ["Oui", "Non", "Je ne sais pas"])

# Question 4: Future participation in surveys
future_participation = st.radio("Seriez-vous prêt à participer à des enquêtes futures concernant les dépenses publiques et le budget ?", 
                                ["Oui", "Non", "Peut-être"])

# Question 5: Transparency in fund management
transparency = st.selectbox("Pensez-vous qu'il y ait suffisamment de transparence dans la gestion des fonds publics ?", 
                            ["Oui, complètement transparent", "Non, mais certaines informations sont disponibles", "Non, il y a un manque de transparence", "Je ne sais pas"])

# Question 6: Area for improvement in public spending
improvement_suggestion = st.text_area("Si vous pouviez suggérer une amélioration dans les dépenses publiques, quelle serait-elle ?", "")

# Display submitted answers
if st.button("✅ Soumettre vos réponses"):
    st.write("Merci pour vos réponses ! Voici ce que vous avez soumis :")
    st.write(f"Satisfaction avec l'allocation du budget: {satisfaction}")
    st.write(f"Secteurs prioritaires pour plus de financement: {', '.join(priority_sector)}")
    st.write(f"Préférence pour programmes sociaux ou croissance économique: {social_vs_growth}")
    st.write(f"Participation future dans les enquêtes: {future_participation}")
    st.write(f"Transparence dans la gestion des fonds publics: {transparency}")
    st.write(f"Amélioration suggérée dans les dépenses publiques: {improvement_suggestion}")
