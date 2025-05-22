from llm_agent import LLMEngine
from rag_agent import RAGEngine
from gan_agent import GANGenerator
import os

class AgentOrchestrator:
    def __init__(self):
        self.llm = LLMEngine(api_key=os.getenv("OPENAI_API_KEY"))
        self.rag = RAGEngine(vectorstore_path="vectorstore/")
        self.gan = GANGenerator(model_path="models/gan.pth")

    def handle_request(self, agent_type: str, input_data: str = "") -> dict:
        if agent_type == "LLM":
            return {"type": "LLM", "output": self.llm.chat(input_data)}
        elif agent_type == "RAG":
            return {"type": "RAG", "output": self.rag.answer(input_data)}
        elif agent_type == "GAN":
            return {"type": "GAN", "image_path": self.gan.generate()}
        else:
            return {"error": "Invalid agent type"}
