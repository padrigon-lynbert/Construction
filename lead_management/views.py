from django.shortcuts import render
from .models import Leads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def leads(request):
    leads = Leads.objects.all()

    return render(request, 'leads.html',{
        "leads": leads
    })

def test(request):
    leads = Leads.objects.all()

    return render(request, 'test.html',{
        "leads": leads
    })


@csrf_exempt
def update_lead(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            lead_id = data.get("id")
            field = data.get("field")
            value = data.get("value")

            lead = Leads.objects.get(id=lead_id)
            setattr(lead, field, value)
            lead.save()

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request"})