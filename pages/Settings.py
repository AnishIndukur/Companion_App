import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Settings - Companion App",
    page_icon="⚙️",
    layout="wide"
)

system_prompt = ''

# Initialize settings in session state if they don't exist
if "settings" not in st.session_state:
    st.session_state.settings = {
        "model": "o3-mini",
        "temperature": 0.7,
        "max_tokens": 1000,
        "stream": True,
        "system_prompt": system_prompt # Add default system prompt
    }

# Main settings page header
st.title("⚙️ Chat Settings")

# Create three columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Model Settings")
    
    # Model selection
    model = st.selectbox(
        "Choose GPT Model",
        ["gpt-4o-mini", "gpt-4o", "o3-mini", "o1"],
        index=0 if st.session_state.settings["model"] == "gpt-4o-mini" else 1,
        help="Select which OpenAI model to use for chat responses."
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=st.session_state.settings["temperature"],
        step=0.1,
        help="Higher values make the output more random, lower values make it more focused and deterministic."
    )
    
    # Max tokens slider
    max_tokens = st.slider(
        "Max Tokens",
        min_value=100,
        max_value=4000,
        value=st.session_state.settings["max_tokens"],
        step=100,
        help="Maximum number of tokens to generate in the response."
    )

with col2:
    st.header("Response Settings")
    
    # Stream toggle
    stream = st.toggle(
        "Enable Streaming",
        value=st.session_state.settings["stream"],
        help="Enable or disable streaming responses. Streaming shows the response as it's being generated."
    )
    
    # Add system prompt input
    st.header("System Prompt")
    system_prompt = st.text_area(
        "Set System Prompt",
        value=st.session_state.settings.get("system_prompt", system_prompt),
        height=150,
        help="Define the AI assistant's behavior and personality."
    )

# Save settings button
if st.button("💾 Save Settings", type="primary"):
    st.session_state.settings.update({
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream,
        "system_prompt": system_prompt  # Add system prompt to saved settings
    })
    st.success("Settings saved successfully!")

# Settings explanation
with st.expander("ℹ️ About these settings"):
    st.markdown("""
    ### Model Settings
    
    - **GPT Model**: Choose between different OpenAI models:
        - GPT-4o-mini: Faster and more cost-effective
        - GPT-4o: More capable but slower and more expensive
        - GPT-o3-mini: Lightweight thinking model
        - GPT-o1: Large scale thinking model
    
    - **Temperature**: Controls randomness in responses:
        - 0.0: Focused and deterministic
        - 1.0: Balanced creativity
        - 2.0: Maximum creativity
    
    - **Max Tokens**: Limits response length:
        - Lower values: Shorter, more concise responses
        - Higher values: Longer, more detailed responses
    
    ### Response Settings
    
    - **Streaming**: When enabled, shows responses as they're generated
        - Provides a more interactive experience
        - Disable for faster bulk processing
        
    ### System Prompt
    
    - Defines how the AI assistant should behave
    - Can be used to specify personality, tone, and expertise
    - Changes apply to new conversations
    """)

# Debug information (only shown when needed)
if st.checkbox("Show Debug Information", value=False):
    st.json(st.session_state.settings)