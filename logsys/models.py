from django.db import models
class Registratin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)