import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_questions(tech_stack):
    prompt = (
        f"Generate 3 to 5 interview-style technical questions "
        f"for a candidate skilled in {tech_stack}. Include a mix of practical and conceptual questions."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    print(response)
    content = response.choices[0].message.content.strip()
    return content.split("\n")
