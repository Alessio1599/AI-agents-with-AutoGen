import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv()

client = openai.OpenAI() # with this client we will be able to call the openai API

# After creating the assistant and thread, we can now send a message to the assistant and run it.

# == Hardcode our ids ==
assistant_id = 'asst_hhUxKDVQaYfUBnBh5V4lclka'
thread_id = 'thread_A83ryKXAIDKTa71iA8rrl0SE'

# == Create a Message ==
message = "What are the best exercises for lean muscles and getting rid of fat?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

# == Run our assistant ==
run =client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as James Bond"
)