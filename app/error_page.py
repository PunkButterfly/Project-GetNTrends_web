import streamlit as st


def error_page(error_description: str = "Doing some work. Come back later"):
    st.error(error_description, icon="🚨")
