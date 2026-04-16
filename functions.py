#from services.main_dashboard import open_dashboard
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

def get_authenticator():
    # Pobieramy dane z secrets.toml
    credentials = st.secrets["auth_credentials"].to_dict()
    cookie = st.secrets["auth_cookie"]

    authenticator = stauth.Authenticate(
        credentials,
        cookie["name"],
        cookie["key"],
        cookie["expiry_days"]
    )
    return authenticator


# def logoff():
#     st.session_state.logged_in = False
#     login()

#
# def login():
#     st.title("Logowanie: ")
#
#     # Pobranie poprawnych danych z pliku secrets.toml
#     correct_username = st.secrets["credentials"]["user_name"]
#     correct_password = st.secrets["credentials"]["password"]
#
#     # Formularz logowania
#     with st.form("login_form"):
#         username = st.text_input("Użytkownik")
#         password = st.text_input("Hasło", type="password")
#         submit = st.form_submit_button("Zaloguj")
#
#         if submit:
#             if username == correct_username and password == correct_password:
#                 st.session_state["logged_in"] = True
#                 st.success("Zalogowano pomyślnie!")
#                 st.rerun()
#             else:
#                 st.error("Błędny login lub hasło")
#     return False
#
    # # Zarządzanie stanem sesji
    # if "logged_in" not in st.session_state:
    #     st.session_state["logged_in"] = False
    #
    # if not st.session_state["logged_in"]:
    #     login()
    # else:
    #     open_dashboard()
    #     # Główna zawartość dashboardu
    #     # st.sidebar.button("Wyloguj", on_click=lambda: st.session_state.update({"logged_in": False}))
    #     # st.title("Mój Dashboard")
    #     # st.write(f"Witaj, {st.secrets['credentials']['username']}! Oto Twoje tajne dane.")
    #     # st.line_chart([1, 5, 2, 6, 3])



# def check_password():
#         # Sprawdza, czy hasło podane przez użytkownika zgadza się z tym w Secrets
#         def password_entered():
#             if st.session_state["password"] == st.secrets["password"]:
#                 st.session_state["password_correct"] = True
#                 del st.session_state["password"]
#             else:
#                 st.session_state["password_correct"] = False
#
#         if st.session_state.get("password_correct"):
#             return True
#
#         st.text_input("Podaj hasło dostępowe", type="password", on_change=password_entered, key="password")
#         if "password_correct" in st.session_state:
#             st.error("😕 Hasło nieprawidłowe")
#         return False


