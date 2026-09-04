Industrial PPE Safety Assistant

An AI-powered safety assistant that uses Retrieval-Augmented Generation (RAG) to answer industrial PPE and workplace safety questions using a curated safety knowledge base.

«Disclaimer: This project is for educational purposes and should not replace official workplace safety procedures, regulations, or professional safety advice.»

Problem

Industrial workers and safety personnel often need quick access to reliable information about Personal Protective Equipment (PPE) and workplace safety practices.

Generic AI assistants may provide answers that are not grounded in a specific safety knowledge base. This can lead to incomplete or unreliable guidance.

This project addresses the problem by providing an AI assistant focused specifically on industrial PPE and safety information.

Solution

The Industrial PPE Safety Assistant uses Retrieval-Augmented Generation (RAG) to combine document retrieval with AI-generated responses.

When a user asks a question, the system:

1. Processes the user's question.
2. Searches the safety knowledge base for relevant information.
3. Retrieves the most relevant content using semantic search.
4. Provides the retrieved context to the language model.
5. Generates a response grounded in the available safety information.

This approach helps reduce unsupported answers and keeps the assistant focused on the information contained in its safety knowledge base.

Tech Stack

Technology| Purpose
Python| Application development
Streamlit| Web interface
ChromaDB| Vector database
Sentence Transformers| Text embeddings
Groq| LLM inference
RAG| Grounded question answering


Architecture

The application follows a Retrieval-Augmented Generation (RAG) pipeline:

Safety Documents
       ↓
Document Loading
       ↓
Text Splitting
       ↓
Text Embeddings
       ↓
ChromaDB Vector Store
       ↓
Semantic Retrieval
       ↓
Relevant Context
       ↓
Language Model
       ↓
Generated Safety Response

The system first processes the available safety documents and converts their content into vector embeddings. These embeddings are stored in ChromaDB, allowing the application to retrieve relevant information when a user asks a question.

The retrieved information is then provided as context to the language model, which generates the final response.


Features

- AI-powered industrial PPE and safety question answering
- Retrieval-Augmented Generation (RAG)
- Semantic search over safety documents
- Vector storage and retrieval using ChromaDB
- Multilingual text embeddings
- Context-aware responses using an LLM
- Interactive Streamlit chat interface


  Demo

The Industrial PPE Safety Assistant provides an interactive chat interface where users can ask questions related to personal protective equipment and workplace safety.

Example questions include:

- What PPE should be worn when working with chemicals?
- Why is eye protection important?
- What type of PPE protects against respiratory hazards?
- When should protective gloves be used?

A visual demonstration of the application will be added here.
