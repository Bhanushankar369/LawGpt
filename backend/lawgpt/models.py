from django.db import models

# Create your models here.
class QAHistory(models.Model):
    question = models.TextField()
    question_embedding = models.JSONField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    