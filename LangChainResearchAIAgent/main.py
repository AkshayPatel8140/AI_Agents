from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables from a .env file (for API keys, etc.)
load_dotenv()

# Define the expected structure of the research response using Pydantic
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize the Anthropic language model (Claude 3.5 Sonnet)
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Set up a parser to enforce the output format using the ResearchResponse schema
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Create a chat prompt template for the agent, including system instructions and placeholders
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

# List of tools available to the agent (web search, Wikipedia, save to file)
tools = [search_tool, wiki_tool, save_tool]

# Create the agent with tool-calling capabilities
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

# Set up the agent executor to handle queries and tool usage
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Prompt the user for a research query
query = input("What can i help you research? ")

# Invoke the agent with the user's query and get the raw response
raw_response = agent_executor.invoke({"query": query})

try:
    # Attempt to parse the agent's output into the structured ResearchResponse format
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    # Handle parsing errors and print the raw response for debugging
    print("Error parsing response", e, "Raw Response - ", raw_response)
