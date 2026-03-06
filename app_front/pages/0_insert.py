import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")


def write_data(name, age, score):
    try:
        payload = {"name": name, "age": age, "score": score}
        response = requests.post(API_URL + "/data", json=payload)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as e:
        st.error(f"Erreur HTTP : {e.response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("Impossible de contacter l'API")

    except Exception as e:
        st.error(f"Erreur inatendue : {e}")
    return


st.title("Ajouter des utilisateurs")
with st.form("add_user_form"):
    name = st.text_input("Prénom", key="name")
    age = st.number_input("Age", min_value=0, step=1, key="age")
    score = st.number_input("Score", min_value=0, step=1, key="score")
    submitted = st.form_submit_button("Ajouter")

    if submitted:
        if not name.strip():
            st.error("Entrez un nom")
            st.stop()

        if not age:
            st.error("Age invalide")
            st.stop()

        response = write_data(name, age, score)
        if response:
            st.success("Utilisateur ajouté !")
