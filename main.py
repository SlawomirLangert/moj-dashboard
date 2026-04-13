from services.functions import check_password
from services.main_dashboard import open_dashboard
import streamlit as st

#dashboard = render_dashboard(Config.filepath)

#początek programu w głównym pliku main
if check_password():
    st.success("Zalogowano pomyślnie!")
    st.write("Witaj w zabezpieczonej aplikacji!")
    open_dashboard()

    # Tutaj Twój kod dashboardu...
