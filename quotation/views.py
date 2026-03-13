from http.client import ImproperConnectionState
from multiprocessing import context
from os import name
from tkinter.tix import STATUS
from urllib import request
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Project

from .models import Project

# Create your views here.

def quotation(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, "quotation.html", context)

def individual_quotation(request, id):
    project = Project.objects.get(id=id)
    items = project.items.all()

    context = {
        'project': project,
        'items': items
    }
    return render(request, "individual_quotation.html", context)
from django.db import models
@csrf_exempt

def update_individual_quotation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            project_id = data.get("id")
            field = data.get("field")
            value = data.get("value")

            project = Project.objects.get(id=project_id) 

            # Convert value type if necessary
            model_field = Project._meta.get_field(field)
            if isinstance(model_field, (models.IntegerField, models.FloatField, models.DecimalField)):
                value = float(value)  # or int(value) depending on field
            elif isinstance(model_field, models.BooleanField):
                value = value.lower() in ['true', '1', 'yes']
            # Add more type conversions if needed

            setattr(project, field, value)
            project.save()

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_empty_project(request):

    if request.method == "POST":
        Project.objects.create(
            name = "New Project",
            details = "Add details here.",
            client_name = "None Selected",
            margin = 30,
            tax = 10
        )
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid Method"}, status = 400)

@csrf_exempt
def delete_project(request, id):
    Project.objects.filter(id=id).delete()
    return HttpResponse("object deleted")