🧠 ChatRoom AI Backend

This repository contains the server-side logic for the ChatRoom App. It is a high-performance Flask application designed to handle AI query processing, prompt orchestration, and response streaming for the Android client.

✨ Key Features

⚡ High-Speed Processing: Optimized to handle 500+ AI requests/day with an average response latency of <400ms (hosted on Render).

🤖 Gemini API Integration: Orchestrates prompts and manages context to deliver intelligent, conversational AI responses.

🔄 Response Streaming: Supports streaming endpoints to reduce perceived latency on the client side.

🛡️ Robust Architecture: Built with clean architecture principles to separate routing, business logic, and external API services.

🛠️ Tech Stack

Language: Python 3.x

Framework: Flask

AI Service: Google Gemini API

Deployment: Render

Tools: Gunicorn (WSGI Server), Dotenv

🚀 Getting Started

Follow these instructions to run the backend server locally.

Prerequisites

Python 3.8 or higher

pip (Python package manager)

A Google Cloud Project with the Gemini API enabled

Installation

Clone the Repository

git clone [https://github.com/TusharGarg12/chatroom-ai-backend.git](https://github.com/TusharGarg12/chatroom-ai-backend.git)
cd chatroom-ai-backend


Create a Virtual Environment

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Environment Configuration
Create a .env file in the root directory and add your API keys:

FLASK_APP=app.py
FLASK_ENV=development
GEMINI_API_KEY=your_gemini_api_key_here
PORT=5000


Run the Server

flask run
# Or using Gunicorn for production-like testing
gunicorn app:app


🔌 API Endpoints

Method

Endpoint

Description

GET

/

Health check to verify server status.

POST

/chat

Accepts a user message and returns the AI's textual response.

POST

/stream

(Optional) Streaming endpoint for real-time token generation.

📦 Deployment (Render)

This project is configured for easy deployment on Render.

Connect your GitHub repository to Render.

Select Web Service as the service type.

Set the Build Command to: pip install -r requirements.txt

Set the Start Command to: gunicorn app:app

Add your GEMINI_API_KEY in the Environment Variables section.

🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

📞 Contact

Tushar Garg

GitHub

LinkedIn
