import streamlit as st
import trends
st.title('Поиск трендов, инсайтов и сборка дайджеста в источнике новостей')

with st.container():
    st.header('Тренды')
    period1, period2, period3, period4 = st.tabs(['Сегодня', 'Неделя', 'Месяц', 'Год'])

    with period1:
        st.subheader('Что интересного?')

        trends_data = trends.get_trends()



with st.container():
   st.write("This is inside the container")

'''
streamlit run app/app.py
'''