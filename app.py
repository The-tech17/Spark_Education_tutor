import streamlit as st
from pruner import extract_chapters, context_pruning
from llm_service import get_tutor_answer

st.set_page_config(page_title="Spark Ed-Tutor", page_icon="📚")
st.title("Education Tutor for Remote India")

uploaded_file = st.file_uploader("Upload State-Board Textbook (PDF)", type="pdf")

# Initialize chapters so it exists even if no file is uploaded yet
chapters = None

if uploaded_file:
    with st.spinner("Analyzing textbook..."):
        # We use st.cache_data here so it doesn't re-process the PDF on every click
        chapters = extract_chapters(uploaded_file)
        st.success("Textbook ingested!")

    # Everything related to the question must stay INSIDE the 'if uploaded_file' block
    # because you can't ask a question if there is no textbook!
    query = st.text_input("Ask a question from the curriculum:")
    
    if query:
        with st.spinner("Pruning context and thinking..."):
            pruned_context = context_pruning(query, chapters)
            context_str = "\n".join(pruned_context)
            answer = get_tutor_answer(query, context_str)
        
        # These display commands are now correctly aligned inside 'if query'
        st.write("### Tutor's Answer:")
        st.success(answer)
        st.info(pruned_context[0] if pruned_context else "No relevant context found.")
