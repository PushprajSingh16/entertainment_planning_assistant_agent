from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL", "llama-3.1-8b-instant"),
            messages=[
                {"role": "system", "content": "You are an entertainment planning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=float(os.getenv("TEMPERATURE", 0.4)),
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating plan: {str(e)}. Please try again later."