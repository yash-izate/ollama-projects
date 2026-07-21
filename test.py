from langchain_ollama import OllamaLLM

# Ngrok tunnel test
llm = OllamaLLM(model="gemma2", base_url="https://ascend-swimwear-smartly.ngrok-free.dev")

print(llm.invoke("Hello, who are you?"))
