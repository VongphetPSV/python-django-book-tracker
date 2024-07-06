from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    genre = models.ForeignKey(
        'Genre', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
