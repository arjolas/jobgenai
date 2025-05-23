from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from agents.services.llm_agent import LLMEngine
from agents.services.rag_agent import RAGEngine
from agents.services.gan_agent import GANGenerator
from agents.services.agent_orchestrator import AgentOrchestrator
import os
import logging

logger = logging.getLogger(__name__)

class GenerateTextView(APIView):
    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            engine = LLMEngine(api_key=os.getenv("OPENAI_API_KEY"))
            result = engine.chat(prompt)
            return Response({"response": result}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("LLM error")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnswerQuestionView(APIView):
    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "Question is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            engine = RAGEngine(vectorstore_path="vectorstore/")
            answer = engine.answer(question)
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("RAG error")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GenerateImageView(APIView):
    def post(self, request):
        latent_dim = request.data.get("latent_dim", 100)

        try:
            engine = GANGenerator(model_path="models/gan.pth")
            image_path = engine.generate(latent_dim=int(latent_dim))
            return Response({"image_path": image_path}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("GAN error")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AgentDispatchView(APIView):
    def post(self, request):
        agent_type = request.data.get("agent_type")
        input_data = request.data.get("input_data", "")

        if agent_type not in ["LLM", "RAG", "GAN"]:
            return Response({"error": "Invalid agent type"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            orchestrator = AgentOrchestrator()
            result = orchestrator.handle_request(agent_type, input_data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("Orchestrator error")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
