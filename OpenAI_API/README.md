# OpenAI API
> JSON (JavaScript Object Notation) is commonly used to format data in various applications, including responses from language models (LLMs)

Issues:
- Take token limits into account
  - OpenAI GPT 3.5 turbo has a token limit of about 16k tokens
  - GPT4 has a limit of 8k tokens -> 100k
    - this limit is input+output tokens

- We can define a function to compute the number of tokens

# References
1. [3 Tips for Working With the OpenAI API, Youtube video](https://www.youtube.com/watch?v=6NShYzAV1Lo)
   1. [GitHub repository](https://github.com/ArjanCodes/examples/tree/main/2024/tuesday_tips/openai)
2. [OpenAI Assistants API – Course for Beginners, freeCodeCamp.org, youtube](https://www.youtube.com/watch?v=qHPonmSX4Ms)
   1. Really nice video, I've created an assistant on OpenAI playground

# OpenAI API references
1. [OpenAI cookbook GitHub repository](https://github.com/openai/openai-cookbook)
2. [Official Python library for the OpenAI API](https://github.com/openai/openai-python)