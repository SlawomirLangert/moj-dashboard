import streamlit as st
import pandas as pd



def check_password():
    # Sprawdza, czy hasło podane przez użytkownika zgadza się z tym w Secrets
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct"):
        return True

    st.text_input("Podaj hasło dostępowe", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state:
        st.error("😕 Hasło nieprawidłowe")
    return False


