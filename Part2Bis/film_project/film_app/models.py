from django.db import models
from datetime import datetime


# Create your models here.
class Poster(models.Model):
    image = models.ImageField()
    explanation_text= models.TextField()

    def __str__(self):
        return self.explanation_text


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    poster = models.OneToOneField(Poster, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Producer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

