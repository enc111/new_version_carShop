# -*- encoding: utf-8 -*-
from django.db import models
#from django.contrib.auth.models import User
# Create your models here.


class Dealer(models.Model):
    class Meta:
        db_table = "dealer"

    address = models.CharField(max_length=300)
    country = models.CharField(max_length=300)

    def __unicode__(self):
        return self.address


class Mark(models.Model):
    class Meta:
        db_table = "mark"
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name


class Model(models.Model):
    class Meta:
        db_table = "model"

    name = models.CharField(max_length=100)
    mark = models.ForeignKey(Mark)

    def __str__(self):
        return '{} {}'.format(self.mark, self.name)

# -*-class Components(models.Model):
 #   class Meta:
 #       db_table = "components"

 #   components_name = models.CharField(max_length=300)


 #   def __unicode__(self):
 #       return self.components_name-*-


class Car(models.Model):
    class Meta:
        db_table = "car"
    COMPLECTATION_BASE = 'base'
    COMPLECTATION_INTERMEDIATE = 'intermediate'
    COMPLECTATION_MAX = 'max'
    COMPLECTATION_CHOICES = (
        (COMPLECTATION_BASE, 'Базовая'),
        (COMPLECTATION_INTERMEDIATE, 'Средняя'),
        (COMPLECTATION_MAX, 'Максимальная'),
    )

    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    color = models.CharField(max_length=300)
    mark = models.ForeignKey(Mark)
    model = models.ForeignKey(Model)
    dealer = models.ForeignKey(Dealer)
    man_year = models.IntegerField()
    complectation = models.CharField(max_length=25, choices=COMPLECTATION_CHOICES)
    car_img = models.ImageField()


class Comments(models.Model):
    class Meta:
        db_table = "comments"

    ctext = models.TextField(verbose_name="Комментарий")
    comments_car = models.ForeignKey(Car)