from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer locally
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Generate text
input_text = "Write a paragraph on the importance of AI in thesis writing."
inputs = tokenizer.encode(input_text, return_tensors='pt')
outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
print(tokenizer.decode(outputs[0]))
