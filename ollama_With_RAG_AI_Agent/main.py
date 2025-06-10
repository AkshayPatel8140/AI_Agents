from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Initialize the Ollama LLM with the specified model
model = OllamaLLM(model="llama3.2")

# Define the prompt template for the agent, including placeholders for reviews and the user's question
template = """
You are an expert in answering questions about a pizza restaurant

# Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

# Create a chat prompt using the template
prompt = ChatPromptTemplate.from_template(template)
# Create a chain that combines the prompt and the model
chain = prompt | model

# Start an interactive loop to accept user questions
while True:
    print("\n\n------------------------------------------------")
    que = input("Ask your question (q to quite): ")
    print("\n")
    # Exit the loop if the user types 'q'
    if que == "q":
        break

    # Retrieve relevant reviews for the user's question using the retriever
    reviews = retriever.invoke(que)
    # Generate a response from the model using the reviews and the question
    response = chain.invoke({"reviews": reviews, "question": que})
    # Print the model's response
    print(response)
