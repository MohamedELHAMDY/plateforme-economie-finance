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
    # ... (autres questions)
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
