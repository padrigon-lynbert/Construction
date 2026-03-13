from ast import Pass
from os import name

from django.db import models
from numpy import multiply

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
    
    # @property
    # def autocost(self):
    #     return self.quantity * self.unit_cost