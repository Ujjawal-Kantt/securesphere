import streamlit as st

def show():
    st.title("🤖 Conversational AI for Threat Insight")

    user_input = st.text_input("Ask about cybersecurity threats:")
    
    if st.button("Get AI Response"):
        st.info(f"🤖 AI Response: (Mock Answer for '{user_input}')")
