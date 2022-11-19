import streamlit as st
from entities import Period, Digest, Trends, Insights, Response


daily_response = Response(Period.DAY)  # TODO: даты
weekly_response = Response(Period.WEEK)
monthly_response = Response(Period.MONTH)
yearly_response = Response(Period.YEAR)
responses = [daily_response, weekly_response, monthly_response, yearly_response]


st.title("Поиск трендов, инсайтов и сборка дайджеста в источнике новостей")

with st.container():
    st.header('Дайджест новостей')

    digest_periods_days_numbers = [item.days_number for item in Period]
    digest_periods_descriptions = [item.description for item in Period]
    digest_tabs = list(st.tabs(digest_periods_descriptions))

    for digest_tab, response_period in zip(digest_tabs, responses):
        with digest_tab:

            digest = response_period.digest

            for news_data in digest.data:
                with st.expander(news_data.title):
                    st.write(news_data.content)
                    st.caption(news_data.date)

with st.container():
    st.header("Текущие тренды")

    trends_periods_days_numbers = [item.days_number for item in Period]
    trends_periods_descriptions = [item.description for item in Period]
    trends_tabs = list(st.tabs(trends_periods_descriptions))

    for trends_tab, response_period in zip(trends_tabs, responses):
        with trends_tab:

            trends = response_period.trends

            for trend_data in trends.data:
                st.write(trend_data.title)

with st.container():
    st.header("Инсайты")

    insights_periods_days_numbers = [item.days_number for item in Period]
    insights_periods_descriptions = [item.description for item in Period]
    insights_tabs = list(st.tabs(insights_periods_descriptions))

    for insights_tab, response_period in zip(insights_tabs, responses):
        with insights_tab:

            insights = response_period.insights

            for insight_data in insights.data:
                st.write(insight_data.title)
                st.caption(insight_data.date)

'''
streamlit run app/app.py
'''
