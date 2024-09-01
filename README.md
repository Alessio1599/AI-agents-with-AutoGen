# AI-agents-with-AutoGen

# Structure
- [Lesson 1: Multi-Agent Conversation and Stand-up Comedy](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/1%20Multi-agent%20conversation%20and%20stand-up%20comedy)
- [Lesson 2: Sequential Chats and Customer Onboarding](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/2%20Sequential%20chats)
- [Lesson 3: Reflection and Blogpost Writing](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/3%20Reflection%20and%20Blogpost%20Writing)
- [Lesson 4: Tool Use and Conversational Chess](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/4%20Tool%20Use%20and%20Conversational%20Chess)
- [Lesson 5: Coding and Financial Analysis](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/5%20Coding%20and%20Financial%20Analysis)
- [Lesson 6: Planning and Stock Report Generation](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/6%20Planning%20and%20Stock%20Report%20Generation)

# Directory structure 
```
├── 1 Multi-agent conversation and stand-up comedy
│   ├── L1_Multi-Agent_Conversation_and_Stand-up_Comedy.ipynb
│   ├── README.md
│   ├── requirements.txt
│   └── utils.py
├── 2 Sequential chats
│   ├── L2_Sequential_Chats_and_Customer_Onboarding.ipynb
│   └── README.md
├── Makefile
├── README.md
└── img
    └── customer_onboarding_task.png
```

```python
from autogen import ConversableAgent

llm_config={"model":"gpt-3.5-turbo"}

agent = ConversableAgent(
    name='chatbot',
    system_message='You are a chatbot and you are an expert financial advisor'
    llm_config=llm_config,
    human_input_mode='NEVER'
)
```

# Reference
- [AI Agentic Design Patterns with AutoGen, DeepLearning.AI, short course](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/)