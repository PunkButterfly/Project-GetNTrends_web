import streamlit as st
from entities import Digest, trends

st.title("Поиск трендов, инсайтов и сборка дайджеста в источнике новостей")

with st.container():
    st.header('Дайджест новостей')
    digest_period_1, digest_period_2, digest_period_3, digest_period_4 = st.tabs(["День", "Неделя", "Месяц", "Год"])

    with digest_period_1:

        daily_digest = Digest()
        daily_digest.get_data()

        with st.expander

with st.container():
    st.header("Тренды за последнее время")
    trends_period_1, trends_period_2, trends_period_3, trends_period_4 = st.tabs(["День", "Неделя", "Месяц", "Год"])

    with trends_period_1:

        trends_data = trends.get_trends()





'''
streamlit run app/app.py
'''