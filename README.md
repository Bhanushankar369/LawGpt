⚖️ LawGpt – AI-Powered Legal Awareness Assistant

LawGpt is a full-stack AI-powered legal assistant that uses Retrieval-Augmented Generation (RAG) to provide accurate, constitution-grounded legal responses.

It consists of:

🧠 Django + DRF Backend API

🎨 Streamlit Frontend

📚 FAISS Vector Database (for semantic search)

⚡ Groq LLM API (for fast inference)

🗄 PostgreSQL caching (to reduce repeated LLM calls & API costs)

🏗 Architecture Overview

User asks question in Streamlit UI

Request sent to Django Backend

FAISS retrieves relevant constitutional context

PostgreSQL cache checked for existing response

If not cached → Groq LLM generates answer

Response stored in DB for future reuse

Answer returned to Streamlit UI

🚀 Local Setup Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/LawGpt.git
cd LawGpt

🔑 Backend Setup (Django)
2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Backend Dependencies
pip install -r requirements.txt

4️⃣ Add Groq API Key

Create a .env file inside backend root:

backend/.env


Add:

GROQ_API_KEY=your_groq_api_key_here


Get your key from:
👉 https://console.groq.com/keys

Load Environment Variables in settings.py
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

5️⃣ Configure PostgreSQL

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lawgpt',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Run migrations:

python manage.py makemigrations
python manage.py migrate

6️⃣ Run Backend Server
python manage.py runserver


Backend runs at:

http://127.0.0.1:8000/

🎨 Frontend Setup (Streamlit)
7️⃣ Install Streamlit (if not included)
pip install streamlit requests

8️⃣ Navigate to Frontend Folder
cd frontend

9️⃣ Run Streamlit App
streamlit run app.py


Streamlit will run at:

http://localhost:8501

📁 Project Structure
LawGpt/
│
├── backend/              # Django Backend
│   ├── lawgpt/
│   ├── manage.py
│   └── .env
│
├── frontend/             # Streamlit UI
│   └── app.py
│
├── requirements.txt
└── README.md

🔥 Key Features

✅ RAG-based constitutional retrieval
✅ Groq ultra-fast inference
✅ PostgreSQL response caching (reduces LLM API calls)
✅ Streamlit interactive chat interface
✅ Tool integration for legal blogs & articles

🛠 Tech Stack

Backend:

Python

Django

Django REST Framework

FAISS

LangChain

Groq API

PostgreSQL

Frontend:

Streamlit

Requests

🧠 Why PostgreSQL Caching?

Instead of calling the LLM repeatedly for similar questions:

Query is first checked in PostgreSQL

If found → return cached answer instantly

If not → call Groq LLM

Store result in DB

This:

⚡ Improves speed

💰 Reduces API cost
