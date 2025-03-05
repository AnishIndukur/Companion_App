# Companion App

![Companion App](https://img.shields.io/badge/Companion-App-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0+-red)
![OpenAI](https://img.shields.io/badge/OpenAI-1.12.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📝 Description

Companion App is an interactive AI chat application built with Streamlit and powered by OpenAI's GPT models. It provides a user-friendly interface for conversing with an AI assistant that can be customized to serve various purposes, from general assistance to therapeutic support.

The application features a multi-page interface with a main chat page and a settings page, allowing users to customize their experience according to their preferences.

## ✨ Features

- **Interactive Chat Interface**: Real-time conversation with AI using Streamlit's chat components
- **Streaming Responses**: See AI responses as they're being generated
- **Customizable AI Settings**:
  - Choose between different OpenAI models (GPT-4o-mini, GPT-4o)
  - Adjust temperature for response creativity
  - Set maximum token length for responses
  - Customize system prompt to define AI behavior
- **Conversation Management**:
  - Save and download conversation history
  - Clear conversations when needed
- **Responsive Design**: Works on desktop and mobile devices
- **Default Therapeutic Assistant**: Comes with a pre-configured therapeutic assistant prompt

## 🛠️ Technology Stack

- **Frontend & Backend**: [Streamlit](https://streamlit.io/) (v1.31.0+)
- **AI Integration**: [OpenAI API](https://openai.com/blog/openai-api) (v1.12.0+)
- **Environment Variables**: python-dotenv (v1.0.0+)

## 📋 Prerequisites

Before running the application, you need:

1. Python 3.7 or higher
2. An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
3. Required Python packages (see Installation section)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnishIndukur/Companion_App.git
   cd Companion_App
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key** (REQUIRED):
   
   a. Create a `.streamlit` directory in the project root if it doesn't exist:
   ```bash
   mkdir -p .streamlit
   ```
   
   b. Create a `secrets.toml` file inside the `.streamlit` directory:
   ```bash
   touch .streamlit/secrets.toml
   ```
   
   c. Add your OpenAI API key to the secrets.toml file:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   ```
   
   d. Replace `"your-openai-api-key"` with your actual OpenAI API key from [OpenAI's platform](https://platform.openai.com/api-keys).

   > **IMPORTANT**: The application will not work without this step. The `.streamlit/secrets.toml` file with a valid OpenAI API key is required to run the application.

## 🖥️ Usage

1. **Start the application**:
   ```bash
   streamlit run Chat.py
   ```

2. **Access the application**:
   Open your web browser and go to `http://localhost:8501`

3. **Using the Chat Interface**:
   - Type your message in the input box at the bottom of the screen
   - The AI will respond in real-time with streaming text
   - Use the sidebar buttons to clear or save the conversation

4. **Customizing Settings**:
   - Navigate to the Settings page using the sidebar
   - Adjust model, temperature, max tokens, and streaming options
   - Customize the system prompt to change the AI's behavior
   - Click "Save Settings" to apply changes

## 📊 Application Structure

```
Companion_App/
├── .streamlit/
│   └── secrets.toml       # Contains API keys and secrets
├── pages/
│   └── Settings.py        # Settings page for customizing the AI
├── Chat.py                # Main application file with chat interface
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🧠 Methodology

### AI Conversation Flow

1. **User Input Processing**:
   - User messages are captured through Streamlit's chat input component
   - Messages are added to the session state to maintain conversation history

2. **OpenAI API Integration**:
   - The application uses OpenAI's Chat Completions API
   - A system prompt defines the AI's behavior and personality
   - User messages and previous conversation history are sent as context

3. **Response Handling**:
   - Responses are streamed in real-time when streaming is enabled
   - Full responses are stored in the conversation history
   - Error handling ensures graceful failure if API issues occur

### Session State Management

The application uses Streamlit's session state to maintain:
- Current conversation messages
- Complete conversation history (for downloading)
- User settings (model, temperature, max tokens, etc.)

This ensures persistence between page navigations and browser refreshes.

### Therapeutic Assistant Implementation

The default system prompt configures the AI as a therapeutic assistant with:
- Empathetic and supportive communication style
- Structured therapeutic questioning techniques
- Focus on emotional well-being and coping strategies
- Professional boundaries (no medical diagnosis)

## 🔧 Advanced Configuration

### Customizing the System Prompt

The system prompt defines how the AI assistant behaves. You can customize it to create different types of assistants:

- **General Assistant**: For everyday tasks and questions
- **Therapeutic Assistant**: For emotional support and mental health (default)
- **Educational Tutor**: For learning and educational content
- **Creative Writing Partner**: For storytelling and creative projects

### Environment Variables

The application uses the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for authentication

These can be set in the `.streamlit/secrets.toml` file.

## 🔍 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Ensure your OpenAI API key is correctly set in `.streamlit/secrets.toml`
   - Verify your API key is active and has sufficient credits

2. **Dependency Issues**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check for version conflicts with existing packages

3. **Streamlit Connection Issues**:
   - Try running on a specific port: `streamlit run Chat.py --server.port 8502`
   - Check firewall settings if accessing remotely

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Streamlit Session State Guide](https://docs.streamlit.io/library/api-reference/session-state)
- [OpenAI Chat Completions Guide](https://platform.openai.com/docs/guides/chat)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [OpenAI](https://openai.com/) for providing the AI models
- All contributors and users of this application
