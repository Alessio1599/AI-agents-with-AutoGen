from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Load pre-trained GPT-Neo model and tokenizer
model_name = "EleutherAI/gpt-neo-2.7B"
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")  # GPT-Neo uses GPT-2 tokenizer

# Generate text
input_text = "Write a paragraph on the importance of AI in thesis writing."
inputs = tokenizer.encode(input_text, return_tensors='pt')
outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
