from multiprocessing import context
from os import name
from tkinter.tix import STATUS
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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
    
    return render(request, "core_spa.html")
