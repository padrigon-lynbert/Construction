from django.urls import path
import quotation
from . import views

urlpatterns = [
    path("leads/", views.leads, name="leads"),
    path("test/", views.test, name="test"),

    # apis
    path('update_lead/', views.update_lead, name='update_lead'),
]