from urllib import request

from django.shortcuts import render

# Create your views here.

def quotation(request):
    return render(request, "quotation.html")
