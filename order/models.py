from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from Car.models import Car
# Create your models here.
class Order(models.Model):
    class Meta:
        db_table = "order"
    #id's generated automaticaly
    STATUS_CONFIRMED = 'confirmed'
    STATUS_ACCEPTED = 'accepted'
    STATUS_CANCELLED = 'cancelled'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = (
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_COMPLETED, 'Completed'),
    )
    user = models.ForeignKey(User)
    vehicle = models.ForeignKey(Car)
    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def confirm(self):
        self.status = self.STATUS_CONFIRMED
        self.save()

    @property
    def price(self):
        return self.vehicle.price
