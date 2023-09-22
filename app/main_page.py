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
            # tabs = list(st.tabs(digest.all_categories))

            # try:
            #     for tab, digest_data in zip(tabs, digest.data):
            #         with tab:
            #             for news_content, news_channel in zip(digest_data.content, digest_data.channels):
            #                 st.write(news_content)
            #                 st.caption(f'Источник: {news_channel}')
            #
            # except Exception:
            #     error_page("Digest being prepared")


            #try:
                #for news_data in digest.data:
                    # with st.expander(news_data.title):
                    #st.write(news_data.content)
                            # st.caption(news_data.channel)
            #except Exception:
                #error_page("Digest being prepared")
    '''
    with st.container():
        st.header("Текущие тренды")

        tabs = list(st.tabs(periods_descriptions))

        for trends_tab, response in zip(tabs, received_responses):
            with trends_tab:

                trends = response.trends
                try:
                    for trend_data in trends.data:
                        with st.expander(trend_data.keywords):
                            news_by_trend = trend_data.contents
                            for news in news_by_trend:
                                st.write("")
                                st.write(news)
                except Exception:
                    error_page("Trends being prepared")
    '''
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