from django.urls import path
import quotation
from . import views

urlpatterns = [
    path("quotation/", views.quotation, name="quotation"),
    path("individual_quotation/", views.individual_quotation, name="individual_quotation"),
]