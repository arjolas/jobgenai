from django.db import models

class Job(models.Model):
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    posted_at = models.DateTimeField()
