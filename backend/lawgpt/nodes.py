from .vectorstore import load_vectorstore
from .llm import generate_answer

from langchain_community.utilities import WikipediaAPIWrapper
from ddgs import DDGS

from langchain_core.messages import AIMessage

vectorstore = load_vectorstore()
def retrieve_node(state):
    docs = vectorstore.similarity_search(state["messages"][-1].content, k=4)
    
    context = "\n".join([doc.page_content for doc in docs])
    
    
    return {"context": context}


# Vector store refined answer

def refine_node(state):
    prompt = f"""
        You are LawGPT, a legal awareness assistant designed to help users understand the Constitution and legal protections in simple language.

        Your job is to:

        1. Use the retrieved context from the Constitution (vector database results) to answer the user's question accurately.
        2. Always prioritize Constitutional articles and legal provisions from the provided context.
        3. Clearly mention relevant Article numbers, clauses, or sections if available in the context.
        4. Explain the answer in simple and practical language so that a common person can understand.
        5. If the retrieved context is insufficient or unclear, use the available tools to fetch:
        - Related legal articles
        - Blogs
        - Case law explanations
        - Practical interpretations
        6. If you use tool results, clearly integrate that information into the answer.
        7. Do NOT hallucinate laws or article numbers.
        8. If the Constitution does not address the issue directly, clearly say so and rely on tool data.
        
        
        This is the question asked by the user:
        {state["messages"][-1].content}
        
        This is the context provided by the Groq LLM use these to generate answer:
        {state["context"]}

        Answer format:
        - Relevant Constitutional Provision (if available)
        - Explanation in simple terms
        - Practical Example (if possible)
        - Additional references (if tool was used)

        Always ensure accuracy and clarity.
    """
    
    refined = generate_answer(prompt)
    
    return {
        "refined_answer": refined
    }


# Duck Duck Go Search Tool

wiki = WikipediaAPIWrapper()

def tool_node(state):

    query = state["messages"][-1].content

    links = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=3):
                links.append(r["href"])
                
    except Exception as e:
        print("DuckDuckGo error:", e)
        links = ["Search unavailable at the moment."]
        
    return {
        "tool_links": links
    }
    
    
def combine_node(state):
    
    refined = state.get("refined_answer", "")
    links = state.get("tool_links", [])
    

    return {
        "messages": f"{refined} + {links})"
    }