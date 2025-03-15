######### CHAT GPT ##############

'''ChatGPT Quick Start: https://platform.openai.com/docs/quickstart?api-mode=chat'''

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
print(query_gpt("Explain what cross-validation is in machine learning."))

######## CLAUDE ###########

'''ANTHROPIC API DOCUMENTATION: https://docs.anthropic.com/en/api/getting-started'''

import anthropic
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY") #export ANTHROPIC_API_KEY="anthropic-key"
client = anthropic.Anthropic(api_key=anthropic_api_key)

def query_claude(prompt):
    response = client.messages.create(
        model="claude-3",  # Change to "claude-2" if needed
        max_tokens=500,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

# Example usage
print(query_claude("Explain what cross-validation is in machine learning."))

####### Google PaLM API (Gemini) #######

'''pip install -q -U google-genai

'''
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)