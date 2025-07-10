import streamlit as st
import requests

st.title("Güncel Kur Bilgileri")
st.markdown("USD/TRY, EUR/TRY ve XAU/TRY (Altın)")

def kur_getir():
    try:
        response = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=TRY,EUR,XAU")
        data = response.json()
        
        usd_try = data["rates"]["TRY"]
        eur_try = usd_try / data["rates"]["EUR"]  # USD bazlıdan EUR/TRY hesaplıyoruz
        xau_try = usd_try / data["rates"]["XAU"]  # USD bazlıdan XAU/TRY hesaplıyoruz

        return round(usd_try, 2), round(eur_try, 2), round(xau_try, 2)
    except Exception as e:
        st.error(f"Kur bilgileri alınamadı: {e}")
        return None, None, None

if st.button("🔄 Tazele"):
    usd, eur, xau = kur_getir()
    if usd and eur and xau:
        st.success("Kurlar başarıyla güncellendi.")
        st.metric("💵 USD/TRY", f"{usd}")
        st.metric("💶 EUR/TRY", f"{eur}")
        st.metric("🥇 XAU/TRY", f"{xau}")
else:
    st.info("Lütfen 'Tazele' butonuna basarak kurları güncelleyin.")
