import streamlit as st

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
    st.session_state.page = "À propos de moi"

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


# Affichage du contenu en fonction de la page sélectionnée

if st.session_state.page == "À propos de moi":
    st.markdown("<h1 style='text-decoration: underline;'>👤 À propos de moi </h1>", unsafe_allow_html=True)
    st.write("""
        Bonjour et bienvenue sur mon portfolio ! Je m'appelle Mariétou et je suis actuellement en reconversion professionnelle dans le domaine de la Data. Après avoir obtenu un Master 2 en Économie, j'ai accumulé cinq années d'expérience dans les achats, où j'ai acquis de solides compétences en gestion de données, analyse de performance et optimisation des processus.

Cependant, ma passion pour les chiffres et l'analyse m'a poussé à me tourner vers le domaine de la Data. Pour cela, j'ai suivi une formation Data Analyst de 5 mois certifiée RNCP niveau 6, où j'ai appris à maîtriser les outils et techniques d'analyse de données, ainsi qu'à travailler avec  des outils d'analyse de données tels que Python, SQL,  et les outils de visualisation tels que Power BI et Tableau.

Je mets aujourd'hui ces compétences au service de nouveaux projets en Data, avec l’objectif de contribuer à l'optimisation des décisions stratégiques basées sur l’analyse de données. Mon parcours hybride, alliant une expertise en gestion et une formation technique en Data, me permet de comprendre à la fois les enjeux métier et les solutions techniques pour y répondre.

Je suis à la recherche d'une opportunité dans le domaine de la Data, où je pourrais mettre à profit mes compétences techniques et mon expérience en gestion pour participer activement à la transformation numérique des entreprises.

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

    st.subheader("📬 Me Contacter")
    st.write("""
        Si vous souhaitez discuter d'un projet ou collaborer, voici mes coordonnées :
        
        - 📧 **Email** : [nd.mariie@gmail.com](mailto:nd.mariie@gmail.com)
        - 💼 **LinkedIn** : [Mariétou NDIAYE](https://www.linkedin.com/in/mariétou-ndiaye-022b98144)
        - 🖥 **GitHub** : [Mariétou12](https://github.com/Marietou12)
    """)

elif st.session_state.page == "MatchMyStream":
    st.title("🎬 Projet : [MatchMyStream](https://matchmystream-ndarhzydzyy5m93uebox3u.streamlit.app/) - Recommandation de Films")
    
    st.markdown("📌 **Merci de suivre [ce lien](https://matchmystream-ndarhzydzyy5m93uebox3u.streamlit.app/) pour voir le rendu de ce projet !**")

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

# Page MatchMyStream (Recommandation de Films)
