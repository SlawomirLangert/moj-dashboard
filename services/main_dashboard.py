import streamlit as st
import pandas as pd
from services.functions import check_password



def open_dashboard():
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