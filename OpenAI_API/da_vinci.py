""" 
You exceeded your current quota, please check your plan and billing details. For more information on this error, 
read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota'
"""
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Once upon a time, in a land far far away, there was a dragon who"

response = openai.completions.create(
    model='gpt-3.5-turbo',
    prompt=prompt,
    temperature=0.4,
    max_tokens=64
    )