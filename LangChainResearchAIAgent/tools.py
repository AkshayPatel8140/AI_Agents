from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# This module defines and configures tools for a research AI agent,
# including web search, Wikipedia queries, and saving results to a text file.

def save_to_txt(data: str, filename: str = "research_output.txt"):
    """
    Save the provided data to a text file with a timestamp.

    Args:
        data (str): The research data to save.
        filename (str, optional): The file to save the data to. Defaults to "research_output.txt".

    Returns:
        str: Confirmation message with the filename.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    # Open the file in append mode and write the formatted text
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

# Define a Tool instance for saving research data to a text file
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

# Create an instance of DuckDuckGoSearchRun for web searches
search = DuckDuckGoSearchRun()

# Define a Tool instance for searching the web using DuckDuckGo
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

# Create a WikipediaAPIWrapper instance for querying Wikipedia
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)

# Define a WikipediaQueryRun tool for retrieving information from Wikipedia
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
