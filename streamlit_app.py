import os
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------------
# Edge browser tabs metadata
# -------------------------------
edge_all_open_tabs = [
    {"pageTitle": "Streamlit", "pageUrl": "https://ollama-projects-yash.streamlit.app", "tabId": 1581721663, "isCurrent": True},
    {"pageTitle": "yash-izate/ollama-projects", "pageUrl": "https://github.com/yash-izate/ollama-projects", "tabId": 1581721649, "isCurrent": False}
]

# Format tabs into readable context
tabs_context = "\n".join(
    [f"- {tab['pageTitle']} ({'Active' if tab['isCurrent'] else 'Background'})"
     for tab in edge_all_open_tabs]
)

# -------------------------------
# Prompt setup
# -------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use browsing context if relevant."),
    ("user", "Question: {question}\n\nOpen Tabs:\n{tabs}")
])

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🚀 Simple Ollama + Streamlit App")
input_text = st.text_input("What question do you have?")

# -------------------------------
# Auto-switch: localhost vs ngrok
# -------------------------------
BASE_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

llm = OllamaLLM(model="gemma2", base_url=BASE_URL)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# -------------------------------
# Run chain
# -------------------------------
if input_text:
    try:
        response = chain.invoke({"question": input_text, "tabs": tabs_context})
        st.markdown("### 🤖 Answer")
        st.write(response)
    except Exception as e:
        st.error(f"Connection failed: {e}")
