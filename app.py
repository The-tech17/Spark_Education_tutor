import streamlit as st
from pruner import extract_chapters, context_pruning

st.set_page_config(page_title="Spark Ed-Tutor", page_icon="📚")
st.title("Education Tutor for Remote India")

uploaded_file = st.file_uploader("Upload State-Board Textbook (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Analyzing textbook..."):
        # In a real app, you'd cache this so it doesn't re-run every time
        chapters = extract_chapters(uploaded_file)
        st.success("Textbook ingested!")

    query = st.text_input("Ask a question from the curriculum:")
    
    if query:
        # Step 1: Prune the context locally (Zero API Cost)
        pruned_context = context_pruning(query, chapters)
        
        # Step 2: Only send the tiny 'pruned' snippet to Gemini
        st.write("### Pruned Context for LLM:")
        st.info(pruned_context[0] if pruned_context else "No relevant context found.")
