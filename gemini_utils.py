import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Function to lazily create the LLM
def get_chain():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(api_key=GROQ_API_KEY, model_name="gemma-7b-it")  # ✅ Fixed model name too

    prompt_template = ChatPromptTemplate.from_template("""
    Based on the following ingredients: {ingredients}, suggest a simple Indian-style recipe.
    Return the response in this format:

    Title: <recipe name>
    Ingredients:
    - list of ingredients
    Steps:
    1. step-by-step instructions
    """)

    output_parser = StrOutputParser()
    return prompt_template | llm | output_parser

# Main function to generate recipe
def generate_recipe(ingredients):
    chain = get_chain()  # 🔁 Chain initialized here, not at import time
    reply = chain.invoke({"ingredients": ingredients})
    lines = reply.strip().splitlines()

    title = lines[0].replace("Title: ", "")
    ingredients_list = []
    steps_list = []
    mode = "ingredients"

    for line in lines[1:]:
        if line.lower().startswith("steps"):
            mode = "steps"
            continue
        if mode == "ingredients" and line.strip():
            ingredients_list.append(line)
        elif mode == "steps" and line.strip():
            steps_list.append(line)

    return {
        "title": title,
        "ingredients": "\n".join(ingredients_list),
        "steps": "\n".join(steps_list)
    }
