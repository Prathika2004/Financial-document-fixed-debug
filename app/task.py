from crewai import Task
from agents import financial_analyst, risk_assessor, investment_advisor

# Task 1: Extraction based on user query
analyze_financial_document = Task(
    description=(
        "1. Use the tool to read the file at {file_path}.\n"
        "2. Analyze the document to answer the user's specific query: {query}.\n"
        "3. Focus on primary financial metrics like Revenue, Net Income, and Cash Flow."
    ),
    expected_output="A professional financial summary addressing the specific user query with factual data.",
    agent=financial_analyst
)

# Task 2: Risk Evaluation
risk_assessment = Task(
    description="Based on the analysis of {file_path}, identify 3 critical financial risks.",
    expected_output="A professional risk assessment report in bullet points.",
    agent=risk_assessor
)

# Task 3: Strategic Recommendation
investment_recommendation = Task(
    description="Synthesize the analysis and risk assessment to provide a Buy/Hold/Sell outlook.",
    expected_output="A final investment memo with a rating and one-sentence justification.",
    agent=investment_advisor
)