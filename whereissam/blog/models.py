from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WindSpeed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WindDirection(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Seastate(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    categories = models.ManyToManyField(Category, blank=True)  # Meerdere categorieën
    windspeed = models.ForeignKey(WindSpeed, on_delete=models.SET_NULL, null=True, blank=True)
    winddirection = models.ForeignKey(WindDirection, on_delete=models.SET_NULL, null=True, blank=True)
    seastate = models.ForeignKey(Seastate, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # afbeelding
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
