import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

# Load Hugging Face API Key
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Define LLM with proper model_kwargs
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens= 50
)


# Initialize LangChain Model
model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.header('🔍 Research Tool')

# User Inputs
paper_input = st.selectbox("Select Research Paper", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
]) 

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])

# Define Prompt Template
template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:

    Explanation Style: {style_input}
    Explanation Length: {length_input}

    1. Mathematical Details:
       - Include relevant mathematical equations if present in the paper.
       - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

    2. Analogies:
       - Use relatable analogies to simplify complex ideas.

    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"]
)

# Generate Prompt
prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)

# Summarization Button
if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)  
