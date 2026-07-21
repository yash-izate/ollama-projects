from langchain_ollama import OllamaLLM

# Local test first
llm = OllamaLLM(model="gemma2", base_url="http://localhost:11434")

print(llm.invoke("Hello, who are you?"))
