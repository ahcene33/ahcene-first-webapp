import streamlit as st
import pandas as pd

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

@st.cache_data
def load_users():
    df = pd.read_csv("users.csv", sep=";")
    df.columns = df.columns.str.strip()
    return df

users_df = load_users()
users_df["name"] = users_df["name"].str.strip()
users_df["password"] = users_df["password"].astype(str).str.strip()

if not st.session_state.logged_in:
    st.title("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        user = users_df[users_df["name"] == username.strip()]
        if not user.empty and user.iloc[0]["password"] == password.strip():
            st.session_state.logged_in = True
            st.session_state.username = username
            # pas de rerun ici : on affiche tout dans la même exécution
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

# suite de l’app, même sans rerun
if st.session_state.logged_in:
    # Barre latérale à gauche
    st.sidebar.title("Menu")
    
    # Message de bienvenue (hors du menu)
    st.sidebar.markdown(f"**Bienvenue {st.session_state.username}**")

    # Menu sans "Bienvenue {utilisateur}" ni "Déconnexion"
    page = st.sidebar.radio("Navigation", ["Accueil", "Les photos de mon chat"])

    # Bouton de déconnexion séparé
    if st.sidebar.button("Déconnexion"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.info("Déconnecté. Rechargez la page si besoin.")

    # Zone principale à droite
    if page == "Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/640px-Lion_waiting_in_Namibia.jpg")

    elif page == "Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat :-)")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://shawsheenanimalhospital.com/wp-content/uploads/2022/12/iStock-1149359608-scaled.jpg")
        with col2:
            st.image("https://www.lifewithcats.tv/wp-content/uploads/2011/04/Jumping-Cat.jpg")
        with col3:
            st.image("https://cdn.prod.website-files.com/5e55edd70aff9d4e8cf28aed/60a42459841a596126136981_wellness.png")



