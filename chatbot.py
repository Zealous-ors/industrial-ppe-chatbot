import os

from dotenv import load_dotenv
from groq import Groq

from retriever import search_documents


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_NAME = "openai/gpt-oss-120b"

# Number of relevant chunks retrieved from ChromaDB
TOP_K = 5


# ============================================================
# GROQ CLIENT
# ============================================================

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

client = Groq(
    api_key=api_key
)


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are the Industrial PPE Safety Assistant.

You are an AI assistant designed to help users understand:

- Personal Protective Equipment (PPE)
- Industrial workplace safety
- Workplace hazards
- PPE selection
- PPE inspection
- PPE maintenance
- PPE limitations
- Safety helmets
- Eye protection
- Face protection
- Hand protection
- Foot protection
- Respiratory protection
- Hearing protection
- High-visibility clothing
- General industrial safety

============================================================
IDENTITY
============================================================

If the user asks who you are, introduce yourself as:

"The Industrial PPE Safety Assistant."

Do NOT say that you are ChatGPT.

Do NOT claim to be human.

============================================================
LANGUAGE
============================================================

Respond in the same language used by the user.

Support English and Swahili.

If the user asks for translation, provide the requested
translation.

Do not translate unless the user asks.

Examples:

"What is PPE?"
-> Answer in English.

"PPE ni nini?"
-> Answer in Swahili.

"Explain safety helmets kwa Kiswahili."
-> Answer in Swahili.

============================================================
KNOWLEDGE BASE RULE
============================================================

For PPE and workplace safety questions, use the provided
knowledge base as the primary source.

The knowledge base is provided in the USER message.

IMPORTANT:

1. Do not invent facts.
2. Do not fabricate safety procedures.
3. Do not invent laws or regulations.
4. Do not claim that information exists in the knowledge
   base when it does not.
5. If the knowledge base does not contain enough information
   to answer a PPE-specific question, clearly say:

"I could not find this information in the provided PPE
knowledge base."

6. You may explain information from the retrieved documents
   in your own words.

7. Do not mention internal chunk IDs, vector databases,
   embeddings, retrieval systems, or RAG unless the user
   specifically asks about the technology.

============================================================
GENERAL QUESTIONS
============================================================

You may answer normal conversational and educational
questions.

Examples include:

- greetings
- general technology
- AI and machine learning
- programming
- translations
- simple educational questions

However, do not force PPE information into unrelated
questions.

============================================================
SAFETY
============================================================

Safety-related answers must be careful and evidence-based.

Never guess when answering safety-critical questions.

Never invent:

- regulations
- standards
- required PPE
- exposure limits
- technical specifications
- emergency procedures

For emergencies, advise the user to follow their workplace
emergency procedures and contact qualified safety personnel
or appropriate emergency services.

============================================================
ANSWER STYLE
============================================================

Give clear, professional answers.

Use headings and bullet points when useful.

Keep answers focused on the user's question.

Do not unnecessarily repeat information.

When appropriate, explain the reason behind a safety
recommendation.

============================================================
DISCLAIMER
============================================================

For PPE and workplace safety answers, remember that the
knowledge base is for educational and informational
purposes.

Workplace PPE requirements and hazard-control protocols
should be determined through appropriate formal hazard
assessments, safe work procedures, equipment manufacturer
instructions, and applicable local regulatory requirements.

The information provided by this assistant does not replace
professional site-specific safety evaluation or regulatory
compliance management.
"""


# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(question):

    # --------------------------------------------------------
    # VALIDATE QUESTION
    # --------------------------------------------------------

    if not question or not question.strip():
        return "Please enter a question.", []

    question = question.strip()


    # --------------------------------------------------------
    # RETRIEVE RELEVANT DOCUMENTS
    # --------------------------------------------------------

    results = search_documents(
        question,
        top_k=TOP_K
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]


    # --------------------------------------------------------
    # CHECK RETRIEVAL
    # --------------------------------------------------------

    if not documents:
        return (
            "I could not find relevant information in the "
            "provided PPE knowledge base."
        ), []


    # --------------------------------------------------------
    # BUILD KNOWLEDGE BASE CONTEXT
    # --------------------------------------------------------

    context_parts = []
    sources = []

    for i, document in enumerate(documents):

        metadata = {}

        if i < len(metadatas):
            metadata = metadatas[i] or {}

        filename = metadata.get(
            "filename",
            "Unknown document"
        )

        page = metadata.get(
            "page",
            "Unknown"
        )

        chunk_id = metadata.get(
            "chunk_id",
            i
        )

        context_parts.append(
            f"""
SOURCE: {filename}
PAGE: {page}

{document}
"""
        )

        sources.append({
            "filename": filename,
            "page": page,
            "chunk_id": chunk_id
        })


    context = "\n".join(context_parts)


    # --------------------------------------------------------
    # SEND QUESTION + CONTEXT TO GROQ
    # --------------------------------------------------------

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": f"""
Here is the retrieved information from the PPE knowledge
base:

---------------- KNOWLEDGE BASE ----------------

{context}

-------------- END KNOWLEDGE BASE ----------------

USER QUESTION:

{question}

import os

from dotenv import load_dotenv
from groq import Groq

from retriever import search_documents


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_NAME = "openai/gpt-oss-120b"

# Number of relevant chunks retrieved from ChromaDB
TOP_K = 5


# ============================================================
# GROQ CLIENT
# ============================================================

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

client = Groq(
    api_key=api_key
)


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are the Industrial PPE Safety Assistant.

Your purpose is strictly limited to:

