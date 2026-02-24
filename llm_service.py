import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your API key from the .env file you just set up
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_tutor_answer(query, pruned_context):
    """
    Sends the user query and ONLY the pruned textbook context to Gemini.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # This system prompt ensures the AI stays in "Tutor Mode"
    prompt = f"""
    You are a helpful Education Tutor for students in rural India. 
    Use the following TEXTBOOK CONTEXT to answer the STUDENT QUESTION.
    If the answer isn't in the context, say you don't know based on the current chapter.
    Keep the language simple and encouraging.

    TEXTBOOK CONTEXT:
    {pruned_context}

    STUDENT QUESTION:
    {query}
    """
    
    response = model.generate_content(prompt)
    return response.text
