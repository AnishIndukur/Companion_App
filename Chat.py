import streamlit as st
from openai import OpenAI
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Companion App",
    page_icon="💬",
    layout="wide"
)

# Initialize OpenAI client with API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Initialize settings in session state if they don't exist
if "settings" not in st.session_state:
    st.session_state.settings = {
        "model": "o3-mini",
        "temperature": 0.7,
        "stream": True,
        "system_prompt": "You are a helpful, AI assistant."
    }

# Main app header
st.title("💭 Chat with AI")

# Sidebar
with st.sidebar:
    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. Type your message in the chat input box and press Enter
        2. The AI will respond in real-time with streaming text
        3. Use the sidebar buttons to clear or save the conversation
        4. Adjust settings in the Settings page
        
        **Note:** Your conversation history is preserved between pages.
        """)
    st.header("Chat Controls")
    
    # Clear conversation button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.session_state.conversation_history = []
        st.rerun()

    # Save conversation button
    if st.button("💾 Save Conversation"):
        # Save conversation button
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.txt"
        
        # Prepare the conversation content
        conversation_content = ""
        for message in st.session_state.conversation_history:
            conversation_content += f"{message['role'].upper()}: {message['content']}\n\n"
        
        # Create download button
        st.download_button(
            label="⬇️ Download Conversation",
            data=conversation_content,
            file_name=filename,
            mime="text/plain"
        )
    
    # Display current settings
    st.divider()
    st.markdown("### Current Settings")
    st.markdown(f"**Model:** {st.session_state.settings['model']}")
    st.markdown(f"**Temperature:** {st.session_state.settings['temperature']}")
    
    # Link to settings page
    st.divider()
    st.markdown("ℹ️ You can adjust these settings in the [Settings Page](Settings)")

    # Footer with instructions
    

# Create a container for chat messages with custom height
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.conversation_history.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Create the API request with system prompt
            response = client.chat.completions.create(
                model=st.session_state.settings["model"],
                messages=[
                    {"role": "system", "content": st.session_state.settings["system_prompt"]}
                ] + [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=st.session_state.settings["stream"]
            )

            # Process the streaming response
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                message_placeholder.write(full_response + "▌")
            
            message_placeholder.write(full_response)
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            full_response = "I apologize, but I encountered an error. Please try again."
            message_placeholder.write(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.session_state.conversation_history.append({"role": "assistant", "content": full_response})

