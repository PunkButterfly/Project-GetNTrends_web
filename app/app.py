import streamlit as st
from entities import Digest, Period

st.title("Поиск трендов, инсайтов и сборка дайджеста в источнике новостей")

with st.container():
    st.header('Дайджест новостей')

    digest_periods_descriptions = [item.description for item in Period]
    digest_periods_days_number = [item.days_number for item in Period]
    digest_tabs = list(st.tabs(digest_periods_descriptions))

    for digest_tab, digest_period in zip(digest_tabs, digest_periods_days_number):
        with digest_tab:

            digest = Digest(digest_period)
            digest.get_data()

            for news_data in digest.data:
                with st.expander(news_data.title):
                    st.write(news_data.content)
                    st.caption(news_data.date)

with st.container():
    st.header("Тренды за последнее время")
    trends_period_1, trends_period_2, trends_period_3, trends_period_4 = st.tabs(["День", "Неделя", "Месяц", "Год"])

    with trends_period_1:
        pass





'''
streamlit run app/app.py
'''