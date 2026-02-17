from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .semantic_cache import check_cache, save_cache
from .graph import graph

from langchain_core.messages import HumanMessage

class ask_question(APIView):
    def post(self, request):
        question = request.data.get("question")
        
        # Check semantic cache
        cached = check_cache(question)
        if cached:
            return Response({"answer": cached, "source": "Cached DB"})
        
        # Run LangGraph
        result = graph.invoke({
            "messages": [HumanMessage(content=question)]
        })
        
        final_answer = result["messages"][-1].content
        
        # Save the ans to DB
        save_cache(question, final_answer)
        
        return Response({"answer": final_answer, "source": "GroqLLM"})
    
    