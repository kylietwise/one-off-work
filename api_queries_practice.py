######### CHAT GPT ##############

from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY") # export OPENAI_API_KEY="your-openai-api-key"

client = OpenAI(api_key=api_key)

def query_gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",  # You can change to "gpt-4" or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

# Example usage
print(query_gpt("Explain black holes in simple terms."))

######## 