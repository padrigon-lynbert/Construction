from django.urls import path
import quotation
from . import views

urlpatterns = [
    path("leads/", views.leads, name="leads"),
]