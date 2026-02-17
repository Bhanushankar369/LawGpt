import numpy as np
from numpy.linalg import norm
from .models import QAHistory
from .embeddings import embed_text

THRESHOLD = 0.85

def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

def check_cache(question):
    query_embedding = embed_text(question)
    records = QAHistory.objects.all()
    
    for record in records:
        similarity = cosine_similarity(
            query_embedding,
            record.question_embedding
        )
        
        if similarity > THRESHOLD:
            return record.answer

    return None

def save_cache(question, answer):
    embedding = embed_text(question)
    QAHistory.objects.create(
        question = question,
        question_embedding=embedding,
        answer=answer
    )