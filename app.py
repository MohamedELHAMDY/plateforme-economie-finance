import streamlit as st
import random

st.set_page_config(page_title="Plateforme Économie & Finance", layout="wide")

# Moroccan Arabic marketing phrases (more options)
welcome_phrases = [
    "Marhaba! Bienvenue sur notre plateforme interactive d'apprentissage de l'économie et de la finance.",
    "Découvrez les secrets de l'économie et de la finance avec nous!",
    "Plongez dans le monde des chiffres et des stratégies financières.",
    "Iqra, Fhem, Wastaqbel l'avenir! (Read, Understand, and Embrace the future!)",  # More motivational
    "Maâa-na, ghadi tqraw kolchi li kayn f'l'économie! (With us, you'll learn everything about economics!)"  # More colloquial
]

# Navigation (with descriptions in Moroccan Arabic)
pages = {
    "Dashboard": {"title_ar": "لوحة التحكم", "description_ar": "نظرة عامة على المؤشرات الرئيسية"},
    "Macro Indicateurs": {"title_ar": "المؤشرات الاقتصادية الكلية", "description_ar": "تحليل المؤشرات الاقتصادية الكلية"},
    "Sector Indicateurs": {"title_ar": "مؤشرات القطاع", "description_ar": "تصور مؤشرات حسب القطاع"},
    "Finances Publiques": {"title_ar": "المالية العامة", "description_ar": "تحليل الميزانيات والنفقات العامة"},
    "Simulation Avancée": {"title_ar": "محاكاة متقدمة", "description_ar": "سيناريوهات اقتصادية تفاعلية"},
    "Tutoriels": {"title_ar": "دروس تعليمية", "description_ar": "موارد تعليمية ودروس"},
    "Analyse": {"title_ar": "تحليل", "description_ar": "أدوات تحليل متقدمة (الارتباط ، الانحدار)"},
    "Quiz": {"title_ar": "اختبار", "description_ar": "اختبر معلوماتك من خلال اختبار تفاعلي"}
}

# Title and welcome message (randomized)
st.title("Plateforme Interactive d’Apprentissage de l’Économie et de la Finance")
st.write(random.choice(welcome_phrases))

# Navigation in the sidebar
selection = st.sidebar.radio("تصفح", list(pages.keys()))  # Right-to-left for Arabic

# Content based on selection
selected_page = pages[selection]
st.header(selected_page["title_ar"])  # Arabic title

# Add content for each section (placeholders)
if selection == "Dashboard":
    st.write(selected_page["description_ar"])  # Arabic description
    st.write("Bienvenue au tableau de bord. Ici, vous trouverez un aperçu des indicateurs clés.")
    # Add your dashboard content here
elif selection == "Macro Indicateurs":
    st.write(selected_page["description_ar"])
    st.write("Section dédiée à l'analyse des indices macroéconomiques.")
    # Add your Macro Indicateurs content here
elif selection == "Sector Indicateurs":
    st.write(selected_page["description_ar"])
    st.write("Visualisation des indicateurs par secteur.")
    # Add your Sector Indicateurs content here
# ... (Add content for other sections)

# Example of dynamic content (you can expand this)
st.subheader("Contenu Dynamique")
if st.checkbox("Afficher des informations supplémentaires"):
    st.write("Voici des informations supplémentaires qui s'affichent dynamiquement.")

# Footer (optional)
st.markdown("---")
st.write("© 2024 Votre Organisation")  # Replace with your organization
