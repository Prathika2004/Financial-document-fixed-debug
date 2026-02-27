import os
import uuid
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

from crewai import Crew, Process
from agents import financial_analyst, risk_assessor, investment_advisor
from task import analyze_financial_document, risk_assessment, investment_recommendation

# --- DATABASE SETUP ---
DATABASE_URL = "sqlite:///./financial_debug.db"
Base = declarative_base()

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    id = Column(String, primary_key=True)
    filename = Column(String)
    query = Column(String)
    result = Column(Text)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

# --- APP SETUP ---
app = FastAPI(title="Professional Financial Document Analyzer")

def run_financial_crew(query: str, file_path: str):
    """Orchestrates the dynamic analysis crew"""
    finance_crew = Crew(
        agents=[financial_analyst, risk_assessor, investment_advisor],
        tasks=[analyze_financial_document, risk_assessment, investment_recommendation],
        process=Process.sequential,
        verbose=True
    )
    # Dynamics inputs: The query is passed from the API directly into the tasks
    result = finance_crew.kickoff(inputs={'query': query, 'file_path': file_path})
    return str(result)

@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Provide a comprehensive financial summary")
):
    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file_id}_{file.filename}"
    
    try:
        # 1. Save File
        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)
        
        # 2. Run Dynamic Crew
        analysis_output = run_financial_crew(query=query, file_path=file_path)
        
        # 3. Store in Database
        db = SessionLocal()
        record = AnalysisResult(id=file_id, filename=file.filename, query=query, result=analysis_output)
        db.add(record)
        db.commit()
        db.close()
        
        return {
            "status": "success",
            "id": file_id,
            "user_query": query,
            "analysis": analysis_output
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)