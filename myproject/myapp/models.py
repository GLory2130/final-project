from django.db import models

# Create your models here.
class User(models.Model):
    username =models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/foods/')
    importance = models.TextField()

    def __str__(self):
        return self.name