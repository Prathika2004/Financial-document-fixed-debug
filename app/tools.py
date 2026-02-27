import os
import PyPDF2
from crewai.tools import tool

class FinancialDocumentTool:
    @tool("read_data_tool")
    def read_data_tool(file_path: str):
        """Reads and extracts text content from a PDF financial document at the provided file_path."""
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
        
        try:
            text = ""
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                # Read the first 5 pages to stay within token limits
                num_pages = min(len(reader.pages), 5)
                for i in range(num_pages):
                    page_content = reader.pages[i].extract_text()
                    if page_content:
                        text += page_content + "\n"
            
            if not text.strip():
                return "The document is empty or contains non-extractable content (images)."
            
            return text[:4000] # Return a concise chunk for the LLM
        except Exception as e:
            return f"Error reading PDF: {str(e)}"