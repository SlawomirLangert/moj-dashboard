import streamlit_authenticator as stauth

# Wpisz tutaj swoje hasło
password = "Haslo123"

# Generowanie haszu w nowej wersji biblioteki
hashed_password = stauth.Hasher.hash(password)

print(f"\nOto Twój hasz do wklejenia do secrets.toml:\n")
print(hashed_password)
print("\n" + "="*50)
