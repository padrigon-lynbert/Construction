from urllib import request

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "login.html")

def quotation(request):
    return render(request, "quotation.html")

def leads(request):
    return render(request, 'leads.html')