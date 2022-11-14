import streamlit as st
from entities import Period, Digest, Trends, Insights

st.title("Поиск трендов, инсайтов и сборка дайджеста в источнике новостей")

with st.container():
    st.header('Дайджест новостей')

    digest_periods_days_numbers = [item.days_number for item in Period]
    digest_periods_descriptions = [item.description for item in Period]
    digest_tabs = list(st.tabs(digest_periods_descriptions))

    for digest_tab, digest_period in zip(digest_tabs, digest_periods_days_numbers):
        with digest_tab:

            digest = Digest(digest_period)
            digest.get_data()

            for news_data in digest.data:
                with st.expander(news_data.title):
                    st.write(news_data.content)
                    st.caption(news_data.date)

with st.container():
    st.header("Текущие тренды")

    trends_periods_days_numbers = [item.days_number for item in Period]
    trends_periods_descriptions = [item.description for item in Period]
    trends_tabs = list(st.tabs(trends_periods_descriptions))

    for trends_tab, trends_period in zip(trends_tabs, trends_periods_days_numbers):
        with trends_tab:

            trends = Trends(trends_period)
            trends.get_data()

            for trend_data in trends.data:
                st.write(trend_data.title)

with st.container():
    st.header("Инсайты")

    insights_periods_days_numbers = [item.days_number for item in Period]
    insights_periods_descriptions = [item.description for item in Period]
    insights_tabs = list(st.tabs(insights_periods_descriptions))

    for insights_tab,  insights_period in zip(insights_tabs,  insights_periods_days_numbers):
        with insights_tab:

            insights = Insights(insights_period)
            insights.get_data()

            for insight_data in insights.data:
                with st.expander(insight_data.header):
                    for source in insight_data.sources:
                        st.write(source.title)
                        st.caption(source.date)








'''
streamlit run app/app.py
'''