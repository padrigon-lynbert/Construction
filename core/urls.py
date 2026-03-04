from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("core_spa/", views.core_spa, name="core_spa"),
    path("quotation/", views.quotation, name="quotation"),
]  