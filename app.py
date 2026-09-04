import streamlit as st

from chatbot import generate_answer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Industrial PPE RAG Chatbot",
    page_icon="🦺",
    layout="centered"
)


# ============================================================
# TITLE
# ============================================================

st.title("Industrial PPE RAG Chatbot")

st.write(
    "Ask questions about industrial PPE and workplace safety."
)


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# QUESTION VALIDATION
# ============================================================

def is_general_greeting(question):
    greetings = {
        "hi",
        "hello",
        "hey",
        "hiya",
        "good morning",
        "good afternoon",
        "good evening",
        "how are you",
        "how are you doing"
    }

    return question.strip().lower() in greetings


def is_safety_question(question):
    safety_keywords = [
        "ppe",
        "personal protective equipment",
        "helmet",
        "hard hat",
        "safety helmet",
        "safety glasses",
        "goggles",
        "face shield",
        "ear protection",
        "earplug",
        "ear plugs",
        "earmuff",
        "respirator",
        "respiratory protection",
        "mask",
        "gloves",
        "protective gloves",
        "safety shoes",
        "safety boots",
        "protective clothing",
        "coveralls",
        "vest",
        "harness",
        "fall protection",
        "workplace safety",
        "industrial safety",
        "occupational safety",
        "workplace hazard",
        "hazard",
        "chemical safety",
        "fire safety",
        "electrical safety",
        "construction safety",
        "protective equipment",
        "safety equipment",
        "accident prevention",
        "risk assessment",
        "workplace protection"
    ]

    question = question.lower()

    return any(keyword in question for keyword in safety_keywords)


def validate_question(question):

    if is_general_greeting(question):
        return "greeting"

    if is_safety_question(question):
        return "safety"

    return "invalid"


# ============================================================
# USER INPUT
# ============================================================

question = st.chat_input(
    "Ask about industrial PPE or workplace safety..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    question_type = validate_question(question)


    # --------------------------------------------------------
    # GENERAL GREETING
    # --------------------------------------------------------

    if question_type == "greeting":

        answer = (
            "Hello. I can help you with industrial PPE "
            "and workplace safety questions."
        )

        with st.chat_message("assistant"):
            st.markdown(answer)


    # --------------------------------------------------------
    # SAFETY QUESTION
    # --------------------------------------------------------

    elif question_type == "safety":

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer, sources = generate_answer(question)

            st.markdown(answer)


    # --------------------------------------------------------
    # UNRELATED QUESTION
    # --------------------------------------------------------

    else:

        answer = (
            "I can only answer questions related to industrial PPE "
            "and workplace safety. Please ask a question within "
            "those topics."
        )

        with st.chat_message("assistant"):
            st.markdown(answer)


    # ========================================================
    # SAVE ASSISTANT RESPONSE
    # ========================================================

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
