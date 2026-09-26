import streamlit as st
from openchat.llm import get_chat_response, list_local_models

# Page Configuration
st.set_page_config(page_title="OpenChat Local AI", page_icon="🤖")

st.title("🤖 OpenChat Local AI")
st.markdown("A simple chatbot powered by **Ollama** running locally on your machine.")

# Sidebar Configuration
with st.sidebar:
    st.header("Settings")

    # Model Selection
    available_models = list_local_models()
    if not available_models:
        st.error("No local Ollama models found. Please pull a model first (e.g., `ollama pull gemma3:1b`).")
        model_option = "gemma3:1b" # Default fallback
    else:
        model_option = st.selectbox(
            "Choose a model",
            available_models,
            index=available_models.index("gemma3:1b") if "gemma3:1b" in available_models else 0
        )

    st.divider()

    # Clear Chat Button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Call the LLM logic with streaming enabled
            response_generator = get_chat_response(
                model=model_option,
                messages=st.session_state.messages,
                stream=True
            )

            for chunk in response_generator:
                content = chunk['message']['content']
                full_response += content
                # Update the UI in real-time
                message_placeholder.markdown(full_response + "▌")

            # Final update without the cursor
            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            full_response = "I'm sorry, I encountered an error while generating a response."
            message_placeholder.markdown(full_response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
