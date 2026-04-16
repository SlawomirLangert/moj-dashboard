#from services.functions import check_password
#from services.functions import login
import streamlit as st
import os
#dashboard = render_dashboard(Config.filepath)
from functions import get_authenticator

# Ten kod wypisze Ci dostępne ścieżki w konsoli lub na stronie
#from streamlit.source_util import get_pages

#
# pages = get_pages("main.py")
# st.write("Dostępne strony w aplikacji:", pages)

# Musi być na samej górze głównego pliku
st.set_page_config(page_title="Logowanie", initial_sidebar_state="collapsed")

# To pokaże Ci, gdzie Streamlit "myśli", że jest
st.write("Twoja ścieżka robocza to:", os.getcwd())

# To sprawdzi, czy plik fizycznie istnieje tam, gdzie Streamlit go szuka
if os.path.exists("pages/main_dashboard.py"):
    st.success("Plik dashboardu został odnaleziony!")
else:
    st.error("BŁĄD: Streamlit nie widzi folderu pages/ lub pliku main_dashboard.py")

# # 1. Inicjalizacja

authenticator = get_authenticator()
#
# # Próba automatycznego logowania przez ciasteczko lub formularz
authenticator.login(location='main')

if st.session_state["authentication_status"]:
    # Jeśli zalogowany, przekieruj do dashboardu
    st.switch_page("pages/main_dashboard.py")
elif st.session_state["authentication_status"] is False:
    st.error('Błędny login lub hasło')
elif st.session_state["authentication_status"] is None:
    st.warning('Proszę się zalogować')







# #początek programu w głównym pliku main
# # 1. Inicjalizacja stanu zalogowania
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# #
# # # 2. Logika wyświetlania
# if not st.session_state.logged_in:
#     # Wywołujemy login() tylko, gdy nie jesteśmy zalogowani
#     if login():
#         st.session_state.logged_in = True
#        # st.rerun() # Odświeżamy aplikację, by wejść w drugi warunek
# else:
#     # Wywołujemy dashboard tylko po zalogowaniu
#     open_dashboard()

# # if check_password():
# #     st.success("Zalogowano pomyślnie!")
# #     st.write("Witaj w zabezpieczonej aplikacji!")
# #     open_dashboard()
#
#
#     # Tutaj Twój kod dashboardu...
