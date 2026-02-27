🚀 Financial Document Analyzer - Fixed & Professionalized
📌 Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents. This project was a debug mission to fix deterministic code bugs and inefficient (malicious) prompts to create a professional-grade financial tool.

🛠️ Bugs Squashed (Debug Report)
1. Deterministic (Code) Bugs
PDF Tool Failure: The original tools.py used an undefined Pdf class. I replaced it with PyPDF2 to handle actual text extraction from PDF streams.
Attribute Errors: Changed tool=[...] to tools=[...] in the Agent definitions to comply with CrewAI syntax.
Model Decommissioning: The original model llama3-8b was retired by Groq. I updated the system to use the stable llama-3.1-8b-instant model.
Provider Identification: Added the groq/ prefix to the model name so the LiteLLM library correctly routes requests to Groq.
Parsing Crashes: Added handle_parsing_errors=True to agents to prevent the "❌ LLM Failed" error when Llama 3 outputs non-standard formatting.
2. Inefficient & Malicious Prompts
Professionalization: Removed sabotage instructions that encouraged agents to "make up facts" or "ignore regulatory compliance." Agents are now CFA-standard professionals.
Hallucination Prevention: Removed tasks requiring "fake URLs" and "contradictory advice."
Dynamic Logic: Replaced hardcoded queries with a dynamic input system where the agents use the PDF data to answer specific user questions provided via the API.
⚙️ Setup & Installation
Clone the Repository
git clone https://github.com/Prathika2004/Financial-document-fixed-debug.gitcd Financial-document-fixed-debug
Install Required Libraries
pip install -r requirements.txt
Configure Environment VariablesCreate a .env file in the project root:
GROQ_API_KEY=your_gsk_api_key_here
🚀 How to Run
To start the FastAPI server, run the following command from the project root:

python -m app.main
📡 API Documentation
POST /analyze
Description:
Processes a financial PDF document and returns a professional 3-stage analysis:

Extraction (Financial metrics)
Risk Assessment (Credit/Market risks)
Investment Rating (Buy/Hold/Sell)
Payload: multipart/form-data

Field
Type
Description
file	File (PDF)	The financial report (e.g., Tesla Q2 Update)
query	string	(Optional) Specific question (e.g., "What is the Gross Margin?")

Example Response:

json

{
  "status": "success",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "user_query": "What is the Gross Margin?",
  "analysis": "The analyst found revenue of $25.5B... Risks include an 89% drop in free cash flow... Rating: Hold."
}
🗄️ Database Integration
Technical Specifications
The system includes a persistent data layer for auditability and historical tracking.

Component
Technology
Engine	SQLAlchemy ORM
Database	SQLite (financial_debug.db)

Functionality
Every analysis operation is automatically recorded, providing a complete audit trail:

Automatic Storage: Each analysis result, including the unique file ID, the user's query, and the AI's final report, is saved to the database.
Historical Tracking: Enables retrieval and review of past analyses for reference and comparison.
Auditability: Provides a reliable log of all processed documents and their outcomes.
