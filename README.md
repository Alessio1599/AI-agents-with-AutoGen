# AI-agents-with-AutoGen

# Structure
- [Lesson 1: Multi-Agent Conversation and Stand-up Comedy](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/1%20Multi-agent%20conversation%20and%20stand-up%20comedy)
- [Lesson 2: Sequential Chats and Customer Onboarding](https://github.com/Alessio1599/AI-agents-with-AutoGen/tree/main/2%20Sequential%20chats)
- []()

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