from ast import Pass
from os import name

from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    margin = models.FloatField(default=0)  # in percent
    tax = models.FloatField(default=0)     # in percent


class ProjectItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=255)
    quantity = models.FloatField(default=0)
    unit_cost = models.FloatField(default=0)
    
    @property
    def autocost(self):
        return self.quantity * self.unit_cost