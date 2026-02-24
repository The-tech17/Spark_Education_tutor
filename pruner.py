import os
from pypdf import PdfReader

def extract_chapters(pdf_path):
    """Simple logic to split a textbook into manageable chunks."""
    reader = PdfReader(pdf_path)
    # Logic to group pages into chapters or topics goes here
    return [page.extract_text() for page in reader.pages]

def context_pruning(query, chunks):
    """
    REQUIRED TECHNIQUE:
    This function should compare the query to the chunks 
    and only return the most relevant 2-3 pages.
    """
    # For now, this is a placeholder for your team to implement 
    # semantic search or keyword filtering.
    relevant_context = [chunk for chunk in chunks if any(word in chunk.lower() for word in query.lower().split())]
    return relevant_context[:3] # Limit to top 3 to save tokens/cost
