from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file (for OpenAI API key)
load_dotenv()

# Initialize ChatOpenAI model
model = ChatOpenAI(
    model='gpt-4',             # Model name
    temperature=1.5,           # Controls randomness (higher = more creative)
    max_completion_tokens=10   # Limit tokens in response
)

# Call the model with a prompt
result = model.invoke("Write a 5 line poem on cricket")

# Print the response content
print(result.content)
