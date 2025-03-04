import os
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Initialize Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=50
)

model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.title("Static Prompting with LangChain PromptTemplate")

# User input
user_input = st.text_area("Enter your prompt:")

# Define static prompt using PromptTemplate
template = PromptTemplate(
    template="""You are an AI assistant. Please respond in a clear and concise manner.
    
    User request: {user_input}
    
    AI Response:
    """.strip(),
    input_variables=["user_input"]
)

# Summarization Button
if st.button('Generate Response'):
    if user_input:
        prompt = template.format(user_input=user_input)  # Fill template with user input
        result = model.invoke(prompt)
        st.subheader("Generated Response:")
        st.write(result.content)
    else:
        st.warning("Please enter a prompt.")
