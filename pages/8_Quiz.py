# pages/8_Quiz.py
import streamlit as st

st.title("Quiz Interactif")
st.markdown("Testez vos connaissances sur l'économie, la finance et l'économie marocaine !")

# Liste de 20 questions sous forme de dictionnaires (exemple)
questions = [
    {
        "question": "Quel indicateur mesure l'évolution des prix à la consommation ?",
        "options": [
            "Indice des prix à la consommation",
            "Indice des prix à la production",
            "Indice du coût de la vie",
            "Indice des salaires"
        ],
        "answer": "Indice des prix à la consommation",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Consumer_Price_Index.svg/1200px-Consumer_Price_Index.svg.png"
    },
    {
        "question": "Quel est l'objectif principal de la politique monétaire ?",
        "options": [
            "Contrôler l'inflation",
            "Augmenter l'emploi",
            "Promouvoir l'exportation",
            "Réduire les impôts"
        ],
        "answer": "Contrôler l'inflation"
    },
    {
        "question": "Que signifie le PIB ?",
        "options": [
            "Produit Intérieur Brut",
            "Produit Industriel Brut",
            "Produit International Brut",
            "Produit Intérieur Brut régional"
        ],
        "answer": "Produit Intérieur Brut"
    },
    {
        "question": "Quel indicateur est utilisé pour mesurer l'inflation ?",
        "options": [
            "Indice des prix à la consommation",
            "Taux de change",
            "Taux de chômage",
            "Solde budgétaire"
        ],
        "answer": "Indice des prix à la consommation"
    },
    {
        "question": "La dette publique représente :",
        "options": [
            "L'ensemble des emprunts contractés par l'État",
            "Les réserves d'or",
            "Les dépenses privées",
            "Les investissements étrangers"
        ],
        "answer": "L'ensemble des emprunts contractés par l'État"
    },
    {
        "question": "Quel secteur contribue majoritairement au PIB du Maroc ?",
        "options": [
            "Agriculture",
            "Industrie",
            "Services",
            "Tourisme"
        ],
        "answer": "Services"
    },
    {
        "question": "Qu'est-ce que l'indice du coût de la vie mesure ?",
        "options": [
            "L'évolution du coût de la vie",
            "Le revenu moyen",
            "Les dépenses publiques",
            "La balance commerciale"
        ],
        "answer": "L'évolution du coût de la vie"
    },
    {
        "question": "Quel est l'impact d'une augmentation du taux d'intérêt sur l'économie ?",
        "options": [
            "Ralentissement de l'investissement",
            "Augmentation de l'inflation",
            "Hausse des exportations",
            "Diminution de l'épargne"
        ],
        "answer": "Ralentissement de l'investissement"
    },
    {
        "question": "Quel indicateur reflète le pouvoir d'achat des ménages ?",
        "options": [
            "Indice des prix à la consommation",
            "Revenu national brut",
            "Taux de chômage",
            "Dette publique"
        ],
        "answer": "Indice des prix à la consommation"
    },
    {
        "question": "Que mesure l'indice des prix à la production ?",
        "options": [
            "L'évolution des coûts de production",
            "La performance boursière",
            "Le niveau des exportations",
            "La dette extérieure"
        ],
        "answer": "L'évolution des coûts de production"
    },
    {
        "question": "Qu'est-ce qu'une subvention ?",
        "options": [
            "Une aide financière versée par l'État",
            "Un impôt indirect",
            "Un emprunt bancaire",
            "Une taxe sur les produits importés"
        ],
        "answer": "Une aide financière versée par l'État"
    },
    {
        "question": "Quel indicateur peut être utilisé pour analyser la compétitivité d'un pays ?",
        "options": [
            "Balance commerciale",
            "Indice du coût de la vie",
            "Taux de croissance du PIB",
            "Décomposition du PIB"
        ],
        "answer": "Balance commerciale"
    },
    {
        "question": "Que représente le budget de fonctionnement ?",
        "options": [
            "Les dépenses courantes de l'État",
            "Les investissements à long terme",
            "Les recettes fiscales",
            "Les exportations nettes"
        ],
        "answer": "Les dépenses courantes de l'État"
    },
    {
        "question": "Quelle est la fonction principale de la Banque centrale ?",
        "options": [
            "Réguler la politique monétaire",
            "Gérer les budgets municipaux",
            "Contrôler les entreprises privées",
            "Imposer les impôts"
        ],
        "answer": "Réguler la politique monétaire"
    },
    {
        "question": "Que signifie 'formation brute du capital fixe' ?",
        "options": [
            "Les investissements réalisés par l'État et le secteur privé",
            "Les revenus du capital",
            "Les subventions publiques",
            "Les exportations de capitaux"
        ],
        "answer": "Les investissements réalisés par l'État et le secteur privé"
    },
    {
        "question": "Quel indicateur mesure l'évolution de la consommation des ménages ?",
        "options": [
            "Dépenses de consommation finale des ménages",
            "Indice des prix à la production",
            "Solde budgétaire",
            "Taux de chômage"
        ],
        "answer": "Dépenses de consommation finale des ménages"
    },
    {
        "question": "Quelle donnée est essentielle pour calculer le taux de croissance économique ?",
        "options": [
            "Le PIB",
            "La dette publique",
            "L'indice du coût de la vie",
            "Les subventions"
        ],
        "answer": "Le PIB"
    },
    {
        "question": "Quel est l'impact d'une baisse des impôts sur l'économie ?",
        "options": [
            "Stimuler la consommation et l'investissement",
            "Augmenter l'inflation",
            "Réduire les investissements étrangers",
            "Diminuer la compétitivité"
        ],
        "answer": "Stimuler la consommation et l'investissement"
    },
    {
        "question": "Que représente le solde budgétaire ?",
        "options": [
            "La différence entre recettes et dépenses publiques",
            "Le niveau de la dette publique",
            "Le montant des exportations",
            "Le revenu par habitant"
        ],
        "answer": "La différence entre recettes et dépenses publiques"
    },
    {
        "question": "Quelle est la principale source de revenus pour financer la dette publique ?",
        "options": [
            "Les impôts",
            "Les subventions",
            "Les investissements étrangers",
            "Les recettes pétrolières"
        ],
        "answer": "Les impôts"
    }
]

with st.form("quiz_form"):
    user_answers = {}
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.markdown(q["question"])
        if "image" in q:
            st.image(q["image"], caption="Illustration", use_container_width=True)
        user_answers[i] = st.radio("Votre réponse :", q["options"], key=f"q_{i}")
    submitted = st.form_submit_button("Valider le quiz")

if submitted:
    score = 0
    st.markdown("## Résultats du Quiz")
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
            st.success(f"Question {i+1} : Correct!")
        else:
            st.error(f"Question {i+1} : Incorrect. La bonne réponse était : **{q['answer']}**")
    st.markdown(f"### Votre score : {score} / {len(questions)}")
