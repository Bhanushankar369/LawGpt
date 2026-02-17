from langchain_community.vectorstores import FAISS
from .embeddings import embedding_model

def load_vectorstore():
    return FAISS.load_local(
        "constitution_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )