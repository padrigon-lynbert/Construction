from http.client import ImproperConnectionState
from multiprocessing import context
from multiprocessing.heap import reduce_arena
from os import name
from tkinter.tix import STATUS
from turtle import st
from urllib import request
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from numpy import delete

from .models import Project, Project_Item


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
    labors = project.labors.all()

    context = {
        'project': project,
        'items': items,
        'labors': labors
    }
    return render(request, "individual_quotation.html", context)

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
                value = float(value) 
            elif isinstance(model_field, models.BooleanField):
                value = value.lower() in ['true', '1', 'yes']

            setattr(project, field, value)
            project.save()

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request"})


@csrf_exempt
def update_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item_id = data.get("id")
            field = data.get("field")
            value = data.get("value")

            item = Project_Item.objects.get(id=item_id)

            if field in ["quantity", "unit_cost"]:
                value = float(value)

            setattr(item, field, value)
            item.save()

            project_id = item.project.id  

            return JsonResponse({"status": "ok", "item_id": item_id, "project_id": project_id})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


@csrf_exempt
def add_or_delete_item(request, id):
    project = Project.objects.get(id=id)

    action = request.POST.get('action')

    if action == 'add':
        Project_Item.objects.create(
            project=project,
            item_name="New Item",
            quantity=0,
            unit_cost=0
        )

    elif action == 'delete':
        item_id = request.POST.get('item_id')
        if item_id:
            Project_Item.objects.filter(id=item_id, project=project).delete()

    return redirect('individual_quotation', id)

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

