from django.db import models

# Create your models here.
class Urls(models.Model):
    original_url = models.CharField(max_length=255)
    shortened_url = models.CharField(max_length=6, unique=True)

    def __str__(self) -> str:
        return self.shortened_url