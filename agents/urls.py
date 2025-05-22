from django.urls import path, include
from .views import (
    GenerateTextView,
    AnswerQuestionView,
    GenerateImageView,
    AgentDispatchView,
)

urlpatterns = [
    path("llm/generate/", GenerateTextView.as_view(), name="generate-llm-text"),
    path("rag/answer/", AnswerQuestionView.as_view(), name="rag-answer"),
    path("gan/generate/", GenerateImageView.as_view(), name="generate-gan-image"),
    path("dispatch/", AgentDispatchView.as_view(), name="dispatch-agent"),
]
