from django.db import models

# Create your models here.
class WordList(models.Model):

    word = models.CharField(max_length=255, unique=True)
    meaning = models.TextField()

    def __str__(self):
        return self.word