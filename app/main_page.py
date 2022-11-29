import streamlit as st
from entities import Period


def main_page(received_responses):
    periods_descriptions = [item.description for item in Period]

    # Содержание страницы
    st.title("Поиск трендов, инсайтов и сборка дайджеста в источнике новостей")

    with st.container():
        st.header('Дайджест новостей')

        tabs = list(st.tabs(periods_descriptions))

        for digest_tab, response in zip(tabs, received_responses):
            with digest_tab:

                digest = response.digest

                for news_data in digest.data:
                    with st.expander(news_data.title):
                        st.write(news_data.content)
                        st.caption(news_data.channel)

    with st.container():
        st.header("Текущие тренды")

        tabs = list(st.tabs(periods_descriptions))

        for trends_tab, response in zip(tabs, received_responses):
            with trends_tab:

                trends = response.trends

                for trend_data in trends.data:
                    with st.expander(trend_data.keywords):
                        news_by_trend = trend_data.contents
                        for news in news_by_trend:
                            st.write("")
                            st.write(news)

    with st.container():
        st.header("Инсайты")

        tabs = list(st.tabs(periods_descriptions))

        for insights_tab, response in zip(tabs, received_responses):
            with insights_tab:

                insights = response.insights

                for insight_data in insights.data:
                    st.write(insight_data.content)
                    st.write("\n")
