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

st.title("🦺 Industrial PPE RAG Chatbot")

st.write(
    "Ask questions about industrial PPE, workplace safety, "
    "or interact naturally with the assistant."
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
# USER INPUT
# ============================================================

question = st.chat_input(
    "Ask anything about industrial PPE..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # Display user message
    with st.chat_message("user"):

        st.markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, sources = generate_answer(question)

        st.markdown(answer)


    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
