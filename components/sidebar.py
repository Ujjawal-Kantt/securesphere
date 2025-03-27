import streamlit as st

def load_sidebar(PAGES):
    st.sidebar.title("🔒 Cybersecurity Dashboard")
    choice = st.sidebar.radio("Navigation", list(PAGES.keys()))

    page = PAGES[choice]  # Get selected page
    page.show()
