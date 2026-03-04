from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def core_spa(request):
    return render(request, 'core_spa.html')