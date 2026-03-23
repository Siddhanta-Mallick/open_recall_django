from django.db import models

# Create your models here.
class WordList(models.Model):
    
    word = models.TextField()
    meaning = models.TextField()

    def __str__(self):
        return self.word