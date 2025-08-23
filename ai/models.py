from typing import List
from pydantic import BaseModel
from ai.enums import ActionItemPriorityType, TopicType, SentimentType

class ActionableItem(BaseModel): 
    action: str
    priority: ActionItemPriorityType
    category: TopicType
    reasoning: str

class FeedbackAnalysis(BaseModel):
    original_text: str
    sentiment: SentimentType
    actionable_items = List[ActionableItem]

