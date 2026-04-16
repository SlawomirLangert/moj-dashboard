import streamlit as st
import pandas as pd
#from services.functions import check_password
# from services.functions import login
# from services.functions import logoff
from functions import get_authenticator

# 1. Zabezpieczenie przed nieautoryzowanym dostępem
if not st.session_state.get("authentication_status"):
    st.switch_page("main.py")
    st.stop()

# 2. Inicjalizacja authenticatora (potrzebna do wylogowania)
authenticator = get_authenticator()
# 3. Przycisk wylogowania (czyści ciasteczko i sesję)
authenticator.logout('Wyloguj się', 'sidebar') # 'sidebar' przeniesie przycisk do menu bocznego

# Treść Twojego dashboardu...
st.info("Twoja sesja zostanie utrzymana nawet po odświeżeniu strony (F5).")

#def open_dashboard():



    # Główna zawartość dashboardu
   # st.sidebar.button("Wyloguj", on_click=lambda: st.session_state.update({"logged_in": False}))
  #  st.title("Mój Dashboard")
   # st.sidebar.write(f"Witaj, {st.secrets['credentials']['user_name']}!")
   # submit = st.form_submit_button("Zaloguj")

  #  st.title("Panel Główny")
st.sidebar.write(f"Witaj, {st.session_state['name']}!")

    # # Przycisk wylogowania
    # # 'main' oznacza, że przycisk pojawi się w głównym oknie
    # authenticator.logout('Wyloguj się', 'main')
    #
    # # Jeśli po kliknięciu stan zmieni się na None, wróć do logowania
    # if not st.session_state["authentication_status"]:
    #     st.switch_page("../main.py")



st.set_page_config(layout="wide", page_title="Aplikacja pogodowa")
st.title("Aplikacja pogodowa")

st.title("Uniwersalny czytnik plików")

    # file_uploader z ograniczonymi rozszerzeniami
uploaded_file = st.sidebar.file_uploader(
        "Wybierz plik (XLSX, CSV lub XML)",
        type=["xlsx", "csv", "xml"]
    )

if uploaded_file is not None:
        # Pobieramy nazwę pliku, aby sprawdzić rozszerzenie
        file_name = uploaded_file.name
        st.info(f"Wczytano plik: {file_name}")

        try:
            # Logika rozpoznawania rozszerzenia
            if file_name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                st.success("Rozpoznano format CSV")

            elif file_name.endswith('.xlsx'):
                # Wymaga biblioteki: pip install openpyxl
                df = pd.read_excel(uploaded_file)
                st.success("Rozpoznano format Excel (XLSX)")

            elif file_name.endswith('.xml'):
                df = pd.read_xml(uploaded_file)
                st.success("Rozpoznano format XML")

            # Wyświetlenie danych
            st.write("Podgląd danych:")
            st.dataframe(df)

            # Prosta statystyka dla zachęty
            st.metric("Liczba wierszy", len(df))

        except Exception as e:
            st.error(f"Błąd podczas wczytywania pliku: {e}")
else:
        st.warning("Czekam na plik...")

st.divider()