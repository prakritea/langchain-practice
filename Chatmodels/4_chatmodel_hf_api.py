from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    task="text-generation"
)

response = llm.invoke("What is the capital of India?")
print(response)
