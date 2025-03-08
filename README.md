Chatbot Project:
A simple yet powerful Chatbot built using Python's FastAPI and OpenAI's GPT-3.5-turbo model. This project demonstrates how to create a web-based chatbot that interacts with users in real-time, powered by OpenAI's natural language processing capabilities.
---------------------------------------------------------------------------------------
![Chatbot](https://github.com/user-attachments/assets/850f5251-06d4-421b-8fa7-13f5cc20dadd)
---------------------------------------------------------------------------------------
🚀 Features
🌐 Web-based Interface – Chat with the bot using a simple web UI.
⚡ FastAPI-powered Backend – Efficient API handling with FastAPI.
🤖 OpenAI GPT-3.5 Integration – Generates responses using OpenAI's API.
🎨 Bootstrap Styling – Responsive and modern UI.
💾 Chat History – Displays previous chatbot interactions.
---------------------------------------------------------------------------------------
Technologies Used
Python: Core programming language.
FastAPI: Backend framework for building the API and serving the web interface.
OpenAI API: Powers the chatbot's natural language processing.
Jinja2 Templates: For rendering dynamic HTML pages.
Bootstrap 5: For styling the web interface.
HTML/CSS: Frontend structure and design.
--------------------------------------------------------------------------------------
🛠️ Installation
Prerequisites
Python 3.7+: Ensure Python is installed on your system.
OpenAI API Key: Obtain an API key from OpenAI.
FastAPI: Install FastAPI and required dependencies.

1. Clone the Repository
2. Create a Virtual Environment
   using: python -m venv .venv
   Activate the virtual environment
3. Install Dependencies
4. Run the Application
   using: uvicorn main:app --reload
   This will start the server at: http://127.0.0.1:8000/

📌 Usage
Open http://127.0.0.1:8000/ in your browser.
Type a message in the input box and press Send.
The chatbot will generate a response using OpenAI's API.
Chat history will be displayed below the input box.

📂 Project Structure
Chatbot/
│── .venv/                   # Virtual environment (not included in GitHub)
│── templates/                # HTML templates for web UI
│   ├── layout.html           # Base layout file
│   ├── home.html             # Chat UI template
│   ├── nav.html              # Navigation bar
│── main.py                   # FastAPI backend
│── requirements.txt           # Required Python packages
│── README.md                 # Project documentation

📜 Dependencies
FastAPI – Backend framework
Uvicorn – ASGI server
Jinja2 – Template rendering
OpenAI – GPT-3.5 API for chatbot

🤝 Acknowledgments
OpenAI for GPT-3.5
FastAPI for building high-performance APIs
Bootstrap for styling

📜 License
This project is licensed under the MIT License.
