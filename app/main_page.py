import streamlit as st
from error_page import error_page


st.set_page_config(layout="wide")


def main_page(received_responses):
    # Содержание страницы
    st.title("Сборка дайджеста и поиск инсайтов в новостях")

    with st.container():
        st.header('Дайджест новостей')

        digest_news_limiter = 3
        for response in received_responses:

            digest = response.digest
            try:
                for digest_category, digest_news in digest.data.items():
                    with st.expander(digest_category):
                        news_by_category = digest_news[:digest_news_limiter-1]
                        for news in news_by_category:
                            st.write("")
                            st.caption(f"{news.date}, {news.channel_id}")
                            st.write(news.text)

            except Exception:
                error_page("Insights being prepared")

    with st.container():
        st.header("Инсайты")

        insights_news_limiter = 7
        for response in received_responses:

            insights = response.insights
            try:
                for insight_data in insights.data:
                    with st.expander(insight_data.content):
                        news_by_insight = insight_data.raw_text[:insights_news_limiter-1]
                        for news in news_by_insight:
                            st.write("")
                            st.write(news)

            except Exception:
                error_page("Insights being prepared")