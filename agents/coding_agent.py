from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def coding_agent(issue, research_result):

    prompt = f"""
You are a senior software engineer.

GitHub Issue:
{issue}

Research Analysis:
{research_result}

Write the corrected Python code to fix the issue.
Only return the fixed code.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content