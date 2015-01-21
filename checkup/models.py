from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from Car.models import Car


class TypeOfService(models.Model):
    class Meta:
        db_table = "TypeOfService"
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=12)


class Checkup(models.Model):
    class Meta:
        db_table = "Checkup"
    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateField(null=True, blank=True)
    reg_number = models.CharField(max_length=15)
    run = models.IntegerField()
    car_man_year = models.ForeignKey(Car)
    user = models.ForeignKey(User)
    type_of_service = models.ForeignKey(TypeOfService)

    @property
    def price(self):
        return self.type_of_service.price

