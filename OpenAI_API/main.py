from file_handler import read_file
from client import initialize_openai_client
from models import OpenAIModels
from dotenv import load_dotenv

load_dotenv()

def main():
    client = initialize_openai_client()
    
    model = OpenAIModels.GPT4
    
    query = read_file("short_story.txt")
    
    result = handle_request(query=query, model=model, client=client)
    
    print(result)