# -*- encoding: utf-8 -*-
from django.db import models
#from django.contrib.auth.models import User
# Create your models here.


class Dealer(models.Model):
    class Meta:
        db_table = "dealer"

    dealer_address = models.CharField(max_length=300)
    dealer_country = models.CharField(max_length=300)

    def __unicode__(self):
        return self.dealer_address


class Marks(models.Model):
    class Meta:
        db_table = "mark"
    marks_name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.marks_name


class Model(models.Model):
    class Meta:
        db_table = "model"

    model_name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.model_name

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

    car_price = models.CharField(max_length=300)
    car_description = models.TextField()
    car_color = models.CharField(max_length=300)
    car_mark = models.ForeignKey(Marks)
    car_model = models.ForeignKey(Model)
    car_dealer = models.ForeignKey(Dealer)
    car_man_year = models.IntegerField()
    car_complectation = models.CharField(max_length=25, choices=COMPLECTATION_CHOICES)
    car_img = models.ImageField()


class Comments(models.Model):
    class Meta:
        db_table = "comments"

    comments_text = models.TextField(verbose_name="Комментарий")
    comments_car = models.ForeignKey(Car)