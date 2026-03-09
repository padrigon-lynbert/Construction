from multiprocessing import context
from urllib import request
from django.shortcuts import render

from .models import Project

# Create your views here.

def quotation(request):
    return render(request, "quotation.html")

def individual_quotation(request):
    project = Project.objects.first()
    item = project.items if project else None

    context = {
        'project': project,
        'item': item
    }
    return render(request, "individual_quotation.html", context)


