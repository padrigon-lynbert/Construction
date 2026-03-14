from ast import Pass
from os import name
from turtle import ondrag

from django.db import models
from numpy import multiply, true_divide

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=750)
    details = models.CharField(max_length=255, null=True, blank=True)
    client_name = models.CharField(max_length=255)
    overhead = models.FloatField(default=20)
    margin = models.FloatField(default=30)  # in percent
    tax = models.FloatField(default=12)     # in percent


class Project_Item(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.FloatField(default=0)
    unit_cost = models.FloatField(default=0)
    
class Project_Labor(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="labors")
    role = models.CharField(max_length=255, null=True, blank=True)
    rate_per_hour = models.FloatField(default=0)
    hours_per_day = models.FloatField(default=0)
    days_per_month = models.FloatField(default=18)


