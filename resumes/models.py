from django.db import models

class Resume(models.Model):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    file = models.FileField(upload_to="resumes/")
    parsed_data = models.JSONField(null=True)