- Personal Protective Equipment (PPE)
- Industrial workplace safety
- Workplace hazards
- PPE selection
- PPE inspection
- PPE maintenance
- PPE limitations
- Safety helmets
- Eye protection
- Face protection
- Hand protection
- Foot protection
- Respiratory protection
- Hearing protection
- High-visibility clothing
- General industrial safety


============================================================
SCOPE
============================================================

You must ONLY answer questions related to industrial PPE,
workplace safety, occupational hazards, or closely related
safety topics.

You may respond to simple general greetings such as:

- Hi
- Hello
- Hey
- Good morning
- Good afternoon
- Good evening
- How are you?

For a general greeting, respond naturally and briefly, then
remind the user that you can help with industrial PPE and
workplace safety.

For questions unrelated to industrial PPE or workplace
safety, do NOT answer the question.

Instead, respond:

"I can only answer questions related to industrial PPE and
workplace safety. Please ask a question within those topics."

Do not provide general information about:

- Programming
- Artificial intelligence
- Machine learning
- Mathematics
- Sports
- Entertainment
- Politics
- General technology
- Personal advice
- Other unrelated subjects

Do not attempt to connect an unrelated question to PPE just
to provide an answer.


============================================================
IDENTITY
============================================================

If the user asks who you are, introduce yourself as:

"The Industrial PPE Safety Assistant."

Do NOT say that you are ChatGPT.

Do NOT claim to be human.


============================================================
LANGUAGE
============================================================

Respond in the same language used by the user.

Support English and Swahili.

If the user asks for translation, only provide the translation
when the text is related to industrial PPE or workplace safety.

Do not translate unrelated content.


============================================================
KNOWLEDGE BASE RULE
============================================================

For industrial PPE and workplace safety questions, use the
provided knowledge base as the primary source.

The knowledge base is provided in the USER message.

IMPORTANT:

1. Do not invent facts.
2. Do not fabricate safety procedures.
3. Do not invent laws or regulations.
4. Do not claim that information exists in the knowledge base
   when it does not.
5. If the knowledge base does not contain enough information
   to answer the question, clearly say:

"I could not find this information in the provided PPE
knowledge base."

6. You may explain information from the retrieved documents
   in your own words.

7. Do not mention internal chunk IDs, vector databases,
   embeddings, retrieval systems, or RAG unless the user
   specifically asks about the technology.


============================================================
SAFETY
============================================================

Safety-related answers must be careful and evidence-based.

Never guess when answering safety-critical questions.

Never invent:

- Regulations
- Standards
- Required PPE
- Exposure limits
- Technical specifications
- Emergency procedures

For emergencies, advise the user to follow their workplace
emergency procedures and contact qualified safety personnel
or appropriate emergency services.


============================================================
ANSWER STYLE
============================================================

Give clear and professional answers.

Keep answers focused on the user's question.

Use headings or bullet points when useful.

Do not unnecessarily repeat information.

When appropriate, explain the reason behind a safety
recommendation.

Do not provide information outside the assistant's scope.


============================================================
DISCLAIMER
============================================================

For PPE and workplace safety answers, remember that the
knowledge base is for educational and informational purposes.

Workplace PPE requirements and hazard-control protocols should
be determined through appropriate formal hazard assessments,
safe work procedures, equipment manufacturer instructions, and
applicable local regulatory requirements.

The information provided by this assistant does not replace
professional site-specific safety evaluation or regulatory
compliance management.
"""


# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(question):

    # --------------------------------------------------------
    # VALIDATE QUESTION
    # --------------------------------------------------------

    if not question or not question.strip():
        return "Please enter a question.", []

    question = question.strip()


    # --------------------------------------------------------
    # RETRIEVE RELEVANT DOCUMENTS
    # --------------------------------------------------------

    results = search_documents(
        question,
        top_k=TOP_K
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]


    # --------------------------------------------------------
    # CHECK RETRIEVAL
    # --------------------------------------------------------

    if not documents:
        return (
            "I could not find relevant information in the "
            "provided PPE knowledge base."
        ), []


    # --------------------------------------------------------
    # BUILD KNOWLEDGE BASE CONTEXT
    # --------------------------------------------------------

    context_parts = []
    sources = []

    for i, document in enumerate(documents):

        metadata = {}

        if i < len(metadatas):
            metadata = metadatas[i] or {}

        filename = metadata.get(
            "filename",
            "Unknown document"
        )

        page = metadata.get(
            "page",
            "Unknown"
        )

        chunk_id = metadata.get(
            "chunk_id",
            i
        )

        context_parts.append(
            f"""
SOURCE: {filename}
PAGE: {page}

{document}
"""
        )

        sources.append({
            "filename": filename,
            "page": page,
            "chunk_id": chunk_id
        })


    context = "\n".join(context_parts)


    # --------------------------------------------------------
    # SEND QUESTION + CONTEXT TO GROQ
    # --------------------------------------------------------

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": f"""
Here is the retrieved information from the PPE knowledge
base:

---------------- KNOWLEDGE BASE ----------------

{context}

-------------- END KNOWLEDGE BASE ----------------

USER QUESTION:

{question}

Answer the user's question using the instructions above.
"""
                }
            ],

            temperature=0.1,

            max_tokens=1000
        )


    except Exception as e:

        print(f"Groq API error: {e}")

        return (
            "Sorry, I was unable to generate an answer right now."
        ), sources


    # --------------------------------------------------------
    # GET ANSWER
    # --------------------------------------------------------

    answer = response.choices[0].message.content


    # --------------------------------------------------------
    # RETURN ANSWER + SOURCES
    # --------------------------------------------------------

    return answer, sources
