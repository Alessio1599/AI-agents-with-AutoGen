""" 
I'm not the only one who has encountered the following error message:
https://github.com/microsoft/autogen/issues/3345 here there is a discussion about the error message

Error:
[autogen.oai.client: 09-01 20:10:48] {164} WARNING - The API key specified is not a valid OpenAI format; it won't work with the OpenAI-hosted model.
user_proxy (to assistant):

openai.RateLimitError: 
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
"""
import os
import autogen  
from autogen import AssistantAgent, UserProxyAgent

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # Load the .env file

# Access the API key
api_key = os.environ.get('OPENAI_API_KEY')

llm_config = {"model": "gpt-3.5-turbo-16k", "api_key": api_key} #"api_key": os.environ["OPENAI_API_KEY"]
assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of NVDA and TESLA stock price change YTD.",
)