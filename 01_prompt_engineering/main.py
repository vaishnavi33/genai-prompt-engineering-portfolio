from transformers import pipeline

# Simple test: text generation
generator = pipeline("text-generation", model="gpt2")

prompt = "Hello, I am building a bias-aware healthcare assistant."
result = generator(prompt, max_length=50, num_return_sequences=1)

print("Generated text:\n")
print(result[0]['generated_text'])
cd ~/genai-prompt-engineering-portfolio/02_rag_systems/
