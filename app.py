import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Platforma Eqtisad & Malia", layout="wide")

# Moroccan Arabic marketing phrases (transliterated)
welcome_phrases = ["Marhaba! Bienvenue sur platforma interactive dyalna l'qraya l'eqtisad w l'maliya.",
                   "Dektachif les secrets d'l'eqtisad w l'maliya m3ana!",
                   "Tplonji f'3alam l'arqam w l'istratijiyat l'maliya."]

# Sample data (replace with your actual data)
data = pd.DataFrame({
    "Secteur": ["Fellaha", "Sina3a", "Khadamat", " السياحة (Siyaha)"],  # Example with one Arabic word
    "Contribution (%)": [15, 25, 50, 10]
})

# Title and welcome message
st.title("Platforma Interactive d’Apprentissage d'l'Eqtisad w l'Maliya")
st.write(welcome_phrases[0])  # Display a random welcome phrase

# Navigation
pages = {
    "Dashboard": " نظرة عامة (Nadra 3ama) w mo2ashshirat mafatih",
    "Macro Indicateurs": "تحليل المؤشرات الماكرو اقتصادية (Tahlil l'mo2ashshirat l'macro-eqtisadiya)",
    "Sector Indicateurs": "تصور مؤشرات القطاع (Tasawur mo2ashshirat l'qita3)",
    "Finances Publiques": "تحليل الميزانيات والنفقات العامة (Tahlil l'mizaniyat w nafaqaat l'3ama)",
    "Simulation Avancée": "سيناريوهات اقتصادية تفاعلية (Sinariyohat iqtisadiya tafa3uliya)",
    "Tutoriels": "موارد تعليمية ودروس (Mawarid ta3limiya w dorous)",
    "Analyse": "أدوات تحليل متقدمة (ارتباط ، انحدار) (Adawat tahlil mutaqadima (irtibat, inhidar))",
    "Quiz": "اختبر معلوماتك من خلال اختبار تفاعلي (Ikhtabar ma3lumatik min khilal ikhtibar tafa3uli)"
}

selection = st.sidebar.radio("Navigation", list(pages.keys()))

# Content based on selection
if selection == "Dashboard":
    st.header("Tableau de Bord / Nadra 3ama")
    st.write("Hna aperçu d'l'mo2ashshirat l'mafatih :")

    # Sample chart
    fig = px.pie(data, values="Contribution (%)", names="Secteur", title="مساهمة القطاعات في الاقتصاد (Musahema l'qita3at fi l'eqtisad)")
    st.plotly_chart(fig)

elif selection == "Macro Indicateurs":
    st.header("Macro Indicateurs /  المؤشرات الماكرو اقتصادية (L'mo2ashshirat l'macro-eqtisadiya)")
    # Add content for Macro Indicateurs

elif selection == "Sector Indicateurs":
    st.header("Sector Indicateurs / مؤشرات القطاع (Mo2ashshirat l'qita3)")
    # Add content for Sector Indicateurs

# Add content for other sections...
