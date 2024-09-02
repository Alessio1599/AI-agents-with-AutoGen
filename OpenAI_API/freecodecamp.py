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
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "How do I get started working out to loose fat and build muscles"

        }
        ]
)
thread_id = thread.id
print(thread_id)