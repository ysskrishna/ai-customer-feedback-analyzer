from typing import Optional
from ai.client import get_openai_client
from ai.prompts import CUSTOMER_FEEDBACK_ANALYSIS_PROMPT
from models.models import FeedbackAnalysis


def analyze_feedback(feedback_text: str) -> Optional[FeedbackAnalysis]:
    client = get_openai_client()
    response = client.responses.parse(
        model="gpt-4o-2024-08-06",
        input=[
            {"role": "system", "content": "You are an expert customer feedback analyst."},
            {"role": "user", "content": CUSTOMER_FEEDBACK_ANALYSIS_PROMPT.format(feedback_text=feedback_text)}
        ],
        text_format=FeedbackAnalysis,
    )
    
    return response.output_parsed