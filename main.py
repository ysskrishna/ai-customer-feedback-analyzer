import streamlit as st
import json
from ai.analyzer import analyze_feedback


def create_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #ccc;
            font-size: 0.85rem;
            padding: 1.5rem 0;
            background-color: #1e1e1e;
            border-radius: 8px;
        '>
            <p style='margin: 0.2rem 0; color: #aaa;'>Created by <strong>Y. Siva Sai Krishna</strong> (@ysskrishna)</p>
            <div style='margin-top: 0.5rem; display: flex; gap: 1rem;'>
                <a href="https://github.com/ysskrishna" target="_blank" style="color: #ccc; text-decoration: none; display: flex; align-items: center; gap: 0.3rem;">
                    <img src="https://img.icons8.com/material-rounded/20/ffffff/github.png"/> GitHub
                </a>
                <a href="https://linkedin.com/in/ysskrishna" target="_blank" style="color: #ccc; text-decoration: none; display: flex; align-items: center; gap: 0.3rem;">
                    <img src="https://img.icons8.com/material-rounded/20/ffffff/linkedin.png"/> LinkedIn
                </a>
                <a href="https://github.com/ysskrishna/ai-customer-feedback-analyzer" target="_blank" style="color: #ccc; text-decoration: none; display: flex; align-items: center; gap: 0.3rem;">
                    <img src="https://img.icons8.com/material-rounded/20/ffffff/source-code.png"/> Repository
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def main():
    st.set_page_config(page_title="AI Customer Feedback Analyzer", layout="wide")
    st.title("AI Customer Feedback Analyzer")

    feedback_text = st.text_area("Enter customer feedback to extract sentiment, topics, and actionable items.")

    if st.button("Analyze Feedback"):
        if not feedback_text.strip():
            st.warning("Please enter some feedback text.")
        else:
            # Show loading spinner while analyzing
            with st.spinner("Analyzing feedback with AI..."):
                try:
                    # Analyze feedback using OpenAI structured output
                    analysis = analyze_feedback(feedback_text)
                    
                    if analysis:
                        st.success("✅ Analysis completed successfully!")
                        st.subheader("Structured Feedback Output")
                        st.json(json.loads(analysis.json()))
                    
                    else:
                        st.error("❌ Failed to analyze feedback. Please check your API key and try again.")
                        
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.info("💡 Make sure you have set your OPENAI_API_KEY in the .env file")
    
    create_footer()


if __name__ == "__main__":
    main()
