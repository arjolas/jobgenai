from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
import os

class RAGEngine:
    def __init__(self, vectorstore_path: str):
        self.embeddings = OpenAIEmbeddings()
        self.db = FAISS.load_local(vectorstore_path, self.embeddings)
        self.llm = OpenAI(model_name="gpt-4")
        self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=self.db.as_retriever())

    def answer(self, question: str) -> str:
        return self.qa_chain.run(question)
