import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Portfolio Data Analyst", page_icon="📊", layout="wide")

# Appliquer du CSS pour uniformiser la taille des boutons

st.sidebar.markdown("""
    <style>
    .sidebar-button {
        width: 100%;
        display: block;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
        background-color: #f0f0f0;
        cursor: pointer;
    }
    .sidebar-button:hover {
        background-color: #ddd;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📁 Menu")

# Initialisation de l'état si non défini
if "page" not in st.session_state:
    st.session_state.page = "Présentation"

# Création des boutons de navigation
if st.sidebar.button("👤 À propos de moi"):
    st.session_state.page = "À propos de moi"
if st.sidebar.button("🏠 Présentation projets"):
    st.session_state.page = "Présentation projets"
if st.sidebar.button("🎬 MatchMyStream"):
    st.session_state.page = "MatchMyStream"
if st.sidebar.button("🧸 Toys & Models"):
    st.session_state.page = "Toys & Models"
if st.sidebar.button("☕ HUG Coffee Shop"):
    st.session_state.page = "HUG Coffee Shop"
if st.sidebar.button("🍷 Domaine des Croix"):
    st.session_state.page = "Domaine des Croix"


# Affichage du contenu en fonction de la page sélectionnée

if st.session_state.page == "À propos de moi":
    st.markdown("<h1 style='text-decoration: underline;'>👤 À propos de moi </h1>", unsafe_allow_html=True)
    st.write("""
    Bonjour et bienvenue sur mon portfolio ! Je m'appelle Mariétou et je suis passionnée par l'analyse de données.

    Je me consacre aujourd'hui à transformer les données en leviers de décision stratégique.  
    Formée aux outils et techniques de Data Analysis, je maîtrise notamment **Python**, **SQL**, **Power BI** et **Tableau**, que j'utilise pour explorer, analyser et visualiser les données de manière claire et pertinente.

    **Mon objectif** : mener des projets Data qui permettent de mieux comprendre les phénomènes, d'identifier des tendances et de résoudre des problématiques concrètes grâce à l’analyse de données.

    N'hésitez pas à explorer ce site pour découvrir davantage mes réalisations en Data.
    """)



if st.session_state.page == "Présentation projets":
   
    st.markdown("<h1 style='text-decoration: underline;'>👋 Bienvenue sur mon Portfolio de Data Analyst</h1>", unsafe_allow_html=True)
    st.write("""
        Découvrez mes projets en Data Analyse, mes tableaux de bord interactifs et mes analyses de données réalisées à l'aide de Python, SQL et des outils de visualisation comme Power BI et Streamlit.
        
        Utilisez le menu de navigation à gauche pour explorer mes différents projets. 🚀
    """)

    st.subheader("📌 Projets présentés :")
    st.markdown("✅ **Toys & Models** : Analyse des différents volets (Finance, RH, ventes et logistique) et Dashboard interactif pour une entreprise vendant des modèles réduits et maquettes.")
    st.markdown("✅ **HUG Coffee Shop** : Analyse des ventes et des performances des coffee shops.")
    st.markdown("✅ **MatchMyStream** : Un moteur de recommandation de films à base de Machine Learning pour un cinéma en perte de vitesse.")
    st.markdown("✅ **Domaine des Croix** : Étude de marché stratégique pour un domaine viticole bourguignon souhaitant exporter aux États-Unis.") 

    st.subheader("📬 Me Contacter")
    st.write("""
        Si vous souhaitez discuter d'un projet ou collaborer, voici mes coordonnées :
        
        - 📧 **Email** : [nd.mariie@gmail.com](mailto:nd.mariie@gmail.com)
        - 💼 **LinkedIn** : [Mariétou NDIAYE](https://www.linkedin.com/in/mariétou-ndiaye-022b98144)
        - 🖥 **GitHub** : [Mariétou12](https://github.com/Marietou12)
    """)


elif st.session_state.page == "MatchMyStream":
    st.title("🎬 Projet : [MatchMyStream](https://matchmystream-ndarhzydzyy5m93uebox3u.streamlit.app/) - Recommandation de Films")
    st.markdown("📌 **Merci de suivre [ce lien](https://matchmystream-ndarhzydzyy5m93uebox3u.streamlit.app/) pour voir le rendu de ce projet.**")

    st.subheader("**Contexte :**")
    st.write("""Un cinéma en perte de vitesse dans la région de la Creuse souhaite se moderniser en créant un **moteur de recommandation de films** sur son site web.
    """)

    st.subheader("📊 Objectifs du Projet")
    st.markdown("""
    - **Étude de marché** : Comprendre les habitudes des spectateurs dans la région.
    - **Analyse des films IMDb** : Identifier les tendances (acteurs, genres, durée, notation).
    - **Système de recommandation** : Utiliser le machine learning pour suggérer des films pertinents.
    - **Visualisation et KPIs** : Présenter des statistiques clés sur les films et les préférences du public.
    """)

    st.subheader("🛠 Méthodologie")
    st.markdown("""
    1. **Analyse de la consommation de cinéma dans la région (données CNC, INSEE).**
    2. **Exploration et nettoyage des datasets IMDb et TMDB.**
    3. **Visualisation des tendances avec Pandas, Seaborn et Matplotlib.**
    4. **Implémentation d’un moteur de recommandation (Scikit-Learn).**
    5. **Affichage des films recommandés avec leurs affiches (API TMDB).**
    """)

    st.subheader("📄 Ressources et Données")
    st.markdown("""
    - **Sources des données** : IMDb, TMDB
    - **Formats** : TSV (IMDb), JSON (TMDB)
    - **Taille des datasets** : 7M films, 10M acteurs
    """)

    st.subheader("🚀 Livrables et Outils")
    st.markdown("""
    - Un **dashboard interactif** avec statistiques et recommandations.
    - Un **système de recommandations basé sur le machine learning**.
    - Une **interface testable** en ligne pour les spectateurs du cinéma.
    """)


  
elif st.session_state.page == "Toys & Models":
 
    st.markdown("<h1 style='text-decoration: underline;'>🧸 Projet : Toys & Models</h1>", unsafe_allow_html=True)

    
    st.subheader("**Contexte :**")
    st.write("""   Une entreprise spécialisée dans la vente de maquettes et modèles réduits souhaitait mettre en place un tableau de bord interactif pour suivre ses performances.
Dans le cadre de ce projet, notre équipe avait pour mission de concevoir un dashboard couvrant les ventes, la logistique, la finance et les ressources humaines.
Pour ma part, j'étais spécifiquement en charge de l'analyse financière.
    """)

    st.subheader("📊 Objectifs du tableau de bord")
    st.markdown("""
    - **Ventes** : Chiffre d'affaires, évolution mensuelle, panier moyen.
    - **Finances** : Meilleurs clients, chiffre d'affaire, taux de paiement, paiement moyen.
    - **Logistique** : Stocks critiques, délais de livraison.
    - **Ressources humaines** : Performance des commerciaux.
    """)

    st.subheader("🎥 Démonstration du Dashboard")
    st.markdown("Vous pouvez voir ci dessous un aperçu de ce Dashboard conçu via Power BI")
    st.video("https://youtu.be/gxveiZud-sQ")
    st.markdown("🔗 [Voir la vidéo complète](https://youtu.be/gxveiZud-sQ)")
    
    st.subheader("📄 Outils utilisés")
    st.markdown("""
    - *SQL, MYSQL*
    - *Power BI* 
    
    """)

# Page HUG Coffee Shop
elif st.session_state.page == "HUG Coffee Shop":
    st.markdown("<h1 style='text-decoration: underline;'>☕ Projet : HUG Coffee Shop</h1>", unsafe_allow_html=True)

    st.subheader("**Contexte :**")
    st.write("""HUG Coffee Shop est une chaîne de cafés souhaitant analyser ses ventes et performances.  
        Mon objectif était d’identifier les produits les plus populaires, les tendances de consommation et les périodes de forte affluence.
    """)

    st.subheader("📊 Objectifs de l’analyse")
    st.markdown("""
    - Analyser les ventes par période (heure, jour, mois).
    - Identifier les produits les plus populaires.
    - Étudier l’impact du prix sur les achats.
    - Optimiser la gestion des stocks et du personnel.
    """)
   
    st.subheader("🎥 Démonstration du Dashboard")
    st.video("https://youtu.be/-5FKrwGF_98")
    st.markdown("🔗 [Voir la vidéo complète](https://youtu.be/-5FKrwGF_98)")

    st.subheader("📄 Rapports et Analyses")
    st.markdown("Pour ce projet, j'ai d'abord fait une analyse descriptive et statistique en utilisant Python pour ensuite élaborer le Dashboard Power BI. Vous trouverez ci dessous les differents rapports élaborés au cours de ce projet")

    col1, col2,col3= st.columns(3)

    with col1:
        st.markdown("##### 📘Rapport graphique")
        with open("rapport_graphique_python.pdf", "rb") as file_stat:
            st.download_button(
                label="📥 Télécharger le rapport graphique",
                data=file_stat,
                file_name="rapport_graphyque_python.pdf",
                mime="application/pdf"
            )
    with col2:
        st.markdown("##### 📘 Analyse Statistique")
        with open("Analyse_PYTHON.pdf", "rb") as file_stat:
            st.download_button(
                label="📥 Télécharger l'Analyse Statistique",
                data=file_stat,
                file_name="analyse_statistique.pdf",
                mime="application/pdf"
            )
    with col3:
        st.markdown("##### 📙 Compte Rendu Final")
        with open("Rapport _global_d'analyse.pdf", "rb") as file_report:
            st.download_button(
                label="📥 Télécharger le Compte Rendu Final",
                data=file_report,
                file_name="compte_rendu_final.pdf",
                mime="application/pdf"
            )
    st.subheader("📄 Outils utilisés")
    st.markdown("""
    - *Python*
    - *Power BI*
    
    """)


elif st.session_state.page == "Domaine des Croix":
    st.title("🍷 Projet : Domaine des Croix – Étude de Marché")
    st.markdown("📌 **Projet de positionnement stratégique sur le marché américain des vins pour le Domaine des Croix.**")

    st.subheader("**Contexte :**")
    st.write("""
    Le Domaine des Croix, producteur de vin en Bourgogne, souhaite exporter aux États-Unis. 
    L'objectif est de déterminer un prix de vente compétitif en s'appuyant sur l'analyse de 130 000 références de vins présents sur le marché américain.
    """)

    st.subheader("📊 Objectifs du Projet")
    st.markdown("""
    - Analyser le marché américain du vin (répartition, prix, notes, cépages).
    - Comparer le vin du client aux produits similaires (Pinot Noir, Bourgogne, même millésime).
    - Évaluer un prix optimal selon la stratégie : entrée, médiane, ou haut de gamme.
    - Créer un tableau de bord interactif (Power BI / Streamlit) pour visualiser les insights.
    """)

    st.subheader("🛠 Méthodologie")
    st.markdown("""
    1. **Nettoyage des données** : suppression des valeurs manquantes, harmonisation des cépages et régions.
    2. **Exploration statistique** : distribution des prix, corrélation notes/prix, répartition géographique.
    3. **Analyse comparative** : focus sur les Pinot Noir de Bourgogne (millésime 2016).
    4. **Calculs statistiques** : médiane, percentiles, scoring de similarité avec description.
    """)

    st.subheader("📄 Ressources et Données")
    st.markdown("""
    - **Dataset principal** : 130 000 vins vendus sur le marché américain.
    - **Dataset client** : 1 vin du Domaine des Croix.
    - **Colonnes clés** : prix, notes (points), pays, région, cépage, description.
    """)

    st.subheader("🚀 Livrables et Outils")
    st.markdown("""
    - **Recommandation de prix personnalisée** (par percentile).
    - **Analyse textuelle** de la description via TF-IDF et similarité cosine.
    - **Visualisations interactives** (Plotly, Power BI, Streamlit).
    - **Dashboard final **
    """)

    st.subheader("🎥 Démonstration du Dashboard")
    st.video("https://www.youtube.com/watch?v=0K2SXe49HFQ")
    st.markdown("🔗 [Voir la vidéo complète](https://www.youtube.com/watch?v=0K2SXe49HFQ)")
