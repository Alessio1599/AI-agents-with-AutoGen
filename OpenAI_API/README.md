# OpenAI API
> JSON (JavaScript Object Notation) is commonly used to format data in various applications, including responses from language models (LLMs)

> Check the OpenAI platform (playground, dashboard)

Issues:
- Take token limits into account
  - OpenAI GPT 3.5 turbo has a token limit of about 16k tokens
  - GPT4 has a limit of 8k tokens -> 100k
    - this limit is input+output tokens

- We can define a function to compute the number of tokens

# OpenAI Assistants API – Course for Beginners, freeCodeCamp.org [2]
Description:

"Learn how to use the OpenAI's Assistants API to build powerful AI assistants. In this course, we'll explore how to leverage the Assistants API by OpenAI to create dynamic, intelligent web apps using Streamlit. 
What we'll cover:

1️⃣ Function Calling with the API: Learn to seamlessly integrate the Assistants API into your applications, enabling advanced AI functionalities right at your fingertips.

2️⃣ Knowledge Retrieval: Discover how to use the API to extract information, answer questions, and make your applications smarter and more responsive.

3️⃣ Code Interpreter Capabilities: Dive into the API's ability to interpret and generate code, a game-changer for automating tasks and enhancing your app's capabilities.

4️⃣ LLM Fundamentals: Gain a solid understanding of Large Language Models (LLMs) and how they form the backbone of OpenAI's Assistants API. This module demystifies the technology and provides a foundation for advanced application development."

# References
1. [3 Tips for Working With the OpenAI API, Youtube video](https://www.youtube.com/watch?v=6NShYzAV1Lo)
   1. [GitHub repository](https://github.com/ArjanCodes/examples/tree/main/2024/tuesday_tips/openai)
2. [OpenAI Assistants API – Course for Beginners, freeCodeCamp.org, youtube](https://www.youtube.com/watch?v=qHPonmSX4Ms)
   1. Really nice video, I've created an assistant on OpenAI playground
3. [OpenAI playground](https://platform.openai.com/playground/chat?models=gpt-4o-mini)
   1. Here I can see the created assistants

# OpenAI API references
1. [OpenAI cookbook GitHub repository](https://github.com/openai/openai-cookbook)
2. [Official Python library for the OpenAI API](https://github.com/openai/openai-python)