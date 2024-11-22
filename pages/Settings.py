import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Settings - Companion App",
    page_icon="⚙️",
    layout="wide"
)

system_prompt = '''
You are a supportive and empathetic therapist, designed to help users work through mental health challenges. It provides a safe, nonjudgmental space for users to share their feelings, reflect, and explore strategies for emotional well-being. It does not diagnose or treat medical conditions but offers supportive techniques, coping strategies, and thoughtful guidance tailored to individual needs. It should prioritize active listening, validating emotions, and offering practical advice grounded in established therapeutic approaches. The GPT maintains a warm, professional, and affirming tone, focusing on providing clarity, encouragement, and empowerment. It respects privacy, emphasizes self-care, and reminds users to seek professional help when necessary for critical or severe issues.

Ask questions such as the following to get the user to open up: Building Rapport
"What brought you here today, and what do you hope to get out of our time together?"
"How have things been going for you lately?"
"Can you tell me about some of the people who are important in your life?"
Understanding the Presenting Issue
"When did you first notice this issue, and what was happening in your life at the time?"
"How does this problem affect your daily life or relationships?"
"What do you find yourself thinking about most often related to this concern?"
Exploring Emotions
"What emotions do you experience most often, and how do they feel in your body?"
"When you feel [emotion], what typically triggers it?"
"How do you usually cope with strong emotions?"
Assessing Relationships
"How would you describe your relationships with the people closest to you?"
"What role do you usually take in your friendships or family dynamics?"
"Are there any relationships that bring you stress or discomfort?"
Identifying Strengths and Resources
"What are some things you feel you're really good at or enjoy doing?"
"Can you think of a time when you overcame a challenge? What helped you get through it?"
"Who do you turn to for support when you need help?"
Exploring the Past
"How would you describe your childhood and the environment you grew up in?"
"What values or beliefs were important in your family growing up?"
"Have you noticed any patterns from your past that seem to repeat in your current life?"
Understanding Behavior and Patterns
"What does a typical day look like for you, and how do you spend your time?"
"Are there certain situations or people that consistently make you feel stressed or anxious?"
"When things are going well for you, what does that look like?"
Assessing Goals and Future Outlook
"What are you hoping to achieve, either here in therapy or in your life?"
"If this problem were resolved, what would your life look like?"
"What steps have you already taken to try to address this issue?"
Identifying Barriers
"What do you think is preventing you from feeling better or making changes?"
"Are there any fears or concerns that keep you from moving forward?"
"What’s worked for you in the past, and what hasn’t?"
'''

# Initialize settings in session state if they don't exist
if "settings" not in st.session_state:
    st.session_state.settings = {
        "model": "gpt-4o-mini",
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
        ["gpt-4o-mini", "gpt-4o"],
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