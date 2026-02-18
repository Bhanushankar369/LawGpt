# ⚖️ LawGpt – AI-Powered Legal Awareness Assistant

LawGpt is a full-stack AI-powered legal assistant built using Retrieval-Augmented Generation (RAG).  
It provides constitution-grounded, context-aware legal answers using semantic search and LLM reasoning.

---

## 🚀 Features

- 📚 FAISS Vector Database for semantic retrieval
- ⚡ Groq LLM API for ultra-fast inference
- 🗄 PostgreSQL caching to reduce repeated LLM calls and API costs
- 🧠 Django + Django REST Framework backend
- 🎨 Streamlit interactive chat frontend
- 🔎 Tool integration for legal blogs and related articles

---

## 🏗 How It Works

1. User asks a question in the Streamlit UI  
2. Request is sent to the Django backend API  
3. FAISS retrieves relevant constitutional context  
4. PostgreSQL cache is checked for an existing response  
5. If cached → return stored answer instantly  
6. If not cached → call Groq LLM  
7. Store generated response in database  
8. Send response back to Streamlit  

---

## 🛠 Tech Stack

Python  
Django  
Django REST Framework  
FAISS  
LangChain  
Groq API  
PostgreSQL  
Streamlit  

---

# 🚀 Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/LawGpt.git
cd LawGpt
```


## 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate:

Windows
```bash
venv\Scripts\activate
```

Mac/Linux
```bash
source venv/bin/activate
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Add Groq API Key

Create a .env file inside the backend folder:
```bash
backend/.env
```

Add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here


### Generate your key from:
https://console.groq.com/keys

Install dotenv if needed:

```bash
pip install python-dotenv
```

Add this inside settings.py:
```bash
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

## 5. Configure PostgreSQL

Update the DATABASES section in settings.py:

```bash
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
```


Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Run Django Backend

```bash
python manage.py runserver
```

Backend runs at:
```bash
http://127.0.0.1:8000/
```

## 7. Run Streamlit Frontend

Install if not installed:
```bash
pip install streamlit requests
```

Navigate to frontend folder:
```bash
cd frontend
```

Run:
```bash
streamlit run app.py
```

Frontend runs at:
```bash
http://localhost:8501
```
## 🧠 PostgreSQL Caching Strategy

Before calling the LLM, the system checks PostgreSQL for an existing response.

If found:
Returns cached answer instantly

If not found:
Calls Groq LLM

Stores response in database
Returns generated answer

Benefits

- ✅Faster responses
- ✅Reduced API cost
- ✅Better scalability
