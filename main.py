import streamlit as st
import json
from ai.analyzer import analyze_feedback
from core.csv_feedback import parse_feedback_csv


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
            font-size: 1rem;
            padding: 1.8rem 0;
            background-color: #181c28;
            border-radius: 8px;
        '>
            <p style='margin: 0.3rem 0; color: #aaa;'>Built with ❤️ by <strong>Y. Siva Sai Krishna</strong> (@ysskrishna)</p>
            <div style='margin-top: 0.6rem; display: flex; gap: 1.2rem;'>
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

    col1, col2 = st.columns([1,5])
    
    with col1:
        if st.button("Analyze Feedback", help="Analyze the feedback text with AI"):
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

    with col2:
        if st.button("Clear All", help="Clear the text area and any previous results"):
            st.rerun()

    st.divider()
    st.subheader("Analyze Feedback CSV")
    uploaded_file = st.file_uploader(
        "Upload a CSV with feedback, Xquik-style text, review, comment, or message rows.",
        type=["csv"],
    )

    if uploaded_file is not None and st.button("Analyze CSV Feedback"):
        try:
            feedback_rows, detected_column = parse_feedback_csv(uploaded_file.read())
        except ValueError as validation_error:
            st.error(str(validation_error))
        else:
            st.caption(f"Using '{detected_column}' as the feedback column.")
            batch_results = []
            with st.spinner("Analyzing uploaded feedback..."):
                for feedback in feedback_rows:
                    analysis = analyze_feedback(feedback)
                    if analysis:
                        batch_results.append(
                            {
                                "feedback": feedback,
                                "analysis": json.loads(analysis.json()),
                            }
                        )

            if batch_results:
                st.success(f"Analyzed {len(batch_results)} feedback rows.")
                st.json(batch_results)
            else:
                st.error("Failed to analyze the uploaded feedback rows.")

    create_footer()


if __name__ == "__main__":
    main()
