import streamlit as st

def show():
    st.title("🧠 Bias-free & Explainable AI")

    st.markdown("Understanding AI's decisions in cybersecurity.")
    
    if st.button("Explain AI Decisions"):
        st.success("💡 Explanation Generated! (Mock Response)")
