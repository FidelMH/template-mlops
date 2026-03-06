import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")


def main():
    """Page d'accueil avec statut de l'API et métriques."""
    st.title("Gestion des utilisateurs")
    st.write("Bienvenue ! Utilisez le menu pour naviguer.")

    # Statut API
    try:
        r = requests.get(f"{API_URL}/health", timeout=2)
        if r.ok:
            st.success("API connectée")
        else:
            st.error("API en erreur")
    except Exception:
        st.error("API inaccessible")

    # Métriques
    try:
        data = requests.get(f"{API_URL}/data").json()
        col1, col2, col3 = st.columns(3)
        col1.metric("Utilisateurs", len(data))
        scores = [u["score"] for u in data]
        col2.metric(
            "Score moyen", round(sum(scores) / len(scores), 1) if scores else 0
        )
        col3.metric("Meilleur score", max(scores) if scores else 0)
    except Exception:
        pass


if __name__ == "__main__":
    main()
