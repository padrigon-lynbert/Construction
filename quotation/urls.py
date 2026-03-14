from django.urls import path
import quotation
from . import views

urlpatterns = [
    path("quotation/", views.quotation, name="quotation"),
    path("individual_quotation/<int:id>", views.individual_quotation, name="individual_quotation"),
    path("add_empty_project/", views.add_empty_project, name="add_empty_project"),
    path("delete_project/<int:id>/", views.delete_project, name="delete_project"),
    path("update_individual_quotation/", views.update_individual_quotation, name="update_individual_quotation"),
    path("update_item/", views.update_item, name="update_item"),
    path("add_or_delete_item/<int:id>", views.add_or_delete_item, name="add_or_delete_item"),
]