import streamlit as st
import requests

st.title("⚖️ LawGPT - Constitution AI")

question = st.text_input("Ask a legal question")

if st.button("Ask"):
    res = requests.post(
        "http://127.0.0.1:8000/ask/",
        json={"question": question}
    )
    
    data = res.json()
    
    st.write("### Answer")
    st.write(data["answer"])
    st.caption(f"Source: {data['source']}")
    
    