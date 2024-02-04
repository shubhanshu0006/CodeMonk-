
from django.db import models

class Paragraph(models.Model):
    content = models.TextField()

class Word(models.Model):
    content = models.CharField(max_length=50)
    paragraph = models.ForeignKey(Paragraph, related_name='words', on_delete=models.CASCADE)


