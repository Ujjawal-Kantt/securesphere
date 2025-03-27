import streamlit as st
from PIL import Image

def show():
    st.title("🖼️ Image-based Security Analysis")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            st.success("🔍 Image Analysis Completed! (Mock Result)")
