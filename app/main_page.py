import streamlit as st
from entities import Period
from error_page import error_page


def main_page(received_responses):
    #periods_descriptions = [item.description for item in Period]
    # received_responses: ResponseData.digest.data: List[News_by_category: .category, .content, .channels;
    # ResponseData.insight.data: List[Insight.content]
    # Содержание страницы
    st.title("Поиск трендов, инсайтов и сборка дайджеста в источниках новостей")

    with st.container():
        st.header('Дайджест новостей')

        #tabs = list(st.tabs(periods_descriptions))
        #tabs = list(st.tabs('default'))

        for response in received_responses:
            print('response proceed', response)

            digest = response.digest
            tabs = list(st.tabs(digest.all_categories))
            print('xuy')
            
            try:
                for tab, digest_data in zip(tabs, digest.data):
                    with tab:
                        for news_content, news_channel in zip(digest_data.content, digest_data.channels):
                            st.write(news_content)
                            st.caption(f'Источник: {news_channel}')

            except Exception:
                error_page("Digest being prepared")


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

        #tabs = list(st.tabs(periods_descriptions))
        #tabs = list(st.tabs('default'))

        for response in received_responses:

            insights = response.insights
            try:
                for insight_data in insights.data:
                    st.write(insight_data.content)
                    st.write("\n")
            except Exception:
                error_page("Insights being prepared")