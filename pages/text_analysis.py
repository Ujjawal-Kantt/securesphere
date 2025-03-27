import streamlit as st

def show():
    st.title("📄 Text-based Security Analysis")
    st.markdown("Upload text files or paste logs for analysis.")
    
    text_input = st.text_area("Enter security log text")
    
    if st.button("Analyze"):
        st.success("🔍 Analysis Completed! (Mock Result)")
