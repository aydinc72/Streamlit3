import streamlit as st
import requests

st.title("Güncel Kur Bilgileri")
st.markdown("USD/TRY, EUR/TRY, Altın, Gümüş")

def kur_getir():
    try:
        #response = requests.get("https://v6.exchangerate-api.com/v6/042c28ecc2f6239f665c9f42/pair/USD/TRY")
        response = requests.get("https://finans.truncgil.com/v4/today.json")
        data = response.json()
        usd_try = data["USD"]["Buying"]   
        usd_change = data["USD"]["Change"]   
        eur_try = data["EUR"]["Buying"]     
        eur_change = data["EUR"]["Change"]   
        #response = requests.get("https://v6.exchangerate-api.com/v6/042c28ecc2f6239f665c9f42/pair/EUR/TRY")
        #data = response.json()
        #eur_try = data["conversion_rate"]   
        xau_try = data["GRA"]["Buying"]   
        xau_change = data["GRA"]["Change"]   
        sil_try = data["GUMUS"]["Buying"]   
        sil_change = data["GUMUS"]["Change"]   

        return round(usd_try, 2), round(eur_try, 2), round(xau_try, 2), round(sil_try, 2), round(usd_change, 2), round(eur_change, 2), round(xau_change, 2), round(sil_change, 2)
    except Exception as e:
        st.error(f"Kur bilgileri alınamadı: {e}")
        return None, None, None, None, None, None, None, None

if st.button("🔄 Tazele"):
    usd, eur, xau, sil, usd_chg, eur_chg, xau_chg, sil_chg = kur_getir()
    if usd and eur and xau and sil:
        st.success("Kurlar başarıyla güncellendi.")
        st.metric("💵 USD/TRY", f"{usd}", delta = usd_chg)
        st.metric("💶 EUR/TRY", f"{eur}", delta = eur_chg)
        st.metric("🥇 GRAM ALTIN", f"{xau}", delta = xau_chg)
        st.metric("🔘 GRAM GÜMÜŞ", f"{sil}", delta = sil_chg)
else:
    st.info("Lütfen 'Tazele' butonuna basarak kurları güncelleyin.")
