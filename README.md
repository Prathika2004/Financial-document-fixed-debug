# 🚀 Financial Document Analyzer - Fixed & Professionalized

## 📌 Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents. This project was a debug mission to fix deterministic code bugs and inefficient (malicious) prompts to create a professional-grade financial tool.

---

## 🛠️ Bugs Squashed (Debug Report)

### 1. Deterministic (Code) Bugs
*   **PDF Tool Failure**: The original `tools.py` used an undefined `Pdf` class. I replaced it with `PyPDF2` to handle actual text extraction from PDF streams.
*   **Attribute Errors**: Changed `tool=[...]` to `tools=[...]` in the Agent definitions to comply with CrewAI syntax.
*   **Model Decommissioning**: The original model `llama3-8b` was retired by Groq. I updated the system to use the stable `llama-3.1-8b-instant` model.
*   **Provider Identification**: Added the `groq/` prefix to the model name so the LiteLLM library correctly routes requests to Groq.
*   **Parsing Crashes**: Added `handle_parsing_errors=True` to agents to prevent the "❌ LLM Failed" error when Llama 3 outputs non-standard formatting.

### 2. Inefficient & Malicious Prompts
*   **Professionalization**: Removed sabotage instructions that encouraged agents to "make up facts" or "ignore regulatory compliance." Agents are now CFA-standard professionals.
*   **Hallucination Prevention**: Removed tasks requiring "fake URLs" and "contradictory advice."
*   **Dynamic Logic**: Replaced hardcoded queries with a dynamic input system where the agents use the PDF data to answer specific user questions provided via the API.

---

## ⚙️ Setup & Installation

1.  **Clone the Repository**
2.  **Install Required Libraries**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment Variables**
    Create a `.env` file in the project root:
    ```env
    GROQ_API_KEY=your_gsk_api_key_here
    ```

---

## 🚀 How to Run

To start the FastAPI server, run the following command from the project root:

```bash
python -m app.main
 ```

## 📡 API Documentation

### **POST** `/analyze`

**Description:**  
Processes a financial PDF document and returns a professional 3-stage analysis: Extraction, Risk Assessment, and Investment Rating.

**Payload:** `multipart/form-data`

| Field | Type | Description |
| :--- | :--- | :--- |
| `file` | `File (PDF)` | The financial report (e.g., Tesla Q2 Update). |
| `query` | `string` | (Optional) Specific question (e.g., "What is the Gross Margin?"). |

**Example Response:**

```json
{
  "status": "success",
  "analysis": "The analyst found revenue of $25.5B... Risks include an 89% drop in free cash flow... Rating: Hold."
}
```
---

## 🗄️ Database Integration

The system includes a persistent data layer for auditability:

*   **Engine:** SQLAlchemy ORM
*   **Database:** SQLite (`financial_analysis.db`)
*   **Functionality:** Every analysis result, including the unique file ID, the user's query, and the AI's final report, is automatically saved to the database for future reference and history tracking.
