import streamlit as st

def show():
    st.title("📊 Automated Security Reports")

    st.markdown("View security reports and summaries.")

    if st.button("Generate Report"):
        st.success("📄 Report Generated Successfully! (Mock Data)")
