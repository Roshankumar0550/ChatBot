# The Riddler - ChatBot

A simple conversational chatbot web app built with Streamlit and Python. This project demonstrates a basic chat interface with persistent memory and chat history, suitable for educational or demo purposes.

## Features
- Interactive chat interface using Streamlit
- Maintains chat history and conversation memory
- Modular backend for easy extension

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ChatBot.git
   cd ChatBot
   ```
2. Install dependencies:
   ```bash
   pip install streamlit
   ```
   (Add any other dependencies from your backend if needed)

### Running the App
Run the following command in your project directory:
```bash
streamlit run genai_frontend.py
```

The app will open in your browser. Enter your queries and chat with the bot!

## Project Structure
- `genai_frontend.py` - Streamlit frontend for the chatbot
- `genai_backend.py`  - Backend logic for conversation and memory

## Customization
- Update `genai_backend.py` to change the bot's behavior or memory logic.
- Modify the Streamlit UI in `genai_frontend.py` as needed.

## License
This project is for educational/demo purposes. Add a license if you plan to distribute.
