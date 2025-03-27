import streamlit as st
from PIL import Image

def show():
    st.title("🏠 Cybersecurity Dashboard")

    # Load and display the logo
    try:
        img = Image.open("assets/logo.png")
        st.image(img, width=200)
    except Exception as e:
        st.error(f"Error loading image: {e}")

    st.markdown("""
        ### Welcome to the Cybersecurity Dashboard  
        This platform helps in analyzing cybersecurity threats using AI-powered models.
    """)
