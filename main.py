import streamlit as st
import json
from ai.models import FeedbackAnalysis, ActionableItem, ActionItemPriorityType, TopicType, SentimentType


def main():
    st.title("Customer Feedback Analysis")
    st.write("Enter customer feedback to extract sentiment, topics, and actionable items.")

    feedback_text = st.text_area("Customer Feedback")

    if st.button("Analyze Feedback"):
        if not feedback_text.strip():
            st.warning("Please enter some feedback text.")
        else:
            # TODO: Replace with OpenAI API call
            example_output = FeedbackAnalysis(
                original_text=feedback_text,
                sentiment=SentimentType.POSITIVE,
                actionable_items=[
                    ActionableItem(
                        action="Improve delivery speed",
                        priority=ActionItemPriorityType.HIGH,
                        category=TopicType.DELIVERY,
                        reasoning="Customer mentioned slow delivery."
                    )
                ]
            )

            st.subheader("Structured Feedback Output")
            st.json(json.loads(example_output.json()))


if __name__ == "__main__":
    main()
