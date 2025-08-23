from core.config import Config
from openai import OpenAI

def get_openai_client() -> OpenAI:
    api_key = Config.OPENAI_API_KEY
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is required. "
            "Please set it in your .env file or environment variables."
        )
    return OpenAI(api_key=api_key)
