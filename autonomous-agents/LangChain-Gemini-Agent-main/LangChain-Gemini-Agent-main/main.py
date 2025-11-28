from dotenv import load_dotenv
from pydantic import BaseModel
# --- CHANGE HERE ---
from langchain_google_genai import ChatGoogleGenerativeAI
# --- END CHANGE ---
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()
from dotenv import load_dotenv
# ... other imports ...

load_dotenv()

import os
print(f"DEBUG: GOOGLE_API_KEY loaded: {os.getenv('GOOGLE_API_KEY') is not None}")
if os.getenv('GOOGLE_API_KEY'):
    print(f"DEBUG: First 5 chars of GOOGLE_API_KEY: {os.getenv('GOOGLE_API_KEY')[:5]}*****")
# ... rest of your code ...

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# --- CHANGE HERE ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0) # Added temperature for more factual output
# --- END CHANGE ---
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    # LangChain's agent output is often nested, so we need to access it correctly
    # The 'output' key typically holds the final result of the agent's work.
    # If the parser is expecting a string, ensure that what you pass is indeed a string.
    # The direct output from invoke is a dictionary. We want the 'output' key, which
    # should be the string that the LLM generated conforming to your Pydantic model.
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e)
    print("Raw Response:", raw_response) # Print the whole raw_response for debugging
    print("Type of raw_response.get('output'):", type(raw_response.get('output')))
    print("Content of raw_response.get('output'):", raw_response.get('output'))