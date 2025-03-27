import streamlit as st
from PIL import Image

def show():
    st.title("🏠 SecureSphere")

    # Load and display the logo
    try:
        img = Image.open("./assets/logo.jpeg")
        st.image(img, width=200)
    except Exception as e:
        st.error(f"Error loading image: {e}")

    st.markdown("""
        ### Welcome to the SecureSphere Dashboard  
        This platform helps in analyzing cybersecurity threats using AI-powered models.
    """)
