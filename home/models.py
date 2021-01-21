from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
