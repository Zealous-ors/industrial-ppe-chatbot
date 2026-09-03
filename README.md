# Industrial PPE Safety Chatbot

An AI-powered chatbot designed to provide information about Personal Protective Equipment (PPE) and industrial safety using Retrieval-Augmented Generation (RAG).

## Features

- Answers industrial PPE and safety questions
- Uses a curated safety knowledge base
- Retrieves relevant information using vector search
- Uses an LLM to generate responses
- Simple Streamlit web interface

## Architecture

Safety Documents
       ↓
Document Loading
       ↓
Text Splitting
       ↓
Embeddings
       ↓
ChromaDB
       ↓
Retriever
       ↓
LLM
       ↓
Safety Chatbot


## Technologies
Python
Streamlit
ChromaDB
RAG
Embeddings
Groq LLM

## Purpose

The project demonstrates how Generative AI and Retrieval-Augmented Generation can be applied to industrial safety and PPE information retrieval.

## Disclaimer

This project is for educational purposes. It should not replace official workplace safety procedures, regulations, or professional safety advice.
