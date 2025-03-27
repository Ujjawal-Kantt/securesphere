import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINIKEY")

if not GENAI_API_KEY:
    st.error("API Key not found. Set GEMINIKEY in .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
def analyze_logs_with_gemini(log_text):
    prompt = f"""
    You are a cybersecurity expert. Analyze the following security logs and provide:
    - A summary of potential threats and vulnerabilities found.
    - Recommendations for security measures to mitigate risks.
    
    Logs:
    {log_text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No valid response received."
    except Exception as e:
        return f"Error: {str(e)}"

def show():
    st.title("📄 Text-based Security Analysis")
    st.markdown("Upload text files or paste logs for analysis.")

    text_input = st.text_area("Enter security log text")

    if st.button("Analyze"):
        if text_input.strip():
            analysis_result = analyze_logs_with_gemini(text_input)
            st.subheader("🔍 Analysis Result:")
            st.write(analysis_result)
        else:
            st.warning("Please enter some log data for analysis.")

if __name__ == "__main__":
    show()
