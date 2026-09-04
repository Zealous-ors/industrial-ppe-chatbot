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
