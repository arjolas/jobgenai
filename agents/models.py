from django.db import models

class Agent(models.Model):
    AGENT_TYPES = [
        ("LLM", "Large Language Model"),
        ("GAN", "Generative Adversarial Network"),
        ("RAG", "Retrieval-Augmented Generation"),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=AGENT_TYPES)
    config = models.JSONField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
