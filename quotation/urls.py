from django.urls import path
import quotation
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("dash/", views.quotation, name="dash"),
    path("leads/", views.leads, name="leads"),
]