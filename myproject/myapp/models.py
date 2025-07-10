from django.db import models
from django.conf import settings
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

class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=20)
    foods = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"