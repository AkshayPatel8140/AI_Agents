from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load the restaurant reviews dataset from a CSV file
df = pd.read_csv("realistic_restaurant_reviews.csv")
# Initialize the Ollama embeddings model
embeddings = OllamaEmbeddings(model="llama3.2")

# Set the location for the Chroma vector database
db_location = "./Chroma_langchain_db"
# Check if the database already exists; if not, we need to add documents
add_Documents = not os.path.exists(db_location)

if add_Documents:
    documents = []
    ids = []
    # Iterate over each row in the DataFrame to create Document objects
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + "\n" + row["Review"],           # Combine title and review
            metadata={"rating": row["Rating"], "Date": row["Date"]},    # Add metadata
            id=str(i),                                                  # Unique ID for each document
        )
        ids.append(str(i))
        documents.append(document)

# Initialize the Chroma vector store with the specified collection and embeddings
vector_store = Chroma(
    collection_name="restaurant_reviews",
    embedding_function=embeddings,
    persist_directory=db_location,
)

# If documents are new, add them to the vector store
if add_Documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Create a retriever to fetch the top 5 most relevant documents for a query
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
