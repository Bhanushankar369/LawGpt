from groq import Groq
from .tools import wikipedia_search, duckduckgo_search

from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY.strip())


tools = [
    {
        "type": "function",
        "function": {
            "name": "wikipedia_search",
            "description": "Search Wikipedia for legal concepts",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "duckduckgo_search",
            "description": "Search DuckDuckGo for legal articles",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    }
]


def generate_answer(prompt):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response.choices[0].message.content