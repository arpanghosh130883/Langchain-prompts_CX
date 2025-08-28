from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)


print(chat_history)

# Save chat history to a text file
with open("chat_history.txt", "w", encoding="utf-8") as f:
    for msg in chat_history:
        role = msg.__class__.__name__.replace("Message", "")
        f.write(f"{role}: {msg.content}\n")
