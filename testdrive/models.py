from django.db import models
from django.contrib.auth.models import User
from Car.models import Car
from django.utils import timezone

class Testdrive(models.Model):

    car =models.ForeignKey(Car)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(default = timezone.now)
    date_completed = models.DateField(null=True, blank=True)



