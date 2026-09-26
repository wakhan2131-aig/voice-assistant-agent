# Voice AI Assistant with LiveKit

This project implements a real-time, low-latency voice AI assistant using the [LiveKit Agents](https://livekit.io/agents) framework. The assistant provides a seamless voice-to-voice experience by integrating state-of-the-art Speech-to-Text (STT), Large Language Models (LLM), and Text-to-Speech (TTS) technologies.

## 🚀 Features

- **Real-time Interaction:** Powered by LiveKit's RTC sessions for minimal latency.
- **Advanced Audio Processing:** Includes noise cancellation using `ai_coustics` (Quail VF S) to ensure clear audio input.
- **Multilingual Support:** Uses Deepgram Nova-3 for high-accuracy, multi-language speech recognition.
- **Intelligent Responses:** Driven by the `gemma-4-31b-it` model for helpful and concise conversations.
- **Natural Voice:** High-quality speech synthesis via Inworld TTS.

## 🛠️ Tech Stack

| Component | Provider/Model |
| :--- | :--- |
| **Framework** | LiveKit Agents |
| **LLM** | Google Gemma-4 (31B IT) |
| **STT** | Deepgram Nova-3 |
| **TTS** | Inworld TTS-2 (Voice: Ashley) |
| **Audio Enhancement** | AI Acoustics (Quail VF S) |

## 📋 Prerequisites

Before running the agent, ensure you have the following:

- Python 3.9+
- A LiveKit project (URL, API Key, and Secret)
- API keys for the following providers:
  - Deepgram
  - Google (for Gemma)
  - Inworld

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd traditional-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install livekit-agents livekit-plugins-ai_coustics python-dotenv
   # Install other necessary plugins as required by the environment
   ```

3. **Environment Configuration:**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   LIVEKIT_URL=wss://your-project.livekit.cloud
   LIVEKIT_API_KEY=your-api-key
   LIVEKIT_API_SECRET=your-api-secret
   DEEPGRAM_API_KEY=your-deepgram-key
   GOOGLE_API_KEY=your-google-key
   INWORLD_API_KEY=your-inworld-key
   ```

## 🏃 Running the Agent

Start the agent server by running:

```bash
python agent.py dev
```

Once the server is running, you can connect to the room via the [LiveKit Sandbox](https://agents-sandbox.livekit.io/) or your own LiveKit client to start talking to the assistant.

## 🤖 Assistant Personality

The assistant is designed to be:
- **Concise:** Provides direct answers without complex formatting or symbols.
- **Friendly:** Maintains a curious and welcoming tone.
- **Humorous:** Occasionally incorporates a sense of humor to make the interaction more natural.
