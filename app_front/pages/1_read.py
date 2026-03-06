import os

import pandas as pd
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")


def read_data():
    """Retrieve data from the API."""
    try:
        response = requests.get(API_URL + "/data")
        return response.json()

    except requests.exceptions.HTTPError as e:
        st.error(f"Erreur HTTP : {e.response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("Impossible de contacter l'API")

    except Exception as e:
        st.error(f"Erreur inatendue : {e}")
    return None


st.title("La listes des utilisateurs")
data = read_data()
if data is not None:
    df = pd.DataFrame(data)
    st.dataframe(df)
