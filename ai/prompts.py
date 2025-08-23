CUSTOMER_FEEDBACK_ANALYSIS_PROMPT = """
Analyze the following customer feedback and produce structured, actionable insights.

Customer Feedback:
{feedback_text}

Produce:
1. Overall sentiment: one of [positive, negative, neutral]
2. Actionable items: each with fields [action, priority, category, reasoning]

Instructions:
- Split distinct issues into separate items; merge duplicates.
- Return at most 5 actionable items. If none are justified, return an empty list.
- Prioritization rubric:
  - high: severe breakage, blocks core flows, or impacts many users
  - medium: noticeable friction with moderate impact
  - low: minor polish or non-urgent improvements
- Categories: product_quality, customer_service, pricing, delivery, user_experience, features, bugs, suggestions, other.
- Reasoning must cite or paraphrase concrete evidence from the feedback; avoid speculation.
- Be concise: one sentence for action and one for reasoning.
- If the feedback is ambiguous or lacks detail, say so and keep priority low or skip.
"""
