from django.db import models

# Create your models here.
class Leads(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    project_type = models.CharField(max_length=255)
    lead_source = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    estimated_budget = models.FloatField()
    deadline = models.DateField()
    notes = models.CharField(max_length=255)
    assigned_to = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)