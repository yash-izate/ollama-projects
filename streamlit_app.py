import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt setup
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("🚀 Where should we begin!")
input_text = st.text_input("What question do you have?")

# Ollama LLM (Gemma2)
llm = OllamaLLM(
    model="gemma2",
    base_url="http://ascend-swimwear-smartly.ngrok-free.dev"
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run chain
if input_text:
    response = chain.invoke({"question": input_text})
    st.markdown("### 🤖 Answer")
    st.write(response)


