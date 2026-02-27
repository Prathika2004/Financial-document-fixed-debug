import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_groq import ChatGroq
from tools import FinancialDocumentTool

load_dotenv()

# Using your preferred model with the groq/ prefix for stability
llm = ChatGroq(
    temperature=0,
    model_name="groq/llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Extract and analyze factual financial data to answer: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a CFA-certified analyst. You specialize in quantitative analysis "
        "and GAAP standards. You provide objective data without speculation."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=5,
    allow_delegation=False,
    handle_parsing_errors=True
)

risk_assessor = Agent(
    role="Risk Management Expert",
    goal="Identify potential market and credit risks from the provided financial data.",
    verbose=True,
    backstory=(
        "You are a former Chief Risk Officer. You excel at identifying liquidity "
        "issues and debt-related threats in corporate filings."
    ),
    llm=llm,
    max_iter=3,
    allow_delegation=False,
    handle_parsing_errors=True
)

investment_advisor = Agent(
    role="Chief Investment Officer",
    goal="Provide a strategic investment recommendation based on the analyst and risk reports.",
    verbose=True,
    backstory=(
        "You manage institutional portfolios. You translate complex data into "
        "clear, actionable Buy/Hold/Sell insights."
    ),
    llm=llm,
    max_iter=3,
    allow_delegation=False,
    handle_parsing_errors=True
)