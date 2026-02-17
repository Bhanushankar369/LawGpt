from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "constitution_index")

from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("data/Indian_Constitution.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=300,
)

chunks = splitter.split_documents(docs)


embeddings = HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2"
)

db = FAISS.from_documents(
    chunks,
    embeddings
)

db.save_local(INDEX_PATH)