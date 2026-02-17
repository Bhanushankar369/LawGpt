from langgraph.graph import StateGraph, START, END
from .graph_state import GraphState
from .nodes import retrieve_node, refine_node, tool_node, combine_node

workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve_node)
workflow.add_node("refine", refine_node)
workflow.add_node("tools", tool_node)
workflow.add_node("combine", combine_node)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "refine")
workflow.add_edge("refine", "tools")
workflow.add_edge("tools", "combine")
workflow.add_edge("combine", END)

graph = workflow.compile()