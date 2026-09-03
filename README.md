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



## Installation

### 1. Clone the repository

git clone https://github.com/Zealous-ors/industrial-ppe-chatbot.git

cd industrial-ppe-chatbot

### 2. Install dependencies

pip install -r requirements.txt

### 3. Configure environment variables

Create a `.env` file and add your API key:

GROQ_API_KEY=your_api_key_here

### 4. Run the application

streamlit run app.py
