🚀 Financial Document Analyzer - Fixed & Professionalized
🛠️ Bugs Identified & Fixed
Deterministic (Code) Bugs
PDF Tool Failure: The original tools.py used an undefined Pdf class. I implemented PyPDF2 to handle actual text extraction from PDF streams.
Attribute Typos: Changed tool=[...] to tools=[...] in Agent definitions (CrewAI syntax requirement).
Variable Mismatch: Unified the variable name file_path across the Tasks, Tools, and API logic to prevent "Missing Argument" errors during tool calling.
Parsing Crash: Added handle_parsing_errors=True to Agents. This prevents the Crew from crashing when Llama 3 outputs text outside the "Thought/Action" format.
Provider Identification: Added the groq/ prefix to the model name (groq/llama-3.1-8b-instant) so the LiteLLM library correctly routes requests to Groq.
Inefficient & Malicious Prompts
Sabotage Instructions: Removed instructions like "make up facts" and "sound confident even when wrong." Agents are now CFA-standard professionals.
Hallucination Prevention: Removed tasks requiring "fake URLs" and "contradictory advice."
Dynamic Logic: Replaced hardcoded queries with a dynamic system where the agent uses the PDF data to answer the specific user-provided string.
⚙️ Setup Instructions
Install dependencies: pip install -r requirements.txt
Configure Environment: Create a .env file in the root folder:
code
Env
GROQ_API_KEY=your_gsk_key_here
Run Application: python -m app.main
📡 API Documentation
POST /analyze
Description: Processes a financial PDF and returns a professional 3-stage analysis (Extraction, Risk, Investment Rating).
Payload: multipart/form-data
file: PDF document.
query: (Optional) String query (e.g., "What is the Gross Margin?").
Response:
code
JSON
{
  "status": "success",
  "analysis": "The analyst found revenue of $25B... Risks include... Rating: Buy"
}
🗄️ Database Integration
The system uses SQLAlchemy to persist every analysis result into a local SQLite database (financial_analysis.db) for future auditing and user history.
