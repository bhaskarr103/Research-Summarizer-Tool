# Research Summarizer Tool

## Overview
The **Research Summarizer Tool** is a Streamlit-based web application that leverages **LangChain** and **Hugging Face Transformers** to generate dynamic research paper summaries. Users can customize the explanation style and length, ensuring tailored and contextualized summaries.
Explained on my Hashnode profile : [Link]( https://static-and-dynamic-prompts-in-langchain.hashnode.dev/writing-a-simple-dynamic-prompt-app-with-streamlit-using-langchain)

## Features
- **Dynamic Prompting:** Generates responses based on user inputs.
- **Customizable Summaries:** Users can select explanation styles and lengths.
- **Mathematical Details:** Includes equations and code snippets where applicable.
- **Analogies for Clarity:** Uses relatable analogies to simplify complex ideas.
- **Customizable Prompting:** Can be modified to critique papers instead of summarizing.

## Technologies Used
- **Streamlit** – For building the web-based user interface.
- **LangChain** – To create structured prompts dynamically.
- **Hugging Face API** – To utilize the TinyLlama model for text generation.
- **Python & dotenv** – For environment variable management.

## Output

![Screenshot (94)](https://github.com/user-attachments/assets/ce0edd1a-ce04-4e4c-94f0-0eff897e799c)


## Installation
### Prerequisites
Ensure you have Python installed (>=3.8). You also need an API key from Hugging Face.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/research-summarizer.git
   cd research-summarizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Hugging Face API key:
     ```
     HUGGINGFACEHUB_ACCESS_TOKEN=your_api_key_here
     ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Select a research paper from the dropdown.
2. Choose the explanation style and length.
3. Click the **Summarize** button to generate the summary.

## Code Structure
- **app.py** – Main application file containing UI and prompt logic.
- **requirements.txt** – Lists required dependencies.
- **.env** – Stores the API key for Hugging Face.

## Example Prompt Template
```python
 template="""
 Please summarize the research paper titled "{paper_input}" with the following specifications:

 Explanation Style: {style_input}
 Explanation Length: {length_input}

 1. Mathematical Details:
 - Include relevant mathematical equations if present in the paper.
 - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

 2. Analogies:
 - Use relatable analogies to simplify complex ideas.

 If certain information is not available in the paper, respond with: "Insufficient information available."
 """
```

## Customization
You can modify the prompt to:
- Change the task (e.g., critique papers instead of summarizing).
- Adjust the explanation style and level of detail.
- Integrate additional functionalities like citation extraction or detailed critiques.



