import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  # Load the .env file
# os.environ["OPENAI_API_KEY"]

# Access the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
OpenAI.api_key = api_key

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
