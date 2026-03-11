from multiprocessing import context
from urllib import request
from django.shortcuts import render

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