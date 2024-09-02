import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv()

# openai.api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI() # with this client we will be able to call the openai API

model ='gpt-3.5-turbo-16k'

#== Create our assistant ==
personal_trainer_assistant = client.beta.assistants.create(
    name="Personal Trainer",
    instructions="""You are the best personal trainer and nutritionist in the world. You have trained high-caliber athletes and movie stars.""",
    model=model
) 

assistant_id = personal_trainer_assistant.id
print(assistant_id)


#== Thread ==
# series of interactions or messages between you and the model that are related to a single topic or conversation.

# this code snippet creates a new conversation thread with an initial message from the user 
# asking about how to start working out to lose fat and build muscle.

# client.beta.threads.create(...): This function call creates a new thread or conversation.
thread = client.beta.threads.create(
    messages=[ # messages=[{...}]: This specifies the content of the initial message(s) in the thread. 
        {
            "role": "user",
            "content": "How do I get started working out to loose fat and build muscles"

        }
        ]
)
thread_id = thread.id
print(thread_id)

# Running the previous part of code I've created an assistant called "Personal Trainer" and a thread with a message from the user asking how to get started working out to loose fat and build muscles. Now I will use the assistant to respond to the user's message.

# == Hardcode our ids ==
assistant_id = 'asst_hhUxKDVQaYfUBnBh5V4lclka'
thread_id = 'thread_A83ryKXAIDKTa71iA8rrl0SE'

# == Create a Message ==
message = "What are the best exercises for lean muscles and getting rid of fat?"
message = client.beta.threads.messages.create(
    
)